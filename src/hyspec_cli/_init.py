# init 할 때 대상 프로젝트에 .specify/ 폴더 뼈대를 만드는 도구
# ※ copy와 반대 — 여기서는 "지금 cd 한 프로젝트 폴더"에 만듦 (repo 루트 아님)

from __future__ import annotations

import shutil
from pathlib import Path

from ._kit import kit_file_path, kit_repo_root

# 프로젝트 루트에 생기는 폴더 이름
SPECIFY_DIR = ".specify"

INIT_DIRS = (
    ".specify/templates",
    ".specify/memory",
    ".specify/scripts/powershell",
)

# kit 짧은 이름 → 프로젝트 안에 복사할 상대 경로 (copy 여러 번을 init 한 번으로)
INIT_COPIES: tuple[tuple[str, str], ...] = (
    ("constitution", ".specify/templates/constitution-template.md"),
    ("constitution", ".specify/memory/constitution.md"),
    ("specify", ".specify/templates/spec-template.md"),
    ("clarify", ".specify/templates/clarify-template.md"),
    ("plan", ".specify/templates/plan-template.md"),
    ("tasks", ".specify/templates/tasks-template.md"),
)


def specify_root(project_dir: Path) -> Path:
    # 예: project_dir / ".specify"
    return project_dir / SPECIFY_DIR


def create_init_dirs(project_dir: Path) -> list[Path]:
    # project_dir 아래 templates/, memory/ 만들기 (있어도 에러 안 남)
    created: list[Path] = []
    for rel in INIT_DIRS:
        path = project_dir / rel
        path.mkdir(parents=True, exist_ok=True)
        created.append(path)
    return created


def copy_init_files(project_dir: Path) -> list[Path]:
    # repo kit md → .specify/ 안 (S2 copy를 init에서 한 번에)
    copied: list[Path] = []
    for name, rel in INIT_COPIES:
        source = kit_file_path(name)
        target = project_dir / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        copied.append(target)
    return copied


def copy_init_scripts(project_dir: Path) -> list[Path]:
    # repo scripts/powershell/ → .specify/scripts/powershell/
    source_dir = kit_repo_root() / "scripts" / "powershell"
    if not source_dir.is_dir():
        raise FileNotFoundError(f"Kit scripts not found: {source_dir}")

    dest_dir = project_dir / ".specify" / "scripts" / "powershell"
    dest_dir.mkdir(parents=True, exist_ok=True)

    copied: list[Path] = []
    for script in sorted(source_dir.iterdir()):
        if script.is_file():
            target = dest_dir / script.name
            shutil.copy2(script, target)
            copied.append(target)
    return copied
