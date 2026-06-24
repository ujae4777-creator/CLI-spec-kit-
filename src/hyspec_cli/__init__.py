"""HYspec CLI."""

from __future__ import annotations

import shutil
from pathlib import Path

import typer

from ._kit import kit_file_path
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


# hyspec copy specify ./out.md — repo 루트 md를 원하는 곳에 복사
@app.command("copy")
def copy_cmd(
    name: str = typer.Argument(help="constitution, specify, clarify, plan"),
    dest: Path = typer.Argument(help="복사할 파일 또는 폴더 경로"),
) -> None:
    """Copy one kit markdown file from the repo to dest."""
    try:
        source = kit_file_path(name)
    except (KeyError, FileNotFoundError) as exc:
        typer.secho(str(exc), fg=typer.colors.RED, err=True)
        raise typer.Exit(code=1) from exc

    # dest가 폴더면 원래 파일 이름 붙임 (예: ./out/ → ./out/SPECIFY.md)
    target = dest / source.name if dest.is_dir() else dest
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)
    typer.echo(f"Copied {source.name} → {target}")


# pyproject.toml에서 hyspec = "hyspec_cli:main" 이 가리키는 곳
def main() -> None:
    app()


if __name__ == "__main__":
    main()
