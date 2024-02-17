from typing import Any, Callable, Optional, Union
import os
import string
import uuid

import docker
from docker.models.containers import Container

from pydantic import PrivateAttr

from pijp.config.jobs.base import BaseJob
from pijp.utils import no_op
from pijp.utils.cli_args import build_cli_options


class ActionJob(BaseJob):
    image: str
    network_mode: str = "bridge"
    volumes: list[str] = []
    privileged: bool = False
    params: dict[str, Union[str, bool, list[str]]]

    _container: Optional[Container] = PrivateAttr(default=None)

    def on_run(
        self,
        pipeline_id: uuid.UUID,
        name: str,
        variables: dict[str, str],
        progress_callback: Callable[[dict[str, Any]], None] = no_op,
    ) -> int:
        image = string.Template(self.image).substitute(**variables)

        client = docker.from_env()
        self._container = client.containers.run(
            image=image,
            privileged=self.privileged,
            command=build_cli_options(self.params, variables),
            working_dir="/opt/workspace",
            volumes=[
                *[os.path.abspath(p) for p in self.volumes],
                f"{os.getcwd()}:/opt/workspace",
            ],
            environment=variables,
            detach=True,
            network_mode=self.network_mode,
            labels={
                "org.pijp.session_id": str(pipeline_id),
                "org.pijp.job_name": name,
            },
        )

        for line in self._container.logs(stream=True, follow=True):
            progress_callback(
                {
                    "job_id": self._id,
                    "name": name,
                    "output": line.decode().rstrip(),
                }
            )

        result = self._container.wait()

        # NOTE: This is to avoid a double removal. At this
        # point we can assume that the container was stopped and removed.
        if not self._cancelled:
            self._container.remove(force=True)

        exit_code = result.get("StatusCode", 0)
        return int(exit_code)

    def on_cancel(self) -> None:
        if self._container is not None:
            self._container.remove(force=True)
