# plan.md / tasks.md 를 feature 폴더에 깔아 주는 SDD 마무리 도구 (step-6)

from __future__ import annotations

import shutil
from pathlib import Path

from ._feature import resolve_feature_dir
from ._init import specify_root

PLAN_TEMPLATE = ".specify/templates/plan-template.md"
TASKS_TEMPLATE = ".specify/templates/tasks-template.md"


def _require_specify(project_dir: Path) -> None:
    if not specify_root(project_dir).is_dir():
        raise FileNotFoundError(
            f"{specify_root(project_dir)} not found. Run hyspec init first."
        )


def _copy_template(project_dir: Path, feature_dir: Path, template_rel: str, dest_name: str) -> Path:
    template = project_dir / template_rel
    if not template.is_file():
        raise FileNotFoundError(f"Template not found: {template}")
    target = feature_dir / dest_name
    shutil.copy2(template, target)
    return target


def scaffold_plan(project_dir: Path, feature: str | None = None) -> tuple[Path, str]:
    # spec.md 있어야 plan (② → ④). 있으면 복사 안 함 (step-8)
    _require_specify(project_dir)
    feature_dir = resolve_feature_dir(project_dir, feature)
    spec_file = feature_dir / "spec.md"
    if not spec_file.is_file():
        raise FileNotFoundError(f"spec.md required before plan: {spec_file}")
    target = feature_dir / "plan.md"
    if target.is_file():
        return target, "exists"
    created = _copy_template(project_dir, feature_dir, PLAN_TEMPLATE, "plan.md")
    return created, "created"


def scaffold_tasks(project_dir: Path, feature: str | None = None) -> tuple[Path, str]:
    # plan.md 있어야 tasks (④ → ⑤). 있으면 복사 안 함 (step-8)
    _require_specify(project_dir)
    feature_dir = resolve_feature_dir(project_dir, feature)
    plan_file = feature_dir / "plan.md"
    if not plan_file.is_file():
        raise FileNotFoundError(f"plan.md required before tasks: {plan_file}")
    target = feature_dir / "tasks.md"
    if target.is_file():
        return target, "exists"
    created = _copy_template(project_dir, feature_dir, TASKS_TEMPLATE, "tasks.md")
    return created, "created"
