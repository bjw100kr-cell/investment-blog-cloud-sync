#!/usr/bin/env python3
import argparse
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_MD = ROOT / "outputs/latest/launch-bundle-report.md"

SETUP_CHECK_JSON = ROOT / "outputs/latest/setup-check-report.json"
AUTOMATION_SCOPE_JSON = ROOT / "outputs/latest/automation-scope.json"
FIRST_APPROVAL_PATH_JSON = ROOT / "outputs/latest/first-approval-path.json"
DAILY_REVENUE_FOCUS_JSON = ROOT / "outputs/latest/daily-revenue-focus.json"
MONETIZATION_ROADMAP_JSON = ROOT / "outputs/latest/monetization-roadmap.json"
FIRST_PUBLISH_OPERATOR_RUN_JSON = ROOT / "outputs/latest/first-publish-operator-run.json"
USER_REVIEW_SHORTLIST_JSON = ROOT / "outputs/latest/user-review-shortlist.json"
PLATFORM_PUBLISH_PLAN_JSON = ROOT / "outputs/latest/platform-publish-plan.json"
REVIEW_APPROVALS_JSON = ROOT / "outputs/latest/review-approvals.json"
FIRST_CLOUD_RUN_VERIFICATION_JSON = ROOT / "outputs/latest/first-cloud-run-verification.json"
GITHUB_LAUNCH_PLAN_JSON = ROOT / "outputs/latest/github-launch-plan.json"
SUCCESS_GATE_JSON = ROOT / "outputs/latest/success-gate.json"
TODAY_OPERATOR_CONSOLE_JSON = ROOT / "outputs/latest/today-operator-console.json"
PIPELINE_WORKFLOW_PARITY_JSON = ROOT / "outputs/latest/pipeline-workflow-parity.json"

SCRIPT_STEPS = [
    ("Setup check", ["python3", "scripts/check_setup.py"]),
    ("Current reference strategy", ["python3", "scripts/build_current_reference_strategy.py"]),
    ("Reference strength benchmark", ["python3", "scripts/build_reference_strength_benchmark.py"]),
    ("Keyword capture strategy", ["python3", "scripts/build_keyword_capture_strategy.py"]),
    ("Automation scope", ["python3", "scripts/build_automation_scope.py"]),
    ("Review packet", ["python3", "scripts/build_review_packet.py"]),
    ("Approval dashboard", ["python3", "scripts/build_approval_dashboard.py"]),
    ("Source freshness board", ["python3", "scripts/build_source_freshness_board.py"]),
    ("Platform publish plan", ["python3", "scripts/build_platform_publish_plan.py"]),
    ("First approval path", ["python3", "scripts/build_first_approval_path.py"]),
    ("Daily revenue focus", ["python3", "scripts/build_daily_revenue_focus.py"]),
    ("Traffic cluster board", ["python3", "scripts/build_traffic_cluster_board.py"]),
    ("Popular reads board", ["python3", "scripts/build_popular_reads_board.py"]),
    ("Retention CTA board", ["python3", "scripts/build_retention_cta_board.py"]),
    ("Monetization roadmap", ["python3", "scripts/build_monetization_roadmap.py"]),
    ("Draft polish board", ["python3", "scripts/build_draft_polish_board.py"]),
    ("First publish operator run", ["python3", "scripts/first_publish_operator_run.py"]),
    ("User review shortlist", ["python3", "scripts/build_user_review_shortlist.py"]),
    ("Current review focus", ["python3", "scripts/build_current_review_focus.py"]),
    ("User approval inbox", ["python3", "scripts/build_user_approval_inbox.py"]),
    ("User review checkpoint", ["python3", "scripts/build_user_review_checkpoint.py"]),
    ("GitHub minimum launch card", ["python3", "scripts/build_github_minimum_launch_card.py"]),
    ("Automation progress board", ["python3", "scripts/build_automation_progress_board.py"]),
    ("Automation unblock card", ["python3", "scripts/build_automation_unblock_card.py"]),
    ("Minimum unblock flow", ["python3", "scripts/run_minimum_unblock_flow.py"]),
    ("First Blogger verify card", ["python3", "scripts/build_first_blogger_verify_card.py"]),
    ("First Blogger verify flow", ["python3", "scripts/run_first_blogger_verify_flow.py"]),
    ("Review preview board", ["python3", "scripts/build_review_preview_board.py"]),
    ("Operator home", ["python3", "scripts/build_operator_home.py"]),
    ("Platform publish plan", ["python3", "scripts/build_platform_publish_plan.py"]),
    ("Cross-platform publish pack", ["python3", "scripts/build_cross_platform_publish_pack.py"]),
    ("Pre-publish quality gate", ["python3", "scripts/build_pre_publish_quality_gate.py"]),
    ("First cloud run verification", []),
    ("GitHub launch plan", ["python3", "scripts/prepare_github_launch_plan.py"]),
    ("Success gate", ["python3", "scripts/build_success_gate.py"]),
    ("Go-live dashboard", ["python3", "scripts/prepare_go_live_dashboard.py"]),
    ("Pipeline workflow parity", ["python3", "scripts/build_pipeline_workflow_parity.py"]),
    ("Cloud launch preflight", ["python3", "scripts/build_cloud_launch_preflight.py"]),
    ("Operator handoff", ["python3", "scripts/generate_operator_handoff.py"]),
    ("Start here runbook", ["python3", "scripts/prepare_start_here_runbook.py"]),
    ("Today operator console", ["python3", "scripts/build_today_operator_console.py"]),
]


