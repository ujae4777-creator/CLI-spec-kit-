# init 시 .cursor/skills/ 로 skill 복사 (Spec Kit cursor-agent 패턴 축소판)

from __future__ import annotations

import shutil
from pathlib import Path

from ._kit import kit_repo_root

SKILLS_DIR = ".cursor/skills"


def skills_dest(project_dir: Path) -> Path:
    return project_dir / SKILLS_DIR


def copy_init_skills(project_dir: Path) -> list[Path]:
    # kit repo skills/<name>/SKILL.md → .cursor/skills/<name>/SKILL.md
    source_root = kit_repo_root() / "skills"
    if not source_root.is_dir():
        raise FileNotFoundError(f"Kit skills not found: {source_root}")

    copied: list[Path] = []
    for skill_dir in sorted(source_root.iterdir()):
        skill_file = skill_dir / "SKILL.md"
        if not skill_dir.is_dir() or not skill_file.is_file():
            continue
        dest_dir = skills_dest(project_dir) / skill_dir.name
        dest_dir.mkdir(parents=True, exist_ok=True)
        target = dest_dir / "SKILL.md"
        shutil.copy2(skill_file, target)
        copied.append(target)
    return copied
