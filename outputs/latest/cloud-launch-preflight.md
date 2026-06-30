# Cloud Launch Preflight

GitHub Actions의 `Run workflow`를 눌러도 되는지 사전에 확인하는 점검 카드입니다.

- ready_to_click_run_workflow: `True`
- blocker_count: `0`
- repo_connected: `True`
- github_status: `needs_gh_cli`
- has_commit: `True`
- approved_ready_count: `1`
- quality_ready_count: `12`
- review_approval_state: `{"user_confirmed_all": false, "user_confirmed_keywords": ["bitcoin"]}`
- next_action: `GitHub Actions -> Daily Investment Intake -> Run workflow`

## Core Gates

- `repo_connected`: `True`
  - why: GitHub 저장소가 연결돼야 컴퓨터가 꺼져 있어도 GitHub Actions가 계속 돌 수 있습니다.
- `has_commit`: `True`
  - why: 클라우드 실행 전에 최소 1회 커밋이 있어야 workflow가 참조할 기준 상태가 생깁니다.
- `required_blogger_secrets_present_locally`: `True`
  - why: Blogger 핵심 Secrets 4개가 로컬에 있어야 GitHub로 옮길 값도 확정됩니다.
- `blogger_channel_ready`: `True`
  - why: 최소 자동 채널은 Blogger이므로 이 채널 준비가 안 되면 무료 자동화 첫 실행 가치가 떨어집니다.
- `workflow_parity_ok`: `True`
  - why: 로컬 파이프라인과 GitHub workflow 순서가 맞아야 같은 산출물이 안정적으로 생성됩니다.
- `review_state_safe_before_first_cloud_run`: `True`
  - why: 첫 클라우드 실행 전에는 승인 목록이 비어 있어야 의도치 않은 게시가 나가지 않습니다.
  - next_action: `python3 scripts/set_review_approvals.py --clear`
- `first_cloud_safety_checks_green`: `True`
  - why: 현재 업로드 차단/승인 게이트/보고서 정합성이 초록 상태여야 첫 GitHub Actions 검증이 안전합니다.

## References

- github minimum launch card: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/github-minimum-launch-card.md`
- pipeline workflow parity: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/pipeline-workflow-parity.md`
- first cloud run verification: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/first-cloud-run-verification.md`
- user review checkpoint: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/user-review-checkpoint.html`
