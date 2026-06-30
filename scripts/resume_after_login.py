#!/usr/bin/env python3
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_JSON = ROOT / "outputs/latest/resume-after-login-report.json"
OUTPUT_MD = ROOT / "outputs/latest/resume-after-login-report.md"
GO_LIVE_DASHBOARD_JSON = ROOT / "outputs/latest/go-live-dashboard.json"
SETUP_JSON = ROOT / "outputs/latest/setup-check-report.json"
START_HERE_MD = ROOT / "outputs/latest/start-here-runbook.md"
GITHUB_MINIMUM_LAUNCH_CARD_MD = ROOT / "outputs/latest/github-minimum-launch-card.md"
TOKEN_JSON = ROOT / "outputs/latest/google-oauth-token-result.json"


def run_step(label: str, command: list[str]) -> dict:
    completed = subprocess.run(
        command,
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
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
    return json.loads(path.read_text())


def next_action_from_dashboard() -> str:
    dashboard = load_json(GO_LIVE_DASHBOARD_JSON)
    setup = load_json(SETUP_JSON)
    env_filled = set(setup.get("env_keys_filled", []))
    git_origin = ((setup.get("git") or {}).get("origin") or "").strip()
    git_branch = ((setup.get("git") or {}).get("branch") or "").strip()

    if "GOOGLE_CLIENT_ID" not in env_filled or "GOOGLE_CLIENT_SECRET" not in env_filled:
        return "python3 scripts/open_login_setup_pages.py --open-next"
    if "GOOGLE_REFRESH_TOKEN" not in env_filled:
        if TOKEN_JSON.exists():
            return "python3 scripts/apply_google_oauth_result.py"
        return "GOOGLE_OAUTH_OPEN_BROWSER=true python3 scripts/get_google_refresh_token.py"
    if not dashboard.get("auto_channel_ready_count"):
        return "python3 scripts/open_login_setup_pages.py --open-next"
    if git_branch in {"", "(none)"}:
        return "bash scripts/prepare_initial_commit.sh"
    if git_origin in {"", "(not configured)"}:
        return "bash scripts/bootstrap_github_remote.sh <OWNER/REPO>"

    commands = dashboard.get("next_commands", [])
    if commands:
        return commands[0]
    return "bash scripts/run_pipeline.sh"


def write_report(results: list[dict], next_action: str) -> None:
    payload = {
        "steps": results,
        "next_action": next_action,
        "token_json_present": TOKEN_JSON.exists(),
    }
    OUTPUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2))

    lines = []
    lines.append("# Resume After Login Report")
    lines.append("")
    for result in results:
        state = "ok" if result["returncode"] == 0 else "failed"
        lines.append(f"- `{state}` {result['label']}: `{result['command']}`")
        if result["stdout"]:
            lines.append(f"  - stdout: {result['stdout']}")
        if result["stderr"]:
            lines.append(f"  - stderr: {result['stderr']}")
    lines.append("")
    lines.append("## Next Action")
    lines.append("")
    lines.append(f"- `{next_action}`")
    lines.append("")
    lines.append("## Reference")
    lines.append("")
    lines.append(f"- [start-here-runbook.md]({START_HERE_MD})")
    lines.append(f"- [github-minimum-launch-card.md]({GITHUB_MINIMUM_LAUNCH_CARD_MD})")
    OUTPUT_MD.write_text("\n".join(lines) + "\n")


def main() -> int:
    results = []
    results.append(run_step("Setup check", ["python3", "scripts/check_setup.py"]))
    results.append(run_step("OAuth bootstrap", ["python3", "scripts/bootstrap_google_oauth_credentials.py"]))

    if TOKEN_JSON.exists():
        results.append(run_step("Apply OAuth token", ["python3", "scripts/apply_google_oauth_result.py"]))

    for label, command in [
        ("Setup check refresh", ["python3", "scripts/check_setup.py"]),
        ("Login checklist refresh", ["python3", "scripts/open_login_setup_pages.py"]),
        ("GitHub sync guide refresh", ["python3", "scripts/export_github_actions_sync_commands.py"]),
        ("Go-live readiness refresh", ["python3", "scripts/build_go_live_readiness_report.py"]),
        ("Platform publish plan refresh", ["python3", "scripts/build_platform_publish_plan.py"]),
        ("First live run plan refresh", ["python3", "scripts/prepare_first_live_run_plan.py"]),
        ("GitHub launch plan refresh", ["python3", "scripts/prepare_github_launch_plan.py"]),
        ("Go-live dashboard refresh", ["python3", "scripts/prepare_go_live_dashboard.py"]),
        ("Cloud launch preflight refresh", ["python3", "scripts/build_cloud_launch_preflight.py"]),
        ("Operator handoff refresh", ["python3", "scripts/generate_operator_handoff.py"]),
        ("Start here refresh", ["python3", "scripts/prepare_start_here_runbook.py"]),
    ]:
        results.append(run_step(label, command))

    next_action = next_action_from_dashboard()
    write_report(results, next_action)
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
