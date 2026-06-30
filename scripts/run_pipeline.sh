#!/usr/bin/env bash
set -euo pipefail
set -E

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

_approval_state_file="outputs/latest/review-approvals.json"
CURRENT_STEP="init"
CONTEXT_FLUSH_EVERY="${PIPELINE_CONTEXT_FLUSH_INTERVAL:-5}"
PIPELINE_STEP_INDEX=0

has_approved_state() {
  python3 - "$1" <<'PY'
import json
import pathlib
import sys

path = pathlib.Path(sys.argv[1])
if not path.exists():
    print("false")
    sys.exit(0)

try:
    data = json.loads(path.read_text())
except Exception:
    print("false")
    sys.exit(0)

approved_all = data.get("user_confirmed_all", data.get("approved_all", False))
approved_keywords = data.get("user_confirmed_keywords", data.get("approved_keywords", []))

print("true" if bool(approved_all or approved_keywords) else "false")
PY
}

if [[ -f ".env" ]]; then
  # shellcheck disable=SC2046
  export $(grep -v '^[[:space:]]*#' .env | grep -v '^[[:space:]]*$' | xargs)
fi

emit_checkpoint() {
  local reason="${1:-pipeline-progress}"
  python3 scripts/emit_context_checkpoint.py --note "$reason"
}

run_step() {
  local step="${1}"
  local label="${2}"
  shift 2

  CURRENT_STEP="${step}-${label}"
  emit_checkpoint "starting-${CURRENT_STEP}"
  echo "[${step}] ${label}"
  "$@"
  emit_checkpoint "completed-${CURRENT_STEP}"

  PIPELINE_STEP_INDEX=$((PIPELINE_STEP_INDEX + 1))
  if (( PIPELINE_STEP_INDEX % CONTEXT_FLUSH_EVERY == 0 )); then
    python3 scripts/persist_session_context.py -n "step-${PIPELINE_STEP_INDEX}-${CURRENT_STEP}" || true
  fi
}

on_failure() {
  local line_no="${1}"
  local cmd="${2-unknown}"
  emit_checkpoint "failed step=${CURRENT_STEP} line=${line_no} cmd=${cmd}"
  echo "Pipeline failed at ${CURRENT_STEP}" >&2
  echo "See outputs/latest/context_checkpoint.md for resume point." >&2
  exit 1
}

trap 'on_failure "$LINENO" "$BASH_COMMAND"' ERR

run_step "1/30" "Collect sources" python3 scripts/collect_investment_sources.py

run_step "2/30" "Build search demand report" python3 scripts/build_search_demand_report.py

run_step "3/30" "Fetch Search Console queries" python3 scripts/fetch_search_console_queries.py

run_step "4/30" "Convert Search Console queries to performance feedback" python3 scripts/search_console_to_feedback.py

run_step "5/30" "Compile performance feedback" python3 scripts/compile_performance_feedback.py

run_step "6/30" "Score daily topics" python3 scripts/score_daily_topics.py

run_step "7/30" "Build draft packets" python3 scripts/build_draft_packets.py

run_step "7.2/30" "Build current reference strategy" python3 scripts/build_current_reference_strategy.py

run_step "7.25/30" "Build reference strength benchmark" python3 scripts/build_reference_strength_benchmark.py

run_step "7.3/30" "Build keyword capture strategy" python3 scripts/build_keyword_capture_strategy.py

run_step "8/30" "Build editorial calendar" python3 scripts/build_editorial_calendar.py

run_step "9/30" "Generate site foundation" python3 scripts/generate_site_foundation.py

run_step "10/30" "Render site foundation pages" python3 scripts/render_site_foundation_pages.py

run_step "11/30" "Build site page publish plan" python3 scripts/build_site_page_publish_plan.py

run_step "12/30" "Generate publishing assets" python3 scripts/generate_publishing_assets.py

run_step "13/30" "Generate blog drafts" python3 scripts/generate_blog_drafts.py

run_step "14/30" "Review human tone" python3 scripts/review_human_tone.py

run_step "14.1/30" "Build draft polish board" python3 scripts/build_draft_polish_board.py

run_step "15/30" "Render publish-ready posts" python3 scripts/render_publish_ready_posts.py

run_step "16/30" "Generate growth report" python3 scripts/generate_growth_report.py

