# Automation Scope

- automation_policy: `automation-first`
- cloud_runtime: `github_actions`
- review_gate_required: `True`

## Active Now

- `blogger`: status=active / ready=True / 무료에 가깝고 GitHub Actions와 결합해 초안 자동 업로드를 검증하기 가장 단순합니다.

## Expand Later

- `wordpress`: status=optional_later / ready=False / 공식 REST API 기반 자동화가 가능하지만 초기 설정 복잡도가 Blogger보다 높습니다.

## Excluded From Automation

- `naver_blog`: 현재 프로젝트에서는 안정적인 공식 자동 발행 경로로 보지 않고 수동 운영 채널로 분리합니다.
- `tistory`: 초기 무자본 자동화 기준에서 운영 안정성이 낮아 1차 범위에서 제외합니다.

## Operating Rule

- 자동화 기본 경로는 `Blogger -> 사용자 검토 -> 승인 후 draft 업로드 -> GitHub Actions 일일 실행` 입니다.
- WordPress는 Blogger 검증이 끝난 뒤 두 번째 자동 채널로만 확장합니다.
