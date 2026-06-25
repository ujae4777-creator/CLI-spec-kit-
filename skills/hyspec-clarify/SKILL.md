---
name: hyspec-clarify
description: >-
  Clarify underspecified requirements in specs/<feature>/spec.md through
  a short interview. Use when the user asks to clarify, fill gaps in spec,
  or work on the Clarify layer (③ 모호성 제거).
---

# HYspec Clarify

## 언제 쓰나

- `spec.md` 가 **비어 있거나** `TBD` / `[NEEDS CLARIFICATION]` 이 남았을 때
- "Clarify", "③", "인터뷰", "모호한 거 정리" 를 언급할 때
- Specify(②) 다음, Plan(④) **전에** spec 을 단단히 할 때

## 먼저 확인

1. `specs/<###-name>/spec.md` 가 있는지
2. `.specify/templates/clarify-template.md` 또는 repo `CLARIFY.md` 의 **원칙** 참고
3. `.specify/memory/constitution.md` — 범위·단순성과 모순 없는지

## 하는 일 (순서)

1. **spec.md 읽기** — 빈 칸, `TBD`, `[NEEDS CLARIFICATION]`, `🔸추측` 표시 찾기
2. **초안 먼저** — 사용자에게 빈 양식을 주지 말고, 이미 있는 내용 + 맥락으로 **추론 채움**
3. **1~2개만 질문** — 가장 중요한 모호함만 (범위 > 완료기준 > 사용자 > 나머지)
4. **spec.md 갱신** — 사용자 답을 반영, 표시 제거
5. **게이트** — WHAT/WHY 가 plan 없이도 이해되면 통과; 아니면 3번 반복
6. **완료 보고** — 남은 TBD 0개 여부, 다음은 Plan(`hyspec plan`) 제안

## 규칙 (CLARIFY.md 요약)

- **초안 먼저, 질문은 나중** — 사용자는 교정만
- **한 번에 1~2질문** — 질문 폭탄 금지
- **추론 가능하면 묻지 않기** — "이렇게 이해했는데 맞아?" 로 확인
- **Plan 층 금지** — 기술 스택·API·파일 구조는 spec 에 넣지 않기
- 사용자가 한국어로 말하면 spec 도 한국어로

## Specify 와의 차이

| | **hyspec-specify** | **hyspec-clarify** |
|--|-------------------|-------------------|
| **입력** | 기능 설명 (새 feature) | **이미 있는** spec.md |
| **목표** | spec **만들기** | spec **다듬기** |
| **다음** | clarify (필요 시) | `hyspec plan` |

## 관련 파일

| 경로 | 역할 |
|------|------|
| `specs/<###-name>/spec.md` | 이 skill 이 **고치는** 파일 |
| `.specify/templates/clarify-template.md` | 인터뷰 원칙 (init 시 복사) |
| `CLARIFY.md` (kit repo) | SSOT — skill 은 축소판 |
