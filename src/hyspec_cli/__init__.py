"""HYspec CLI."""

from __future__ import annotations

import shutil
from pathlib import Path

import typer

from ._feature import create_feature
from ._init import (
    copy_init_files,
    copy_init_scripts,
    create_init_dirs,
    specify_root,
    write_init_options,
)
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
    name: str = typer.Argument(help="constitution, specify, clarify, plan, tasks, checklist"),
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
def init_cmd(
    force: bool = typer.Option(
        False, "--force", help="Overwrite existing kit files, scripts, and skills"
    ),
) -> None:
    """Create .specify/ folder layout in the current directory."""
    project_dir = Path.cwd()  # 터미널에서 cd 한 곳 = 대상 프로젝트
    create_init_dirs(project_dir)
    options = write_init_options(project_dir)
    copied_files, skipped_files = copy_init_files(project_dir, force=force)
    copied_scripts, skipped_scripts = copy_init_scripts(project_dir, force=force)
    copied_skills, skipped_skills = copy_init_skills(project_dir, force=force)
    typer.echo(f"Initialized {specify_root(project_dir)}")
    typer.echo(f"  init-options → {options}")
    typer.echo(
        f"  kit: {len(copied_files)} copied"
        + (f", {len(skipped_files)} skipped" if skipped_files else "")
    )
    typer.echo(
        f"  scripts: {len(copied_scripts)} copied"
        + (f", {len(skipped_scripts)} skipped" if skipped_scripts else "")
    )
    typer.echo(
        f"  skills: {len(copied_skills)} copied"
        + (f", {len(skipped_skills)} skipped" if skipped_skills else "")
    )
    if skipped_files or skipped_scripts or skipped_skills:
        if not force:
            typer.echo("  (use --force to overwrite existing files)")


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
    typer.echo(f"  active → {feature_dir.relative_to(project_dir.resolve()).as_posix()}")


# hyspec plan — specs/.../plan.md 템플릿 깔기 (spec.md 필요)
@app.command("plan")
def plan_cmd(
    feature: str | None = typer.Argument(
        None, help="specs 폴더 이름 (없으면 번호가 가장 큰 feature)"
    ),
) -> None:
    """Scaffold plan.md if missing; otherwise point to hyspec-plan skill."""
    project_dir = Path.cwd()
    try:
        plan_file, status = scaffold_plan(project_dir, feature)
    except FileNotFoundError as exc:
        typer.secho(str(exc), fg=typer.colors.RED, err=True)
        raise typer.Exit(code=1) from exc

    if status == "created":
        typer.echo(f"Created {plan_file}")
        typer.echo("Next: use hyspec-plan skill in Cursor to fill plan.md from spec.md")
    else:
        typer.echo(f"Already exists: {plan_file}")
        typer.echo("Use hyspec-plan skill to update plan.md (CLI does not overwrite)")


# hyspec tasks — specs/.../tasks.md 템플릿 깔기 (plan.md 필요)
@app.command("tasks")
def tasks_cmd(
    feature: str | None = typer.Argument(
        None, help="specs 폴더 이름 (없으면 번호가 가장 큰 feature)"
    ),
) -> None:
    """Scaffold tasks.md if missing; otherwise point to hyspec-tasks skill."""
    project_dir = Path.cwd()
    try:
        tasks_file, status = scaffold_tasks(project_dir, feature)
    except FileNotFoundError as exc:
        typer.secho(str(exc), fg=typer.colors.RED, err=True)
        raise typer.Exit(code=1) from exc

    if status == "created":
        typer.echo(f"Created {tasks_file}")
        typer.echo("Next: use hyspec-tasks skill in Cursor to fill tasks.md from plan.md")
    else:
        typer.echo(f"Already exists: {tasks_file}")
        typer.echo("Use hyspec-tasks skill to update tasks.md (CLI does not overwrite)")


# pyproject.toml에서 hyspec = "hyspec_cli:main" 이 가리키는 곳
def main() -> None:
    app()


if __name__ == "__main__":
    main()
