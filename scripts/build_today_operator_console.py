#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GO_LIVE_DASHBOARD_JSON = ROOT / "outputs/latest/go-live-dashboard.json"
USER_REVIEW_SHORTLIST_JSON = ROOT / "outputs/latest/user-review-shortlist.json"
FIRST_APPROVAL_PATH_JSON = ROOT / "outputs/latest/first-approval-path.json"
FIRST_PUBLISH_OPERATOR_RUN_JSON = ROOT / "outputs/latest/first-publish-operator-run.json"
DAILY_REVENUE_FOCUS_JSON = ROOT / "outputs/latest/daily-revenue-focus.json"
DAILY_TRAFFIC_GOAL_JSON = ROOT / "outputs/latest/daily-traffic-goal.json"
MONETIZATION_ROADMAP_JSON = ROOT / "outputs/latest/monetization-roadmap.json"
IMAGE_UPGRADE_QUEUE_JSON = ROOT / "outputs/latest/image-upgrade-queue.json"
IMAGE_LEVERAGE_BOARD_JSON = ROOT / "outputs/latest/image-leverage-board.json"
TOP_IMAGE_ACTION_CARD_MD = ROOT / "outputs/latest/top-image-action-card.md"
OUTPUT_JSON = ROOT / "outputs/latest/today-operator-console.json"
OUTPUT_MD = ROOT / "outputs/latest/today-operator-console.md"
REVIEW_PREVIEW_BOARD_HTML = ROOT / "outputs/latest/review-preview-board.html"
REVIEW_PACKET_MD = ROOT / "outputs/latest/review-packet.md"
USER_REVIEW_SHORTLIST_MD = ROOT / "outputs/latest/user-review-shortlist.md"
REFERENCE_STRENGTH_BENCHMARK_MD = ROOT / "outputs/latest/reference-strength-benchmark.md"
IMAGE_UPGRADE_QUEUE_MD = ROOT / "outputs/latest/image-upgrade-queue.md"
IMAGE_LEVERAGE_BOARD_MD = ROOT / "outputs/latest/image-leverage-board.md"
FULL_DRAFT_REVIEW_SHEET_MD = ROOT / "outputs/latest/full-draft-review-sheet.md"
DRAFT_POLISH_BOARD_MD = ROOT / "outputs/latest/draft-polish-board.md"
DAILY_TRAFFIC_GOAL_MD = ROOT / "outputs/latest/daily-traffic-goal.md"
TRAFFIC_CLUSTER_BOARD_MD = ROOT / "outputs/latest/traffic-cluster-board.md"
TRAFFIC_AMPLIFICATION_PLAN_MD = ROOT / "outputs/latest/traffic-amplification-plan.md"
VISITOR_PROOF_BOARD_JSON = ROOT / "outputs/latest/visitor-proof-board.json"
VISITOR_PROOF_BOARD_MD = ROOT / "outputs/latest/visitor-proof-board.md"
SEARCH_CONSOLE_SETUP_CARD_MD = ROOT / "outputs/latest/search-console-setup-card.md"
INDEXING_PRIORITY_PACK_MD = ROOT / "outputs/latest/indexing-priority-pack.md"
INTERNAL_LINK_APPLICATION_REPORT_MD = ROOT / "outputs/latest/internal-link-application-report.md"
POPULAR_READS_APPLICATION_REPORT_MD = ROOT / "outputs/latest/popular-reads-application-report.md"
READER_SHARE_APPLICATION_REPORT_MD = ROOT / "outputs/latest/reader-share-application-report.md"
POPULAR_READS_BOARD_MD = ROOT / "outputs/latest/popular-reads-board.md"
RETENTION_CTA_BOARD_MD = ROOT / "outputs/latest/retention-cta-board.md"
EDITORIAL_CALENDAR_MD = ROOT / "outputs/latest/editorial-calendar.md"
APPROVAL_EVIDENCE_SHEET_MD = ROOT / "outputs/latest/approval-evidence-sheet.md"
APPROVAL_BRIEFING_BOARD_HTML = ROOT / "outputs/latest/approval-briefing-board.html"
SHORTLIST_PUBLISH_ACTION_BOARD_MD = ROOT / "outputs/latest/shortlist-publish-action-board.md"
SHORTLIST_LAUNCHPAD_HTML = ROOT / "outputs/latest/shortlist-launchpad.html"
CURRENT_REVIEW_FOCUS_HTML = ROOT / "outputs/latest/current-review-focus.html"
USER_APPROVAL_INBOX_HTML = ROOT / "outputs/latest/user-approval-inbox.html"
USER_APPROVAL_INBOX_JSON = ROOT / "outputs/latest/user-approval-inbox.json"
USER_REVIEW_CHECKPOINT_HTML = ROOT / "outputs/latest/user-review-checkpoint.html"
SOURCE_FRESHNESS_BOARD_MD = ROOT / "outputs/latest/source-freshness-board.md"
GITHUB_MINIMUM_LAUNCH_CARD_MD = ROOT / "outputs/latest/github-minimum-launch-card.md"
PIPELINE_WORKFLOW_PARITY_MD = ROOT / "outputs/latest/pipeline-workflow-parity.md"
CLOUD_LAUNCH_PREFLIGHT_MD = ROOT / "outputs/latest/cloud-launch-preflight.md"
AUTOMATION_PROGRESS_BOARD_MD = ROOT / "outputs/latest/automation-progress-board.md"
AUTOMATION_UNBLOCK_CARD_MD = ROOT / "outputs/latest/automation-unblock-card.md"
MINIMUM_UNBLOCK_FLOW_MD = ROOT / "outputs/latest/minimum-unblock-flow.md"
FIRST_BLOGGER_VERIFY_CARD_MD = ROOT / "outputs/latest/first-blogger-verify-card.md"
CROSS_PLATFORM_PUBLISH_PACK_JSON = ROOT / "outputs/latest/cross-platform-publish-pack.json"
CLICK_TITLE_SYNC_REPORT_MD = ROOT / "outputs/latest/click-title-sync-report.md"
TITLE_EXPERIMENT_BOARD_MD = ROOT / "outputs/latest/title-experiment-board.md"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def build_report() -> dict:
    dashboard = load_json(GO_LIVE_DASHBOARD_JSON)
    shortlist = load_json(USER_REVIEW_SHORTLIST_JSON)
    approval = load_json(FIRST_APPROVAL_PATH_JSON)
    operator_run = load_json(FIRST_PUBLISH_OPERATOR_RUN_JSON)
    revenue_focus = load_json(DAILY_REVENUE_FOCUS_JSON)
    traffic_goal = load_json(DAILY_TRAFFIC_GOAL_JSON)
    visitor_proof = load_json(VISITOR_PROOF_BOARD_JSON)
    roadmap = load_json(MONETIZATION_ROADMAP_JSON)
    image_upgrade_queue = load_json(IMAGE_UPGRADE_QUEUE_JSON)
    image_leverage_board = load_json(IMAGE_LEVERAGE_BOARD_JSON)
    approval_inbox = load_json(USER_APPROVAL_INBOX_JSON)
    reply_flow_examples = approval_inbox.get("reply_flow_examples", [])

    return {
        "top_state": {
            "ready_for_first_live_run": dashboard.get("ready_for_first_live_run", False),
            "repo_connected": dashboard.get("repo_connected", False),
            "first_live_run_status": dashboard.get("first_live_run_status", ""),
            "github_launch_status": dashboard.get("github_launch_status", ""),
        },
        "review_shortlist": shortlist.get("shortlist", [])[:3],
        "approval": {
            "single_command": (shortlist.get("single_approval_command") or (approval.get("recommended_single") or {}).get("approval_command", "")),
            "batch_command": (shortlist.get("batch_approval_command") or (approval.get("recommended_batch") or {}).get("approval_command", "")),
        },
        "review_board": {
            "html_path": str(REVIEW_PREVIEW_BOARD_HTML),
            "exists": REVIEW_PREVIEW_BOARD_HTML.exists(),
        },
        "review_paths": {
            "shortlist_md": str(USER_REVIEW_SHORTLIST_MD),
            "reference_strength_benchmark_md": str(REFERENCE_STRENGTH_BENCHMARK_MD),
            "review_packet_md": str(REVIEW_PACKET_MD),
            "image_upgrade_queue_md": str(IMAGE_UPGRADE_QUEUE_MD),
            "image_leverage_board_md": str(IMAGE_LEVERAGE_BOARD_MD),
            "top_image_action_card_md": str(TOP_IMAGE_ACTION_CARD_MD),
            "full_draft_review_sheet_md": str(FULL_DRAFT_REVIEW_SHEET_MD),
            "draft_polish_board_md": str(DRAFT_POLISH_BOARD_MD),
            "daily_traffic_goal_md": str(DAILY_TRAFFIC_GOAL_MD),
            "traffic_cluster_board_md": str(TRAFFIC_CLUSTER_BOARD_MD),
            "traffic_amplification_plan_md": str(TRAFFIC_AMPLIFICATION_PLAN_MD),
            "visitor_proof_board_md": str(VISITOR_PROOF_BOARD_MD),
            "search_console_setup_card_md": str(SEARCH_CONSOLE_SETUP_CARD_MD),
            "indexing_priority_pack_md": str(INDEXING_PRIORITY_PACK_MD),
            "internal_link_application_report_md": str(INTERNAL_LINK_APPLICATION_REPORT_MD),
            "popular_reads_application_report_md": str(POPULAR_READS_APPLICATION_REPORT_MD),
            "reader_share_application_report_md": str(READER_SHARE_APPLICATION_REPORT_MD),
            "popular_reads_board_md": str(POPULAR_READS_BOARD_MD),
            "retention_cta_board_md": str(RETENTION_CTA_BOARD_MD),
            "editorial_calendar_md": str(EDITORIAL_CALENDAR_MD),
            "approval_evidence_sheet_md": str(APPROVAL_EVIDENCE_SHEET_MD),
            "approval_briefing_board_html": str(APPROVAL_BRIEFING_BOARD_HTML),
            "shortlist_publish_action_board_md": str(SHORTLIST_PUBLISH_ACTION_BOARD_MD),
            "shortlist_launchpad_html": str(SHORTLIST_LAUNCHPAD_HTML),
            "current_review_focus_html": str(CURRENT_REVIEW_FOCUS_HTML),
            "user_approval_inbox_html": str(USER_APPROVAL_INBOX_HTML),
            "user_review_checkpoint_html": str(USER_REVIEW_CHECKPOINT_HTML),
            "source_freshness_board_md": str(SOURCE_FRESHNESS_BOARD_MD),
            "github_minimum_launch_card_md": str(GITHUB_MINIMUM_LAUNCH_CARD_MD),
            "pipeline_workflow_parity_md": str(PIPELINE_WORKFLOW_PARITY_MD),
            "cloud_launch_preflight_md": str(CLOUD_LAUNCH_PREFLIGHT_MD),
            "automation_progress_board_md": str(AUTOMATION_PROGRESS_BOARD_MD),
            "automation_unblock_card_md": str(AUTOMATION_UNBLOCK_CARD_MD),
            "minimum_unblock_flow_md": str(MINIMUM_UNBLOCK_FLOW_MD),
            "first_blogger_verify_card_md": str(FIRST_BLOGGER_VERIFY_CARD_MD),
            "click_title_sync_report_md": str(CLICK_TITLE_SYNC_REPORT_MD),
            "title_experiment_board_md": str(TITLE_EXPERIMENT_BOARD_MD),
        },
        "operator_run": {
            "approval_mode": operator_run.get("approval_mode", ""),
            "planned_commands": operator_run.get("planned_commands", [])[:4],
        },
        "reply_flow": {
            "preview_command": reply_flow_examples[0] if reply_flow_examples else "",
            "apply_command": reply_flow_examples[1] if len(reply_flow_examples) > 1 else "",
        },
        "revenue_path": revenue_focus.get("today_path", [])[:3],
        "traffic_goal": traffic_goal,
        "visitor_proof": visitor_proof,
        "roadmap_phases": roadmap.get("phases", [])[:3],
        "image_upgrade_queue": image_upgrade_queue.get("items", [])[:3],
        "image_leverage_lanes": image_leverage_board.get("lanes", [])[:3],
        "cross_platform_publish_pack": json.loads(CROSS_PLATFORM_PUBLISH_PACK_JSON.read_text())
        if CROSS_PLATFORM_PUBLISH_PACK_JSON.exists()
        else {},
    }


