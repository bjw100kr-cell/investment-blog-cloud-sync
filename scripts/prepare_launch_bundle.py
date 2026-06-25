#!/usr/bin/env python3
import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_MD = ROOT / "outputs/latest/launch-bundle-report.md"

SCRIPT_STEPS = [
    ("Setup check", ["python3", "scripts/check_setup.py"]),
    ("GitHub secrets checklist", ["python3", "scripts/export_secrets_checklist.py"]),
    ("Login launch checklist", ["python3", "scripts/open_login_setup_pages.py"]),
    ("OAuth client discovery", ["python3", "scripts/find_google_oauth_client.py"]),
    ("GitHub Actions sync guide", ["python3", "scripts/export_github_actions_sync_commands.py"]),
    ("Go-live readiness report", ["python3", "scripts/build_go_live_readiness_report.py"]),
    ("SEO backlog", ["python3", "scripts/build_seo_backlog.py"]),
    ("SEO draft packets", ["python3", "scripts/build_seo_draft_packets.py"]),
    ("SEO draft generation", ["python3", "scripts/generate_seo_blog_drafts.py"]),
    ("SEO publishing assets", ["python3", "scripts/generate_seo_publishing_assets.py"]),
    ("SEO publish-ready render", ["python3", "scripts/render_seo_publish_ready_posts.py"]),
    ("Publish inventory", ["python3", "scripts/build_publish_inventory.py"]),
    ("Distribution pack", ["python3", "scripts/build_distribution_pack.py"]),
    ("Keyword opportunity board", ["python3", "scripts/build_keyword_opportunity_board.py"]),
    ("Monetization readiness report", ["python3", "scripts/build_monetization_readiness_report.py"]),
    ("First live run plan", ["python3", "scripts/prepare_first_live_run_plan.py"]),
    ("GitHub launch plan", ["python3", "scripts/prepare_github_launch_plan.py"]),
    ("Go-live dashboard", ["python3", "scripts/prepare_go_live_dashboard.py"]),
    ("Success gate", ["python3", "scripts/build_success_gate.py"]),
    ("Operator handoff", ["python3", "scripts/generate_operator_handoff.py"]),
    ("Start here runbook", ["python3", "scripts/prepare_start_here_runbook.py"]),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Refresh all launch-preparation reports for the investment blog automation stack.")
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


def write_report(results: list[dict]) -> None:
    lines = []
    lines.append("# Launch Bundle Report")
    lines.append("")
    for result in results:
        state = "ok" if result["returncode"] == 0 else "failed"
        lines.append(f"- `{state}` {result['label']}: `{result['command']}`")
        if result["stdout"]:
            lines.append(f"  - stdout: {result['stdout']}")
        if result["stderr"]:
            lines.append(f"  - stderr: {result['stderr']}")
    lines.append("")
    OUTPUT_MD.write_text("\n".join(lines))


def main() -> int:
    args = parse_args()
    results = []
    exit_code = 0

    for label, command in SCRIPT_STEPS:
        result = run_step(label, command, args.verbose)
        results.append(result)
        if result["returncode"] != 0 and exit_code == 0:
            exit_code = result["returncode"]

    write_report(results)
    print(OUTPUT_MD)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
