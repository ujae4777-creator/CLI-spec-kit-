"""HYspec CLI."""

from __future__ import annotations

import shutil
from pathlib import Path

import typer

from ._feature import create_feature
from ._init import copy_init_files, copy_init_scripts, create_init_dirs, specify_root
from ._sdd import scaffold_plan, scaffold_tasks
from ._skill import copy_init_skills
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
    name: str = typer.Argument(help="constitution, specify, clarify, plan, tasks"),
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


# hyspec init — 지금 cd 한 폴더에 .specify/ 뼈대 만들기
@app.command("init")
def init_cmd() -> None:
    """Create .specify/ folder layout in the current directory."""
    project_dir = Path.cwd()  # 터미널에서 cd 한 곳 = 대상 프로젝트
    create_init_dirs(project_dir)
    copied = copy_init_files(project_dir)
    scripts = copy_init_scripts(project_dir)
    skills = copy_init_skills(project_dir)
    typer.echo(
        f"Initialized {specify_root(project_dir)} "
        f"({len(copied)} kit files, {len(scripts)} scripts, {len(skills)} skills)"
    )


# hyspec feature "설명" — specs/001-이름/ + spec.md 만들기
@app.command("feature")
def feature_cmd(
    description: str = typer.Argument(help="기능 설명 (폴더 이름에 반영)"),
) -> None:
    """Create specs/<###-slug>/ with spec.md from the template."""
    project_dir = Path.cwd()
    try:
        feature_dir = create_feature(project_dir, description)
    except FileNotFoundError as exc:
        typer.secho(str(exc), fg=typer.colors.RED, err=True)
        raise typer.Exit(code=1) from exc

    spec_file = feature_dir / "spec.md"
    typer.echo(f"Created {feature_dir.name}/")
    typer.echo(f"  spec.md → {spec_file}")


# hyspec plan — specs/.../plan.md 템플릿 깔기 (spec.md 필요)
@app.command("plan")
def plan_cmd(
    feature: str | None = typer.Argument(
        None, help="specs 폴더 이름 (없으면 번호가 가장 큰 feature)"
    ),
) -> None:
    """Copy plan template into the active feature folder."""
    project_dir = Path.cwd()
    try:
        plan_file = scaffold_plan(project_dir, feature)
    except FileNotFoundError as exc:
        typer.secho(str(exc), fg=typer.colors.RED, err=True)
        raise typer.Exit(code=1) from exc

    typer.echo(f"Created {plan_file}")


# hyspec tasks — specs/.../tasks.md 템플릿 깔기 (plan.md 필요)
@app.command("tasks")
def tasks_cmd(
    feature: str | None = typer.Argument(
        None, help="specs 폴더 이름 (없으면 번호가 가장 큰 feature)"
    ),
) -> None:
    """Copy tasks template into the active feature folder."""
    project_dir = Path.cwd()
    try:
        tasks_file = scaffold_tasks(project_dir, feature)
    except FileNotFoundError as exc:
        typer.secho(str(exc), fg=typer.colors.RED, err=True)
        raise typer.Exit(code=1) from exc

    typer.echo(f"Created {tasks_file}")


# pyproject.toml에서 hyspec = "hyspec_cli:main" 이 가리키는 곳
def main() -> None:
    app()


if __name__ == "__main__":
    main()
