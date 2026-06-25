# HYspec 학습 — Git 구간

> **용도:** 단계마다 커밋·태그로 학습 구간을 남긴다.  
> **원칙:** 한 커밋 = 로드맵 한 칸. **동작하는 상태**만 커밋.

---

## 지금 repo (step-5)

| 항목 | 값 |
|------|-----|
| **태그** | `step-5-skill` |
| **포함** | init + `.cursor/skills/hyspec-specify` |
| **GitHub** | `origin/master` |

```powershell
git log -7 --oneline --decorate
git tag -l "step-*"
```

---

## 로드맵 (6단계)

| 구간 | 태그 | 포함 내용 | 상태 |
|:---:|------|-----------|:----:|
| step-1 | `step-1-cli` | CLI + `version` + kit md 4종 | ✅ |
| step-2 | `step-2-copy` | `_kit.py` + `hyspec copy` | ✅ |
| step-3 | `step-3-init` | `hyspec init` → `.specify/` + md | ✅ |
| step-4 | `step-4-scripts` | `feature` + scripts/ + specs/ | ✅ |
| step-5 | `step-5-skill` | Cursor skill 1개 | ✅ **지금** |
| step-6 | `step-6-sdd` | tasks / implement | ⏳ 다음 |

---

## diff 연습

```powershell
# step-4 vs step-5 (skill 추가분)
git diff --stat step-4-scripts HEAD
git diff step-4-scripts HEAD

# skill 복사 커밋 하나
git show skill복사
```

---

## step-6 이후 (초안)

```powershell
git commit -m "step-6: sdd"
git tag -a step-6-sdd -m "Learning: tasks implement"
git push origin master
git push origin step-6-sdd
```

---

## 자주 쓰는 명령

```powershell
git log --oneline --decorate
git checkout step-4-scripts      # 4단계 스냅샷 보기
git checkout step-5-skill        # 5단계 스냅샷 보기
git checkout master              # 최신으로
```

---

## 커밋하지 않는 것

- `.venv/`, `__pycache__/`, `*.pyc`
- 테스트용 복사 폴더 (`hyspec-test/` 등)
