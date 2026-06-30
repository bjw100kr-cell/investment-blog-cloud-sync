# Resume After Login Report

- `ok` Setup check: `python3 scripts/check_setup.py`
  - stdout: Investment Blog Cloud Sync setup check

- project: /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync
- .env present: yes
- git branch: main
- git origin: https://github.com/bjw100kr-cell/investment-blog-cloud-sync.git
- outputs/latest present: yes

Local .env values
- ADSENSE_PUBLISHER_ID: missing
- ADSENSE_SITE_VERIFICATION: missing
- BLOGGER_ALLOW_REUPLOAD_SAME_CONTENT: default (false)
- BLOGGER_API_BACKOFF_BASE_SECONDS: default (1.5)
- BLOGGER_API_BACKOFF_MAX_SECONDS: default (20.0)
- BLOGGER_API_MAX_ATTEMPTS: default (4)
- BLOGGER_AUTO_PUBLISH_POSTS: set (****)
- BLOGGER_BLOG_ID: set (691***88)
- BLOGGER_INCLUDE_OPTIONAL_SITE_PAGES: set (*****)
- BLOGGER_MAX_POSTS_PER_RUN: set (*)
- BLOGGER_PUBLISH_ONLY_DUE_POSTS: set (*****)
- BLOGGER_REQUIRE_REVIEW_APPROVAL: set (*****)
- BLOGGER_SITE_PAGES_PUBLISH: set (*****)
- BLOGGER_SYNC_SITE_PAGES: set (*****)
- BLOG_BASE_URL: set (htt***m/)
- GA4_MEASUREMENT_ID: missing
- GOOGLE_ACCESS_TOKEN: missing
- GOOGLE_CLIENT_ID: set (786***om)
- GOOGLE_CLIENT_SECRET: set (GOC***1Z)
- GOOGLE_OAUTH_OPEN_BROWSER: set (****)
- GOOGLE_OAUTH_PRESET: set (com***ed)
- GOOGLE_REDIRECT_URI: set (htt***ck)
- GOOGLE_REFRESH_TOKEN: set (1//***Jg)
- NAVER_CLIENT_ID: missing
- NAVER_CLIENT_SECRET: missing
- NEWSLETTER_SUBSCRIBE_URL: missing
- OPENAI_API_KEY: missing
- OPENAI_MODEL: set (gpt***ni)
- SEARCH_CONSOLE_ACCESS_TOKEN: missing
- SEARCH_CONSOLE_CLIENT_ID: set (786***om)
- SEARCH_CONSOLE_CLIENT_SECRET: set (GOC***1Z)
- SEARCH_CONSOLE_LAG_DAYS: set (*)
- SEARCH_CONSOLE_REFRESH_TOKEN: set (1//***Jg)
- SEARCH_CONSOLE_SITE_URL: missing
- SEARCH_CONSOLE_WINDOW_DAYS: set (*)
- WORDPRESS_APPLICATION_PASSWORD: missing
- WORDPRESS_AUTO_PUBLISH_POSTS: default (false)
- WORDPRESS_MAX_POSTS_PER_RUN: default (1)
- WORDPRESS_PUBLISH_ONLY_DUE_POSTS: default (true)
- WORDPRESS_REQUIRE_REVIEW_APPROVAL: default (true)
- WORDPRESS_SITE_URL: missing
- WORDPRESS_USERNAME: missing

Integration readiness
- naver_datalab: missing NAVER_CLIENT_ID, NAVER_CLIENT_SECRET
- search_console: missing SEARCH_CONSOLE_SITE_URL
- openai_drafts: missing OPENAI_API_KEY
- blogger_upload: ready
- wordpress_upload: missing WORDPRESS_SITE_URL, WORDPRESS_USERNAME, WORDPRESS_APPLICATION_PASSWORD

Publish-ready status
- report exists: yes
- items: 4
- ready html items: 4

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
- Automation-first 운영 기준에서 현재 1차 채널은 Blogger, WordPress는 나중 확장입니다.

JSON report written to: /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/setup-check-report.json
- `ok` OAuth bootstrap: `python3 scripts/bootstrap_google_oauth_credentials.py`
  - stdout: /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/google-oauth-bootstrap-report.md
- `ok` Apply OAuth token: `python3 scripts/apply_google_oauth_result.py`
  - stdout: /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/google-oauth-apply-report.md
- `ok` Setup check refresh: `python3 scripts/check_setup.py`
  - stdout: Investment Blog Cloud Sync setup check

- project: /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync
- .env present: yes
- git branch: main
- git origin: https://github.com/bjw100kr-cell/investment-blog-cloud-sync.git
- outputs/latest present: yes

Local .env values
- ADSENSE_PUBLISHER_ID: missing
- ADSENSE_SITE_VERIFICATION: missing
- BLOGGER_ALLOW_REUPLOAD_SAME_CONTENT: default (false)
- BLOGGER_API_BACKOFF_BASE_SECONDS: default (1.5)
- BLOGGER_API_BACKOFF_MAX_SECONDS: default (20.0)
- BLOGGER_API_MAX_ATTEMPTS: default (4)
- BLOGGER_AUTO_PUBLISH_POSTS: set (****)
- BLOGGER_BLOG_ID: set (691***88)
- BLOGGER_INCLUDE_OPTIONAL_SITE_PAGES: set (*****)
- BLOGGER_MAX_POSTS_PER_RUN: set (*)
- BLOGGER_PUBLISH_ONLY_DUE_POSTS: set (*****)
- BLOGGER_REQUIRE_REVIEW_APPROVAL: set (*****)
- BLOGGER_SITE_PAGES_PUBLISH: set (*****)
- BLOGGER_SYNC_SITE_PAGES: set (*****)
- BLOG_BASE_URL: set (htt***m/)
- GA4_MEASUREMENT_ID: missing
- GOOGLE_ACCESS_TOKEN: missing
- GOOGLE_CLIENT_ID: set (786***om)
- GOOGLE_CLIENT_SECRET: set (GOC***1Z)
- GOOGLE_OAUTH_OPEN_BROWSER: set (****)
- GOOGLE_OAUTH_PRESET: set (com***ed)
- GOOGLE_REDIRECT_URI: set (htt***ck)
- GOOGLE_REFRESH_TOKEN: set (1//***Jg)
- NAVER_CLIENT_ID: missing
- NAVER_CLIENT_SECRET: missing
- NEWSLETTER_SUBSCRIBE_URL: missing
- OPENAI_API_KEY: missing
- OPENAI_MODEL: set (gpt***ni)
- SEARCH_CONSOLE_ACCESS_TOKEN: missing
- SEARCH_CONSOLE_CLIENT_ID: set (786***om)
- SEARCH_CONSOLE_CLIENT_SECRET: set (GOC***1Z)
- SEARCH_CONSOLE_LAG_DAYS: set (*)
- SEARCH_CONSOLE_REFRESH_TOKEN: set (1//***Jg)
- SEARCH_CONSOLE_SITE_URL: missing
- SEARCH_CONSOLE_WINDOW_DAYS: set (*)
- WORDPRESS_APPLICATION_PASSWORD: missing
- WORDPRESS_AUTO_PUBLISH_POSTS: default (false)
- WORDPRESS_MAX_POSTS_PER_RUN: default (1)
- WORDPRESS_PUBLISH_ONLY_DUE_POSTS: default (true)
- WORDPRESS_REQUIRE_REVIEW_APPROVAL: default (true)
- WORDPRESS_SITE_URL: missing
- WORDPRESS_USERNAME: missing

Integration readiness
- naver_datalab: missing NAVER_CLIENT_ID, NAVER_CLIENT_SECRET
- search_console: missing SEARCH_CONSOLE_SITE_URL
- openai_drafts: missing OPENAI_API_KEY
- blogger_upload: ready
- wordpress_upload: missing WORDPRESS_SITE_URL, WORDPRESS_USERNAME, WORDPRESS_APPLICATION_PASSWORD

Publish-ready status
- report exists: yes
- items: 4
- ready html items: 4

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
- Automation-first 운영 기준에서 현재 1차 채널은 Blogger, WordPress는 나중 확장입니다.

JSON report written to: /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/setup-check-report.json
- `ok` Login checklist refresh: `python3 scripts/open_login_setup_pages.py`
  - stdout: /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/login-launch-checklist.md
- `ok` GitHub sync guide refresh: `python3 scripts/export_github_actions_sync_commands.py`
  - stdout: /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/github-actions-sync.md
- `ok` Go-live readiness refresh: `python3 scripts/build_go_live_readiness_report.py`
- `ok` Platform publish plan refresh: `python3 scripts/build_platform_publish_plan.py`
  - stdout: /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/platform-publish-plan.md
- `ok` First live run plan refresh: `python3 scripts/prepare_first_live_run_plan.py`
  - stdout: /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/first-live-run-plan.md
- `ok` GitHub launch plan refresh: `python3 scripts/prepare_github_launch_plan.py`
  - stdout: /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/github-launch-plan.md
- `ok` Go-live dashboard refresh: `python3 scripts/prepare_go_live_dashboard.py`
  - stdout: /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/go-live-dashboard.md
- `ok` Cloud launch preflight refresh: `python3 scripts/build_cloud_launch_preflight.py`
  - stdout: /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/cloud-launch-preflight.md
- `ok` Operator handoff refresh: `python3 scripts/generate_operator_handoff.py`
  - stdout: /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/operator-handoff.md
- `ok` Start here refresh: `python3 scripts/prepare_start_here_runbook.py`
  - stdout: /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/start-here-runbook.md

## Next Action

- `python3 scripts/export_github_actions_sync_commands.py`

## Reference

- [start-here-runbook.md](/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/start-here-runbook.md)
- [github-minimum-launch-card.md](/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/github-minimum-launch-card.md)
