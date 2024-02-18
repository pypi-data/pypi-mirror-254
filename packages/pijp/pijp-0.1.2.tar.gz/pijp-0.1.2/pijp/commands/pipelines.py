import click

from rich.table import Table

from pijp.config import Manifest
from pijp.utils.console import console


@click.command(help="Lists all available pipelines defined in the manifest.")
@click.pass_context
def pipelines(ctx: click.Context) -> None:
    manifest: Manifest = ctx.obj["manifest"]

    table = Table(expand=True)
    table.add_column("Title")
    table.add_column("Description")
    table.add_column("Jobs")

    for name, pipeline in manifest.pipelines.items():
        table.add_row(name, pipeline.description, str(len(pipeline.jobs)))

    console.print(table)
