# init 할 때 대상 프로젝트에 .specify/ 폴더 뼈대를 만드는 도구
# ※ copy와 반대 — 여기서는 "지금 cd 한 프로젝트 폴더"에 만듦 (repo 루트 아님)

from __future__ import annotations

from pathlib import Path

# 프로젝트 루트에 생기는 폴더 이름
SPECIFY_DIR = ".specify"

# 3-1: 빈 폴더만 (md 복사는 3-3~)
INIT_DIRS = (
    ".specify/templates",
    ".specify/memory",
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
