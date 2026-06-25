# E2E 워크스루 — SDD 한 사이클

> 시나리오: [`SCENARIO.md`](./SCENARIO.md)  
> **목표:** CLI 로 뼈대 깔고 → Cursor skill 로 문서 채우고 → implement 까지 **한 번** 경험.

---

## 준비

```powershell
# 1) HYspec 설치 (repo 루트)
cd C:\path\to\spec-first-kit
pip install -e .

# 2) 실습 폴더 (gitignore 된 hyspec-test 써도 됨)
mkdir C:\path\to\my-e2e
cd C:\path\to\my-e2e

# 3) Cursor 로 이 폴더 열기
```

| 도구 | 역할 |
|------|------|
| **터미널** | `hyspec` CLI |
| **Cursor Agent** | `hyspec-*` skill 로 md 작성·검증·구현 |

---

## 흐름 한눈에

```text
init → constitution → feature → specify → clarify → checklist
  → plan → tasks → analyze → implement
```

| 단계 | CLI | Cursor skill |
|------|-----|--------------|
| ① 설치 | `hyspec init` | — |
| ② 헌법 | — | hyspec-constitution |
| ③ feature | `hyspec feature "…"` | — |
| ④ spec | — | hyspec-specify |
| ⑤ clarify | — | hyspec-clarify |
| ⑥ checklist | — | hyspec-checklist |
| ⑦ plan | `hyspec plan` | hyspec-plan |
| ⑧ tasks | `hyspec tasks` | hyspec-tasks |
| ⑨ analyze | — | hyspec-analyze |
| ⑩ implement | — | hyspec-implement |

---

## ① init

```powershell
hyspec init
```

**확인:**

```powershell
Test-Path .specify\init-options.json          # True
(Get-ChildItem .cursor\skills).Count            # 8
```

---

## ② constitution (skill)

Cursor 채팅 예:

```text
hyspec-constitution skill 따라 .specify/memory/constitution.md 채워줘.
이 프로젝트는 로컬 단일 사용자, 단순함 우선.
```

**확인:** `constitution.md` 가 빈 템플릿이 아닌지.

---

## ③ feature (CLI)

```powershell
hyspec feature "오늘 기분 한 줄 메모"
```

**확인:**

```powershell
Get-Content .specify\feature.json
Get-ChildItem specs\
# specs\001-mood-one-line\spec.md (이름은 slug 에 따라 다름)
```

---

## ④ specify (skill)

```text
hyspec-specify skill 사용. SCENARIO.md 내용을 spec.md 에 반영해줘.
경로: examples/e2e-mini/SCENARIO.md (kit repo) 또는 아래 스토리 요약.
```

스토리 요약: 오늘 기분 한 줄 저장, 같은 날 정책 명확, 날짜순 조회. 로그인·공유 제외.

**확인:** `spec.md` 에 문제·범위·완료기준. **기술 스택 없음.**

---

## ⑤ clarify (skill)

```text
hyspec-clarify skill 로 spec.md TBD 정리해줘.
특히 "같은 날 두 번째 메모" 는 덮어쓰기 vs 거부 중 하나로 고정.
```

**게이트:** plan 하기 전 WHAT/WHY 만으로 이해되면 통과.

---

## ⑥ checklist (skill)

```text
hyspec-checklist skill 로 ux checklist 만들어줘.
spec 요구사항 품질만, 구현 테스트 문장 금지.
```

**확인:**

```powershell
Get-ChildItem specs\*\checklists\
# 예: specs\001-...\checklists\ux.md
```

---

## ⑦ plan (CLI + skill)

```powershell
hyspec plan
```

```text
hyspec-plan skill 로 plan.md 채워줘.
로컬 파일 저장, Python CLI 또는 단순 HTML 중 하나로 제안해줘.
```

**확인:** `plan.md` 에 스택·모듈·파일 구조. spec 범위 안.

---

## ⑧ tasks (CLI + skill)

```powershell
hyspec tasks
```

```text
hyspec-tasks skill 로 tasks.md 를 plan 순서대로 쪼개줘.
```

**확인:** 각 task 에 **파일/행동**이 구체적.

---

## ⑨ analyze (skill)

```text
hyspec-analyze skill 로 spec·plan·tasks 정합 검사해줘.
```

**게이트:** 불일치 0건 또는 수정 후 재검사. 통과 전 **implement 하지 않기**.

---

## ⑩ implement (skill)

```text
hyspec-implement skill 로 tasks.md 순서대로 구현해줘.
constitution.md 규칙 지켜.
```

**확인:** tasks 의 완료 기준을 **실제로 실행**해 본다.

---

## 완료 시 파일 트리 (예시)

```text
my-e2e/
├── .specify/
│   ├── init-options.json
│   ├── feature.json
│   ├── memory/constitution.md
│   └── templates/ ...
├── .cursor/skills/          (8개)
├── specs/001-mood-one-line/
│   ├── spec.md
│   ├── plan.md
│   ├── tasks.md
│   └── checklists/ux.md
└── src/ ...                 (implement 산출물)
```

---

## 자주 하는 실수

| 실수 | 올바른 순서 |
|------|-------------|
| spec 에 React/SQLite 먼저 씀 | plan 층으로 미룸 |
| plan 없이 tasks | `hyspec plan` 먼저 |
| analyze 건너뜀 | implement 전 analyze |
| checklist 에 "버튼 클릭 테스트" | "요구사항이 정의됐는가?" 형태 |

---

## 다시 처음부터 (같은 폴더)

```powershell
hyspec init --force    # kit·skill 덮어쓰기
# specs/ 는 그대로 — 새 feature 는 hyspec feature 로 추가
```

---

## kit repo 에서 시나리오만 읽기

```powershell
cd C:\path\to\spec-first-kit\examples\e2e-mini
Get-Content SCENARIO.md
```

실습 프로젝트는 **별도 폴더**에서 `hyspec init` 하는 것을 권장.
