#!/usr/bin/env python3
import html
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TODAY_OPERATOR_CONSOLE_JSON = ROOT / "outputs/latest/today-operator-console.json"
LAUNCH_BUNDLE_REPORT_MD = ROOT / "outputs/latest/launch-bundle-report.md"
REVIEW_PREVIEW_BOARD_HTML = ROOT / "outputs/latest/review-preview-board.html"
USER_REVIEW_SHORTLIST_MD = ROOT / "outputs/latest/user-review-shortlist.md"
REFERENCE_STRENGTH_BENCHMARK_MD = ROOT / "outputs/latest/reference-strength-benchmark.md"
REVIEW_PACKET_MD = ROOT / "outputs/latest/review-packet.md"
START_HERE_RUNBOOK_MD = ROOT / "outputs/latest/start-here-runbook.md"
PLATFORM_PUBLISH_PLAN_JSON = ROOT / "outputs/latest/platform-publish-plan.json"
CROSS_PLATFORM_PUBLISH_PACK_MD = ROOT / "outputs/latest/cross-platform-publish-pack.md"
CROSS_PLATFORM_PUBLISH_PACK_JSON = ROOT / "outputs/latest/cross-platform-publish-pack.json"
FIRST_CLOUD_RUN_VERIFICATION_JSON = ROOT / "outputs/latest/first-cloud-run-verification.json"
PRE_PUBLISH_QUALITY_GATE_JSON = ROOT / "outputs/latest/pre-publish-quality-gate.json"
IMAGE_UPGRADE_QUEUE_JSON = ROOT / "outputs/latest/image-upgrade-queue.json"
IMAGE_LEVERAGE_BOARD_JSON = ROOT / "outputs/latest/image-leverage-board.json"
TOP_IMAGE_ACTION_CARD_MD = ROOT / "outputs/latest/top-image-action-card.md"
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
CRYPTO_MARKET_SIGNAL_MD = ROOT / "outputs/latest/crypto-market-signal.md"
GITHUB_MINIMUM_LAUNCH_CARD_MD = ROOT / "outputs/latest/github-minimum-launch-card.md"
PIPELINE_WORKFLOW_PARITY_MD = ROOT / "outputs/latest/pipeline-workflow-parity.md"
CLOUD_LAUNCH_PREFLIGHT_MD = ROOT / "outputs/latest/cloud-launch-preflight.md"
AUTOMATION_PROGRESS_BOARD_MD = ROOT / "outputs/latest/automation-progress-board.md"
AUTOMATION_UNBLOCK_CARD_MD = ROOT / "outputs/latest/automation-unblock-card.md"
MINIMUM_UNBLOCK_FLOW_MD = ROOT / "outputs/latest/minimum-unblock-flow.md"
FIRST_BLOGGER_VERIFY_CARD_MD = ROOT / "outputs/latest/first-blogger-verify-card.md"
SETUP_JSON = ROOT / "outputs/latest/setup-check-report.json"
LOGIN_LAUNCH_CHECKLIST_JSON = ROOT / "outputs/latest/login-launch-checklist.json"
OUTPUT_JSON = ROOT / "outputs/latest/operator-home.json"
OUTPUT_MD = ROOT / "outputs/latest/operator-home.md"
OUTPUT_HTML = ROOT / "outputs/latest/operator-home.html"
IMAGE_UPGRADE_QUEUE_MD = ROOT / "outputs/latest/image-upgrade-queue.md"
IMAGE_LEVERAGE_BOARD_MD = ROOT / "outputs/latest/image-leverage-board.md"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text()


def to_uri(path: Path) -> str:
    if not path.exists():
        return ""
    return path.resolve().as_uri()


def extract_blockers(launch_bundle_md: str) -> list[str]:
    lines = launch_bundle_md.splitlines()
    blockers = []
    in_blockers = False
    for line in lines:
        if line.startswith("## "):
            in_blockers = line.strip() == "## Current Blockers"
            continue
        if in_blockers and line.startswith("- "):
            blockers.append(line[2:].strip())
    return blockers


def integration_lookup(setup: dict) -> dict:
    return {item.get("name"): item for item in setup.get("integrations", [])}


def build_core_blockers(state: dict, integrations: dict) -> list[str]:
    blockers = []
    if not state.get("repo_connected", False):
        blockers.append("GitHub repo 연결이 아직 없어 컴퓨터가 꺼져도 도는 클라우드 자동화를 시작할 수 없습니다.")
    blogger = integrations.get("blogger_upload", {})
    if blogger and not blogger.get("ready", False):
        missing = ", ".join(blogger.get("missing", []))
        blockers.append(f"Blogger 업로드 자격이 아직 덜 준비됐습니다: {missing}")
    return blockers


def build_later_improvements(integrations: dict) -> list[str]:
    later = []
    if not integrations.get("search_console", {}).get("ready", False):
        later.append("Search Console은 나중에 붙여도 됩니다. 현재는 fallback 검색 수요 로직으로 운영이 가능합니다.")
    if not integrations.get("openai_drafts", {}).get("ready", False):
        later.append("OpenAI 키는 선택 사항입니다. 지금도 fallback 초안으로 발행 루프를 검증할 수 있습니다.")
    if not integrations.get("wordpress_upload", {}).get("ready", False):
        later.append("WordPress는 2차 확장 채널입니다. Blogger 루프를 먼저 검증한 뒤 붙이면 됩니다.")
    return later


