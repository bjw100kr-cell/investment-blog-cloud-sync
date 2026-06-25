# Resume After Login Report

- `ok` Setup check: `python3 scripts/check_setup.py`
  - stdout: Investment Blog Cloud Sync setup check

- project: /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync
- .env present: yes
- git branch: main
- git origin: (not configured)
- outputs/latest present: yes

Local .env values
- ADSENSE_PUBLISHER_ID: missing
- ADSENSE_SITE_VERIFICATION: missing
- BLOGGER_AUTO_PUBLISH_POSTS: set (*****)
- BLOGGER_BLOG_ID: set (691***88)
- BLOGGER_INCLUDE_OPTIONAL_SITE_PAGES: set (*****)
- BLOGGER_MAX_POSTS_PER_RUN: set (*)
- BLOGGER_PUBLISH_ONLY_DUE_POSTS: set (****)
- BLOGGER_SITE_PAGES_PUBLISH: set (*****)
- BLOGGER_SYNC_SITE_PAGES: set (*****)
- BLOG_BASE_URL: missing
- GA4_MEASUREMENT_ID: missing
- GOOGLE_ACCESS_TOKEN: missing
- GOOGLE_CLIENT_ID: missing
- GOOGLE_CLIENT_SECRET: missing
- GOOGLE_OAUTH_OPEN_BROWSER: set (*****)
- GOOGLE_OAUTH_PRESET: set (com***ed)
- GOOGLE_REDIRECT_URI: set (htt***ck)
- GOOGLE_REFRESH_TOKEN: missing
- NAVER_CLIENT_ID: missing
- NAVER_CLIENT_SECRET: missing
- NEWSLETTER_SUBSCRIBE_URL: missing
- OPENAI_API_KEY: missing
- OPENAI_MODEL: set (gpt***ni)
- SEARCH_CONSOLE_ACCESS_TOKEN: missing
- SEARCH_CONSOLE_CLIENT_ID: missing
- SEARCH_CONSOLE_CLIENT_SECRET: missing
- SEARCH_CONSOLE_LAG_DAYS: set (*)
- SEARCH_CONSOLE_REFRESH_TOKEN: missing
- SEARCH_CONSOLE_SITE_URL: missing
- SEARCH_CONSOLE_WINDOW_DAYS: set (*)

Integration readiness
- naver_datalab: missing NAVER_CLIENT_ID, NAVER_CLIENT_SECRET
- search_console: missing SEARCH_CONSOLE_SITE_URL, SEARCH_CONSOLE_CLIENT_ID, SEARCH_CONSOLE_CLIENT_SECRET, SEARCH_CONSOLE_REFRESH_TOKEN
- openai_drafts: missing OPENAI_API_KEY
- blogger_upload: missing GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, GOOGLE_REFRESH_TOKEN

Publish-ready status
- report exists: yes
- items: 3
- ready html items: 3

Site-page status
- plan exists: yes
- items: 10
- required rendered pages: 9 / 9

Go-live report
- report exists: yes

GitHub Actions notes
- Local .env values do not automatically sync to GitHub Secrets.
- Add the same keys manually in GitHub -> Settings -> Secrets and variables -> Actions.
- Public repositories are usually the safest free option for this lightweight schedule.

JSON report written to: /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/setup-check-report.json
- `ok` OAuth bootstrap: `python3 scripts/bootstrap_google_oauth_credentials.py`
  - stdout: /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/google-oauth-bootstrap-report.md
- `ok` Setup check refresh: `python3 scripts/check_setup.py`
  - stdout: Investment Blog Cloud Sync setup check

- project: /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync
- .env present: yes
- git branch: main
- git origin: (not configured)
- outputs/latest present: yes

