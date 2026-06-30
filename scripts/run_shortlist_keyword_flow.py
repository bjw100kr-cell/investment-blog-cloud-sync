#!/usr/bin/env python3
import argparse
import json
import shlex
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ACTION_BOARD_JSON = ROOT / "outputs/latest/shortlist-publish-action-board.json"
OUTPUT_JSON = ROOT / "outputs/latest/shortlist-keyword-flow-run.json"
OUTPUT_MD = ROOT / "outputs/latest/shortlist-keyword-flow-run.md"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Preview or run the keyword-specific shortlist flow after user review."
    )
    parser.add_argument("--keyword", required=True, help="Target shortlist keyword.")
    parser.add_argument("--apply", action="store_true", help="Actually run the generated command chain.")
    parser.add_argument("--image-url", default="", help="Required when the next step is hero image selection.")
    parser.add_argument("--image-credit", default="Photo by ...", help="Credit line used with --image-url.")
    return parser.parse_args()


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def board_item_for_keyword(keyword: str) -> dict:
    payload = load_json(ACTION_BOARD_JSON)
    for item in payload.get("items", []):
        if item.get("keyword") == keyword:
            return item
    return {}


def materialize_command(command: str, args: argparse.Namespace) -> str:
    if "<IMAGE_URL>" not in command:
        if args.apply and "prepare_first_cloud_run_verification.py" in command and "--allow-approved-state" not in command:
            return f"{command} --allow-approved-state"
        return command
    if not args.image_url:
        return command
    return (
        command.replace("<IMAGE_URL>", args.image_url)
        .replace('"Photo by ..."', json.dumps(args.image_credit, ensure_ascii=False))
    )


def build_chain(item: dict, args: argparse.Namespace) -> list[str]:
    commands = []
    next_command = item.get("next_command", "")
    if next_command:
        commands.append(materialize_command(next_command, args))
    for command in item.get("followup_commands", []):
        commands.append(materialize_command(command, args))
    return commands


def validate_apply(item: dict, commands: list[str], args: argparse.Namespace) -> str:
    if not args.apply:
        return ""
    if not item:
        return "keyword not found in shortlist publish action board"
    if any("<IMAGE_URL>" in command for command in commands):
        return "image-url is required before apply because this keyword still needs hero image selection"
    return ""


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


def build_report(args: argparse.Namespace) -> dict:
    item = board_item_for_keyword(args.keyword)
    commands = build_chain(item, args)
    error = validate_apply(item, commands, args)

    results = []
    if args.apply and not error:
        for command in commands:
            results.append(run_command(command))
            if results[-1]["returncode"] != 0:
                break

    return {
        "keyword": args.keyword,
        "apply_mode": args.apply,
        "found": bool(item),
        "error": error,
        "title": item.get("title", ""),
        "next_action": item.get("next_action", ""),
        "hard_blocking_checks": item.get("hard_blocking_checks", []),
        "advisory_checks": item.get("advisory_checks", []),
        "commands": commands,
        "results": results,
        "success": all(result.get("returncode") == 0 for result in results) if results else None,
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# Shortlist Keyword Flow Run")
    lines.append("")
    lines.append("shortlist 글 1개 기준으로 실제 실행 체인을 preview하거나 apply한 결과입니다.")
    lines.append("")
    lines.append(f"- keyword: `{report.get('keyword', '')}`")
    lines.append(f"- title: `{report.get('title', '')}`")
    lines.append(f"- apply_mode: `{report.get('apply_mode', False)}`")
    lines.append(f"- found: `{report.get('found', False)}`")
    if report.get("error"):
        lines.append(f"- error: `{report.get('error', '')}`")
    if report.get("hard_blocking_checks"):
        lines.append(f"- hard_blocking_checks: {', '.join(report.get('hard_blocking_checks', []))}")
    if report.get("advisory_checks"):
        lines.append(f"- advisory_checks: {', '.join(report.get('advisory_checks', []))}")
    lines.append(f"- next_action: {report.get('next_action', '')}")
    lines.append("")
    lines.append("## Command Chain")
    lines.append("")
    for command in report.get("commands", []):
        lines.append(f"- `{command}`")
    if not report.get("commands"):
        lines.append("- none")
    lines.append("")

    if report.get("results"):
        lines.append("## Execution Results")
        lines.append("")
        for result in report.get("results", []):
            state = "ok" if result.get("returncode") == 0 else "failed"
            lines.append(f"- `{state}` `{result.get('command', '')}`")
            if result.get("stdout"):
                lines.append(f"  - stdout: {result.get('stdout', '')}")
            if result.get("stderr"):
                lines.append(f"  - stderr: {result.get('stderr', '')}")
        lines.append("")
        lines.append(f"- success: `{report.get('success')}`")
    else:
        lines.append("## How To Use")
        lines.append("")
        lines.append(
            f"- preview: `python3 scripts/run_shortlist_keyword_flow.py --keyword {report.get('keyword', '')}`"
        )
        if "hero_image_selected" in report.get("hard_blocking_checks", []):
            lines.append(
                f"- apply with image: `python3 scripts/run_shortlist_keyword_flow.py --keyword {report.get('keyword', '')} --image-url <IMAGE_URL> --image-credit \"Photo by ...\" --apply`"
            )
        else:
            lines.append(
                f"- apply: `python3 scripts/run_shortlist_keyword_flow.py --keyword {report.get('keyword', '')} --apply`"
            )
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
