#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SETUP_JSON = ROOT / "outputs/latest/setup-check-report.json"
GO_LIVE_JSON = ROOT / "outputs/latest/go-live-readiness-report.json"
FIRST_LIVE_JSON = ROOT / "outputs/latest/first-live-run-plan.json"
GITHUB_LAUNCH_JSON = ROOT / "outputs/latest/github-launch-plan.json"
OUTPUT_JSON = ROOT / "outputs/latest/success-gate.json"
OUTPUT_MD = ROOT / "outputs/latest/success-gate.md"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def build_gate() -> dict:
    setup = load_json(SETUP_JSON)
    go_live = load_json(GO_LIVE_JSON)
    first_live = load_json(FIRST_LIVE_JSON)
    github_launch = load_json(GITHUB_LAUNCH_JSON)

    env_filled = set(setup.get("env_keys_filled", []))
    git_info = setup.get("git") or {}
    has_commit = bool(git_info.get("has_commit", False))
    git_repo_connected = (git_info.get("origin") or "") not in {"", "(not configured)"}
    github_repo_connected = bool(github_launch.get("repo_connected", False))
    github_repo_accessible = bool(github_launch.get("repo_accessible", False))
    repo_connected = bool(git_repo_connected and github_repo_connected)

    checks = [
        {
            "name": "google_client_connected",
            "ready": "GOOGLE_CLIENT_ID" in env_filled and "GOOGLE_CLIENT_SECRET" in env_filled,
            "next_action": "python3 scripts/bootstrap_google_oauth_credentials.py",
            "required": True,
        },
        {
            "name": "google_refresh_token_connected",
            "ready": "GOOGLE_REFRESH_TOKEN" in env_filled,
            "next_action": "GOOGLE_OAUTH_OPEN_BROWSER=true python3 scripts/get_google_refresh_token.py",
            "required": True,
        },
        {
            "name": "openai_connected",
            "ready": "OPENAI_API_KEY" in env_filled,
            "next_action": "OPENAI_API_KEY를 .env 에 입력(선택)",
            "required": False,
        },
        {
            "name": "initial_commit_created",
            "ready": has_commit,
            "next_action": "bash scripts/prepare_initial_commit.sh",
            "required": True,
        },
        {
            "name": "github_repo_connected",
            "ready": repo_connected and github_repo_accessible,
            "next_action": "bash scripts/bootstrap_github_remote.sh <OWNER/REPO>",
            "required": True,
        },
        {
            "name": "first_live_run_ready",
            "ready": bool(go_live.get("ready_for_first_live_run", False)),
            "next_action": "bash scripts/run_pipeline.sh",
            "required": True,
        },
    ]

    next_actions = [item["next_action"] for item in checks if item.get("required") and not item["ready"]]
    return {
        "all_green": all(item["ready"] for item in checks if item.get("required", True)),
        "first_live_status": first_live.get("status", ""),
        "github_launch_status": github_launch.get("status", ""),
        "checks": checks,
        "next_actions": next_actions[:3],
    }


def write_markdown(gate: dict) -> None:
    lines = []
    lines.append("# Success Gate")
    lines.append("")
    lines.append(f"- all_green: `{gate.get('all_green', False)}`")
    lines.append(f"- first_live_status: `{gate.get('first_live_status', '')}`")
    lines.append(f"- github_launch_status: `{gate.get('github_launch_status', '')}`")
    lines.append("")
    lines.append("## Checks")
    lines.append("")
    for item in gate.get("checks", []):
        state = "ready" if item.get("ready") else "pending"
        required_label = "required" if item.get("required", True) else "optional"
        lines.append(f"- `{item.get('name')}`: {state} ({required_label})")
        if not item.get("ready"):
            lines.append(f"  - next: `{item.get('next_action')}`")
    lines.append("")
    lines.append("## Top Next Actions")
    lines.append("")
    for action in gate.get("next_actions", []):
        lines.append(f"- `{action}`")
    OUTPUT_MD.write_text("\n".join(lines) + "\n")


def main() -> int:
    gate = build_gate()
    OUTPUT_JSON.write_text(json.dumps(gate, ensure_ascii=False, indent=2))
    write_markdown(gate)
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
