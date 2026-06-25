---
name: hyspec-analyze
description: >-
  Cross-check spec.md, plan.md, and tasks.md for consistency using checklist
  template. Use when the user asks to analyze, review artifacts, or verify quality.
---

# HYspec Analyze

## 언제 쓰나

- spec · plan · tasks **세 문서가 서로 맞는지** 검사할 때
- "Analyze", "분석", "정합성", "품질 검사" 를 언급할 때
- plan/tasks/implement **전에** 게이트로 쓸 때

## 먼저 확인

1. `.specify/feature.json` — active feature
2. `specs/<###-name>/spec.md`, `plan.md`, `tasks.md` 존재
3. `.specify/templates/checklist-template.md` — 항목 참고
4. `.specify/memory/constitution.md` — 위반 여부

## 하는 일 (순서)

1. **세 파일 읽기** — scope, stack, task 목록
2. **불일치 찾기** — 예: plan 에만 있는 기능, tasks 에 없는 spec 요구
3. **checklist 작성** (선택) — `specs/<###-name>/checklists/quality.md`
   - template 구조 사용, CHK001… 번호
4. **보고** — 통과 / 수정 필요 목록 (어떤 파일을 고칠지)

## 규칙

- **코드 수정하지 않음** — analyze 는 문서 검사만 (implement 와 분리)
- 문제 발견 시 **implement 중단** 제안
- checklist 파일 없어도 **구두 보고** 가능

## Spec Kit 대응

| Spec Kit | HYspec |
|----------|--------|
| `speckit-analyze` | **이 skill** |
| checklist-template | `.specify/templates/checklist-template.md` |
