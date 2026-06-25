---
name: hyspec-implement
description: >-
  Implement code from specs/<feature>/tasks.md following plan.md and
  constitution. Use when the user asks to implement, build, or execute tasks.
---

# HYspec Implement

## 언제 쓰나

- `tasks.md` 체크리스트대로 **코드를 짜**달라고 할 때
- "implement", "구현", "⑤ Tasks 실행" 을 언급할 때
- spec/plan 은 끝났고 **이제 코드** 단계일 때

## 먼저 확인

1. `specs/<###-name>/spec.md` — 범위·가치 (WHAT/WHY)
2. `specs/<###-name>/plan.md` — 구조·기술·경계 (HOW)
3. `specs/<###-name>/tasks.md` — **지금 할 일 목록**
4. `.specify/memory/constitution.md` — 헌법 (①) · 경계·단순성

## 하는 일 (순서)

1. **대상 feature** — `specs/` 최신 또는 사용자 지정 폴더
2. **tasks.md 읽기** — Phase 순서, `- [ ]` 항목부터
3. **한 작업씩 구현** — plan.md 의 모듈·SSOT·의존 방향 지키기
4. **완료 시 체크** — 해당 줄을 `- [x]` 로 바꾸기 (tasks.md 갱신)
5. **보고** — 바꾼 파일, 남은 task, spec 범위 밖 요청은 거절

## 규칙

- spec 에 없는 기능 **추가하지 않기** — scope creep 금지
- plan·헌법 **어기는 구조** 만들지 않기 (순환 의존, 갓파일)
- 모호하면 **코드부터 만들지 말고** spec/plan 으로 되돌리기
- 테스트는 plan/tasks 에 **명시된 경우만**

## 관련 파일

| 경로 | 역할 |
|------|------|
| `specs/<###-name>/tasks.md` | **이 skill 의 입력** |
| `specs/<###-name>/plan.md` | 구조·스택 참조 |
| `specs/<###-name>/spec.md` | 범위 참조 |

## CLI와 함께 쓰기

```powershell
hyspec feature "설명"
hyspec plan
hyspec tasks
# → tasks.md 채운 뒤 이 skill 로 구현
```
