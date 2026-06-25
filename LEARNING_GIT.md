# HYspec 학습 — Git 구간

> **용도:** 단계마다 커밋·태그로 학습 구간을 남긴다.  
> **원칙:** 한 커밋 = 로드맵 한 칸. **동작하는 상태**만 커밋.

---

## 지금 repo (step-11)

| 항목 | 값 |
|------|-----|
| **태그** | `step-11-checklist` |
| **포함** | hyspec-checklist skill + analyze 역할 분리 |
| **GitHub** | `origin/master` |

```powershell
git log -5 --oneline --decorate
git tag -l "step-*"
```

---

## 로드맵

| 구간 | 태그 | 포함 내용 | 상태 |
|:---:|------|-----------|:----:|
| step-1 ~ step-10 | … `step-10-init` | CLI + SDD + init-options | ✅ |
| step-11 | `step-11-checklist` | checklist skill + analyze 정리 | ✅ **지금** |
| step-12 | (예정) | e2e 실습 또는 wheel 번들 | ⏳ 다음 |

---

## diff 연습

```powershell
git diff --stat step-10-init step-11-checklist
git show checklist스킬
```

---

## 자주 쓰는 명령

```powershell
git checkout step-10-init
git checkout step-11-checklist
git checkout master
```

---

## 커밋하지 않는 것

- `.venv/`, `__pycache__/`, `*.pyc`
- 테스트용 복사 폴더 (`hyspec-test/` 등)
