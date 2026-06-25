---
name: hyspec-plan
description: >-
  Write specs/<feature>/plan.md from spec.md using HYspec plan template.
  Use when the user asks to plan, design implementation, or work on layer ④.
---

# HYspec Plan

## 언제 쓰나

- `spec.md` 가 **어느 정도 채워진 뒤** HOW 를 정할 때
- "Plan", "④", "구현 계획", "기술 설계" 를 언급할 때
- `hyspec plan` 으로 **빈 plan.md** 가 이미 있을 때 — **내용을 채우는** 단계

## 먼저 확인

1. `.specify/feature.json` 또는 `specs/<###-name>/` — **대상 feature**
2. `specs/<###-name>/spec.md` — WHAT/WHY (비어 있으면 specify/clarify 먼저)
3. `.specify/memory/constitution.md` — §2 경계·§3 단순성
4. `plan.md` 없으면 → 사용자에게 `hyspec plan` 실행 요청 (템플릿만 깔림)

## 하는 일 (순서)

1. **spec.md 읽기** — 범위·완료기준·제외 항목
2. **plan.md 열기** — `.specify/templates/plan-template.md` 섹션 순서 유지
3. **HOW 채우기** — 스택, 모듈 경계, SSOT, 데이터 shape (spec 에 없던 WHAT 추가 금지)
4. **헌법 검사** — plan-template 의 검사 항목 반영
5. **완료 보고** — plan 경로, 핵심 결정, tasks 로 넘길 준비 여부

## 규칙

- spec **범위 밖** 기능 plan 에 넣지 않기
- **순환 의존·갓파일** 설계 금지 (constitution §2·§3)
- 사용자가 한국어 spec 이면 plan 도 한국어로
- tasks.md 작성은 **hyspec-tasks** skill / `hyspec tasks` 층

## CLI와 역할 나누기

| 도구 | 역할 |
|------|------|
| `hyspec plan` | plan.md **없으면** 템플릿 복사만 |
| **이 skill** | plan.md **내용 작성** (Agent) |

## 관련 파일

| 경로 | 역할 |
|------|------|
| `specs/<###-name>/spec.md` | 입력 |
| `specs/<###-name>/plan.md` | **산출물** |
| `.specify/templates/plan-template.md` | 섹션 구조 |