Local .env values
- ADSENSE_PUBLISHER_ID: missing
- ADSENSE_SITE_VERIFICATION: missing
- BLOGGER_AUTO_PUBLISH_POSTS: set (*****)
- BLOGGER_BLOG_ID: set (691***88)
- BLOGGER_INCLUDE_OPTIONAL_SITE_PAGES: set (*****)
- BLOGGER_MAX_POSTS_PER_RUN: set (*)
- BLOGGER_PUBLISH_ONLY_DUE_POSTS: set (****)
- BLOGGER_SITE_PAGES_PUBLISH: set (*****)
- BLOGGER_SYNC_SITE_PAGES: set (*****)
- BLOG_BASE_URL: missing
- GA4_MEASUREMENT_ID: missing
- GOOGLE_ACCESS_TOKEN: missing
- GOOGLE_CLIENT_ID: missing
- GOOGLE_CLIENT_SECRET: missing
- GOOGLE_OAUTH_OPEN_BROWSER: set (*****)
- GOOGLE_OAUTH_PRESET: set (com***ed)
- GOOGLE_REDIRECT_URI: set (htt***ck)
- GOOGLE_REFRESH_TOKEN: missing
- NAVER_CLIENT_ID: missing
- NAVER_CLIENT_SECRET: missing
- NEWSLETTER_SUBSCRIBE_URL: missing
- OPENAI_API_KEY: missing
- OPENAI_MODEL: set (gpt***ni)
- SEARCH_CONSOLE_ACCESS_TOKEN: missing
- SEARCH_CONSOLE_CLIENT_ID: missing
- SEARCH_CONSOLE_CLIENT_SECRET: missing
- SEARCH_CONSOLE_LAG_DAYS: set (*)
- SEARCH_CONSOLE_REFRESH_TOKEN: missing
- SEARCH_CONSOLE_SITE_URL: missing
- SEARCH_CONSOLE_WINDOW_DAYS: set (*)

Integration readiness
- naver_datalab: missing NAVER_CLIENT_ID, NAVER_CLIENT_SECRET
- search_console: missing SEARCH_CONSOLE_SITE_URL, SEARCH_CONSOLE_CLIENT_ID, SEARCH_CONSOLE_CLIENT_SECRET, SEARCH_CONSOLE_REFRESH_TOKEN
- openai_drafts: missing OPENAI_API_KEY
- blogger_upload: missing GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, GOOGLE_REFRESH_TOKEN

Publish-ready status
- report exists: yes
- items: 3
- ready html items: 3

Site-page status
- plan exists: yes
- items: 10
- required rendered pages: 9 / 9

Go-live report
- report exists: yes

GitHub Actions notes
- Local .env values do not automatically sync to GitHub Secrets.
- Add the same keys manually in GitHub -> Settings -> Secrets and variables -> Actions.
- Public repositories are usually the safest free option for this lightweight schedule.

JSON report written to: /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/setup-check-report.json
- `ok` GitHub sync guide refresh: `python3 scripts/export_github_actions_sync_commands.py`
  - stdout: /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/github-actions-sync.md
- `ok` Go-live readiness refresh: `python3 scripts/build_go_live_readiness_report.py`
- `ok` First live run plan refresh: `python3 scripts/prepare_first_live_run_plan.py`
  - stdout: /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/first-live-run-plan.md
- `ok` GitHub launch plan refresh: `python3 scripts/prepare_github_launch_plan.py`
  - stdout: /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/github-launch-plan.md
- `ok` Go-live dashboard refresh: `python3 scripts/prepare_go_live_dashboard.py`
  - stdout: /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/go-live-dashboard.md
- `ok` Operator handoff refresh: `python3 scripts/generate_operator_handoff.py`
  - stdout: /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/operator-handoff.md
- `ok` Start here refresh: `python3 scripts/prepare_start_here_runbook.py`
  - stdout: /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/start-here-runbook.md

## Next Action

- `python3 scripts/open_login_setup_pages.py --open`

## Reference

- [start-here-runbook.md](/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/start-here-runbook.md)