def build_next_action(state: dict, today: dict, login_checklist: dict, integrations: dict) -> dict:
    approval = today.get("approval", {})
    operator_run = today.get("operator_run", {})
    review_shortlist = today.get("review_shortlist", [])

    if review_shortlist:
        if approval.get("single_command"):
            return {
                "label": "Shortlist 초안 먼저 확인",
                "command": "",
                "detail": "지금은 shortlist 글 초안과 미리보기를 먼저 읽고, 괜찮은 글만 사용자 최종 확인으로 넘기는 단계입니다. 확인 전에는 실제 업로드가 계속 차단됩니다.",
                "link": to_uri(USER_REVIEW_CHECKPOINT_HTML),
            }
        return {
            "label": "리뷰 보드 열기",
            "command": "",
            "detail": "승인 후보 글이 있으니 초안과 근거를 먼저 확인합니다. 사용자 최종 확인 전에는 실제 업로드가 진행되지 않습니다.",
            "link": to_uri(REVIEW_PREVIEW_BOARD_HTML),
        }

    if not state.get("repo_connected", False):
        return {
            "label": "GitHub public repo 연결",
            "command": "bash scripts/bootstrap_github_remote.sh <OWNER/REPO>",
            "detail": "무료 클라우드 자동화를 시작하려면 GitHub repo를 먼저 연결해야 합니다.",
            "link": login_checklist.get("next_page", {}).get("url", "https://github.com/new"),
        }

    if not integrations.get("blogger_upload", {}).get("ready", False):
        next_page = login_checklist.get("next_page", {})
        return {
            "label": "Blogger 자격 마무리",
            "command": "python3 scripts/open_login_setup_pages.py --open-next",
            "detail": "Blogger 업로드 필수값이 아직 덜 준비된 상태입니다.",
            "link": next_page.get("url", ""),
        }

    if approval.get("single_command"):
        planned = operator_run.get("planned_commands", [])
        followup = planned[1] if len(planned) > 1 else ""
        detail = "첫 검증 글을 승인해 Blogger draft 업로드 루프를 실제로 한 번 확인합니다."
        if followup:
            detail += f" 승인 뒤에는 `{followup}` 순서로 이어가면 됩니다."
        return {
            "label": "첫 검증 글 승인",
            "command": approval.get("single_command", ""),
            "detail": detail,
            "link": "",
        }

    return {
        "label": "리뷰 보드 열기",
        "command": "",
        "detail": "승인할 글이 있는지 검토 보드부터 확인합니다.",
        "link": to_uri(REVIEW_PREVIEW_BOARD_HTML),
    }


