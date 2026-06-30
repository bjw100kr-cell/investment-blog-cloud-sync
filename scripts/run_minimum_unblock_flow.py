#!/usr/bin/env python3
import argparse
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIRST_APPROVAL_PATH_JSON = ROOT / "outputs/latest/first-approval-path.json"
AUTOMATION_UNBLOCK_CARD_JSON = ROOT / "outputs/latest/automation-unblock-card.json"
OUTPUT_JSON = ROOT / "outputs/latest/minimum-unblock-flow.json"
OUTPUT_MD = ROOT / "outputs/latest/minimum-unblock-flow.md"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Preview or apply the shortest unblock flow for first Blogger verification and free cloud automation."
    )
    parser.add_argument("--repo", default="", help="GitHub OWNER/REPO or full remote URL for bootstrap_github_remote.sh")
    parser.add_argument("--skip-approval", action="store_true", help="Skip applying the recommended single approval command.")
    parser.add_argument("--skip-repo", action="store_true", help="Skip the GitHub remote bootstrap step.")
    parser.add_argument("--apply", action="store_true", help="Actually run the selected steps. Without this, only preview the chain.")
    return parser.parse_args()


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def run_command(command: str) -> dict:
    completed = subprocess.run(
        command,
        cwd=ROOT,
        shell=True,
        capture_output=True,
        text=True,
    )
    return {
        "command": command,
        "returncode": completed.returncode,
        "stdout": completed.stdout.strip(),
        "stderr": completed.stderr.strip(),
    }


def build_command_chain(args: argparse.Namespace) -> list[str]:
    approval = load_json(FIRST_APPROVAL_PATH_JSON).get("recommended_single", {}).get("approval_command", "")
    commands: list[str] = []
    if approval and not args.skip_approval:
        commands.append(approval)
    if args.repo and not args.skip_repo:
        commands.append(f"bash scripts/bootstrap_github_remote.sh {json.dumps(args.repo)}")
    return commands


def build_report(args: argparse.Namespace) -> dict:
    unblock = load_json(AUTOMATION_UNBLOCK_CARD_JSON)
    commands = build_command_chain(args)
    results = []
    if args.apply:
        for command in commands:
            result = run_command(command)
            results.append(result)
            if result.get("returncode") != 0:
                break

    return {
        "headline": unblock.get("headline", ""),
        "main_candidate": unblock.get("main_candidate", {}),
        "repo_input": args.repo,
        "apply_mode": args.apply,
        "commands": commands,
        "execution_results": results,
        "success": all(item.get("returncode") == 0 for item in results) if results else None,
        "how_to_use": {
            "preview": "python3 scripts/run_minimum_unblock_flow.py",
            "preview_with_repo": "python3 scripts/run_minimum_unblock_flow.py --repo OWNER/REPO",
            "apply_with_repo": "python3 scripts/run_minimum_unblock_flow.py --repo OWNER/REPO --apply",
        },
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# Minimum Unblock Flow")
    lines.append("")
    lines.append("첫 Blogger 검증과 무료 클라우드 자동화 진입을 위한 최소 실행 체인입니다.")
    lines.append("")
    lines.append(f"- headline: {report.get('headline', '')}")
    lines.append(f"- repo_input: `{report.get('repo_input', '') or 'none'}`")
    lines.append(f"- apply_mode: `{report.get('apply_mode', False)}`")
    candidate = report.get("main_candidate", {})
    lines.append(f"- main_candidate: `{candidate.get('keyword', '')}` / {candidate.get('title', '')}")
    lines.append("")
    lines.append("## Command Chain")
    lines.append("")
    for command in report.get("commands", []):
        lines.append(f"- `{command}`")
    if not report.get("commands"):
        lines.append("- 현재 선택된 실행 명령이 없습니다.")
    lines.append("")
    if report.get("execution_results"):
        lines.append("## Execution Results")
        lines.append("")
        for result in report.get("execution_results", []):
            status = "ok" if result.get("returncode") == 0 else "failed"
            lines.append(f"- `{status}` `{result.get('command', '')}`")
            if result.get("stdout"):
                lines.append(f"  - stdout: {result.get('stdout', '')}")
            if result.get("stderr"):
                lines.append(f"  - stderr: {result.get('stderr', '')}")
        lines.append(f"- success: `{report.get('success')}`")
        lines.append("")
    lines.append("## How To Use")
    lines.append("")
    how = report.get("how_to_use", {})
    lines.append(f"- preview: `{how.get('preview', '')}`")
    lines.append(f"- preview_with_repo: `{how.get('preview_with_repo', '')}`")
    lines.append(f"- apply_with_repo: `{how.get('apply_with_repo', '')}`")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def main() -> int:
    args = parse_args()
    report = build_report(args)
    OUTPUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    write_markdown(report)
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
