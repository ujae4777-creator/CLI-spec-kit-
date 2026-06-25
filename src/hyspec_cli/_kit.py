# kit md 4개가 어디 있는지 찾는 도구 (copy 명령이 씀)
# ※ 터미널에서 cd 한 "지금 폴더"가 아님!
#    → spec-first-kit 프로젝트 폴더( pyproject.toml 있는 곳 )을 찾음

from __future__ import annotations

from pathlib import Path

# 짧은 이름 → repo 루트에 있는 md 파일 이름
# (예: specify → SPECIFY.md)
KIT_FILES: dict[str, str] = {
    "constitution": "CONSTITUTION.md",
    "specify": "SPECIFY.md",
    "clarify": "CLARIFY.md",
    "plan": "PLAN.md",
    "tasks": "TASKS.md",
}


def kit_repo_root() -> Path:
    # spec-first-kit 루트 찾기 (pyproject.toml 있는 폴더)
    # pip install -e . 해도 md는 repo에 그대로 → 여기서 찾아야 함
    current = Path(__file__).resolve().parent  # _kit.py 있는 폴더부터
    for _ in range(6):  # 위로 올라가며 pyproject.toml 찾기
        if (current / "pyproject.toml").is_file():
            return current  # 여기가 spec-first-kit 루트
        if current.parent == current:
            break
        current = current.parent
    raise FileNotFoundError(
        "Kit repo not found. pip install -e . 로 설치했는지 확인하세요."
    )


def kit_file_path(name: str) -> Path:
    # repo 루트에서 md 하나 집어 오기
    # 예: "specify" → ...\spec-first-kit\SPECIFY.md
    # (어느 폴더에서 hyspec 치든 같은 경로)
    filename = KIT_FILES.get(name)
    if filename is None:
        known = ", ".join(sorted(KIT_FILES))
        raise KeyError(f"Unknown kit file {name!r}. Known: {known}")
    path = kit_repo_root() / filename
    if not path.is_file():
        raise FileNotFoundError(f"Kit file not found: {path}")
    return path
