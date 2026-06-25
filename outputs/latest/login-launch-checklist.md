# Login Launch Checklist

- repo_connected: `False`
- blogger_ready: `False`
- search_console_ready: `False`
- openai_ready: `True`

## Missing Keys

- `blogger_upload`: GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, GOOGLE_REFRESH_TOKEN
- `search_console`: SEARCH_CONSOLE_SITE_URL, SEARCH_CONSOLE_CLIENT_ID, SEARCH_CONSOLE_CLIENT_SECRET, SEARCH_CONSOLE_REFRESH_TOKEN
- `openai_drafts`: none
- `github_actions`: none

## Open These Pages

- [Google Cloud Console](https://console.cloud.google.com/): OAuth client, API activation, consent screen setup
- [Google OAuth consent screen](https://console.cloud.google.com/apis/credentials/consent): App name, email, and consent screen publishing
- [Google OAuth client credentials](https://console.cloud.google.com/apis/credentials): Create or copy GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET
- [Blogger API activation page](https://console.cloud.google.com/apis/library/blogger.googleapis.com): Enable Blogger API
- [Search Console API activation page](https://console.cloud.google.com/apis/library/searchconsole.googleapis.com): Enable Search Console API
- [Blogger dashboard](https://www.blogger.com/blog/posts/6916836934814427288): Check blog access and confirm BLOGGER_BLOG_ID target
- [Google Search Console](https://search.google.com/search-console): Verify property access and confirm SEARCH_CONSOLE_SITE_URL
- [GitHub repository or new repo](https://github.com/new): Connect the repo before enabling cloud automation

## Suggested Order

1. Google Cloud Console에서 Blogger API와 Search Console API를 켭니다.
2. OAuth 동의 화면과 OAuth Client를 만든 뒤 GOOGLE_CLIENT_ID / GOOGLE_CLIENT_SECRET을 확보합니다.
3. 로컬에서 get_google_refresh_token.py를 실행해 GOOGLE_REFRESH_TOKEN을 발급합니다.
4. Blogger 대시보드에서 대상 블로그가 맞는지 확인합니다.
5. Search Console에서 사이트 속성 접근 권한과 SEARCH_CONSOLE_SITE_URL을 확인합니다.
6. GitHub 저장소를 먼저 연결한 뒤 Actions Secrets/Variables에 같은 값을 입력합니다.
7. OPENAI_API_KEY를 넣어 사람 같은 초안 생성 품질을 높입니다.
