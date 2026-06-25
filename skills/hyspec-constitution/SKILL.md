---
name: hyspec-constitution
description: >-
  Create or update .specify/memory/constitution.md project governing rules.
  Use when the user asks for constitution, dev principles, or layer ①.
---

# HYspec Constitution

## 언제 쓰나

- 프로젝트 **헌법**을 처음 쓰거나 고칠 때
- "Constitution", "①", "개발 헌법", "CLAUDE.md 규칙" 을 언급할 때
- plan/spec 작성 **전에** 팀·프로젝트 원칙을 고정할 때

## 대상 파일

- **`.specify/memory/constitution.md`** — 프로젝트마다 하나 (init 시 kit 에서 복사됨)
- 참고 SSOT: kit repo `CONSTITUTION.md`, `.specify/templates/constitution-template.md`

## 하는 일 (순서)

1. **현재 constitution.md 읽기** — 비어 있으면 template/CONSTITUTION.md 구조 따름
2. **사용자·프로젝트에 맞게 채우기** — 보안·경계·단순성·테스트 원칙
3. **프로젝트 SSOT 경로** 등 `<>` 자리는 실제 경로로 교체
4. **완료 보고** — 핵심 규칙 3~5줄 요약, 이후 specify/plan 이 이 파일을 따름

## 규칙

- **전 프로젝트 공통** — feature 마다 바꾸지 않음 (feature 별 spec/plan 과 구분)
- **짧고 강제 가능하게** — "좋은 코드" 같은 막연한 문장 금지
- 코드보다 **문서** — constitution 은 Agent·사람이 plan/spec 검사할 때 참조
- 한국어 프로젝트면 constitution 도 한국어

## 다른 skill 과 관계

| skill | constitution 사용 |
|-------|-------------------|
| specify / clarify | 범위·단순성 |
| plan | §2 경계·§3 복잡도 |
| implement | §4 에러·§5 타입·§6 테스트 |

## CLI

- `hyspec init` — constitution.md **복사** (내용 작성은 이 skill)
