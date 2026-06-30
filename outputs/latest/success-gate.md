# Success Gate

- all_green: `True`
- first_live_status: `ready_for_draft_test`
- github_launch_status: `needs_gh_cli`

## Checks

- `google_client_connected`: ready (required)
- `google_refresh_token_connected`: ready (required)
- `openai_connected`: pending (optional)
  - next: `OPENAI_API_KEY를 .env 에 입력(선택)`
- `initial_commit_created`: ready (required)
- `github_repo_connected`: ready (required)
- `first_live_run_ready`: ready (required)

## Top Next Actions

