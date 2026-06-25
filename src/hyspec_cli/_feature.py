# feature(기능) 하나마다 specs/001-이름/ 폴더를 만드는 도구
# ※ init으로 .specify/ 가 있어야 spec-template.md 를 spec.md 로 복사할 수 있음

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

from ._init import specify_root

SPECS_DIR = "specs"
SPEC_TEMPLATE = ".specify/templates/spec-template.md"
FEATURE_JSON = "feature.json"


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

    save_feature_json(project_dir, feature_dir)
    return feature_dir


def feature_json_path(project_dir: Path) -> Path:
    return specify_root(project_dir) / FEATURE_JSON


def save_feature_json(project_dir: Path, feature_dir: Path) -> Path:
    # Spec Kit 와 같이 "지금 작업 중 feature" 경로 저장 (상대 경로)
    rel = feature_dir.relative_to(project_dir.resolve()).as_posix()
    path = feature_json_path(project_dir)
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {"feature_directory": rel}
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return path


def load_feature_dir_from_json(project_dir: Path) -> Path | None:
    path = feature_json_path(project_dir)
    if not path.is_file():
        return None
    data = json.loads(path.read_text(encoding="utf-8"))
    rel = data.get("feature_directory")
    if not isinstance(rel, str) or not rel.strip():
        raise FileNotFoundError(f"Invalid {path}: missing feature_directory")
    feature_dir = project_dir / rel
    if not feature_dir.is_dir():
        raise FileNotFoundError(f"Feature in {path} not found: {rel}")
    return feature_dir


def resolve_feature_dir(project_dir: Path, name: str | None = None) -> Path:
    # specs/001-foo/ 고르기 — 이름 없으면 feature.json → 없으면 번호 최대
    specs = project_dir / SPECS_DIR
    if not specs.is_dir():
        raise FileNotFoundError("No specs/ folder. Run hyspec feature first.")

    if name is not None:
        feature_dir = specs / name
        if not feature_dir.is_dir():
            raise FileNotFoundError(f"Feature not found: {feature_dir}")
        return feature_dir

    pinned = load_feature_dir_from_json(project_dir)
    if pinned is not None:
        return pinned

    candidates = [
        item
        for item in specs.iterdir()
        if item.is_dir() and len(item.name) >= 3 and item.name[:3].isdigit()
    ]
    if not candidates:
        raise FileNotFoundError("No feature folders in specs/.")
    return max(candidates, key=lambda item: int(item.name[:3]))