def build_report() -> dict:
    today = load_json(TODAY_OPERATOR_CONSOLE_JSON)
    publish_plan = load_json(PLATFORM_PUBLISH_PLAN_JSON)
    cloud = load_json(FIRST_CLOUD_RUN_VERIFICATION_JSON)
    quality_gate = load_json(PRE_PUBLISH_QUALITY_GATE_JSON)
    visitor_proof = load_json(VISITOR_PROOF_BOARD_JSON)
    image_upgrade_queue = load_json(IMAGE_UPGRADE_QUEUE_JSON)
    image_leverage_board = load_json(IMAGE_LEVERAGE_BOARD_JSON)
    setup = load_json(SETUP_JSON)
    login_checklist = load_json(LOGIN_LAUNCH_CHECKLIST_JSON)
    approval_inbox = load_json(USER_APPROVAL_INBOX_JSON)
    launch_bundle_md = read_text(LAUNCH_BUNDLE_REPORT_MD)
    integrations = integration_lookup(setup)
    top_state = today.get("top_state", {})
    reply_flow_examples = approval_inbox.get("reply_flow_examples", [])

    channels = publish_plan.get("channels", [])
    return {
        "top_state": top_state,
        "approval": today.get("approval", {}),
        "reply_flow": {
            "preview_command": reply_flow_examples[0] if reply_flow_examples else "",
            "apply_command": reply_flow_examples[1] if len(reply_flow_examples) > 1 else "",
        },
        "review_shortlist": today.get("review_shortlist", []),
        "operator_run": today.get("operator_run", {}),
        "revenue_path": today.get("revenue_path", []),
        "roadmap_phases": today.get("roadmap_phases", []),
        "blockers": build_core_blockers(top_state, integrations) or extract_blockers(launch_bundle_md),
        "later_improvements": build_later_improvements(integrations),
        "next_action": build_next_action(top_state, today, login_checklist, integrations),
        "review_board_html": str(REVIEW_PREVIEW_BOARD_HTML),
        "review_board_uri": to_uri(REVIEW_PREVIEW_BOARD_HTML),
        "review_shortlist_md": str(USER_REVIEW_SHORTLIST_MD),
        "review_shortlist_uri": to_uri(USER_REVIEW_SHORTLIST_MD),
        "reference_strength_benchmark_md": str(REFERENCE_STRENGTH_BENCHMARK_MD),
        "reference_strength_benchmark_uri": to_uri(REFERENCE_STRENGTH_BENCHMARK_MD),
        "review_packet_md": str(REVIEW_PACKET_MD),
        "review_packet_uri": to_uri(REVIEW_PACKET_MD),
        "full_draft_review_sheet_md": str(FULL_DRAFT_REVIEW_SHEET_MD),
        "full_draft_review_sheet_uri": to_uri(FULL_DRAFT_REVIEW_SHEET_MD),
        "draft_polish_board_md": str(DRAFT_POLISH_BOARD_MD),
        "draft_polish_board_uri": to_uri(DRAFT_POLISH_BOARD_MD),
        "daily_traffic_goal_md": str(DAILY_TRAFFIC_GOAL_MD),
        "daily_traffic_goal_uri": to_uri(DAILY_TRAFFIC_GOAL_MD),
        "traffic_cluster_board_md": str(TRAFFIC_CLUSTER_BOARD_MD),
        "traffic_cluster_board_uri": to_uri(TRAFFIC_CLUSTER_BOARD_MD),
        "traffic_amplification_plan_md": str(TRAFFIC_AMPLIFICATION_PLAN_MD),
        "traffic_amplification_plan_uri": to_uri(TRAFFIC_AMPLIFICATION_PLAN_MD),
        "visitor_proof_board_md": str(VISITOR_PROOF_BOARD_MD),
        "visitor_proof_board_uri": to_uri(VISITOR_PROOF_BOARD_MD),
        "search_console_setup_card_md": str(SEARCH_CONSOLE_SETUP_CARD_MD),
        "search_console_setup_card_uri": to_uri(SEARCH_CONSOLE_SETUP_CARD_MD),
        "indexing_priority_pack_md": str(INDEXING_PRIORITY_PACK_MD),
        "indexing_priority_pack_uri": to_uri(INDEXING_PRIORITY_PACK_MD),
        "internal_link_application_report_md": str(INTERNAL_LINK_APPLICATION_REPORT_MD),
        "internal_link_application_report_uri": to_uri(INTERNAL_LINK_APPLICATION_REPORT_MD),
        "popular_reads_application_report_md": str(POPULAR_READS_APPLICATION_REPORT_MD),
        "popular_reads_application_report_uri": to_uri(POPULAR_READS_APPLICATION_REPORT_MD),
        "popular_reads_board_md": str(POPULAR_READS_BOARD_MD),
        "popular_reads_board_uri": to_uri(POPULAR_READS_BOARD_MD),
        "retention_cta_board_md": str(RETENTION_CTA_BOARD_MD),
        "retention_cta_board_uri": to_uri(RETENTION_CTA_BOARD_MD),
        "editorial_calendar_md": str(EDITORIAL_CALENDAR_MD),
        "editorial_calendar_uri": to_uri(EDITORIAL_CALENDAR_MD),
        "approval_evidence_sheet_md": str(APPROVAL_EVIDENCE_SHEET_MD),
        "approval_evidence_sheet_uri": to_uri(APPROVAL_EVIDENCE_SHEET_MD),
        "approval_briefing_board_html": str(APPROVAL_BRIEFING_BOARD_HTML),
        "approval_briefing_board_uri": to_uri(APPROVAL_BRIEFING_BOARD_HTML),
        "shortlist_publish_action_board_md": str(SHORTLIST_PUBLISH_ACTION_BOARD_MD),
        "shortlist_publish_action_board_uri": to_uri(SHORTLIST_PUBLISH_ACTION_BOARD_MD),
        "shortlist_launchpad_html": str(SHORTLIST_LAUNCHPAD_HTML),
        "shortlist_launchpad_uri": to_uri(SHORTLIST_LAUNCHPAD_HTML),
        "current_review_focus_html": str(CURRENT_REVIEW_FOCUS_HTML),
        "current_review_focus_uri": to_uri(CURRENT_REVIEW_FOCUS_HTML),
        "user_approval_inbox_html": str(USER_APPROVAL_INBOX_HTML),
        "user_approval_inbox_uri": to_uri(USER_APPROVAL_INBOX_HTML),
        "user_review_checkpoint_html": str(USER_REVIEW_CHECKPOINT_HTML),
        "user_review_checkpoint_uri": to_uri(USER_REVIEW_CHECKPOINT_HTML),
        "source_freshness_board_md": str(SOURCE_FRESHNESS_BOARD_MD),
        "source_freshness_board_uri": to_uri(SOURCE_FRESHNESS_BOARD_MD),
        "crypto_market_signal_md": str(CRYPTO_MARKET_SIGNAL_MD),
        "crypto_market_signal_uri": to_uri(CRYPTO_MARKET_SIGNAL_MD),
        "github_minimum_launch_card_md": str(GITHUB_MINIMUM_LAUNCH_CARD_MD),
        "github_minimum_launch_card_uri": to_uri(GITHUB_MINIMUM_LAUNCH_CARD_MD),
        "pipeline_workflow_parity_md": str(PIPELINE_WORKFLOW_PARITY_MD),
        "pipeline_workflow_parity_uri": to_uri(PIPELINE_WORKFLOW_PARITY_MD),
        "cloud_launch_preflight_md": str(CLOUD_LAUNCH_PREFLIGHT_MD),
        "cloud_launch_preflight_uri": to_uri(CLOUD_LAUNCH_PREFLIGHT_MD),
        "automation_progress_board_md": str(AUTOMATION_PROGRESS_BOARD_MD),
        "automation_progress_board_uri": to_uri(AUTOMATION_PROGRESS_BOARD_MD),
        "automation_unblock_card_md": str(AUTOMATION_UNBLOCK_CARD_MD),
        "automation_unblock_card_uri": to_uri(AUTOMATION_UNBLOCK_CARD_MD),
        "minimum_unblock_flow_md": str(MINIMUM_UNBLOCK_FLOW_MD),
        "minimum_unblock_flow_uri": to_uri(MINIMUM_UNBLOCK_FLOW_MD),
        "first_blogger_verify_card_md": str(FIRST_BLOGGER_VERIFY_CARD_MD),
        "first_blogger_verify_card_uri": to_uri(FIRST_BLOGGER_VERIFY_CARD_MD),
        "image_upgrade_queue_md": str(IMAGE_UPGRADE_QUEUE_MD),
        "image_upgrade_queue_uri": to_uri(IMAGE_UPGRADE_QUEUE_MD),
        "image_leverage_board_md": str(IMAGE_LEVERAGE_BOARD_MD),
        "image_leverage_board_uri": to_uri(IMAGE_LEVERAGE_BOARD_MD),
        "top_image_action_card_md": str(TOP_IMAGE_ACTION_CARD_MD),
        "top_image_action_card_uri": to_uri(TOP_IMAGE_ACTION_CARD_MD),
        "runbook_md": str(START_HERE_RUNBOOK_MD),
        "runbook_uri": to_uri(START_HERE_RUNBOOK_MD),
        "launch_bundle_md": str(LAUNCH_BUNDLE_REPORT_MD),
        "launch_bundle_uri": to_uri(LAUNCH_BUNDLE_REPORT_MD),
        "cross_platform_publish_pack_md": str(CROSS_PLATFORM_PUBLISH_PACK_MD),
        "cross_platform_publish_pack_uri": to_uri(CROSS_PLATFORM_PUBLISH_PACK_MD),
        "cross_platform_publish_pack_data": load_json(CROSS_PLATFORM_PUBLISH_PACK_JSON),
        "cloud_verification_ok": cloud.get("all_core_checks_passed", False),
        "quality_gate_summary": quality_gate.get("summary", {}),
        "visitor_proof": visitor_proof,
        "image_upgrade_queue": image_upgrade_queue.get("items", [])[:4],
        "image_leverage_lanes": image_leverage_board.get("lanes", [])[:3],
        "channels": channels,
    }


