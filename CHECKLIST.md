---
type: checklist
vault: spec-first-kit
feature:              # specs/<###-name>/
---

# CHECKLIST — 품질 점검

> **품질 게이트** — spec / plan / tasks 가 **서로 맞는지** 확인할 때 쓴다.
> Agent(`hyspec-checklist` 로 생성, 사람·Agent 가 `- [ ]` → `- [x]`) — `hyspec-analyze` 는 정합 검사용.

**Purpose:** [이 checklist 가 검사하는 것 — 예: spec 완성도]
**Created:** [DATE]
**Feature:** [specs/001-name/spec.md 링크]

---

## Spec 품질 (WHAT/WHY)

- [ ] CHK001 한 줄 설명만 읽어도 기능이 이해됨
- [ ] CHK002 범위(포함/제외)가 모순 없음
- [ ] CHK003 완료 기준으로 "끝" 판정 가능
- [ ] CHK004 구현 세부(언어·API)가 spec 에 없음

---

## Plan 정합 (HOW)

- [ ] CHK005 plan 이 spec 범위를 벗어나지 않음
- [ ] CHK006 의존 방향이 한 방향 (순환 없음)
- [ ] CHK007 SSOT 경로가 명시됨

---

## Tasks 실행 준비

- [ ] CHK008 tasks 가 plan 모듈 순서와 맞음
- [ ] CHK009 각 task 에 파일/행동이 구체적임

---

## Notes

- `[x]` 로 완료 표시
- 문제 있으면 **spec/plan/tasks** 중 어디를 고칠지 적기
