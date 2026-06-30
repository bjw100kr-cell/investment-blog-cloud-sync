# GitHub Actions Sync Guide

- script: `/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/github-actions-sync.sh`
- repo_connected: `True`
- repo_slug: `bjw100kr-cell/investment-blog-cloud-sync`

## What It Does

- `.env`에서 비어 있지 않은 값을 읽습니다.
- GitHub Actions `Secrets`와 `Variables`를 `gh` CLI로 한 번에 올립니다.
- 이미 비어 있는 키는 자동으로 건너뜁니다.

## Usage

```bash
bash outputs/latest/github-actions-sync.sh bjw100kr-cell/investment-blog-cloud-sync
```

## Keys With Local Values That Will Sync

- `OPENAI_MODEL` (variable)
- `BLOGGER_BLOG_ID` (secret)
- `GOOGLE_CLIENT_ID` (secret)
- `GOOGLE_CLIENT_SECRET` (secret)
- `GOOGLE_REFRESH_TOKEN` (secret)
- `BLOGGER_SYNC_SITE_PAGES` (variable)
- `BLOGGER_SITE_PAGES_PUBLISH` (variable)
- `BLOGGER_INCLUDE_OPTIONAL_SITE_PAGES` (variable)
- `BLOGGER_AUTO_PUBLISH_POSTS` (variable)
- `BLOGGER_PUBLISH_ONLY_DUE_POSTS` (variable)
- `BLOGGER_MAX_POSTS_PER_RUN` (variable)
- `BLOGGER_REQUIRE_REVIEW_APPROVAL` (variable)
- `BLOG_BASE_URL` (variable)
- `SEARCH_CONSOLE_CLIENT_ID` (secret)
- `SEARCH_CONSOLE_CLIENT_SECRET` (secret)
- `SEARCH_CONSOLE_REFRESH_TOKEN` (secret)
- `SEARCH_CONSOLE_LAG_DAYS` (variable)
- `SEARCH_CONSOLE_WINDOW_DAYS` (variable)

## Local Only Keys

- `GOOGLE_REDIRECT_URI`
- `GOOGLE_OAUTH_PRESET`
- `GOOGLE_OAUTH_OPEN_BROWSER`

## Before Running

- `gh auth login` 이 완료되어 있어야 합니다.
- GitHub 저장소가 먼저 생성되어 있어야 합니다.
- `.env` 안의 값이 최신인지 확인합니다.
