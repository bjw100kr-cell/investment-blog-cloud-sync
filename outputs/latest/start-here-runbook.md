# Start Here Runbook

이 문서만 따라가면 첫 로그인부터 첫 Blogger 테스트 업로드와 GitHub 자동화 연결까지 진행할 수 있습니다.

## 현재 상태

- first_live_status: `awaiting_credentials`
- github_status: `needs_initial_commit`
- repo_connected: `False`
- missing_credentials_count: `3`

## 지금 바로 할 일

로그인을 마치고 다시 돌아오면 먼저 이 명령을 실행해도 됩니다:
- `python3 scripts/resume_after_login.py`

1. Google Cloud Console에서 OAuth client JSON을 다운로드합니다.
2. `python3 scripts/bootstrap_google_oauth_credentials.py`
3. `GOOGLE_OAUTH_OPEN_BROWSER=true python3 scripts/get_google_refresh_token.py`
4. `python3 scripts/apply_google_oauth_result.py`
5. `bash scripts/prepare_initial_commit.sh`
6. GitHub에서 새 public repo를 만들고 URL을 복사합니다.
7. `bash scripts/bootstrap_github_remote.sh <YOUR_GITHUB_REPO_URL>`
8. `python3 scripts/check_setup.py`
9. `bash scripts/run_pipeline.sh`
10. Blogger draft와 site page가 정상 생성됐는지 확인합니다.

## OpenAI 키 미입력 모드

- OpenAI 키 없이도 템플릿 fallback 초안으로 일일 업로드를 시작할 수 있습니다.
- 수익성/톤을 더 다듬으려면 `OPENAI_API_KEY`를 나중에 추가하고 같은 파이프라인을 재실행하세요.

## 첫 업로드 목표

- 1차 테스트 글: `FOMC 이후 시장 해설`
- 유형: `main_post`
- CTA 포커스: 환율·금리·미국증시 evergreen 글로 연결

## 안전모드 확인

- `BLOGGER_SYNC_SITE_PAGES=true`
- `BLOGGER_SITE_PAGES_PUBLISH=false`
- `BLOGGER_AUTO_PUBLISH_POSTS=false`
- `BLOGGER_PUBLISH_ONLY_DUE_POSTS=true`
- `BLOGGER_MAX_POSTS_PER_RUN=1`

## 참고 문서

- [first-live-run-plan.md](/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/first-live-run-plan.md)
- [github-launch-plan.md](/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/github-launch-plan.md)
- [go-live-dashboard.md](/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/go-live-dashboard.md)
- [operator-handoff.md](/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/operator-handoff.md)
- [success-gate.md](/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/success-gate.md)
