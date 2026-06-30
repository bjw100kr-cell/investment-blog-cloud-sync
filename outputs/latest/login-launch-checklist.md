# Login Launch Checklist

- repo_connected: `True`
- repo_url: `https://github.com/bjw100kr-cell/investment-blog-cloud-sync`
- repo_accessible: `True`
- blogger_ready: `True`
- wordpress_ready: `False`
- search_console_ready: `False`
- openai_ready: `False`
- openai_optional: `True`
- openai_note: `현재는 OpenAI 키가 없더라도 무료 템플릿/기반 워크플로는 동작합니다.`
- next_page: [GitHub Actions secrets](https://github.com/bjw100kr-cell/investment-blog-cloud-sync/settings/secrets/actions)

## Minimum Go-Live Path

- [GitHub Actions secrets](https://github.com/bjw100kr-cell/investment-blog-cloud-sync/settings/secrets/actions): Add Actions secrets and variables for cloud runs

## Missing Keys

- `blogger_upload`: none
- `wordpress_upload`: WORDPRESS_SITE_URL, WORDPRESS_USERNAME, WORDPRESS_APPLICATION_PASSWORD
- `search_console`: SEARCH_CONSOLE_SITE_URL
- `openai_drafts`: none
- `github_actions`: none

## Open These Pages

- [Google Cloud Console](https://console.cloud.google.com/): OAuth client, API activation, consent screen setup
- [Google OAuth consent screen](https://console.cloud.google.com/apis/credentials/consent): App name, email, and consent screen publishing
- [Google OAuth client credentials](https://console.cloud.google.com/apis/credentials): Create or copy GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET
- [Search Console API activation page](https://console.cloud.google.com/apis/library/searchconsole.googleapis.com): Enable Search Console API
- [Google Search Console](https://search.google.com/search-console): Verify property access and confirm SEARCH_CONSOLE_SITE_URL
- [GitHub repository or new repo](https://github.com/bjw100kr-cell/investment-blog-cloud-sync): Connect the repo before enabling cloud automation
- [GitHub Actions secrets](https://github.com/bjw100kr-cell/investment-blog-cloud-sync/settings/secrets/actions): Add Actions secrets and variables for cloud runs

## Suggested Order

1. Blogger 필수값은 준비되어 있으니 GitHub Actions Secrets/Variables만 반영하면 됩니다.
2. Search Console은 첫 가동 뒤 붙여도 됩니다. 지금은 SEARCH_CONSOLE_SITE_URL 없이도 시작 가능합니다.
3. WordPress는 지금 열지 않고 Blogger 자동화 검증이 끝난 뒤 두 번째 채널로 붙입니다.
4. OpenAI 키도 후순위입니다. 나중에 넣으면 사람 같은 초안 품질을 더 끌어올릴 수 있습니다.
