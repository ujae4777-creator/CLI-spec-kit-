# HYspec 학습 — Git 구간

> **용도:** 단계마다 커밋·태그로 학습 구간을 남긴다.  
> **원칙:** 한 커밋 = 로드맵 한 칸. **동작하는 상태**만 커밋.

---

## 지금 repo (step-2)

| 항목 | 값 |
|------|-----|
| **태그** | `step-2-copy` |
| **포함** | `version` + `copy` · `_kit.py` · kit md 4종 |
| **GitHub** | `origin/master` |

```powershell
git log -3 --oneline --decorate
git tag -l "step-*"
```

---

## 로드맵 (6단계)

| 구간 | 태그 | 포함 내용 | 상태 |
|:---:|------|-----------|:----:|
| step-1 | `step-1-cli` | CLI + `version` + kit md 4종 | ✅ |
| step-2 | `step-2-copy` | `_kit.py` + `hyspec copy` | ✅ **지금** |
| step-3 | `step-3-init` | `hyspec init` → `.specify/` | ⏳ 다음 |
| step-4 | `step-4-scripts` | `scripts/` + feature 폴더 | ⏳ |
| step-5 | `step-5-skill` | Cursor skill 1개 | ⏳ |
| step-6 | `step-6-sdd` | tasks / implement | ⏳ |

---

## diff 연습

```powershell
# step-1 vs step-2 (copy 추가분)
git diff --stat step-1-cli HEAD
git diff step-1-cli HEAD

# copy만 추가된 커밋 하나
git show md복사명령
```

---

## step-3 이후 (초안)

```powershell
git commit -m "step-3: init"
git tag -a step-3-init -m "Learning: .specify layout"
git push origin master
git push origin step-3-init
```

---

## 자주 쓰는 명령

```powershell
git log --oneline --decorate
git checkout step-1-cli          # 1단계 스냅샷 보기
git checkout step-2-copy         # 2단계 스냅샷 보기
git checkout master              # 최신으로
```

---

## 커밋하지 않는 것

- `.venv/`, `__pycache__/`, `*.pyc`
- 테스트용 복사 폴더 (`hyspec-test/` 등)
