---
name: hyspec-specify
description: >-
  Fill specs/<feature>/spec.md from a feature description using HYspec
  templates. Use when the user asks to specify a feature, write a spec,
  or work on the Specify layer (② 무엇을·왜).
---

# HYspec Specify

## 언제 쓰나

- 사용자가 **기능을 말로 설명**할 때
- `spec.md` 를 쓰거나 고치라고 할 때
- "Specify", "②", "무엇을·왜" 를 언급할 때

## 먼저 확인

1. `.specify/` 가 있는지 (`hyspec init` 했는지)
2. `specs/<###-이름>/` 가 있는지 — 없으면 `hyspec feature "설명"` 으로 만들기
3. `.specify/memory/constitution.md` 를 읽어 **프로젝트 원칙** 반영

## 하는 일 (순서)

1. **대상 feature 고르기** — `specs/` 아래 가장 최근 폴더 또는 사용자가 지정한 폴더
2. **`spec.md` 열기** — `specs/<###-name>/spec.md` (템플릿에서 복사된 파일)
3. **사용자 설명으로 채우기** — `.specify/templates/spec-template.md` 섹션 순서 유지
   - **WHAT / WHY** 만 — 구현·기술·화면 세부는 쓰지 않음 (PLAN 층)
   - 모르면 `TBD` 또는 `[NEEDS CLARIFICATION: 질문]` (최대 3개)
4. **완료 보고** — feature 폴더 경로, 채운 섹션, 남은 TBD/CLARIFICATION

## 규칙

- spec 에 **언어·프레임워크·DB·API** 넣지 않기
- 사용자가 한국어로 말하면 spec 도 한국어로
- checklist·plan·tasks 는 이 skill 범위 밖 (다른 단계)

## 관련 파일

| 경로 | 역할 |
|------|------|
| `.specify/templates/spec-template.md` | 섹션 구조 원본 |
| `.specify/memory/constitution.md` | 헌법 (①) |
| `specs/<###-name>/spec.md` | 이 skill 의 **산출물** |
