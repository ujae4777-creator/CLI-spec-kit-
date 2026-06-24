"""HYspec CLI."""

from __future__ import annotations

import typer

from ._version import __version__

# hyspec 프로그램 본체 (아무것도 안 치면 도움말 보여줌)
app = typer.Typer(
    no_args_is_help=True,
    help="HYspec — Spec-Driven Development CLI.",
)


@app.callback()
def root() -> None:
    """HYspec root command group."""


# hyspec version 이라고 치면 이 함수가 실행돼요
@app.command("version")
def version_cmd() -> None:
    """Show CLI version."""
    typer.echo(__version__)


# pyproject.toml에서 hyspec = "hyspec_cli:main" 이 가리키는 곳
def main() -> None:
    app()


if __name__ == "__main__":
    main()
