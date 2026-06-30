#!/usr/bin/env python3
import argparse
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPLY_HELPER = ROOT / "scripts/apply_user_approval_reply.py"
PLAN_JSON = ROOT / "outputs/latest/user-approval-reply-plan.json"
PUBLISH_PLAN_JSON = ROOT / "outputs/latest/platform-publish-plan.json"
PUBLISH_INVENTORY_JSON = ROOT / "outputs/latest/publish-inventory.json"
QUALITY_GATE_JSON = ROOT / "outputs/latest/pre-publish-quality-gate.json"
FRESHNESS_JSON = ROOT / "outputs/latest/source-freshness-board.json"
OUTPUT_JSON = ROOT / "outputs/latest/user-approval-rehearsal.json"
OUTPUT_MD = ROOT / "outputs/latest/user-approval-rehearsal.md"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Safely rehearse a user approval reply without real upload side effects.")
    parser.add_argument("--reply", required=True, help='Natural-language reply like "bitcoin 글 먼저 진행"')
    return parser.parse_args()


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def run_reply_preview(reply: str) -> dict:
    command = ["python3", str(REPLY_HELPER), "--reply", reply]
    completed = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
    return {
        "command": " ".join(command),
        "returncode": completed.returncode,
        "stdout": completed.stdout.strip(),
        "stderr": completed.stderr.strip(),
        "plan": load_json(PLAN_JSON),
    }


def build_lookup(items: list[dict], key: str) -> dict[str, dict]:
    return {item.get(key, ""): item for item in items if item.get(key)}


def collect_candidate_items(approved_keywords: list[str]) -> list[dict]:
    inventory = load_json(PUBLISH_INVENTORY_JSON)
    quality_lookup = build_lookup(load_json(QUALITY_GATE_JSON).get("items", []), "keyword")
    freshness_lookup = build_lookup(load_json(FRESHNESS_JSON).get("items", []), "keyword")
    publish_plan = load_json(PUBLISH_PLAN_JSON)
    blogger_lookup = build_lookup(
        next((channel for channel in publish_plan.get("channels", []) if channel.get("name") == "blogger"), {}).get("items", []),
        "keyword",
    )

    items = []
    approved = set(approved_keywords)
    for item in inventory.get("items", []):
        keyword = item.get("keyword", "")
        if keyword not in approved and item.get("source_keyword", "") not in approved:
            continue
        quality = quality_lookup.get(keyword, {})
        freshness = freshness_lookup.get(keyword, {})
        blogger = blogger_lookup.get(keyword, {})
        quality_status = quality.get("status", "")
        freshness_status = freshness.get("freshness_status", "")
        if quality_status == "needs_fix":
            predicted = "blocked"
            reason = "pre_publish_quality_gate_needs_fix"
        elif quality_status == "review_before_publish":
            predicted = "blocked"
            reason = "pre_publish_quality_gate_review"
        elif freshness_status == "stale":
            predicted = "blocked"
            reason = "source_freshness_stale"
        elif blogger:
            predicted = "candidate"
            reason = "would_enter_blogger_candidate_set"
        else:
            predicted = "candidate"
            reason = "approved_but_not_in_current_blogger_channel_list"
        items.append(
            {
                "keyword": keyword,
                "source_keyword": item.get("source_keyword", ""),
                "title": item.get("title", ""),
                "inventory_type": item.get("inventory_type", ""),
                "role": item.get("role", ""),
                "quality_status": quality_status,
                "freshness_status": freshness_status,
                "predicted_state": predicted,
                "predicted_reason": reason,
                "html_path": item.get("html_path", ""),
            }
        )

    items.sort(key=lambda entry: (0 if entry.get("predicted_state") == "candidate" else 1, entry.get("keyword", "")))
    return items


def build_report(reply: str) -> dict:
    preview = run_reply_preview(reply)
    plan = preview.get("plan", {})
    approved_keywords = plan.get("approved_keywords", [])
    candidate_items = collect_candidate_items(approved_keywords) if plan.get("clear_enough_to_apply") else []
    return {
        "reply": reply,
        "clear_enough_to_apply": plan.get("clear_enough_to_apply", False),
        "approved_keywords": approved_keywords,
        "held_keywords": plan.get("held_keywords", []),
        "ambiguous_keywords": plan.get("mentioned_but_ambiguous_keywords", []),
        "preview_command_result": {
            "command": preview.get("command", ""),
            "returncode": preview.get("returncode", 1),
            "stdout": preview.get("stdout", ""),
            "stderr": preview.get("stderr", ""),
        },
        "candidate_items": candidate_items,
        "summary": {
            "candidate_count": sum(1 for item in candidate_items if item.get("predicted_state") == "candidate"),
            "blocked_count": sum(1 for item in candidate_items if item.get("predicted_state") == "blocked"),
        },
        "safety_note": "이 리허설은 approval plan만 해석하고, 실제 review-approvals.json이나 Blogger 업로드 상태는 바꾸지 않습니다.",
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# User Approval Rehearsal")
    lines.append("")
    lines.append("자연어 승인 답변이 실제 업로드 전에 어떤 후보 상태를 만들지 안전하게 미리 보는 리허설입니다.")
    lines.append("")
    lines.append(f"- reply: `{report.get('reply', '')}`")
    lines.append(f"- clear_enough_to_apply: `{report.get('clear_enough_to_apply', False)}`")
    lines.append(f"- approved_keywords: `{', '.join(report.get('approved_keywords', [])) or 'none'}`")
    lines.append(f"- held_keywords: `{', '.join(report.get('held_keywords', [])) or 'none'}`")
    lines.append(f"- ambiguous_keywords: `{', '.join(report.get('ambiguous_keywords', [])) or 'none'}`")
    lines.append(f"- safety_note: {report.get('safety_note', '')}")
    lines.append("")
    lines.append("## Preview Command")
    lines.append("")
    preview = report.get("preview_command_result", {})
    lines.append(f"- command: `{preview.get('command', '')}`")
    lines.append(f"- returncode: `{preview.get('returncode', '')}`")
    if preview.get("stdout"):
        lines.append(f"- stdout: `{preview.get('stdout', '')}`")
    if preview.get("stderr"):
        lines.append(f"- stderr: `{preview.get('stderr', '')}`")
    lines.append("")
    lines.append("## Candidate Outcomes")
    lines.append("")
    for item in report.get("candidate_items", []):
        lines.append(
            f"- `{item.get('keyword', '')}` / {item.get('title', '')} / {item.get('inventory_type', '')} / quality `{item.get('quality_status', '')}` / freshness `{item.get('freshness_status', '')}` / predicted `{item.get('predicted_state', '')}` / reason `{item.get('predicted_reason', '')}`"
        )
    if not report.get("candidate_items"):
        lines.append("- 현재 답변 기준으로 계산된 후보가 없습니다.")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def main() -> int:
    args = parse_args()
    report = build_report(args.reply)
    OUTPUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    write_markdown(report)
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