def write_markdown(report: dict) -> None:
    state = report.get("top_state", {})
    lines = []
    lines.append("# Today Operator Console")
    lines.append("")
    lines.append("오늘 운영자가 바로 보면 되는 핵심만 모은 한 장짜리 콘솔입니다.")
    lines.append("")
    lines.append(f"- ready_for_first_live_run: `{state.get('ready_for_first_live_run', False)}`")
    lines.append(f"- repo_connected: `{state.get('repo_connected', False)}`")
    lines.append(f"- first_live_run_status: `{state.get('first_live_run_status', '')}`")
    lines.append(f"- github_launch_status: `{state.get('github_launch_status', '')}`")
    lines.append("")
    lines.append("## 1. 먼저 읽을 글")
    lines.append("")
    lines.append(f"- shortlist: `{report.get('review_paths', {}).get('shortlist_md', '')}`")
    lines.append(f"- reference strength benchmark: `{report.get('review_paths', {}).get('reference_strength_benchmark_md', '')}`")
    lines.append(f"- user review checkpoint: `{report.get('review_paths', {}).get('user_review_checkpoint_html', '')}`")
    lines.append(f"- current review focus: `{report.get('review_paths', {}).get('current_review_focus_html', '')}`")
    lines.append(f"- user approval inbox: `{report.get('review_paths', {}).get('user_approval_inbox_html', '')}`")
    lines.append(f"- source freshness board: `{report.get('review_paths', {}).get('source_freshness_board_md', '')}`")
    lines.append(f"- github minimum launch card: `{report.get('review_paths', {}).get('github_minimum_launch_card_md', '')}`")
    lines.append(f"- pipeline workflow parity: `{report.get('review_paths', {}).get('pipeline_workflow_parity_md', '')}`")
    lines.append(f"- cloud launch preflight: `{report.get('review_paths', {}).get('cloud_launch_preflight_md', '')}`")
    lines.append(f"- automation progress board: `{report.get('review_paths', {}).get('automation_progress_board_md', '')}`")
    lines.append(f"- automation unblock card: `{report.get('review_paths', {}).get('automation_unblock_card_md', '')}`")
    lines.append(f"- minimum unblock flow: `{report.get('review_paths', {}).get('minimum_unblock_flow_md', '')}`")
    lines.append(f"- first blogger verify card: `{report.get('review_paths', {}).get('first_blogger_verify_card_md', '')}`")
    lines.append(f"- click title sync report: `{report.get('review_paths', {}).get('click_title_sync_report_md', '')}`")
    lines.append(f"- title experiment board: `{report.get('review_paths', {}).get('title_experiment_board_md', '')}`")
    lines.append(f"- review packet: `{report.get('review_paths', {}).get('review_packet_md', '')}`")
    lines.append(f"- full draft review sheet: `{report.get('review_paths', {}).get('full_draft_review_sheet_md', '')}`")
    lines.append(f"- draft polish board: `{report.get('review_paths', {}).get('draft_polish_board_md', '')}`")
    lines.append(f"- daily traffic goal: `{report.get('review_paths', {}).get('daily_traffic_goal_md', '')}`")
    lines.append(f"- traffic cluster board: `{report.get('review_paths', {}).get('traffic_cluster_board_md', '')}`")
    lines.append(f"- traffic amplification plan: `{report.get('review_paths', {}).get('traffic_amplification_plan_md', '')}`")
    lines.append(f"- visitor proof board: `{report.get('review_paths', {}).get('visitor_proof_board_md', '')}`")
    lines.append(f"- search console setup card: `{report.get('review_paths', {}).get('search_console_setup_card_md', '')}`")
    lines.append(f"- indexing priority pack: `{report.get('review_paths', {}).get('indexing_priority_pack_md', '')}`")
    lines.append(f"- internal link application report: `{report.get('review_paths', {}).get('internal_link_application_report_md', '')}`")
    lines.append(f"- popular reads application report: `{report.get('review_paths', {}).get('popular_reads_application_report_md', '')}`")
    lines.append(f"- reader share application report: `{report.get('review_paths', {}).get('reader_share_application_report_md', '')}`")
    lines.append(f"- popular reads board: `{report.get('review_paths', {}).get('popular_reads_board_md', '')}`")
    lines.append(f"- retention cta board: `{report.get('review_paths', {}).get('retention_cta_board_md', '')}`")
    lines.append(f"- editorial calendar: `{report.get('review_paths', {}).get('editorial_calendar_md', '')}`")
    lines.append(f"- approval evidence sheet: `{report.get('review_paths', {}).get('approval_evidence_sheet_md', '')}`")
    lines.append(f"- approval briefing board: `{report.get('review_paths', {}).get('approval_briefing_board_html', '')}`")
    lines.append(f"- shortlist publish action board: `{report.get('review_paths', {}).get('shortlist_publish_action_board_md', '')}`")
    lines.append(f"- shortlist launchpad: `{report.get('review_paths', {}).get('shortlist_launchpad_html', '')}`")
    lines.append(f"- image upgrade queue: `{report.get('review_paths', {}).get('image_upgrade_queue_md', '')}`")
    lines.append(f"- image leverage board: `{report.get('review_paths', {}).get('image_leverage_board_md', '')}`")
    lines.append(f"- top image action card: `{report.get('review_paths', {}).get('top_image_action_card_md', '')}`")
    lines.append("- 원칙: 이 단계에서 글을 읽고 확인한 뒤에만 다음 단계로 넘어갑니다.")
    lines.append("")
    cross_platform_publish_pack = report.get("cross_platform_publish_pack", {})
    if cross_platform_publish_pack.get("manual_channels"):
        lines.append("## 수동 채널 발행 패턴")
        lines.append("")
        for channel in cross_platform_publish_pack.get("manual_channels", []):
            lines.append(f"- {channel.get('label', '')}")
            if channel.get("ready_command"):
                lines.append(f"  - ready_command: `{channel.get('ready_command', '')}`")
            if channel.get("ready_item_count"):
                lines.append(f"  - ready_item_count: `{channel.get('ready_item_count', 0)}`")
            lines.append("  - one-by-one steps")
            for step in channel.get("recommended_steps", []):
                lines.append(f"    - {step}")
            lines.append("")
    for item in report.get("review_shortlist", []):
        lines.append(
            f"- `{item.get('title', '')}` / keyword `{item.get('keyword', '')}` / verdict `{item.get('review_verdict', '')}` / publish `{item.get('publish_date', '')}`"
        )
    if not report.get("review_shortlist"):
        lines.append("- 아직 검토 축약본이 없습니다.")
    lines.append("")
    lines.append("## 1.5. 하루 200명 목표")
    lines.append("")
    traffic_goal = report.get("traffic_goal", {})
    lines.append(f"- target: `{traffic_goal.get('target_daily_visitors', 200)}`")
    lines.append(f"- projected: `{traffic_goal.get('projected_daily_visitors', 0)}`")
    lines.append(f"- gap: `{traffic_goal.get('gap_to_target', 0)}`")
    lines.append(f"- status: `{traffic_goal.get('status', '')}`")
    for item in traffic_goal.get("top_path", [])[:4]:
        lines.append(f"- `{item.get('keyword', '')}` 예상 `{item.get('estimated_daily_visitors', 0)}`명: {item.get('title', '')}")
    visitor_proof = report.get("visitor_proof", {})
    if visitor_proof:
        lines.append(f"- actual_verified: `{visitor_proof.get('actual_verified_visitors', 0)}`")
        lines.append(f"- proof_status: `{visitor_proof.get('proof_status', '')}`")
        lines.append(f"- proof_gap: `{visitor_proof.get('gap_to_verified_target', 0)}`")
    lines.append("")
    lines.append("## 2. 사용자 확인 명령")
    lines.append("")
    if report.get("approval", {}).get("single_command"):
        lines.append(f"- single: `{report['approval']['single_command']}`")
    if report.get("approval", {}).get("batch_command"):
        lines.append(f"- batch: `{report['approval']['batch_command']}`")
    if report.get("review_board", {}).get("exists"):
        lines.append(f"- review board: `{report['review_board']['html_path']}`")
    if report.get("reply_flow", {}).get("preview_command"):
        lines.append(f"- reply preview: `{report['reply_flow']['preview_command']}`")
    if report.get("reply_flow", {}).get("apply_command"):
        lines.append(f"- reply apply: `{report['reply_flow']['apply_command']}`")
    lines.append("")
    lines.append("## 3. 사용자 확인 후 실행")
    lines.append("")
    planned_commands = report.get("operator_run", {}).get("planned_commands", [])
    if report.get("reply_flow", {}).get("apply_command"):
        lines.append(f"- `{report['reply_flow']['apply_command']}`")
    for command in planned_commands[1:] if len(planned_commands) > 1 else planned_commands:
        lines.append(f"- `{command}`")
    if not planned_commands:
        lines.append("- 아직 실행 카드가 없습니다.")
    lines.append("")
    lines.append("## 4. 이미지 하나만 보완하면 되는 글")
    lines.append("")
    for item in report.get("image_upgrade_queue", []):
        lines.append(
            f"- `{item.get('title', '')}` / keyword `{item.get('keyword', '')}` / {item.get('provider_name', '')} / `{item.get('search_query', '')}`"
        )
    if not report.get("image_upgrade_queue"):
        lines.append("- 현재는 이미지 하나만 보완하면 되는 별도 후보가 없습니다.")
    lines.append("")
    lines.append("## 5. 이미지 작업 레버리지 라인")
    lines.append("")
    for lane in report.get("image_leverage_lanes", []):
        lines.append(
            f"- `{lane.get('lane_label', '')}` / unlock `{lane.get('unlock_count', 0)}` / main `{lane.get('main_count', 0)}` / seo `{lane.get('seo_count', 0)}` / revenue_hit `{lane.get('revenue_hit', False)}`"
        )
    if not report.get("image_leverage_lanes"):
        lines.append("- 현재는 이미지 레버리지 라인 계산 결과가 없습니다.")
    lines.append("")
    lines.append("## 6. 오늘 수익화 경로")
    lines.append("")
    for item in report.get("revenue_path", []):
        lines.append(f"- `{item.get('step', '')}` / `{item.get('title', '')}` / {item.get('why_revenue', '')}")
    if not report.get("revenue_path"):
        lines.append("- 아직 수익화 경로 카드가 없습니다.")
    lines.append("")
    lines.append("## 7. 다음 큰 단계")
    lines.append("")
    for phase in report.get("roadmap_phases", []):
        lines.append(f"- `{phase.get('phase', '')}` / {phase.get('gate', '')}")
    if not report.get("roadmap_phases"):
        lines.append("- 아직 수익화 로드맵이 없습니다.")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def main() -> int:
    report = build_report()
    OUTPUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    write_markdown(report)
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
