---
name: hyspec-checklist
description: >-
  Generate custom requirement-quality checklists in specs/<feature>/checklists/.
  Use when the user asks for checklist, quality gate, ux/security review of spec,
  or "unit tests for requirements".
---

# HYspec Checklist

## 핵심 개념

**요구사항 영어의 단위 테스트** — 구현이 맞는지가 아니라, **spec/plan 에 글이 잘 쓰였는지** 검사한다.

| ❌ 하지 않음 | ✅ 한다 |
|-------------|--------|
| "버튼이 잘 눌리는지 확인" | "버튼 상태 요구사항이 정의됐는가?" |
| API 200 응답 테스트 | "오류 응답 형식이 요구사항에 있는가?" |
| 코드·UI 동작 검증 | 완전성·명확성·일관성·측정 가능성 |

## 언제 쓰나

- spec/plan 을 **품질 관점**으로 점검할 checklist 가 필요할 때
- "Checklist", "품질 게이트", "ux 점검", "보안 요구사항 검토" 를 언급할 때
- **clarify 이후**, plan/tasks/implement **전** (또는 spec 갱신 후)

## analyze 와 차이

| | **hyspec-checklist** | **hyspec-analyze** |
|--|---------------------|-------------------|
| **산출물** | `checklists/<domain>.md` 파일 | 불일치 **보고** (선택적으로 checklist 참고) |
| **초점** | 요구사항 **작성 품질** | spec·plan·tasks **서로 맞는지** |
| **시점** | spec(±plan) 있을 때 | plan + tasks 깬 뒤 게이트 |

## 먼저 확인

1. `.specify/feature.json` — active feature
2. `specs/<###-name>/spec.md` (필수), `plan.md` (있으면 참고)
3. `.specify/templates/checklist-template.md` — CHK001 형식·섹션 구조
4. `.specify/memory/constitution.md` — 프로젝트 원칙

## 하는 일 (순서)

1. **맥락 읽기** — spec/plan 에서 도메인 키워드·리스크·모호한 표현 추출
2. **초점 정하기** — 사용자 요청 또는 맥락에서 1~2개 (예: `ux`, `security`, `api`)
   - 모호하면 **한 가지만** 질문 (깊이: 가벼운 점검 vs 릴리스 게이트)
3. **파일 만들기/추가** — `specs/<###-name>/checklists/<domain>.md`
   - 없으면 새로 생성 (CHK001부터)
   - 있으면 **기존 항목 유지**, CHK 번호 이어서 **append**
4. **항목 작성** — template 구조 + 카테고리 예:
   - Requirement Completeness / Clarity / Consistency
   - Acceptance Criteria / Scenario & Edge Case / NFR
5. **완료 보고** — 파일 경로, 항목 수, 초점 영역, `- [ ]` 로 남긴 이유

## 항목 작성 규칙

**패턴:** `질문 형태` + `[품질차원]` + 선택적 `[Spec §…]` / `[Gap]`

```markdown
- [ ] CHK001 "빠른 로딩"에 구체적 시간 기준이 있는가? [Clarity, Gap]
- [ ] CHK002 모든 인터랙션 요소에 키보드 접근 요구가 정의됐는가? [Completeness, Gap]
- [ ] CHK003 §FR-1 과 §FR-3 의 카드 개수 요구가 모순 없는가? [Consistency]
```

**금지:** Verify / Test / Confirm / Click / 렌더 / 동작 확인 같은 **구현 검증** 문장

## 다른 skill 과 관계

| skill | 관계 |
|-------|------|
| clarify | 모호함 줄인 뒤 checklist 가 의미 있음 |
| plan | plan 있으면 plan 요구 품질 항목 추가 가능 |
| analyze | checklist 로 품질 점검 → analyze 로 세 문서 정합 |
| implement | checklist 미완이면 implement 보류 제안 |

## 관련 파일

| 경로 | 역할 |
|------|------|
| `.specify/templates/checklist-template.md` | 형식 SSOT |
| `specs/<###-name>/checklists/<domain>.md` | **이 skill 의 산출물** |
| `CHECKLIST.md` (kit repo) | 원본 참고 |

## Spec Kit 대응

| Spec Kit | HYspec |
|----------|--------|
| `speckit-checklist` | **이 skill** |
| `checklists/ux.md` 등 | `specs/.../checklists/<domain>.md` |

## CLI

- `hyspec init` — checklist-template + 이 skill 복사
- checklist **생성**은 CLI 없음 — Cursor 에서 이 skill 사용