def write_markdown(report: dict) -> None:
    state = report.get("top_state", {})
    lines = []
    lines.append("# Operator Home")
    lines.append("")
    lines.append("운영자가 매일 가장 먼저 열면 되는 단일 시작 화면 요약입니다.")
    lines.append("")
    lines.append("## Publish Safety Promise")
    lines.append("")
    lines.append("- 1단계: 제가 먼저 `user-review-checkpoint`와 검토 보드로 초안과 미리보기를 보여드립니다.")
    lines.append("- 2단계: 사용자가 확인한 keyword만 업로드 후보가 됩니다.")
    lines.append("- 3단계: 사용자가 확인하기 전에는 어떤 글도 실제 업로드 단계로 넘기지 않습니다.")
    lines.append("- 4단계: 최종 확인이 끝난 글만 Blogger 업로드 후보로 계산됩니다.")
    lines.append("")
    lines.append(f"- ready_for_first_live_run: `{state.get('ready_for_first_live_run', False)}`")
    lines.append(f"- repo_connected: `{state.get('repo_connected', False)}`")
    lines.append(f"- first_live_run_status: `{state.get('first_live_run_status', '')}`")
    lines.append(f"- github_launch_status: `{state.get('github_launch_status', '')}`")
    lines.append(f"- cloud_verification_ok: `{report.get('cloud_verification_ok', False)}`")
    lines.append(f"- quality_needs_fix_count: `{report.get('quality_gate_summary', {}).get('needs_fix_count', 0)}`")
    lines.append(f"- quality_review_count: `{report.get('quality_gate_summary', {}).get('review_before_publish_count', 0)}`")
    visitor_proof = report.get("visitor_proof", {})
    if visitor_proof:
        lines.append(f"- visitor_proof_status: `{visitor_proof.get('proof_status', '')}`")
        lines.append(f"- actual_verified_visitors: `{visitor_proof.get('actual_verified_visitors', 0)}`")
        lines.append(f"- visitor_proof_gap: `{visitor_proof.get('gap_to_verified_target', 0)}`")
    lines.append("")
    lines.append("## Single Next Action")
    lines.append("")
    next_action = report.get("next_action", {})
    if next_action.get("label"):
        lines.append(f"- action: `{next_action.get('label', '')}`")
        if next_action.get("command"):
            lines.append(f"- command: `{next_action.get('command', '')}`")
        if next_action.get("link"):
            lines.append(f"- link: `{next_action.get('link', '')}`")
        if report.get("reply_flow", {}).get("apply_command"):
            lines.append(f"- one-command after approval: `{report['reply_flow']['apply_command']}`")
        lines.append(f"- why: {next_action.get('detail', '')}")
    else:
        lines.append("- none")
    lines.append("")
    lines.append("## Main Links")
    lines.append("")
    lines.append(f"- review shortlist: `{report.get('review_shortlist_md', '')}`")
    lines.append(f"- reference strength benchmark: `{report.get('reference_strength_benchmark_md', '')}`")
    lines.append(f"- user review checkpoint: `{report.get('user_review_checkpoint_html', '')}`")
    lines.append(f"- current review focus: `{report.get('current_review_focus_html', '')}`")
    lines.append(f"- user approval inbox: `{report.get('user_approval_inbox_html', '')}`")
    lines.append(f"- source freshness board: `{report.get('source_freshness_board_md', '')}`")
    lines.append(f"- crypto market signal: `{report.get('crypto_market_signal_md', '')}`")
    lines.append(f"- github minimum launch card: `{report.get('github_minimum_launch_card_md', '')}`")
    lines.append(f"- pipeline workflow parity: `{report.get('pipeline_workflow_parity_md', '')}`")
    lines.append(f"- cloud launch preflight: `{report.get('cloud_launch_preflight_md', '')}`")
    lines.append(f"- automation progress board: `{report.get('automation_progress_board_md', '')}`")
    lines.append(f"- automation unblock card: `{report.get('automation_unblock_card_md', '')}`")
    lines.append(f"- minimum unblock flow: `{report.get('minimum_unblock_flow_md', '')}`")
    lines.append(f"- first blogger verify card: `{report.get('first_blogger_verify_card_md', '')}`")
    lines.append(f"- review board: `{report.get('review_board_html', '')}`")
    lines.append(f"- review packet: `{report.get('review_packet_md', '')}`")
    lines.append(f"- full draft review sheet: `{report.get('full_draft_review_sheet_md', '')}`")
    lines.append(f"- draft polish board: `{report.get('draft_polish_board_md', '')}`")
    lines.append(f"- daily traffic goal: `{report.get('daily_traffic_goal_md', '')}`")
    lines.append(f"- traffic cluster board: `{report.get('traffic_cluster_board_md', '')}`")
    lines.append(f"- traffic amplification plan: `{report.get('traffic_amplification_plan_md', '')}`")
    lines.append(f"- visitor proof board: `{report.get('visitor_proof_board_md', '')}`")
    lines.append(f"- search console setup card: `{report.get('search_console_setup_card_md', '')}`")
    lines.append(f"- indexing priority pack: `{report.get('indexing_priority_pack_md', '')}`")
    lines.append(f"- internal link application report: `{report.get('internal_link_application_report_md', '')}`")
    lines.append(f"- popular reads application report: `{report.get('popular_reads_application_report_md', '')}`")
    lines.append(f"- popular reads board: `{report.get('popular_reads_board_md', '')}`")
    lines.append(f"- retention cta board: `{report.get('retention_cta_board_md', '')}`")
    lines.append(f"- editorial calendar: `{report.get('editorial_calendar_md', '')}`")
    lines.append(f"- approval evidence sheet: `{report.get('approval_evidence_sheet_md', '')}`")
    lines.append(f"- approval briefing board: `{report.get('approval_briefing_board_html', '')}`")
    lines.append(f"- shortlist publish action board: `{report.get('shortlist_publish_action_board_md', '')}`")
    lines.append(f"- shortlist launchpad: `{report.get('shortlist_launchpad_html', '')}`")
    lines.append(f"- image upgrade queue: `{report.get('image_upgrade_queue_md', '')}`")
    lines.append(f"- image leverage board: `{report.get('image_leverage_board_md', '')}`")
    lines.append(f"- top image action card: `{report.get('top_image_action_card_md', '')}`")
    lines.append(f"- runbook: `{report.get('runbook_md', '')}`")
    lines.append(f"- launch bundle: `{report.get('launch_bundle_md', '')}`")
    lines.append(f"- cross platform publish pack: `{report.get('cross_platform_publish_pack_md', '')}`")
    lines.append("")
    cross_platform_publish_pack_data = report.get("cross_platform_publish_pack_data", {})
    manual_channels = cross_platform_publish_pack_data.get("manual_channels", [])
    if manual_channels:
        lines.append("## Manual Publish Pattern")
        lines.append("")
        for channel in manual_channels:
            lines.append(f"- {channel.get('label', '')} (`{channel.get('editor_url', '')}`)")
            if channel.get("ready_command"):
                lines.append(f"  - ready_command: `{channel.get('ready_command', '')}`")
            if channel.get("ready_item_count"):
                lines.append(f"  - ready_item_count: `{channel.get('ready_item_count', 0)}`")
            lines.append("  - one-by-one sequence")
            for step in channel.get("recommended_steps", []):
                lines.append(f"    - {step}")
            lines.append("")
    lines.append("## Current Blockers")
    lines.append("")
    for blocker in report.get("blockers", []):
        lines.append(f"- {blocker}")
    if not report.get("blockers"):
        lines.append("- none")
    lines.append("")
    lines.append("## Later Improvements")
    lines.append("")
    for item in report.get("later_improvements", []):
        lines.append(f"- {item}")
    if not report.get("later_improvements"):
        lines.append("- none")
    lines.append("")
    lines.append("## User Confirmation Commands")
    lines.append("")
    if report.get("approval", {}).get("single_command"):
        lines.append(f"- single: `{report['approval']['single_command']}`")
    if report.get("approval", {}).get("batch_command"):
        lines.append(f"- batch: `{report['approval']['batch_command']}`")
    if report.get("reply_flow", {}).get("preview_command"):
        lines.append(f"- reply preview: `{report['reply_flow']['preview_command']}`")
    if report.get("reply_flow", {}).get("apply_command"):
        lines.append(f"- reply apply: `{report['reply_flow']['apply_command']}`")
    lines.append("")
    lines.append("## After Confirmation")
    lines.append("")
    planned_commands = report.get("operator_run", {}).get("planned_commands", [])
    if report.get("reply_flow", {}).get("apply_command"):
        lines.append(f"- `{report['reply_flow']['apply_command']}`")
    for command in planned_commands[1:] if len(planned_commands) > 1 else planned_commands:
        lines.append(f"- `{command}`")
    if not planned_commands:
        lines.append("- none")
    lines.append("")
    lines.append("## Image Upgrade Queue")
    lines.append("")
    for item in report.get("image_upgrade_queue", []):
        lines.append(
            f"- `{item.get('title', '')}` / `{item.get('keyword', '')}` / {item.get('provider_name', '')} / `{item.get('search_query', '')}`"
        )
    if not report.get("image_upgrade_queue"):
        lines.append("- none")
    lines.append("")
    lines.append("## Image Leverage Lanes")
    lines.append("")
    for lane in report.get("image_leverage_lanes", []):
        lines.append(
            f"- `{lane.get('lane_label', '')}` / unlock `{lane.get('unlock_count', 0)}` / main `{lane.get('main_count', 0)}` / seo `{lane.get('seo_count', 0)}` / revenue_hit `{lane.get('revenue_hit', False)}`"
        )
    if not report.get("image_leverage_lanes"):
        lines.append("- none")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def render_list(items: list[str], empty_label: str) -> str:
    if not items:
        return f"<li>{html.escape(empty_label)}</li>"
    return "".join(f"<li>{html.escape(item)}</li>" for item in items)


