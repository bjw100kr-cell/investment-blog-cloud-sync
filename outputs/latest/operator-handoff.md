# Operator Handoff

블로그 자동화를 실제 발행 단계로 넘기기 전에 필요한 값과 현재 상태를 정리한 문서입니다.

## 지금 상태

- git origin: https://github.com/bjw100kr-cell/investment-blog-cloud-sync.git
- .env present: True
- publish-ready items: 4
- publish-ready actual HTML count: 4
- publish queue ready count: 4
- publish inventory ready count: 13
- monetization readiness score: 50.0
- first live run ready: True
- first live run plan status: ready_for_draft_test
- github launch plan status: needs_gh_cli

## 꼭 필요한 값

- `BLOGGER_BLOG_ID`: 업로드할 Blogger 블로그 ID
- `GOOGLE_CLIENT_ID`: Google OAuth client ID
- `GOOGLE_CLIENT_SECRET`: Google OAuth client secret
- `GOOGLE_REFRESH_TOKEN`: Blogger 업로드용 refresh token
- `GitHub repository URL`: 클라우드 자동 실행 연결

## 있으면 바로 좋아지는 값

- `OPENAI_API_KEY`
- `SEARCH_CONSOLE_SITE_URL`
- `SEARCH_CONSOLE_CLIENT_ID`
- `SEARCH_CONSOLE_CLIENT_SECRET`
- `SEARCH_CONSOLE_REFRESH_TOKEN`
- `NAVER_CLIENT_ID`
- `NAVER_CLIENT_SECRET`
- `BLOG_BASE_URL`
- `GA4_MEASUREMENT_ID`
- `ADSENSE_PUBLISHER_ID`
- `ADSENSE_SITE_VERIFICATION`
- `NEWSLETTER_SUBSCRIBE_URL`
- `BLOGGER_SYNC_SITE_PAGES`
- `BLOGGER_SITE_PAGES_PUBLISH`
- `BLOGGER_AUTO_PUBLISH_POSTS`
- `BLOGGER_PUBLISH_ONLY_DUE_POSTS`
- `BLOGGER_MAX_POSTS_PER_RUN`
- `WORDPRESS_SITE_URL`
- `WORDPRESS_USERNAME`
- `WORDPRESS_APPLICATION_PASSWORD`
- `WORDPRESS_AUTO_PUBLISH_POSTS`
- `WORDPRESS_PUBLISH_ONLY_DUE_POSTS`
- `WORDPRESS_MAX_POSTS_PER_RUN`

## 현재 미연결 항목

- openai_drafts: missing OPENAI_API_KEY
- blogger_upload: ready
- wordpress_upload: missing WORDPRESS_SITE_URL, WORDPRESS_USERNAME, WORDPRESS_APPLICATION_PASSWORD
- search_console: missing SEARCH_CONSOLE_SITE_URL
- naver_datalab: missing NAVER_CLIENT_ID, NAVER_CLIENT_SECRET

## 자동 채널 운영 상태

- 현재 공식 1차 자동 채널은 `blogger`입니다.
- `wordpress`는 Blogger 검증 뒤 붙이는 2차 확장 채널입니다.
- blogger: ready=True / approved_ready_items=1 / command python3 scripts/upload_blogger_drafts.py
- wordpress: ready=False / approved_ready_items=1 / command python3 scripts/upload_wordpress_drafts.py

## 연결 순서

1. `.env.example`를 복사해서 `.env` 생성
2. `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET` 입력
3. `python3 scripts/bootstrap_google_oauth_credentials.py`로 client json을 자동 반영
4. `GOOGLE_OAUTH_OPEN_BROWSER=true python3 scripts/get_google_refresh_token.py` 실행
5. `python3 scripts/apply_google_oauth_result.py`로 refresh token 반영
6. `GOOGLE_REFRESH_TOKEN`, `BLOGGER_BLOG_ID` 확인
7. `BLOGGER_SYNC_SITE_PAGES=false`, `BLOGGER_SITE_PAGES_PUBLISH=false`로 첫 테스트
8. `BLOGGER_AUTO_PUBLISH_POSTS=true`, `BLOGGER_PUBLISH_ONLY_DUE_POSTS=false`, `BLOGGER_MAX_POSTS_PER_RUN=3`로 안전모드 설정
9. `bash scripts/prepare_initial_commit.sh` 실행
10. GitHub 원격 연결 후 Actions Secrets/Variables 입력
11. `python3 scripts/check_setup.py` 재실행
12. `bash scripts/run_pipeline.sh` 재실행
13. `outputs/latest/first-approval-path.md` 기준으로 첫 승인 keyword 결정
14. Blogger 검증이 안정화된 뒤에만 WordPress 값과 OpenAI/GA4/AdSense/Newsletter를 순차 추가

## 오늘 운영자가 바로 할 일

- 1순위 발행: `bitcoin` / 비트코인 핵심 흐름 해설 / urgency fresh
- 1순위 액션: 사용자 검토만 통과하면 바로 게시 후보로 유지해도 됩니다.
- 추천 묶음 승인: `가장 먼저 볼 메인 글` / command `python3 /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- 단건 승인 시작점: `bitcoin` / 비트코인 핵심 흐름 해설 / command `python3 /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- 2순위 준비: `bitcoin` / 비트코인 핵심 흐름 해설 / urgency prep_today
- 오늘 후속 SEO 후보: `FOMC 이후 시장이 주식과 코인에 미치는 영향`
- 후속 검색 의도: 뉴스를 봤지만 내 투자에 어떻게 연결되는지 쉽게 이해하고 싶은 독자
- 전체 업로드 가능 재고: 13개
- 재고판 1순위: `FOMC 이후 시장 해설` (main_post)
- 현재 1차 자동 채널: `blogger` / 실행 명령 `python3 scripts/upload_blogger_drafts.py`

## 수익화 기준에서 남은 것

- content_engine: ready
- publishing_engine: ready
- search_demand_engine: ready
- analytics_stack: not_ready
  - next: GA4 측정 ID를 연결해 어떤 글이 실제 체류시간과 재방문을 만드는지 확인합니다.
- adsense_stack: not_ready
  - next: AdSense 승인 이후 publisher id와 사이트 검증값을 붙여 수익화 스택을 완성합니다.
- retention_stack: not_ready
  - next: 뉴스레터나 텔레그램 같은 재방문 수단 URL을 연결해 한 번 들어온 독자를 쌓습니다.

## 참고 파일

- setup report: `/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/setup-check-report.json`
- publish-ready report: `/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/publish-ready-report.json`
- publish queue: `/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/publish-queue.json`
- publish inventory: `/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/publish-inventory.json`
- monetization report: `/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/monetization-readiness-report.json`
- go-live report: `/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/go-live-readiness-report.json`
- keyword opportunity board: `/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/keyword-opportunity-board.json`
- first live run plan: `/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/first-live-run-plan.json`
- github launch plan: `/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/github-launch-plan.json`
- platform publish plan: `/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/platform-publish-plan.json`
- first approval path: `/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/first-approval-path.json`
- github checklist: `/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/github-secrets-checklist.md`
