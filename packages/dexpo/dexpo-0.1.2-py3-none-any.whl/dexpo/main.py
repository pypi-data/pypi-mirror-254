from os import getenv
from typing import Annotated

import typer

from .choices import Platform
from .callbacks import project_callback, version_callback
from .info import get_project_info
from .outputs import write_project_info


app = typer.Typer()


@app.command()
def main(
    project: Annotated[
        str,
        typer.Argument(
            callback=project_callback,
            show_default=False,
            help="Project to search for (i.e. pandas).",
        ),
    ],
    api_key: Annotated[
        str,
        typer.Option(
            show_default=False,
            help="libraries.io API key. Key must be provided or stored in env var called 'LIBRARIESIO_API_KEY'. Create an account to get your key. https://libraries.io",
        ),
    ] = getenv("LIBRARIESIO_API_KEY"),
    platform: Annotated[
        Platform,
        typer.Option(
            show_choices=True,
            help="Package managment platform to search.",
            case_sensitive=False,
        ),
    ] = Platform.pypi,
    report: Annotated[
        bool,
        typer.Option(
            help="Enable to write console output to an svg file in cwd.",
        ),
    ] = False,
    version: Annotated[
        bool,
        typer.Option(
            callback=version_callback,
            is_eager=True,
            help="Print the installed dexpo version and exit.",
        ),
    ] = None,
):
    """
    Print a basic report (and optionally write to an SVG file with `--report` flag) about a PROJECT.
    """
    project_info = get_project_info(project, platform.value, api_key)
    write_project_info(project_info, report)
