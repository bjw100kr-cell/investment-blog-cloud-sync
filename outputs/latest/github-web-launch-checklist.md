# GitHub Web Launch Checklist

- repo_connected: `True`
- repo_accessible: `True`
- repo_slug: `bjw100kr-cell/investment-blog-cloud-sync`
- repo_accessible: `True`
- gh_installed: `False`
- repo_create_link: https://github.com/bjw100kr-cell/investment-blog-cloud-sync
- actions_secrets_link: https://github.com/bjw100kr-cell/investment-blog-cloud-sync/settings/secrets/actions
- actions_run_link: https://github.com/bjw100kr-cell/investment-blog-cloud-sync/actions/workflows/daily-investment-intake.yml

## Minimum Go-Live Path

- 지금 필요한 Secrets 수: `4`
- 지금 필요한 Variables 수: `8`
- WordPress 지금 필수 여부: `False`
- OpenAI 지금 필수 여부: `False`
- 첫 목표: GitHub Actions에서 Blogger 자동 업로드/공개가 정상적으로 동작하는지 확인

## UI Path

- repo_creation: `GitHub > New repository`
- actions_settings: `Repo > Settings > Secrets and variables > Actions`
- workflow_run: `Repo > Actions > Daily Investment Intake > Run workflow`

## First Run Secrets

- `BLOGGER_BLOG_ID`: Blogger 업로드 대상 블로그 ID / local_filled=True
- `GOOGLE_CLIENT_ID`: Google OAuth client id / local_filled=True
- `GOOGLE_CLIENT_SECRET`: Google OAuth client secret / local_filled=True
- `GOOGLE_REFRESH_TOKEN`: Blogger 업로드용 refresh token / local_filled=True

## Secrets Copy Checklist

```text
BLOGGER_BLOG_ID
GOOGLE_CLIENT_ID
GOOGLE_CLIENT_SECRET
GOOGLE_REFRESH_TOKEN
```

## First Run Variables

- `OPENAI_MODEL=gpt-4o-mini`: 초안 생성 모델. 현재 기본값 유지 가능 / local_filled=True
- `BLOGGER_SYNC_SITE_PAGES=false`: 필요 시 신뢰 페이지까지 동기화 / local_filled=True
- `BLOGGER_SITE_PAGES_PUBLISH=false`: 첫 실행에서는 페이지도 공개하지 않음 / local_filled=True
- `BLOGGER_INCLUDE_OPTIONAL_SITE_PAGES=false`: 필수 페이지부터 시작 / local_filled=True
- `BLOGGER_REQUIRE_REVIEW_APPROVAL=false`: 자동 모드면 승인 단계 생략 / local_filled=True
- `BLOGGER_AUTO_PUBLISH_POSTS=true`: 드래프트 업로드 후 즉시 공개 / local_filled=True
- `BLOGGER_PUBLISH_ONLY_DUE_POSTS=false`: 발행일 제한 없이 동작 / local_filled=True
- `BLOGGER_MAX_POSTS_PER_RUN=3`: 처음부터 3건씩 처리(필요 시 조정) / local_filled=True

## WordPress Later

- secret `WORDPRESS_SITE_URL`: WordPress 사이트 주소 / local_filled=False
- secret `WORDPRESS_USERNAME`: WordPress 로그인 계정 / local_filled=False
- secret `WORDPRESS_APPLICATION_PASSWORD`: WordPress Application Password / local_filled=False
- variable `WORDPRESS_AUTO_PUBLISH_POSTS=false`: 초기에는 draft만 생성 / local_filled=False
- variable `WORDPRESS_PUBLISH_ONLY_DUE_POSTS=true`: 기한 도래 글만 대상으로 제한 / local_filled=False
- variable `WORDPRESS_MAX_POSTS_PER_RUN=1`: 첫 실행은 1건만 업로드 / local_filled=False

## Variables Copy Block

```text
OPENAI_MODEL=gpt-4o-mini
BLOGGER_SYNC_SITE_PAGES=false
BLOGGER_SITE_PAGES_PUBLISH=false
BLOGGER_INCLUDE_OPTIONAL_SITE_PAGES=false
BLOGGER_REQUIRE_REVIEW_APPROVAL=false
BLOGGER_AUTO_PUBLISH_POSTS=true
BLOGGER_PUBLISH_ONLY_DUE_POSTS=false
BLOGGER_MAX_POSTS_PER_RUN=3
```

## Next Steps

1. GitHub에서 새 public repo를 만듭니다.
2. 로컬에서 `bash scripts/bootstrap_github_remote.sh <OWNER/REPO>` 를 실행합니다.
3. GitHub 웹 UI에서 Actions Secrets 4개와 Variables를 먼저 입력합니다.
4. Actions에서 Daily Investment Intake를 수동 실행합니다.
5. Blogger 업로드 결과에서 processed_count, published, skipped 이유를 확인합니다.

## Fastest Reference

- 더 짧은 값 카드: `/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/first-run-values-card.md`
