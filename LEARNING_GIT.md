# HYspec 학습 — Git 구간

> **용도:** 단계마다 커밋·태그로 학습 구간을 남긴다.  
> **원칙:** 한 커밋 = 로드맵 한 칸. **동작하는 상태**만 커밋.

---

## 지금 repo (step-7)

| 항목 | 값 |
|------|-----|
| **태그** | `step-7-clarify` |
| **포함** | clarify skill + `.specify/feature.json` |
| **GitHub** | `origin/master` |

```powershell
git log -5 --oneline --decorate
git tag -l "step-*"
```

---

## 로드맵

| 구간 | 태그 | 포함 내용 | 상태 |
|:---:|------|-----------|:----:|
| step-1 ~ step-6 | `step-1-cli` … `step-6-sdd` | CLI + SDD 골격 | ✅ |
| step-7 | `step-7-clarify` | clarify skill + feature.json | ✅ **지금** |
| step-8 | (예정) | plan/tasks Agent skill | ⏳ 다음 |

---

## diff 연습

```powershell
git diff --stat step-6-sdd step-7-clarify
git show feature기억
```

---

## 자주 쓰는 명령

```powershell
git checkout step-6-sdd
git checkout step-7-clarify
git checkout master
```

---

## 커밋하지 않는 것

- `.venv/`, `__pycache__/`, `*.pyc`
- 테스트용 복사 폴더 (`hyspec-test/` 등)