def has_approved_state() -> bool:
    if not REVIEW_APPROVALS_JSON.exists():
        return False

    try:
        payload = json.loads(REVIEW_APPROVALS_JSON.read_text())
    except (json.JSONDecodeError, ValueError):
        return False

    confirmed_all = bool(payload.get("user_confirmed_all", payload.get("approved_all", False)))
    confirmed_keywords = payload.get("user_confirmed_keywords", payload.get("approved_keywords", []))
    return bool(confirmed_all or confirmed_keywords)


def with_first_cloud_run_command() -> list[str]:
    command = ["python3", "scripts/prepare_first_cloud_run_verification.py"]
    if has_approved_state():
        command.append("--allow-approved-state")
    return command


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Refresh automation-focused launch outputs for the investment blog stack."
    )
    parser.add_argument("--verbose", action="store_true", help="Print full command output while running.")
    return parser.parse_args()


def run_step(label: str, command: list[str], verbose: bool) -> dict:
    completed = subprocess.run(
        command,
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if verbose:
        if completed.stdout.strip():
            print(completed.stdout.strip())
        if completed.stderr.strip():
            print(completed.stderr.strip(), file=sys.stderr)
    return {
        "label": label,
        "command": " ".join(command),
        "returncode": completed.returncode,
        "stdout": completed.stdout.strip(),
        "stderr": completed.stderr.strip(),
    }


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text())
    except json.JSONDecodeError:
        return {}


def bool_label(value: bool) -> str:
    return "yes" if value else "no"


def append_command_list(lines: list[str], commands: list[str]) -> None:
    if not commands:
        lines.append("- none")
        return
    for command in commands:
        lines.append(f"- `{command}`")


def summarize_integrations(setup_report: dict) -> list[str]:
    ready = []
    blocked = []
    for integration in setup_report.get("integrations", []):
        name = integration.get("name", "unknown")
        missing = integration.get("missing", [])
        if integration.get("ready"):
            ready.append(name)
        else:
            blocked.append(f"{name} ({', '.join(missing)})")
    lines = []
    lines.append("Ready integrations")
    if ready:
        for name in ready:
            lines.append(f"- `{name}`")
    else:
        lines.append("- none")
    lines.append("")
    lines.append("Blocked integrations")
    if blocked:
        for item in blocked:
            lines.append(f"- `{item}`")
    else:
        lines.append("- none")
    return lines


