from typing import Optional

import click

from rich.tree import Tree

from pijp.config import Manifest
from pijp.utils.console import console


@click.command(help="Generates an execution plan for the specified pipeline.")
@click.argument("name")
@click.option(
    "-c",
    "--concurrent",
    type=int,
    default=None,
    help="Number of concurrent jobs",
)
@click.pass_context
def plan(ctx: click.Context, name: str, concurrent: Optional[int]) -> None:
    manifest: Manifest = ctx.obj["manifest"]

    if name not in manifest.pipelines:
        raise ValueError(f"No pipeline named {name}")

    pipeline = manifest.pipelines[name]
    pipeline_plan = pipeline.build_graph().topological_sort()
    max_jobs = concurrent or pipeline.concurrent

    tree = Tree("Stages")
    for stage_index, stage in enumerate(pipeline_plan):
        stage_leaf = tree.add(f"Stage {stage_index + 1}")

        batches = pipeline.prepare_batches(stage, max_jobs)
        for batch_index, batch in enumerate(batches):
            batch_leaf = stage_leaf.add(f"Batch {batch_index + 1}")

            for job_name in batch:
                batch_leaf.add(
                    f"{job_name} (Isolated)" if pipeline.jobs[job_name].isolated else job_name
                )

    console.print(tree)
