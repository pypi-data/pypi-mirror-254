from typing import Any, Callable, Optional
import abc
import enum
import itertools
import logging
import time
import uuid

from contexttimer import Timer
from func_timeout import func_timeout, FunctionTimedOut
from pydantic import BaseModel, Field, PrivateAttr
from simpleeval import SimpleEval, NameNotDefined

from pijp.utils import no_op


class JobStatus(enum.Enum):
    PENDING = 0
    RUNNING = 10
    SUCCESS = 20
    SKIPPED = 30
    CANCELLED = 40
    FAILED = 100
    FAILED_EXIT_CODE = 101
    FAILED_TIMEOUT = 102
    FAILED_EXCEPTION = 103


class JobResult(BaseModel):
    buffer: list[str] = []
    exit_code: Optional[int] = None
    duration: Optional[float] = None
    status: JobStatus = JobStatus.PENDING
    created_at: float = Field(default_factory=time.time)


class BaseJob(BaseModel, abc.ABC):
    description: str = ""
    dotenv: list[str] = []
    variables: dict[str, str] = {}
    can_fail: bool = False
    isolated: bool = False
    needs: list[str] = []
    when: Optional[str] = None
    timeout: int = 3600
    matrix: Optional[list[dict[str, list[str]]]] = None

    _id: uuid.UUID = PrivateAttr(default_factory=uuid.uuid4)
    _cancelled: bool = PrivateAttr(default=False)

    @property
    def id(self) -> uuid.UUID:
        return self._id

    @abc.abstractmethod
    def on_run(
        self,
        pipeline_id: uuid.UUID,
        name: str,
        variables: dict[str, str],
        progress_callback: Callable[[dict[str, Any]], None] = no_op,
    ) -> int:
        pass

    @abc.abstractmethod
    def on_cancel(self) -> None:
        pass

    def run(
        self,
        pipeline_id: uuid.UUID,
        name: str,
        variables: dict[str, Optional[str]],
        job_start_callback: Callable[[dict[str, Any]], None] = no_op,
        job_progress_callback: Callable[[dict[str, Any]], None] = no_op,
        job_complete_callback: Callable[[dict[str, Any]], None] = no_op,
    ) -> JobResult:
        result = JobResult()

        with Timer() as timer:
            result.status = JobStatus.RUNNING
            job_start_callback(
                {
                    "job_id": self._id,
                    "name": name,
                }
            )

            if not self.can_run(variables):
                result.status = JobStatus.SKIPPED
            else:

                def progress_wrapper(data: dict[str, Any]) -> None:
                    result.buffer.append(data["output"])
                    job_progress_callback(data)

                try:
                    exit_code = func_timeout(
                        self.timeout,
                        self.on_run,
                        args=(
                            pipeline_id,
                            name,
                            variables,
                            progress_wrapper,
                        ),
                    )
                    result.exit_code = exit_code

                    if not self._cancelled:
                        result.status = (
                            JobStatus.SUCCESS
                            if result.exit_code == 0
                            else JobStatus.FAILED_EXIT_CODE
                        )
                    else:
                        result.status = JobStatus.CANCELLED
                except FunctionTimedOut:
                    result.status = JobStatus.FAILED_TIMEOUT
                    self.cancel()
                except Exception as exc:  # pylint: disable=W0718
                    logging.error(exc)

                    result.status = JobStatus.FAILED_EXCEPTION
                    self.cancel()

        result.duration = timer.elapsed
        job_complete_callback(
            {
                "job_id": self._id,
                "name": name,
                "status": result.status,
            }
        )

        return result

    def cancel(self) -> None:
        self._cancelled = True

        self.on_cancel()

    def can_run(self, variables: dict[str, Optional[str]]) -> bool:
        evaluator = SimpleEval(names=variables)
        try:
            return bool(evaluator.eval(self.when)) if self.when else True
        except NameNotDefined as exc:
            logging.debug("Evaluation failed: %s", exc)
            return False

    def generate_matrix_jobs(self, prefix: str, sep: str = ":") -> Optional[dict[str, "BaseJob"]]:
        if self.matrix is None:
            return None

        result = {}
        for group in self.matrix:
            pairs = list(dict(zip(group, x)) for x in itertools.product(*group.values()))

            for pair in pairs:
                new_job = self.model_copy()
                new_job.matrix = None
                new_job.variables = {**new_job.variables, **pair}

                name = f"{prefix}{sep}{sep.join(str(value) for value in pair.values())}"
                result[name] = new_job

        return result
