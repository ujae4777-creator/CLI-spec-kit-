# HYspec 학습 — Git 구간

> **용도:** 단계마다 커밋·태그로 학습 구간을 남긴다.  
> **원칙:** 한 커밋 = 로드맵 한 칸. **동작하는 상태**만 커밋.

---

## 지금 repo (step-6 · 로드맵 완료)

| 항목 | 값 |
|------|-----|
| **태그** | `step-6-sdd` |
| **포함** | `plan` + `tasks` + implement skill · SDD 파이프라인 |
| **GitHub** | `origin/master` |

```powershell
git log -8 --oneline --decorate
git tag -l "step-*"
```

---

## 로드맵 (6단계) — 전부 완료

| 구간 | 태그 | 포함 내용 | 상태 |
|:---:|------|-----------|:----:|
| step-1 | `step-1-cli` | CLI + `version` + kit md 4종 | ✅ |
| step-2 | `step-2-copy` | `_kit.py` + `hyspec copy` | ✅ |
| step-3 | `step-3-init` | `hyspec init` → `.specify/` + md | ✅ |
| step-4 | `step-4-scripts` | `feature` + scripts/ + specs/ | ✅ |
| step-5 | `step-5-skill` | Cursor skill (specify) | ✅ |
| step-6 | `step-6-sdd` | `plan` / `tasks` + implement skill | ✅ **끝** |

---

## diff 연습

```powershell
# step-5 vs step-6 (SDD 마무리)
git diff --stat step-5-skill HEAD
git diff step-5-skill HEAD

# plan/tasks 명령 커밋
git show plan tasks명령
```

---

## 전체 구간 한눈에

```powershell
git diff --stat step-1-cli step-6-sdd
```

---

## 자주 쓰는 명령

```powershell
git log --oneline --decorate
git checkout step-1-cli          # 1단계
git checkout step-6-sdd          # 6단계 (최종 학습 스냅샷)
git checkout master              # 최신 작업
```

---

## 커밋하지 않는 것

- `.venv/`, `__pycache__/`, `*.pyc`
- 테스트용 복사 폴더 (`hyspec-test/` 등)
