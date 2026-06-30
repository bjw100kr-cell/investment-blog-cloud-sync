#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

if ! command -v gh >/dev/null 2>&1; then
  echo "GitHub CLI (gh)가 설치되어 있지 않습니다."
  echo "https://cli.github.com/ 에서 설치 후 다시 실행하세요."
  exit 1
fi

if [[ ! -f ".env" ]]; then
  echo ".env 파일이 없습니다."
  exit 1
fi

REPO_SLUG="${1:-bjw100kr-cell/investment-blog-cloud-sync}"
SECRET_KEYS=("NAVER_CLIENT_ID" "NAVER_CLIENT_SECRET" "SEARCH_CONSOLE_SITE_URL" "SEARCH_CONSOLE_CLIENT_ID" "SEARCH_CONSOLE_CLIENT_SECRET" "SEARCH_CONSOLE_REFRESH_TOKEN" "OPENAI_API_KEY" "BLOGGER_BLOG_ID" "GOOGLE_CLIENT_ID" "GOOGLE_CLIENT_SECRET" "GOOGLE_REFRESH_TOKEN" "GOOGLE_ACCESS_TOKEN" "SEARCH_CONSOLE_ACCESS_TOKEN" "WORDPRESS_SITE_URL" "WORDPRESS_USERNAME" "WORDPRESS_APPLICATION_PASSWORD")
VARIABLE_KEYS=("SEARCH_CONSOLE_LAG_DAYS" "SEARCH_CONSOLE_WINDOW_DAYS" "OPENAI_MODEL" "BLOG_BASE_URL" "BLOGGER_SYNC_SITE_PAGES" "BLOGGER_SITE_PAGES_PUBLISH" "BLOGGER_INCLUDE_OPTIONAL_SITE_PAGES" "BLOGGER_REQUIRE_REVIEW_APPROVAL" "BLOGGER_AUTO_PUBLISH_POSTS" "BLOGGER_PUBLISH_ONLY_DUE_POSTS" "BLOGGER_MAX_POSTS_PER_RUN" "WORDPRESS_AUTO_PUBLISH_POSTS" "WORDPRESS_PUBLISH_ONLY_DUE_POSTS" "WORDPRESS_MAX_POSTS_PER_RUN" "GA4_MEASUREMENT_ID" "ADSENSE_PUBLISHER_ID" "ADSENSE_SITE_VERIFICATION" "NEWSLETTER_SUBSCRIBE_URL")

set -a
source .env
set +a

echo "Sync target repo: $REPO_SLUG"
echo

for key in "${SECRET_KEYS[@]}"; do
  value="${!key:-}"
  if [[ -z "$value" ]]; then
    echo "skip secret: $key (empty)"
    continue
  fi
  gh secret set "$key" --repo "$REPO_SLUG" --body "$value"
  echo "set secret: $key"
done

for key in "${VARIABLE_KEYS[@]}"; do
  value="${!key:-}"
  if [[ -z "$value" ]]; then
    echo "skip variable: $key (empty)"
    continue
  fi
  gh variable set "$key" --repo "$REPO_SLUG" --body "$value"
  echo "set variable: $key"
done

echo
echo "GitHub Actions secrets/variables sync complete."
echo "Next: GitHub Actions -> Daily Investment Intake -> Run workflow"
