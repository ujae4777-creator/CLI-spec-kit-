# HYspec 학습 — Git 구간 초안

> **용도:** 단계마다 커밋·태그로 학습 구간을 남긴다.  
> **원칙:** 한 커밋 = 로드맵 한 칸. **동작하는 상태**만 커밋.

---

## 구간 정의 (6단계)

| 구간 | 태그 | 포함 내용 | 상태 |
|:---:|------|-----------|:----:|
| step-0 | `step-0-cli` | `pyproject.toml`, `hyspec_cli` + `version`만 | 📋 과거 (이미 지나침) |
| step-1 | — | (선택) kit md 4종만, CLI 없음 | 📋 생략 가능 |
| step-2 | `step-2-copy` | step-0 + `_kit.py` + `hyspec copy` | ✅ **지금 repo** |
| step-3 | `step-3-init` | `hyspec init` → `.specify/` | ⏳ 다음 |
| step-4 | `step-4-scripts` | `scripts/` + feature 폴더 규칙 | ⏳ |
| step-5 | `step-5-skill` | Cursor skill 1개 | ⏳ |
| step-6 | `step-6-sdd` | tasks / implement 쪽 | ⏳ |

---

## 지금 시작할 때 (catch-up 1커밋)

이미 step-2까지 코드가 있으므로 **과거 step-0 커밋을 되살리지 않고**,  
**현재 상태 = step-2 baseline** 으로 잡는다.

### 1) 저장소 초기화

```powershell
cd C:\Users\정우재\Desktop\spec-first-kit
git init
```

### 2) 첫 커밋 (step-2)

```powershell
git add .
git status
git commit -m "$(cat <<'EOF'
step-2: add hyspec copy command

- pyproject.toml: hyspec CLI entry point
- hyspec version + hyspec copy
- _kit.py: resolve kit md from repo root
- kit templates: CONSTITUTION, SPECIFY, CLARIFY, PLAN
EOF
)"
git tag -a step-2-copy -m "Learning: version + copy"
```

PowerShell에서 HEREDOC이 안 되면:

```powershell
git commit -m "step-2: add hyspec copy command" -m "- pyproject.toml: hyspec CLI entry point" -m "- hyspec version + hyspec copy" -m "- _kit.py: resolve kit md from repo root" -m "- kit templates: CONSTITUTION, SPECIFY, CLARIFY, PLAN"
git tag -a step-2-copy -m "Learning: version + copy"
```

---

## 앞으로 커밋 메시지 초안

### step-3-init

```
step-3: add hyspec init command

Install .specify/templates/, memory/constitution.md, init-options.json.
Mirrors specify init shared_infra (learning edition).
```

```powershell
git tag -a step-3-init -m "Learning: hyspec init / .specify layout"
```

### step-4-scripts

```
step-4: add feature folder script

PowerShell script to create specs/001-name/ (minimal).
```

```powershell
git tag -a step-4-scripts -m "Learning: specs folder scaffolding"
```

### step-5-skill

```
step-5: install clarify skill for Cursor

Copy CLARIFY.md into .cursor/skills/ on init or separate command.
```

```powershell
git tag -a step-5-skill -m "Learning: first agent skill"
```

### step-6-sdd

```
step-6: extend SDD pipeline (tasks or implement stub)

Document or minimal command aligned with Spec Kit workflow.
```

```powershell
git tag -a step-6-sdd -m "Learning: SDD pipeline extension"
```

---

## 자주 쓰는 명령

```powershell
# 지금 구간 확인
git log --oneline --decorate

# step-2 상태로 되돌리기 (작업 트리만)
git checkout step-2-copy -- .

# step-2와 step-3 diff (init 만든 뒤)
git diff step-2-copy..HEAD

# 태그 목록
git tag -l "step-*"
```

---

## step-0을 꼭 남기고 싶다면 (선택, 나중에)

새 브랜치에서 **역사 재연** — **필수 아님**.

1. `git checkout -b replay`
2. 파일을 version-only로 수동 축소 → commit `step-0-cli`
3. copy 추가 → commit `step-2-copy`
4. 학습용으로만 `replay` 브랜치 유지, 일상은 `main`

---

## Spec Kit 대照 (커밋 볼 때)

| HYspec 태그 | Spec Kit 참고 |
|-------------|----------------|
| step-2-copy | `shared_infra` 일부, 수동 copy |
| step-3-init | `commands/init.py`, `shared_infra.py` |
| step-4-scripts | `scripts/powershell/create-new-feature.ps1` |
| step-5-skill | `integrations/cursor_agent`, `templates/commands/` |

---

## 커밋하지 않는 것

- `.venv/`, `__pycache__/`, `*.pyc`
- 테스트용 복사 폴더 (`hyspec-test/` 등) — 만들면 `.gitignore`에 추가
