# Success Gate

- all_green: `False`
- first_live_status: `needs_preflight_review`
- github_launch_status: `needs_repo_creation`

## Checks

- `google_client_connected`: ready (required)
- `google_refresh_token_connected`: ready (required)
- `openai_connected`: pending (optional)
  - next: `OPENAI_API_KEY를 .env 에 입력(선택)`
- `initial_commit_created`: ready (required)
- `github_repo_connected`: pending (required)
  - next: `bash scripts/bootstrap_github_remote.sh <OWNER/REPO>`
- `first_live_run_ready`: pending (required)
  - next: `bash scripts/run_pipeline.sh`

## Top Next Actions

- `bash scripts/bootstrap_github_remote.sh <OWNER/REPO>`
- `bash scripts/run_pipeline.sh`
