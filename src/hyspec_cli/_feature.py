# feature(기능) 하나마다 specs/001-이름/ 폴더를 만드는 도구
# ※ init으로 .specify/ 가 있어야 spec-template.md 를 spec.md 로 복사할 수 있음

from __future__ import annotations

import re
import shutil
from pathlib import Path

from ._init import specify_root

SPECS_DIR = "specs"
SPEC_TEMPLATE = ".specify/templates/spec-template.md"


def slugify(description: str) -> str:
    # "Add user login" → user-login (짧은 단어·기호 제거, 최대 3단어)
    words = re.sub(r"[^a-z0-9\s]", " ", description.lower()).split()
    picked = [word for word in words if len(word) >= 3][:3]
    if picked:
        return "-".join(picked)
    return "feature"


def next_feature_number(project_dir: Path) -> int:
    # specs/ 안 기존 001-*, 002-* … 번호 중 가장 큰 다음 번호
    specs = project_dir / SPECS_DIR
    highest = 0
    if specs.is_dir():
        for item in specs.iterdir():
            if item.is_dir() and len(item.name) >= 3 and item.name[:3].isdigit():
                highest = max(highest, int(item.name[:3]))
    return highest + 1


def feature_branch_name(project_dir: Path, description: str) -> str:
    number = next_feature_number(project_dir)
    return f"{number:03d}-{slugify(description)}"


def create_feature(project_dir: Path, description: str) -> Path:
    # specs/001-slug/ + spec.md (템플릿 복사)
    if not specify_root(project_dir).is_dir():
        raise FileNotFoundError(
            f"{specify_root(project_dir)} not found. Run hyspec init first."
        )

    branch = feature_branch_name(project_dir, description)
    feature_dir = project_dir / SPECS_DIR / branch
    feature_dir.mkdir(parents=True, exist_ok=True)

    template = project_dir / SPEC_TEMPLATE
    spec_file = feature_dir / "spec.md"
    if template.is_file():
        shutil.copy2(template, spec_file)
    else:
        raise FileNotFoundError(f"Spec template not found: {template}")

    return feature_dir
