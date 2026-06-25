# HYspec 학습 — Git 구간

> **용도:** 단계마다 커밋·태그로 학습 구간을 남긴다.  
> **원칙:** 한 커밋 = 로드맵 한 칸. **동작하는 상태**만 커밋.

---

## 지금 repo (step-10)

| 항목 | 값 |
|------|-----|
| **태그** | `step-10-init` |
| **포함** | init-options + setup scripts + init --force |
| **GitHub** | `origin/master` |

```powershell
git log -5 --oneline --decorate
git tag -l "step-*"
```

---

## 로드맵

| 구간 | 태그 | 포함 내용 | 상태 |
|:---:|------|-----------|:----:|
| step-1 ~ step-9 | … `step-9-quality` | CLI + SDD + quality skills | ✅ |
| step-10 | `step-10-init` | init-options + setup scripts + --force | ✅ **지금** |
| step-11 | (예정) | core_pack wheel 또는 e2e 실습 | ⏳ 다음 |

---

## diff 연습

```powershell
git diff --stat step-9-quality step-10-init
git show init옵션
```

---

## 자주 쓰는 명령

```powershell
git checkout step-9-quality
git checkout step-10-init
git checkout master
```

---

## 커밋하지 않는 것

- `.venv/`, `__pycache__/`, `*.pyc`
- 테스트용 복사 폴더 (`hyspec-test/` 등)
