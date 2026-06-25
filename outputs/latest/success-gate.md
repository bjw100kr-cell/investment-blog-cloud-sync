# Success Gate

- all_green: `False`
- first_live_status: `awaiting_credentials`
- github_launch_status: `needs_initial_commit`

## Checks

- `google_client_connected`: pending (required)
  - next: `python3 scripts/bootstrap_google_oauth_credentials.py`
- `google_refresh_token_connected`: pending (required)
  - next: `GOOGLE_OAUTH_OPEN_BROWSER=true python3 scripts/get_google_refresh_token.py`
- `openai_connected`: pending (optional)
  - next: `OPENAI_API_KEY를 .env 에 입력(선택)`
- `initial_commit_created`: pending (required)
  - next: `bash scripts/prepare_initial_commit.sh`
- `github_repo_connected`: pending (required)
  - next: `bash scripts/bootstrap_github_remote.sh <YOUR_GITHUB_REPO_URL>`
- `first_live_run_ready`: pending (required)
  - next: `bash scripts/run_pipeline.sh`

## Top Next Actions

- `python3 scripts/bootstrap_google_oauth_credentials.py`
- `GOOGLE_OAUTH_OPEN_BROWSER=true python3 scripts/get_google_refresh_token.py`
- `bash scripts/prepare_initial_commit.sh`
