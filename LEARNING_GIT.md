# HYspec 학습 — Git 구간

> **용도:** 단계마다 커밋·태그로 학습 구간을 남긴다.  
> **원칙:** 한 커밋 = 로드맵 한 칸. **동작하는 상태**만 커밋.

---

## 지금 repo (step-12)

| 항목 | 값 |
|------|-----|
| **태그** | `step-12-e2e` |
| **포함** | examples/e2e-mini SDD 워크스루 |
| **GitHub** | `origin/master` |

```powershell
git log -5 --oneline --decorate
git tag -l "step-*"
```

---

## 로드맵

| 구간 | 태그 | 포함 내용 | 상태 |
|:---:|------|-----------|:----:|
| step-1 ~ step-11 | … `step-11-checklist` | CLI + SDD + 8 skills | ✅ |
| step-12 | `step-12-e2e` | e2e 미니 프로젝트 가이드 | ✅ **지금** |
| step-13 | (예정) | wheel 번들 또는 prerequisites | ⏳ 다음 |

---

## diff 연습

```powershell
git diff --stat step-11-checklist step-12-e2e
git show e2e시나리오
```

---

## e2e 실습 시작

```powershell
cd examples\e2e-mini
Get-Content README.md
# 별도 폴더에서 WALKTHROUGH.md 따름
```

---

## 자주 쓰는 명령

```powershell
git checkout step-11-checklist
git checkout step-12-e2e
git checkout master
```

---

## 커밋하지 않는 것

- `.venv/`, `__pycache__/`, `*.pyc`
- 테스트용 복사 폴더 (`hyspec-test/` 등)
