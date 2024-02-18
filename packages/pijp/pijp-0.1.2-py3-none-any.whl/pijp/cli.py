import logging
import os

import click

from rich.logging import RichHandler

from pijp.commands import run, pipelines, plan
from pijp.config.manifest import Manifest
from pijp.utils.console import console
from pijp.utils.ids import get_runner_id


def setup_root_logger(debug: bool) -> None:
    """
    Sets up the root logger with specified logging level and format.

    Args:
        debug (bool): If True, sets the logging level to DEBUG, otherwise INFO.
    """

    logging.basicConfig(
        level=logging.DEBUG if debug else logging.INFO,
        format="%(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            RichHandler(
                console=console,
                show_path=False,
            )
        ],
    )


@click.group()
@click.option(
    "-f",
    "--file",
    type=str,
    default="pijp.yml",
    help="Specify the manifest file to use (default: pijp.yml).",
)
@click.option(
    "--debug",
    is_flag=True,
    help="Enable debug mode for verbose logging.",
)
@click.version_option()
@click.pass_context
def cli(ctx: click.Context, file: str, debug: bool) -> None:
    """
    Main entry point for the CLI.

    Manages and orchestrates data processing tasks.
    Use this CLI to interact with the pipeline system, providing options
    to specify a manifest file and enable debug mode.
    """

    ctx.ensure_object(dict)

    ctx.obj["debug"] = debug
    setup_root_logger(debug)

    ctx.obj["runner_id"] = get_runner_id()
    ctx.obj["manifest_path"] = os.path.abspath(file)
    ctx.obj["manifest"] = Manifest.load_file(ctx.obj["manifest_path"])


cli.add_command(pipelines)
cli.add_command(plan)
cli.add_command(run)


def main() -> None:
    """
    Executes the CLI application.

    This function is the primary entry point for running the CLI.
    It handles command-line arguments and manages the execution flow.
    """

    try:
        cli()  # pylint: disable=E1120
    except Exception as exc:  # pylint: disable=W0718
        logging.error(exc)
