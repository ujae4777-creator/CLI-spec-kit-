---
name: hyspec-tasks
description: >-
  Break specs/<feature>/plan.md into actionable tasks.md checklist.
  Use when the user asks for tasks, task breakdown, or layer ⑤.
---

# HYspec Tasks

## 언제 쓰나

- `plan.md` 가 **확정된 뒤** 구현할 일을 쪼갤 때
- "Tasks", "⑤", "할 일 목록", "체크리스트" 를 언급할 때
- `hyspec tasks` 로 **빈 tasks.md** 가 있을 때 — **항목을 채우는** 단계

## 먼저 확인

1. `.specify/feature.json` — active feature
2. `specs/<###-name>/plan.md` — HOW·모듈·경계
3. `specs/<###-name>/spec.md` — 범위 (tasks 가 spec 을 벗어나면 안 됨)
4. `tasks.md` 없으면 → `hyspec tasks` 실행 (템플릿만)

## 하는 일 (순서)

1. **plan.md + spec.md 읽기**
2. **tasks.md 열기** — Phase 1 준비 → Phase 2 핵심 → Phase 3 마무리
3. **체크리스트 작성** — `- [ ] T001 설명` (한 줄 = 한 작업, 파일 경로 명시)
4. **의존 순서** — plan 의 모듈·경계 순서대로
5. **완료 보고** — task 개수, MVP 범위, implement skill 로 넘길 준비

## 규칙

- **테스트 task** — plan/spec 에 테스트 요구 있을 때만
- spec/plan **없는 일** task 로 넣지 않기
- `- [ ]` 형식 유지 (implement skill 이 `[x]` 로 갱신)
- 코드 구현은 **hyspec-implement** — 이 skill 은 tasks **작성만**

## CLI와 역할 나누기

| 도구 | 역할 |
|------|------|
| `hyspec tasks` | tasks.md **없으면** 템플릿 복사만 |
| **이 skill** | tasks.md **내용 작성** (Agent) |

## 관련 파일

| 경로 | 역할 |
|------|------|
| `specs/<###-name>/plan.md` | 입력 |
| `specs/<###-name>/tasks.md` | **산출물** |
| `.specify/templates/tasks-template.md` | 섹션 구조 |