run_step "17/30" "Build publish queue" python3 scripts/build_publish_queue.py

run_step "18/30" "Build monetization readiness report" python3 scripts/build_monetization_readiness_report.py

run_step "18.2/30" "Build monetization roadmap" python3 scripts/build_monetization_roadmap.py

run_step "19/30" "Build go-live readiness report" python3 scripts/build_go_live_readiness_report.py

run_step "20/30" "Build SEO backlog" python3 scripts/build_seo_backlog.py

run_step "21/30" "Build SEO draft packets" python3 scripts/build_seo_draft_packets.py

run_step "22/30" "Generate SEO blog drafts" python3 scripts/generate_seo_blog_drafts.py

run_step "23/30" "Build keyword opportunity board" python3 scripts/build_keyword_opportunity_board.py

run_step "24/30" "Generate SEO publishing assets" python3 scripts/generate_seo_publishing_assets.py

run_step "24.5/30" "Build safe image suggestions" python3 scripts/build_safe_image_suggestions.py

run_step "25/30" "Render SEO publish-ready posts" python3 scripts/render_seo_publish_ready_posts.py

run_step "26/30" "Build publish inventory" python3 scripts/build_publish_inventory.py

run_step "27/34" "Build distribution pack" python3 scripts/build_distribution_pack.py

run_step "27.2/34" "Build pre-publish quality gate" python3 scripts/build_pre_publish_quality_gate.py

run_step "27.3/34" "Build cross-platform publish pack" python3 scripts/build_cross_platform_publish_pack.py

run_step "28/34" "Prepare first live run plan" python3 scripts/prepare_first_live_run_plan.py

run_step "28.2/34" "Build automation scope" python3 scripts/build_automation_scope.py

run_step "28.5/34" "Build platform publish plan" python3 scripts/build_platform_publish_plan.py

run_step "29/34" "Build review packet" python3 scripts/build_review_packet.py

run_step "30/34" "Build approval dashboard" python3 scripts/build_approval_dashboard.py

run_step "30.2/34" "Build first approval path" python3 scripts/build_first_approval_path.py

run_step "30.3/34" "Build daily revenue focus" python3 scripts/build_daily_revenue_focus.py

run_step "30.35/34" "Build traffic cluster board" python3 scripts/build_traffic_cluster_board.py

run_step "30.36/34" "Build popular reads board" python3 scripts/build_popular_reads_board.py

run_step "30.37/34" "Build retention CTA board" python3 scripts/build_retention_cta_board.py

run_step "30.4/34" "Build first publish operator run preview" python3 scripts/first_publish_operator_run.py

run_step "30.45/34" "Build user review shortlist" python3 scripts/build_user_review_shortlist.py

run_step "30.452/35" "Build full draft review sheet" python3 scripts/build_full_draft_review_sheet.py

run_step "30.453/35" "Build approval evidence sheet" python3 scripts/build_approval_evidence_sheet.py

run_step "30.454/35" "Build approval briefing board" python3 scripts/build_approval_briefing_board.py

run_step "30.4545/35" "Build shortlist publish action board" python3 scripts/build_shortlist_publish_action_board.py

run_step "30.4547/35" "Build shortlist launchpad" python3 scripts/build_shortlist_launchpad.py

run_step "30.45475/35" "Build source freshness board" python3 scripts/build_source_freshness_board.py

run_step "30.4548/35" "Build current review focus" python3 scripts/build_current_review_focus.py

run_step "30.4549/35" "Build user approval inbox" python3 scripts/build_user_approval_inbox.py

run_step "30.45495/35" "Build user review checkpoint" python3 scripts/build_user_review_checkpoint.py

run_step "30.4550/39" "Build GitHub minimum launch card" python3 scripts/build_github_minimum_launch_card.py

run_step "30.4551/39" "Build automation progress board" python3 scripts/build_automation_progress_board.py

run_step "30.4552/39" "Build automation unblock card" python3 scripts/build_automation_unblock_card.py

run_step "30.4553/39" "Build minimum unblock flow" python3 scripts/run_minimum_unblock_flow.py

run_step "30.4554/39" "Build first Blogger verify card" python3 scripts/build_first_blogger_verify_card.py

run_step "30.4555/39" "Build first Blogger verify flow" python3 scripts/run_first_blogger_verify_flow.py

