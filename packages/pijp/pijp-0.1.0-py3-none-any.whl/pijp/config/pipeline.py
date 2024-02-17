from concurrent.futures import Future, ThreadPoolExecutor, as_completed
from typing import Any, Callable, Optional
import enum
import fnmatch
import os
import time
import uuid

from pydantic import BaseModel, Field, PrivateAttr, validator
import contexttimer
import docker

from pijp.config.jobs import JobResult, JobStatus, ActionJob, BaseJob, ContainerJob, ShellJob
from pijp.utils import no_op
from pijp.utils.graph import Graph
from pijp.utils.vars import load_dotenv_files


JOBS_MAPPING = {
    "action": ActionJob,
    "container": ContainerJob,
    "shell": ShellJob,
}


class PipelineStatus(enum.Enum):
    PENDING = 0
    RUNNING = 10
    SUCCESS = 20
    FAILED = 100


class PipelineResult(BaseModel):
    plan: list[list[str]] = []
    duration: Optional[float] = None
    status: PipelineStatus = PipelineStatus.PENDING
    jobs: dict[str, JobResult] = {}
    created_at: float = Field(default_factory=time.time)


class Pipeline(BaseModel):
    description: str = ""
    dotenv: list[str] = []
    variables: dict[str, str] = {}
    concurrent: int = Field(gt=0, le=os.cpu_count() * 5, default=os.cpu_count())
    jobs: dict[str, BaseJob] = {}

    _id: uuid.UUID = PrivateAttr(default_factory=uuid.uuid4)
    _cancelled: bool = PrivateAttr(default=False)
    _executor: Optional[ThreadPoolExecutor] = PrivateAttr(default=None)
    _running_tasks: dict[Future[JobResult], str] = PrivateAttr(default={})

    @validator("jobs", pre=True)
    def deserialize_jobs(cls, value) -> dict[str, BaseJob]:  # pylint: disable=E0213
        jobs = {}
        for job_name, data in value.items():
            job = data if isinstance(data, BaseJob) else JOBS_MAPPING[data.get("type")](**data)

            if not isinstance(job, BaseJob):
                raise ValueError(f"Unknown job type: {data.get('type')}")

            additional_jobs = job.generate_matrix_jobs(prefix=job_name)
            if additional_jobs is not None:
                jobs.update(additional_jobs)
            else:
                jobs[job_name] = job

        return jobs

    def run(
        self,
        name: str,
        extra_vars: Optional[dict[str, str]] = None,
        concurrent: Optional[int] = None,
        pipeline_start_callback: Callable[[dict[str, Any]], None] = no_op,
        pipeline_complete_callback: Callable[[dict[str, Any]], None] = no_op,
        stage_start_callback: Callable[[dict[str, Any]], None] = no_op,
        stage_complete_callback: Callable[[dict[str, Any]], None] = no_op,
        job_start_callback: Callable[[dict[str, Any]], None] = no_op,
        job_progress_callback: Callable[[dict[str, Any]], None] = no_op,
        job_complete_callback: Callable[[dict[str, Any]], None] = no_op,
    ) -> PipelineResult:
        pipeline_start_callback(
            {
                "pipeline_id": self._id,
                "name": name,
            }
        )

        plan = self.build_graph().topological_sort()
        result = PipelineResult(plan=plan)
        max_jobs = concurrent or self.concurrent
        self._executor = ThreadPoolExecutor(max_workers=max_jobs)

        with contexttimer.Timer() as timer:
            result.status = PipelineStatus.RUNNING

            for index, stage in enumerate(plan):
                if self._cancelled:
                    break

                stage_start_callback(
                    {
                        "pipeline_id": self._id,
                        "name": name,
                        "index": index + 1,
                        "job_names": stage,
                    }
                )

                for batch in self.prepare_batches(stage, max_jobs):
                    for job_name in batch:
                        job = self.jobs[job_name]

                        task = self._executor.submit(
                            job.run,
                            self._id,
                            job_name,
                            self.prepare_variables(
                                name=name,
                                job_name=job_name,
                                job=job,
                                extra_vars=extra_vars or {},
                                stage_index=index,
                            ),
                            job_start_callback,
                            job_progress_callback,
                            job_complete_callback,
                        )
                        self._running_tasks[task] = job_name

                    for task in as_completed(self._running_tasks):
                        job_name = self._running_tasks[task]
                        self._running_tasks.pop(task, None)

                        result.jobs[job_name] = task.result()
                        if result.jobs[job_name].status.value < JobStatus.FAILED.value:
                            continue

                        if not self.jobs[job_name].can_fail:
                            self.cancel()

                            result.status = PipelineStatus.FAILED
                            result.duration = timer.elapsed

                            stage_complete_callback(
                                {
                                    "pipeline_id": self._id,
                                    "name": name,
                                    "index": index + 1,
                                }
                            )
                            pipeline_complete_callback(
                                {
                                    "pipeline_id": self._id,
                                    "name": name,
                                    "status": result.status,
                                }
                            )

                            return result

                    stage_complete_callback(
                        {
                            "pipeline_id": self._id,
                            "name": name,
                            "index": index + 1,
                        }
                    )

        result.status = PipelineStatus.SUCCESS
        result.duration = timer.elapsed

        pipeline_complete_callback(
            {
                "pipeline_id": self._id,
                "name": name,
                "status": result.status,
            }
        )

        return result

    def cancel(self) -> None:
        self._cancelled = True

        if self._executor:
            self._executor.shutdown(wait=False)

        for task, job_name in self._running_tasks.items():
            if not task.done():
                self.jobs[job_name].cancel()

        self._executor = None
        self._running_tasks = {}

        # Remove any orphan containers...
        client = docker.from_env()
        containers = client.containers.list(filters={"label": f"org.pijp.session_id={self._id}"})
        for container in containers:
            container.remove(force=True)

    def prepare_variables(
        self,
        name: str,
        job_name: str,
        job: BaseJob,
        extra_vars: dict[str, str],
        stage_index: int,
    ) -> dict[str, Optional[str]]:
        return {
            **load_dotenv_files(self.dotenv),
            **self.variables,
            **load_dotenv_files(job.dotenv),
            **job.variables,
            **extra_vars,
            "PIJP_PIPELINE_NAME": name,
            "PIJP_PIPELINE_ID": str(self._id),
            "PIJP_PIPELINE_STAGE": str(stage_index),
            "PIJP_JOB_NAME": job_name,
            "PIJP_JOB_ID": str(job.id),
        }

    def prepare_batches(self, stage_jobs: list[str], concurrent: int) -> list[list[str]]:
        result = []
        temp = []
        for job_name in stage_jobs:
            if self.jobs[job_name].isolated:
                result.append([job_name])
            else:
                temp.append(job_name)

                if len(temp) == concurrent:
                    result.append(temp)
                    temp = []

        if temp:
            result.append(temp)

        return result

    def build_graph(self) -> Graph:
        graph = Graph()
        job_names = list(self.jobs.keys())

        for job_name, job in self.jobs.items():
            graph.add_vertex(job_name)

            for pattern in job.needs:
                dependencies = [dep for dep in job_names if fnmatch.fnmatch(dep, pattern)]

                for dependency in dependencies:
                    graph.add_edge(job_name, dependency)

        return graph
