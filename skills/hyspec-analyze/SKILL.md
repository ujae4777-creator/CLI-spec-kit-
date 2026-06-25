---
name: hyspec-analyze
description: >-
  Cross-check spec.md, plan.md, and tasks.md for consistency. Use when the user
  asks to analyze, review artifacts, or verify cross-document alignment. For
  requirement-quality checklists use hyspec-checklist instead.
---

# HYspec Analyze

## 언제 쓰나

- spec · plan · tasks **세 문서가 서로 맞는지** 검사할 때
- "Analyze", "분석", "정합성", "품질 검사" 를 언급할 때
- plan/tasks/implement **전에** 게이트로 쓸 때

## checklist 와 차이

| | **hyspec-checklist** | **hyspec-analyze** (이 skill) |
|--|---------------------|------------------------------|
| **목표** | 요구사항 **작성 품질** checklist 생성 | spec·plan·tasks **상호 정합** |
| **산출물** | `checklists/<domain>.md` | 불일치 보고 |

## 먼저 확인

1. `.specify/feature.json` — active feature
2. `specs/<###-name>/spec.md`, `plan.md`, `tasks.md` 존재
3. `.specify/memory/constitution.md` — 위반 여부
4. (선택) `checklists/*.md` — checklist skill 이 만든 항목 참고

## 하는 일 (순서)

1. **세 파일 읽기** — scope, stack, task 목록
2. **불일치 찾기** — 예: plan 에만 있는 기능, tasks 에 없는 spec 요구
3. **보고** — 통과 / 수정 필요 목록 (어떤 파일을 고칠지)
4. checklist 가 필요하면 **hyspec-checklist** skill 제안 (이 skill 이 대신 만들지 않음)

## 규칙

- **코드 수정하지 않음** — analyze 는 문서 검사만 (implement 와 분리)
- 문제 발견 시 **implement 중단** 제안
- 요구사항 품질 checklist 는 **hyspec-checklist** 가 담당

## Spec Kit 대응

| Spec Kit | HYspec |
|----------|--------|
| `speckit-analyze` | **이 skill** |
| `speckit-checklist` | `hyspec-checklist` skill |