def render_shortlist(cards: list[dict]) -> str:
    if not cards:
        return "<p class='muted'>No review shortlist available.</p>"
    blocks = []
    for card in cards:
        blocks.append(
            f"""
            <article class="mini-card">
              <div class="mini-top">
                <span class="tag">{html.escape(card.get('keyword', ''))}</span>
                <span class="tag alt">{html.escape(card.get('review_verdict', ''))}</span>
              </div>
              <h3>{html.escape(card.get('title', ''))}</h3>
              <p class="muted">{html.escape(card.get('cta_focus', ''))}</p>
              <p class="tiny">publish {html.escape(card.get('publish_date', ''))}</p>
            </article>
            """
        )
    return "".join(blocks)


def render_channels(channels: list[dict]) -> str:
    if not channels:
        return "<p class='muted'>No channel data available.</p>"
    blocks = []
    for channel in channels:
        first = channel.get("first_item", {}) or {}
        first_title = first.get("title", "없음")
        blocks.append(
            f"""
            <article class="channel-card">
              <div class="mini-top">
                <span class="tag">{html.escape(channel.get('name', ''))}</span>
                <span class="tag alt">{'ready' if channel.get('ready') else 'not ready'}</span>
              </div>
              <p><strong>Approved ready items:</strong> {html.escape(str(channel.get('ready_item_count', 0)))}</p>
              <p><strong>First item:</strong> {html.escape(first_title)}</p>
              <code>{html.escape(channel.get('command', ''))}</code>
            </article>
            """
        )
    return "".join(blocks)


