from typing import Any, Callable, Optional
import subprocess
import uuid

from pydantic import PrivateAttr

from pijp.config.jobs.base import BaseJob
from pijp.utils import no_op
from pijp.utils.scripts import get_script_file


class ShellJob(BaseJob):
    interpreter: str = "/bin/sh"
    pre_commands: list[str] = []
    commands: list[str] = []
    post_commands: list[str] = []

    _process: Optional[subprocess.Popen] = PrivateAttr(default=None)

    def on_run(
        self,
        pipeline_id: uuid.UUID,
        name: str,
        variables: dict[str, str],
        progress_callback: Callable[[dict[str, Any]], None] = no_op,
    ) -> int:
        with subprocess.Popen(
            get_script_file(
                commands=[
                    *self.pre_commands,
                    *self.commands,
                    *self.post_commands,
                ],
                interpreter=self.interpreter,
            ),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            shell=True,
            text=True,
            env=variables,
        ) as self._process:
            if self._process.stdout:
                for line in self._process.stdout:
                    progress_callback(
                        {
                            "job_id": self._id,
                            "name": name,
                            "output": line.rstrip(),
                        }
                    )

        exit_code = self._process.wait()
        return exit_code

    def on_cancel(self) -> None:
        if self._process:
            self._process.terminate()
