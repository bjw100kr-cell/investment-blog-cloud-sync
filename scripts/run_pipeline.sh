#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

if [[ -f ".env" ]]; then
  # shellcheck disable=SC2046
  export $(grep -v '^[[:space:]]*#' .env | grep -v '^[[:space:]]*$' | xargs)
fi

echo "[1/30] Collect sources"
python3 scripts/collect_investment_sources.py

echo "[2/30] Build search demand report"
python3 scripts/build_search_demand_report.py

echo "[3/30] Fetch Search Console queries"
python3 scripts/fetch_search_console_queries.py

echo "[4/30] Convert Search Console queries to performance feedback"
python3 scripts/search_console_to_feedback.py

echo "[5/30] Compile performance feedback"
python3 scripts/compile_performance_feedback.py

echo "[6/30] Score daily topics"
python3 scripts/score_daily_topics.py

echo "[7/30] Build draft packets"
python3 scripts/build_draft_packets.py

echo "[8/30] Build editorial calendar"
python3 scripts/build_editorial_calendar.py

echo "[9/30] Generate site foundation"
python3 scripts/generate_site_foundation.py

echo "[10/30] Render site foundation pages"
python3 scripts/render_site_foundation_pages.py

echo "[11/30] Build site page publish plan"
python3 scripts/build_site_page_publish_plan.py

echo "[12/30] Generate publishing assets"
python3 scripts/generate_publishing_assets.py

echo "[13/30] Generate blog drafts"
python3 scripts/generate_blog_drafts.py

echo "[14/30] Review human tone"
python3 scripts/review_human_tone.py

echo "[15/30] Render publish-ready posts"
python3 scripts/render_publish_ready_posts.py

echo "[16/30] Generate growth report"
python3 scripts/generate_growth_report.py

echo "[17/30] Build publish queue"
python3 scripts/build_publish_queue.py

echo "[18/30] Build monetization readiness report"
python3 scripts/build_monetization_readiness_report.py

echo "[19/30] Build go-live readiness report"
python3 scripts/build_go_live_readiness_report.py

echo "[20/30] Build SEO backlog"
python3 scripts/build_seo_backlog.py

echo "[21/30] Build SEO draft packets"
python3 scripts/build_seo_draft_packets.py

echo "[22/30] Generate SEO blog drafts"
python3 scripts/generate_seo_blog_drafts.py

echo "[23/30] Build keyword opportunity board"
python3 scripts/build_keyword_opportunity_board.py

echo "[24/30] Generate SEO publishing assets"
python3 scripts/generate_seo_publishing_assets.py

echo "[25/30] Render SEO publish-ready posts"
python3 scripts/render_seo_publish_ready_posts.py

echo "[26/30] Build publish inventory"
python3 scripts/build_publish_inventory.py

echo "[27/30] Build distribution pack"
python3 scripts/build_distribution_pack.py

echo "[28/30] Prepare first live run plan"
python3 scripts/prepare_first_live_run_plan.py

echo "[29/30] Sync Blogger site pages"
if [[ -n "${BLOGGER_BLOG_ID:-}" && -n "${GOOGLE_CLIENT_ID:-}" && -n "${GOOGLE_CLIENT_SECRET:-}" && -n "${GOOGLE_REFRESH_TOKEN:-}" ]]; then
  python3 scripts/sync_blogger_site_pages.py
else
  echo "Skip: Blogger credentials not set (BLOGGER_BLOG_ID, GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, GOOGLE_REFRESH_TOKEN)"
  echo "Tip: run with credentials set to enable site page sync."
fi

echo "[30/30] Upload Blogger drafts"
if [[ -n "${BLOGGER_BLOG_ID:-}" && -n "${GOOGLE_CLIENT_ID:-}" && -n "${GOOGLE_CLIENT_SECRET:-}" && -n "${GOOGLE_REFRESH_TOKEN:-}" ]]; then
  python3 scripts/upload_blogger_drafts.py
else
  echo "Skip: Blogger credentials not set (BLOGGER_BLOG_ID, GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, GOOGLE_REFRESH_TOKEN)"
  echo "Publish plan and draft assets were still generated above."
fi

echo
echo "Pipeline finished."
echo "Check outputs/latest/ for results."