def write_html(report: dict) -> None:
    state = report.get("top_state", {})
    single = html.escape(report.get("approval", {}).get("single_command", ""))
    batch = html.escape(report.get("approval", {}).get("batch_command", ""))
    reply_preview = html.escape(report.get("reply_flow", {}).get("preview_command", ""))
    reply_apply = html.escape(report.get("reply_flow", {}).get("apply_command", ""))
    next_action = report.get("next_action", {})
    next_action_label = html.escape(next_action.get("label", ""))
    next_action_command = html.escape(next_action.get("command", ""))
    next_action_detail = html.escape(next_action.get("detail", ""))
    next_action_link = html.escape(next_action.get("link", ""))
    review_board_uri = html.escape(report.get("review_board_uri", ""))
    reference_strength_benchmark_uri = html.escape(report.get("reference_strength_benchmark_uri", ""))
    full_draft_review_sheet_uri = html.escape(report.get("full_draft_review_sheet_uri", ""))
    draft_polish_board_uri = html.escape(report.get("draft_polish_board_uri", ""))
    daily_traffic_goal_uri = html.escape(report.get("daily_traffic_goal_uri", ""))
    traffic_cluster_board_uri = html.escape(report.get("traffic_cluster_board_uri", ""))
    traffic_amplification_plan_uri = html.escape(report.get("traffic_amplification_plan_uri", ""))
    popular_reads_board_uri = html.escape(report.get("popular_reads_board_uri", ""))
    retention_cta_board_uri = html.escape(report.get("retention_cta_board_uri", ""))
    editorial_calendar_uri = html.escape(report.get("editorial_calendar_uri", ""))
    approval_evidence_sheet_uri = html.escape(report.get("approval_evidence_sheet_uri", ""))
    approval_briefing_board_uri = html.escape(report.get("approval_briefing_board_uri", ""))
    shortlist_publish_action_board_uri = html.escape(report.get("shortlist_publish_action_board_uri", ""))
    shortlist_launchpad_uri = html.escape(report.get("shortlist_launchpad_uri", ""))
    current_review_focus_uri = html.escape(report.get("current_review_focus_uri", ""))
    user_approval_inbox_uri = html.escape(report.get("user_approval_inbox_uri", ""))
    user_review_checkpoint_uri = html.escape(report.get("user_review_checkpoint_uri", ""))
    crypto_market_signal_uri = html.escape(report.get("crypto_market_signal_uri", ""))
    github_minimum_launch_card_uri = html.escape(report.get("github_minimum_launch_card_uri", ""))
    pipeline_workflow_parity_uri = html.escape(report.get("pipeline_workflow_parity_uri", ""))
    cloud_launch_preflight_uri = html.escape(report.get("cloud_launch_preflight_uri", ""))
    automation_progress_board_uri = html.escape(report.get("automation_progress_board_uri", ""))
    automation_unblock_card_uri = html.escape(report.get("automation_unblock_card_uri", ""))
    minimum_unblock_flow_uri = html.escape(report.get("minimum_unblock_flow_uri", ""))
    first_blogger_verify_card_uri = html.escape(report.get("first_blogger_verify_card_uri", ""))
    runbook_uri = html.escape(report.get("runbook_uri", ""))
    launch_bundle_uri = html.escape(report.get("launch_bundle_uri", ""))
    cross_platform_publish_pack_uri = html.escape(report.get("cross_platform_publish_pack_uri", ""))
    top_image_action_card_uri = html.escape(report.get("top_image_action_card_uri", ""))
    html_text = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Operator Home</title>
  <style>
    :root {{
      --bg: #f3efe8;
      --panel: rgba(255, 252, 245, 0.92);
      --ink: #171814;
      --muted: #5d6056;
      --line: #d8cfbf;
      --accent: #8c2f39;
      --accent-soft: #f3dde1;
      --accent-alt: #1f5c56;
      --accent-alt-soft: #dff0ec;
      --shadow: 0 20px 45px rgba(33, 25, 12, 0.08);
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      color: var(--ink);
      font-family: "Avenir Next", "Pretendard", "Apple SD Gothic Neo", sans-serif;
      background:
        radial-gradient(circle at top left, rgba(140, 47, 57, 0.08), transparent 24%),
        radial-gradient(circle at bottom right, rgba(31, 92, 86, 0.08), transparent 22%),
        linear-gradient(180deg, #fbf8f1 0%, var(--bg) 100%);
    }}
    .page {{
      max-width: 1480px;
      margin: 0 auto;
      padding: 28px 18px 64px;
    }}
    .hero, .panel {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 24px;
      box-shadow: var(--shadow);
    }}
    .hero {{
      padding: 28px;
      margin-bottom: 22px;
    }}
    .next-action {{
      margin-top: 18px;
      padding: 18px;
      border-radius: 20px;
      background: linear-gradient(135deg, rgba(140, 47, 57, 0.08), rgba(31, 92, 86, 0.08));
      border: 1px solid var(--line);
    }}
    h1 {{
      margin: 0 0 10px;
      font-size: clamp(2.2rem, 4.8vw, 4rem);
      line-height: 0.96;
      letter-spacing: -0.05em;
    }}
    h2 {{
      margin: 0 0 14px;
      font-size: 1.15rem;
      letter-spacing: -0.02em;
    }}
    p {{ line-height: 1.6; }}
    .muted {{ color: var(--muted); }}
    .status-grid, .content-grid {{
      display: grid;
      gap: 18px;
    }}
    .status-grid {{
      grid-template-columns: repeat(5, minmax(0, 1fr));
      margin-top: 18px;
    }}
    .content-grid {{
      grid-template-columns: 1.1fr 0.9fr;
      align-items: start;
    }}
    .panel {{
      padding: 20px;
    }}
    .stat {{
      padding: 14px;
      border-radius: 18px;
      background: #fcf8f0;
      border: 1px solid var(--line);
    }}
    .label {{
      font-size: 0.8rem;
      color: var(--muted);
      text-transform: uppercase;
      letter-spacing: 0.08em;
    }}
    .value {{
      display: block;
      margin-top: 6px;
      font-weight: 700;
      font-size: 1.15rem;
    }}
    .eyebrow {{
      margin: 0 0 8px;
      font-size: 0.8rem;
      color: var(--muted);
      text-transform: uppercase;
      letter-spacing: 0.12em;
    }}
    .link-row, .command-list {{
      display: grid;
      gap: 10px;
    }}
    .main-link {{
      display: block;
      padding: 14px 16px;
      border-radius: 16px;
      text-decoration: none;
      color: var(--ink);
      background: #fcf8f0;
      border: 1px solid var(--line);
    }}
    .main-link strong {{
      display: block;
      margin-bottom: 4px;
      font-size: 1rem;
    }}
    code {{
      display: block;
      padding: 12px 14px;
      border-radius: 14px;
      background: #141613;
      color: #f6f1e7;
      overflow-wrap: anywhere;
      font-family: "SFMono-Regular", Consolas, monospace;
    }}
    ul {{
      margin: 0;
      padding-left: 18px;
    }}
    .mini-grid, .channel-grid {{
      display: grid;
      gap: 12px;
    }}
    .mini-grid {{
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }}
    .channel-grid {{
      grid-template-columns: repeat(2, minmax(0, 1fr));
      margin-top: 12px;
    }}
    .mini-card, .channel-card {{
      border: 1px solid var(--line);
      border-radius: 18px;
      padding: 14px;
      background: #fcf8f0;
    }}
    .mini-card h3 {{
      margin: 10px 0 8px;
      font-size: 1.02rem;
      line-height: 1.2;
    }}
    .mini-top {{
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }}
    .tag {{
      display: inline-flex;
      align-items: center;
      border-radius: 999px;
      padding: 5px 10px;
      font-size: 0.76rem;
      background: var(--accent-soft);
      color: var(--accent);
      font-weight: 700;
    }}
    .tag.alt {{
      background: var(--accent-alt-soft);
      color: var(--accent-alt);
    }}
    .tiny {{
      font-size: 0.86rem;
      color: var(--muted);
      margin: 6px 0 0;
    }}
    iframe {{
      width: 100%;
      height: 820px;
      border: 1px solid var(--line);
      border-radius: 18px;
      background: white;
    }}
    @media (max-width: 1100px) {{
      .status-grid {{
        grid-template-columns: repeat(2, minmax(0, 1fr));
      }}
      .content-grid {{
        grid-template-columns: 1fr;
      }}
      .mini-grid, .channel-grid {{
        grid-template-columns: 1fr;
      }}
      iframe {{
        height: 620px;
      }}
    }}
  </style>
