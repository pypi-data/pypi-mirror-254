import datetime
import importlib.metadata
import logging
import time
import uuid

from humanize import naturaldelta
from pydantic import BaseModel, Field

from rich import box
from rich.table import Table
from rich.text import Text

from pijp.config.pipeline import Pipeline, PipelineResult
from pijp.config.jobs import JobStatus
from pijp.report.system import SystemReport
from pijp.utils.console import console


class RunnerReport(BaseModel):
    system: SystemReport = SystemReport()
    runner_id: uuid.UUID
    version: str = importlib.metadata.version("pijp")
    manifest_path: str
    pipelines: dict[str, Pipeline] = {}
    results: dict[str, PipelineResult] = {}
    created_at: float = Field(default_factory=time.time)

    def print(self) -> None:
        console.rule("Pipeline report")
        console.print("")

        for name, result in self.results.items():
            pipeline_duration = (
                naturaldelta(result.duration) if result.duration is not None else "Unknown"
            )
            table = Table(
                title=(f"Pipeline '{name}'" f": {result.status.name} " f"in {pipeline_duration}"),
                expand=True,
                show_lines=True,
                safe_box=True,
                box=box.SQUARE,
            )
            table.add_column("Name")
            table.add_column("Type")
            table.add_column("Stage")
            table.add_column("Started at")
            table.add_column("Duration")
            table.add_column("Status")
            table.add_column("Exit code")
            table.add_column("Can fail")

            for index, stage in enumerate(result.plan):
                for job_name in stage:
                    if job_name not in result.jobs:
                        logging.warning("Job %s has no report. Probably never ran!", job_name)
                        continue

                    job_result = result.jobs[job_name]

                    job_status = Text("Unknown", style="gray")
                    if job_result.status is not None:
                        if job_result.status is JobStatus.SUCCESS:
                            style = "green"
                        elif job_result.status is JobStatus.SKIPPED:
                            style = "yellow"
                        else:
                            style = "red"

                        job_status = Text(job_result.status.name, style=style)

                    job = self.pipelines[name].jobs[job_name]
                    table.add_row(
                        job_name,
                        str(type(job).__name__),
                        str(index + 1),
                        str(datetime.datetime.fromtimestamp(job_result.created_at)),
                        naturaldelta(job_result.duration)
                        if job_result.duration is not None
                        else "No data",
                        job_status,
                        str(job_result.exit_code)
                        if job_result.exit_code is not None
                        else "Unknown",
                        "Yes" if job.can_fail else "No",
                    )

            console.print(table)
