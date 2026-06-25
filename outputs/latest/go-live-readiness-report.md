# Go Live Readiness Report

- first live run ready: `False`
- monetization score: `33.3`

## Live Prerequisites

- `site_pages_html_ready`: True
- `blog_posts_ready`: True
- `blogger_connection_ready`: False
- `draft_engine_ready`: True
- `git_remote_ready`: False

## Site Pages

- required ready: `9` / `9`
- first publish target: `about`
- first publish target: `disclosure`
- first publish target: `privacy-policy`
- first publish target: `editorial-policy`
- first publish target: `contact`

## Posts

- ready posts: `3`
- first draft upload target: `fomc`
- first draft upload target: `bitcoin`
- first draft upload target: `cpi`

## Required Credentials

- `OPENAI_API_KEY`
- `GOOGLE_CLIENT_ID`
- `GOOGLE_CLIENT_SECRET`
- `GOOGLE_REFRESH_TOKEN`

## Optional Growth Keys

- `SEARCH_CONSOLE_SITE_URL`
- `SEARCH_CONSOLE_CLIENT_ID`
- `SEARCH_CONSOLE_CLIENT_SECRET`
- `SEARCH_CONSOLE_REFRESH_TOKEN`
- `GA4_MEASUREMENT_ID`
- `ADSENSE_PUBLISHER_ID`
- `ADSENSE_SITE_VERIFICATION`
- `NEWSLETTER_SUBSCRIBE_URL`

## Next Steps

- Blogger와 Google OAuth 값을 연결합니다.
- 신뢰 페이지를 먼저 Blogger Pages로 동기화합니다.
- publish queue 상위 글을 Blogger draft로 업로드합니다.
- GitHub 원격 저장소와 Actions Secrets/Variables를 연결합니다.