def write_report(results: list[dict]) -> None:
    setup_report = load_json(SETUP_CHECK_JSON)
    automation_scope = load_json(AUTOMATION_SCOPE_JSON)
    approval_path = load_json(FIRST_APPROVAL_PATH_JSON)
    revenue_focus = load_json(DAILY_REVENUE_FOCUS_JSON)
    roadmap = load_json(MONETIZATION_ROADMAP_JSON)
    operator_run = load_json(FIRST_PUBLISH_OPERATOR_RUN_JSON)
    shortlist = load_json(USER_REVIEW_SHORTLIST_JSON)
    publish_plan = load_json(PLATFORM_PUBLISH_PLAN_JSON)
    cloud_verification = load_json(FIRST_CLOUD_RUN_VERIFICATION_JSON)
    github_plan = load_json(GITHUB_LAUNCH_PLAN_JSON)
    success_gate = load_json(SUCCESS_GATE_JSON)
    today_console = load_json(TODAY_OPERATOR_CONSOLE_JSON)
    parity = load_json(PIPELINE_WORKFLOW_PARITY_JSON)

    top_state = today_console.get("top_state", {})
    primary_channel = (automation_scope.get("primary_channel") or {}).get("name", "blogger")
    secondary_channel = (automation_scope.get("secondary_channel") or {}).get("name", "wordpress")
    manual_only = [
        channel.get("name", "unknown")
        for channel in automation_scope.get("manual_only_channels", [])
        if isinstance(channel, dict)
    ]
    single = approval_path.get("recommended_single", {})
    batch = approval_path.get("recommended_batch", {})
    shortlist_items = shortlist.get("shortlist", [])
    today_path = revenue_focus.get("today_path", [])
    roadmap_phases = roadmap.get("phases", [])
    failed_steps = [result for result in results if result["returncode"] != 0]

    lines = []
    lines.append("# Launch Bundle Report")
    lines.append("")
    lines.append("## Automation Snapshot")
    lines.append(f"- primary channel now: `{primary_channel}`")
    lines.append(f"- secondary channel later: `{secondary_channel}`")
    lines.append(f"- manual-only channels: `{', '.join(manual_only) if manual_only else 'none'}`")
    lines.append(f"- ready for first live run: `{bool_label(bool(top_state.get('ready_for_first_live_run')))}`")
    lines.append(f"- repo connected: `{bool_label(bool(top_state.get('repo_connected')))}`")
    lines.append(f"- first live status: `{top_state.get('first_live_run_status', success_gate.get('first_live_status', 'unknown'))}`")
    lines.append(f"- GitHub launch status: `{top_state.get('github_launch_status', github_plan.get('status', 'unknown'))}`")
    lines.append(f"- approved upload candidates right now: `{publish_plan.get('approved_ready_count', 0)}`")
    lines.append(f"- review gate still blocking uploads: `{bool_label(publish_plan.get('approved_ready_count', 0) == 0)}`")
    lines.append("")
    lines.append("## Integration Status")
    lines.extend(summarize_integrations(setup_report))
    lines.append("")
    lines.append("## Pipeline Parity")
    lines.append(f"- all_core_scripts_present: `{bool_label(bool(parity.get('all_core_scripts_present')) )}`")
    lines.append(f"- order_aligned: `{bool_label(bool(parity.get('order_aligned')) )}`")
    if parity.get("missing_in_workflow"):
        lines.append(f"- missing_in_workflow: `{', '.join(parity.get('missing_in_workflow', []))}`")
    else:
        lines.append("- missing_in_workflow: `none`")
    if parity.get("missing_in_pipeline"):
        lines.append(f"- missing_in_pipeline: `{', '.join(parity.get('missing_in_pipeline', []))}`")
    else:
        lines.append("- missing_in_pipeline: `none`")
    lines.append(f"- parity report: `outputs/latest/pipeline-workflow-parity.md`")
    lines.append("")
    lines.append("## Today Approval Focus")
    if single:
        lines.append(f"- top single approval: `{single.get('keyword', 'unknown')}` -> `{single.get('title', 'unknown')}`")
    if batch:
        lines.append(f"- top batch approval: `{', '.join(batch.get('keywords', []))}`")
    lines.append("- user review shortlist:")
    if shortlist_items:
        for item in shortlist_items[:3]:
            lines.append(
                f"- `{item.get('title', 'unknown')}` | keyword `{item.get('keyword', 'unknown')}` | verdict `{item.get('review_verdict', 'unknown')}`"
            )
    else:
        lines.append("- no shortlisted posts")
    lines.append("")
    lines.append("## Revenue Path")
    if today_path:
        for step in today_path[:3]:
            lines.append(
                f"- `{step.get('step', 'unknown')}`: `{step.get('title', 'unknown')}` | `{step.get('why_revenue', 'unknown')}`"
            )
    else:
        lines.append("- no revenue path available")
    lines.append("")
    lines.append("## Next Commands After Approval")
    append_command_list(lines, operator_run.get("planned_commands", []))
    lines.append("")
    lines.append("## Current Blockers")
    if not top_state.get("repo_connected"):
        lines.append("- GitHub repo is not connected yet, so cloud automation cannot continue after local preparation.")
    if not single:
        lines.append("- No single approval recommendation was found, so the user review path needs regeneration.")
    if not cloud_verification.get("all_core_checks_passed", True):
        lines.append("- First cloud run verification is not fully green yet.")
    search_console_blocked = "SEARCH_CONSOLE_SITE_URL" in setup_report.get("env_keys_empty", [])
    if search_console_blocked:
        lines.append("- Search Console site URL is still missing, so keyword refinement is still using fallback signals.")
    openai_blocked = "OPENAI_API_KEY" in setup_report.get("env_keys_empty", [])
    if openai_blocked:
        lines.append("- OpenAI API key is missing, so paid human-tone draft expansion remains disabled.")
    if not failed_steps and top_state.get("repo_connected") and not search_console_blocked:
        lines.append("- none")
    lines.append("")
    lines.append("## Roadmap")
    if roadmap_phases:
        for phase in roadmap_phases[:4]:
            lines.append(
                f"- `{phase.get('phase', 'unknown')}`: `{phase.get('focus', 'unknown')}`"
            )
    else:
        lines.append("- no roadmap phases available")
    lines.append("")
    lines.append("## Refresh Result")
    if failed_steps:
        lines.append("- failed steps detected:")
        for result in failed_steps:
            lines.append(f"- `{result['label']}` -> `{result['command']}`")
            if result["stderr"]:
                lines.append(f"- stderr: {result['stderr']}")
    else:
        lines.append("- all automation-focused refresh steps completed successfully")
    lines.append("")
    lines.append("## Refreshed Files")
    refreshed = [
        "outputs/latest/automation-scope.md",
        "outputs/latest/current-reference-strategy.md",
        "outputs/latest/reference-strength-benchmark.md",
        "outputs/latest/keyword-capture-strategy.md",
        "outputs/latest/review-packet.md",
        "outputs/latest/approval-dashboard.md",
        "outputs/latest/source-freshness-board.md",
        "outputs/latest/first-approval-path.md",
        "outputs/latest/daily-revenue-focus.md",
        "outputs/latest/traffic-cluster-board.md",
        "outputs/latest/popular-reads-board.md",
        "outputs/latest/retention-cta-board.md",
        "outputs/latest/monetization-roadmap.md",
        "outputs/latest/draft-polish-board.md",
        "outputs/latest/first-publish-operator-run.md",
        "outputs/latest/user-review-shortlist.md",
        "outputs/latest/current-review-focus.html",
        "outputs/latest/user-approval-inbox.html",
        "outputs/latest/user-review-checkpoint.html",
        "outputs/latest/github-minimum-launch-card.md",
        "outputs/latest/automation-progress-board.md",
        "outputs/latest/automation-unblock-card.md",
        "outputs/latest/minimum-unblock-flow.md",
        "outputs/latest/first-blogger-verify-card.md",
        "outputs/latest/first-blogger-verify-flow.md",
        "outputs/latest/review-preview-board.html",
        "outputs/latest/operator-home.html",
        "outputs/latest/platform-publish-plan.md",
        "outputs/latest/cross-platform-publish-pack.md",
        "outputs/latest/pre-publish-quality-gate.md",
        "outputs/latest/first-cloud-run-verification.md",
        "outputs/latest/go-live-dashboard.md",
        "outputs/latest/pipeline-workflow-parity.md",
        "outputs/latest/cloud-launch-preflight.md",
        "outputs/latest/start-here-runbook.md",
        "outputs/latest/today-operator-console.md",
    ]
    for path in refreshed:
        lines.append(f"- `{path}`")
    lines.append("")
    OUTPUT_MD.write_text("\n".join(lines))


def main() -> int:
    args = parse_args()
    results = []
    exit_code = 0

    for label, command in SCRIPT_STEPS:
        if label == "First cloud run verification":
            command = with_first_cloud_run_command()
        result = run_step(label, command, args.verbose)
        results.append(result)
        if result["returncode"] != 0 and exit_code == 0:
            exit_code = result["returncode"]

    write_report(results)
    print(OUTPUT_MD)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