</head>
<body>
  <main class="page">
    <section class="hero">
      <h1>Operator Home</h1>
      <p class="muted">매일 제일 먼저 열어서 검토 후보, blocker, 사용자 확인 명령, 실제 글 미리보기를 한 번에 보는 운영 시작 화면입니다.</p>
      <div class="next-action" style="margin-top:14px;">
        <p class="eyebrow">Publish Safety Promise</p>
        <h2>초안 먼저 확인, 확인 전 업로드 차단</h2>
        <p>1단계는 제가 먼저 초안과 미리보기를 보여드리는 것이고, 2단계는 사용자가 확인한 글만 업로드 후보로 넘기는 것입니다. 사용자 최종 확인이 없으면 실제 업로드는 계속 막혀 있습니다.</p>
      </div>
      <div class="next-action">
        <p class="eyebrow">Single Next Action</p>
        <h2>{next_action_label or 'No action'}</h2>
        <p>{next_action_detail}</p>
        {f'<code>{next_action_command}</code>' if next_action_command else ''}
        {f'<code>{reply_apply}</code>' if reply_apply else ''}
        {f'<p><a class="main-link" href="{next_action_link}" target="_blank" rel="noreferrer"><strong>Open Next Page</strong>지금 단계에서 바로 열어야 하는 페이지</a></p>' if next_action_link else ''}
      </div>
        <div class="status-grid">
          <div class="stat"><span class="label">First Live</span><span class="value">{html.escape(str(state.get('ready_for_first_live_run', False)))}</span></div>
          <div class="stat"><span class="label">Repo Connected</span><span class="value">{html.escape(str(state.get('repo_connected', False)))}</span></div>
          <div class="stat"><span class="label">Draft Status</span><span class="value">{html.escape(state.get('first_live_run_status', ''))}</span></div>
          <div class="stat"><span class="label">GitHub</span><span class="value">{html.escape(state.get('github_launch_status', ''))}</span></div>
          <div class="stat"><span class="label">Cloud Checks</span><span class="value">{html.escape(str(report.get('cloud_verification_ok', False)))}</span></div>
          <div class="stat"><span class="label">Quality Needs Fix</span><span class="value">{html.escape(str(report.get('quality_gate_summary', {}).get('needs_fix_count', 0)))}</span></div>
          <div class="stat"><span class="label">Quality Review</span><span class="value">{html.escape(str(report.get('quality_gate_summary', {}).get('review_before_publish_count', 0)))}</span></div>
        </div>
    </section>
    <section class="content-grid">
      <div class="panel">
        <h2>Main Links</h2>
        <div class="link-row">
          <a class="main-link" href="{report.get('review_shortlist_uri', '')}" target="_blank" rel="noreferrer"><strong>User Review Shortlist</strong>오늘 먼저 볼 글만 짧게 추린 카드</a>
          <a class="main-link" href="{reference_strength_benchmark_uri}" target="_blank" rel="noreferrer"><strong>Reference Strength Benchmark</strong>잘 되는 경제·코인 레퍼런스의 강점을 우리 운영 규칙으로 번역한 카드</a>
          <a class="main-link" href="{user_review_checkpoint_uri}" target="_blank" rel="noreferrer"><strong>User Review Checkpoint</strong>게시 전에 내가 먼저 보여줄 초안 1순위를 바로 여는 화면</a>
          <a class="main-link" href="{current_review_focus_uri}" target="_blank" rel="noreferrer"><strong>Current Review Focus</strong>지금 사용자에게 바로 보여줄 1순위 초안 카드</a>
          <a class="main-link" href="{user_approval_inbox_uri}" target="_blank" rel="noreferrer"><strong>User Approval Inbox</strong>사용자가 승인 여부만 빠르게 답하는 확인 전용 화면</a>
          <a class="main-link" href="{report.get('source_freshness_board_uri', '')}" target="_blank" rel="noreferrer"><strong>Source Freshness Board</strong>오래된 뉴스 초안이 섞이지 않도록 최신 근거 시각을 확인하는 보드</a>
          <a class="main-link" href="{crypto_market_signal_uri}" target="_blank" rel="noreferrer"><strong>Crypto Market Signal</strong>코인 글감에 반영되는 가격, 거래량, 공포탐욕 시장 센서</a>
          <a class="main-link" href="{github_minimum_launch_card_uri}" target="_blank" rel="noreferrer"><strong>GitHub Minimum Launch Card</strong>무료 클라우드 자동화를 붙이는 최소 실행 카드</a>
          <a class="main-link" href="{pipeline_workflow_parity_uri}" target="_blank" rel="noreferrer"><strong>Pipeline Workflow Parity</strong>로컬과 GitHub Actions 단계 정합성 점검 리포트</a>
          <a class="main-link" href="{cloud_launch_preflight_uri}" target="_blank" rel="noreferrer"><strong>Cloud Launch Preflight</strong>지금 GitHub Actions 실행 버튼을 눌러도 되는지 확인하는 사전 점검 카드</a>
          <a class="main-link" href="{automation_progress_board_uri}" target="_blank" rel="noreferrer"><strong>Automation Progress Board</strong>전체 자동화 목표 기준 진행, 완료, 막힘 상태를 한 장에 정리한 보드</a>
          <a class="main-link" href="{automation_unblock_card_uri}" target="_blank" rel="noreferrer"><strong>Automation Unblock Card</strong>지금 사용자 쪽에서 딱 해야 하는 2개만 압축한 카드</a>
          <a class="main-link" href="{minimum_unblock_flow_uri}" target="_blank" rel="noreferrer"><strong>Minimum Unblock Flow</strong>bitcoin 승인과 repo 연결을 preview/apply 체인으로 묶은 최소 실행 흐름</a>
          <a class="main-link" href="{first_blogger_verify_card_uri}" target="_blank" rel="noreferrer"><strong>First Blogger Verify Card</strong>GitHub 연결 전에도 로컬 Blogger draft 검증까지 바로 가는 shortcut 카드</a>
          <a class="main-link" href="{review_board_uri}" target="_blank" rel="noreferrer"><strong>Review Preview Board</strong>실제 렌더링 글을 보고 사용자 확인하는 화면</a>
          <a class="main-link" href="{report.get('review_packet_uri', '')}" target="_blank" rel="noreferrer"><strong>Review Packet</strong>상세 검토 패킷과 이미지 후보 확인</a>
          <a class="main-link" href="{full_draft_review_sheet_uri}" target="_blank" rel="noreferrer"><strong>Full Draft Review Sheet</strong>shortlist 글 전문을 그대로 읽는 검토 시트</a>
          <a class="main-link" href="{draft_polish_board_uri}" target="_blank" rel="noreferrer"><strong>Draft Polish Board</strong>사람이 쓴 느낌을 더 살리기 위한 문장 보정 보드</a>
          <a class="main-link" href="{daily_traffic_goal_uri}" target="_blank" rel="noreferrer"><strong>Daily Traffic Goal</strong>하루 200명 목표 기준 예상 방문자와 부족분을 보는 보드</a>
          <a class="main-link" href="{traffic_cluster_board_uri}" target="_blank" rel="noreferrer"><strong>Traffic Cluster Board</strong>메인 글과 후속 글 묶음으로 페이지뷰와 재방문을 키우는 우선순위 보드</a>
          <a class="main-link" href="{traffic_amplification_plan_uri}" target="_blank" rel="noreferrer"><strong>Traffic Amplification Plan</strong>공개 URL을 어디에 어떤 문구로 공유할지 정리한 200명 목표 배포 플랜</a>
          <a class="main-link" href="{popular_reads_board_uri}" target="_blank" rel="noreferrer"><strong>Popular Reads Board</strong>메인 글 아래와 허브에 붙일 대표 읽을거리 후보 묶음</a>
          <a class="main-link" href="{retention_cta_board_uri}" target="_blank" rel="noreferrer"><strong>Retention CTA Board</strong>재방문과 나중 구독 전환까지 고려한 글 하단 CTA 운영 카드</a>
          <a class="main-link" href="{editorial_calendar_uri}" target="_blank" rel="noreferrer"><strong>Editorial Calendar</strong>이번 주 레인 균형과 stale 회피까지 반영한 7일 운영 캘린더</a>
          <a class="main-link" href="{approval_evidence_sheet_uri}" target="_blank" rel="noreferrer"><strong>Approval Evidence Sheet</strong>shortlist 글의 소스와 수요 근거를 빠르게 보는 시트</a>
          <a class="main-link" href="{approval_briefing_board_uri}" target="_blank" rel="noreferrer"><strong>Approval Briefing Board</strong>전문, 근거, 이미지 상태, 승인 명령을 한 화면에 보는 보드</a>
          <a class="main-link" href="{shortlist_publish_action_board_uri}" target="_blank" rel="noreferrer"><strong>Shortlist Publish Action Board</strong>글별 남은 blocker와 다음 한 줄 실행 보드</a>
          <a class="main-link" href="{shortlist_launchpad_uri}" target="_blank" rel="noreferrer"><strong>Shortlist Launchpad</strong>shortlist 2개만 빠르게 검토하고 실행하는 시작 화면</a>
          <a class="main-link" href="{report.get('image_upgrade_queue_uri', '')}" target="_blank" rel="noreferrer"><strong>Image Upgrade Queue</strong>이미지 1장만 고르면 ready 후보가 되는 글 모음</a>
          <a class="main-link" href="{top_image_action_card_uri}" target="_blank" rel="noreferrer"><strong>Top Image Action Card</strong>지금 가장 먼저 고를 이미지 라인 실행 카드</a>
          <a class="main-link" href="{runbook_uri}" target="_blank" rel="noreferrer"><strong>Start Here Runbook</strong>오늘 해야 할 순서형 체크리스트</a>
          <a class="main-link" href="{launch_bundle_uri}" target="_blank" rel="noreferrer"><strong>Launch Bundle Report</strong>자동화 blocker 와 준비 상태 요약</a>
          <a class="main-link" href="{cross_platform_publish_pack_uri}" target="_blank" rel="noreferrer"><strong>Cross-Platform Publish Pack</strong>자동/수동 채널별 업로드 후보 보관함</a>
        </div>
        <h2 style="margin-top:22px;">Current Blockers</h2>
        <ul>{render_list(report.get('blockers', []), 'No blockers')}</ul>
        <h2 style="margin-top:22px;">Later Improvements</h2>
        <ul>{render_list(report.get('later_improvements', []), 'none')}</ul>
        <h2 style="margin-top:22px;">User Confirmation Commands</h2>
        <div class="command-list">
          <code>{single or 'single confirmation command unavailable'}</code>
          <code>{batch or 'batch confirmation command unavailable'}</code>
          <code>{reply_preview or 'reply preview command unavailable'}</code>
          <code>{reply_apply or 'reply apply command unavailable'}</code>
        </div>
        <h2 style="margin-top:22px;">After Confirmation</h2>
        <ul>{render_list(([report.get('reply_flow', {}).get('apply_command', '')] if report.get('reply_flow', {}).get('apply_command') else []) + (report.get('operator_run', {}).get('planned_commands', [])[1:] if len(report.get('operator_run', {}).get('planned_commands', [])) > 1 else report.get('operator_run', {}).get('planned_commands', [])), 'No next commands')}</ul>
        <h2 style="margin-top:22px;">Image Upgrade Queue</h2>
        <ul>{render_list([f"{item.get('title', '')} / {item.get('keyword', '')} / {item.get('provider_name', '')}" for item in report.get('image_upgrade_queue', [])], 'No image-upgrade items')}</ul>
        <h2 style="margin-top:22px;">Review Shortlist</h2>
        <div class="mini-grid">{render_shortlist(report.get('review_shortlist', []))}</div>
        <h2 style="margin-top:22px;">Channels</h2>
        <div class="channel-grid">{render_channels(report.get('channels', []))}</div>
      </div>
      <div class="panel">
        <h2>Embedded Review Board</h2>
        <iframe src="{review_board_uri}" title="Review Preview Board" loading="lazy"></iframe>
      </div>
    </section>
  </main>
</body>
</html>
"""
    OUTPUT_HTML.write_text(html_text)


def main() -> int:
    report = build_report()
    OUTPUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    write_markdown(report)
    write_html(report)
    print(OUTPUT_HTML)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
