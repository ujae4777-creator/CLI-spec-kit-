"""HYspec CLI."""

from __future__ import annotations

import typer

from ._version import __version__

app = typer.Typer(
    no_args_is_help=True,
    help="HYspec — Spec-Driven Development CLI.",
)


@app.callback()
def root() -> None:
    """HYspec root command group."""


@app.command("version")
def version_cmd() -> None:
    """Show CLI version."""
    typer.echo(__version__)


def main() -> None:
    app()


if __name__ == "__main__":
    main()