run_step "30.456/39" "Build image upgrade queue" python3 scripts/build_image_upgrade_queue.py

run_step "30.457/39" "Build image leverage board" python3 scripts/build_image_leverage_board.py

run_step "30.458/39" "Build top image action card" python3 scripts/build_top_image_action_card.py

run_step "30.46/39" "Build review preview board" python3 scripts/build_review_preview_board.py

run_step "30.47/39" "Build today operator console" python3 scripts/build_today_operator_console.py

run_step "30.48/39" "Build operator home" python3 scripts/build_operator_home.py

CURRENT_STEP="30.5/39-cloud-run-verification"
emit_checkpoint "starting-${CURRENT_STEP}"
echo "[30.5/39] Prepare first cloud run verification"
if [[ "$(has_approved_state "$_approval_state_file")" == "true" ]]; then
  python3 scripts/prepare_first_cloud_run_verification.py --allow-approved-state
else
  python3 scripts/prepare_first_cloud_run_verification.py
fi
emit_checkpoint "completed-${CURRENT_STEP}"

run_step "30.6/39" "Prepare first run values card" python3 scripts/prepare_first_run_values_card.py

run_step "30.7/39" "Build pipeline workflow parity" python3 scripts/build_pipeline_workflow_parity.py

run_step "30.71/39" "Build cloud launch preflight" python3 scripts/build_cloud_launch_preflight.py

CURRENT_STEP="32/39-sync-blogger-site"
emit_checkpoint "starting-${CURRENT_STEP}"
echo "[32/39] Sync Blogger site pages"
if [[ -n "${BLOGGER_BLOG_ID:-}" && -n "${GOOGLE_CLIENT_ID:-}" && -n "${GOOGLE_CLIENT_SECRET:-}" && -n "${GOOGLE_REFRESH_TOKEN:-}" ]]; then
  python3 scripts/sync_blogger_site_pages.py
else
  echo "Skip: Blogger credentials not set (BLOGGER_BLOG_ID, GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, GOOGLE_REFRESH_TOKEN)"
  echo "Tip: run with credentials set to enable site page sync."
fi
emit_checkpoint "completed-${CURRENT_STEP}"

CURRENT_STEP="33/39-upload-blogger"
emit_checkpoint "starting-${CURRENT_STEP}"
echo "[33/39] Upload Blogger drafts"
if [[ -n "${BLOGGER_BLOG_ID:-}" && -n "${GOOGLE_CLIENT_ID:-}" && -n "${GOOGLE_CLIENT_SECRET:-}" && -n "${GOOGLE_REFRESH_TOKEN:-}" ]]; then
  BLOGGER_REQUIRE_REVIEW_APPROVAL="${BLOGGER_REQUIRE_REVIEW_APPROVAL:-false}" \
  python3 scripts/upload_blogger_drafts.py
else
  echo "Skip: Blogger credentials not set (BLOGGER_BLOG_ID, GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, GOOGLE_REFRESH_TOKEN)"
  echo "Publish plan and draft assets were still generated above."
fi
emit_checkpoint "completed-${CURRENT_STEP}"

CURRENT_STEP="34/39-upload-wordpress"
emit_checkpoint "starting-${CURRENT_STEP}"
echo "[34/39] Upload WordPress drafts"
if [[ -n "${WORDPRESS_SITE_URL:-}" && -n "${WORDPRESS_USERNAME:-}" && -n "${WORDPRESS_APPLICATION_PASSWORD:-}" ]]; then
  WORDPRESS_REQUIRE_REVIEW_APPROVAL="${WORDPRESS_REQUIRE_REVIEW_APPROVAL:-true}" \
  python3 scripts/upload_wordpress_drafts.py
else
  echo "Skip: WordPress credentials not set (WORDPRESS_SITE_URL, WORDPRESS_USERNAME, WORDPRESS_APPLICATION_PASSWORD)"
  echo "Publish plan and draft assets were still generated above."
fi
emit_checkpoint "completed-${CURRENT_STEP}"

run_step "35/39" "Emit context checkpoint" python3 scripts/emit_context_checkpoint.py --note "pipeline-finished"

echo "[35.1/39] Persist compressed session context"
python3 scripts/persist_session_context.py -n "pipeline-finished"

echo
echo "Pipeline finished."
echo "Check outputs/latest/ for results."

emit_checkpoint "pipeline-finished"
