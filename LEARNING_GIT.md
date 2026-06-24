# HYspec 학습 — Git 구간

> **용도:** 단계마다 커밋·태그로 학습 구간을 남긴다.  
> **원칙:** 한 커밋 = 로드맵 한 칸. **동작하는 상태**만 커밋.

---

## 지금 repo (step-1)

| 항목 | 값 |
|------|-----|
| **태그** | `step-1-cli` |
| **포함** | `hyspec version`만 · kit md 4종(루트, CLI 배포 없음) |
| **GitHub** | `origin/master` |

```powershell
git log -1 --oneline --decorate
git tag -l "step-*"
```

---

## 로드맵 (6단계)

| 구간 | 태그 | 포함 내용 | 상태 |
|:---:|------|-----------|:----:|
| step-1 | `step-1-cli` | CLI + `version` + kit md 4종 | ✅ **지금** |
| step-2 | `step-2-copy` | `_kit.py` + `hyspec copy` | ⏳ 다음 |
| step-3 | `step-3-init` | `hyspec init` → `.specify/` | ⏳ |
| step-4 | `step-4-scripts` | `scripts/` + feature 폴더 | ⏳ |
| step-5 | `step-5-skill` | Cursor skill 1개 | ⏳ |
| step-6 | `step-6-sdd` | tasks / implement | ⏳ |

---

## step-1 이후 커밋·태그 (초안)

### step-2-copy

```powershell
git add .
git commit -m "step-2: add hyspec copy"
git tag -a step-2-copy -m "Learning: copy command"
git push origin master
git push origin step-2-copy
```

### step-3-init

```powershell
git commit -m "step-3: add hyspec init"
git tag -a step-3-init -m "Learning: .specify layout"
```

---

## 자주 쓰는 명령

```powershell
git log --oneline --decorate
git checkout step-1-cli          # 1단계로 되돌아보기 (읽기)
git checkout master              # 최신으로
git tag -f step-1-cli            # amend 후 태그 옮기기
git push origin step-1-cli --force
```

---

## 커밋하지 않는 것

- `.venv/`, `__pycache__/`, `*.pyc`
- 테스트용 복사 폴더 (`hyspec-test/` 등)
