"""HYspec CLI."""

from __future__ import annotations

import typer

from ._version import __version__

# CLI 앱 본체. no_args_is_help=True → 인자 없이 hyspec 치면 --help 표시
app = typer.Typer(
    no_args_is_help=True,
    help="HYspec — Spec-Driven Development CLI.",
)


@app.callback()
def root() -> None:
    """HYspec root command group."""


# @app.command("version") → 터미널에서 hyspec version
@app.command("version")
def version_cmd() -> None:
    """Show CLI version."""
    typer.echo(__version__)


# pyproject.toml [project.scripts] hyspec = "hyspec_cli:main" 이 가리키는 함수
def main() -> None:
    app()


if __name__ == "__main__":
    main()
