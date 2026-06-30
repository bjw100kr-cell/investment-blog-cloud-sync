#!/usr/bin/env python3
import argparse
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INBOX_JSON = ROOT / "outputs/latest/user-approval-inbox.json"
OUTPUT_JSON = ROOT / "outputs/latest/user-approval-reply-plan.json"
OUTPUT_MD = ROOT / "outputs/latest/user-approval-reply-plan.md"
SET_APPROVALS = ROOT / "scripts/set_review_approvals.py"

APPROVE_HINTS = ("진행", "승인", "확인", "올려", "게시", "포스팅", "먼저")
HOLD_HINTS = ("보류", "대기", "나중", "다시 보기", "다시보기", "수정", "아직", "제외")
RECOVERY_HINTS = ("seo", "후속", "전환", "메인 말고", "메인말고", "대체", "evergreen")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Translate a short user approval reply into approval actions.")
    parser.add_argument("--reply", required=True, help="Natural-language reply like 'fomc 글 먼저 진행'")
    parser.add_argument("--apply", action="store_true", help="Write review-approvals.json when the reply is clear enough.")
    return parser.parse_args()


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def build_keyword_aliases(item: dict) -> list[str]:
    keyword = item.get("keyword", "").strip()
    title = item.get("title", "").strip()
    aliases = [keyword.lower()] if keyword else []
    if title:
        aliases.append(title.lower())
        simplified = title.lower().replace(" ", "")
        if simplified not in aliases:
            aliases.append(simplified)
    return aliases


def build_recovery_aliases(item: dict) -> list[str]:
    aliases: list[str] = []
    recovery_title = item.get("recovery_title", "").strip()
    recovery_keyword = item.get("recovery_keyword", "").strip()
    if recovery_keyword:
        aliases.append(recovery_keyword.lower())
    if recovery_title:
        aliases.append(recovery_title.lower())
        simplified = recovery_title.lower().replace(" ", "")
        if simplified not in aliases:
            aliases.append(simplified)
    return aliases


def contains_any(text: str, hints: tuple[str, ...]) -> bool:
    return any(hint in text for hint in hints)


def split_segments(reply_text: str) -> list[str]:
    normalized = reply_text.replace(" 그리고 ", ",").replace(" and ", ",")
    parts = [part.strip() for part in normalized.split(",")]
    return [part for part in parts if part]


def local_windows(text: str, aliases: list[str], radius: int = 8) -> list[str]:
    windows: list[str] = []
    compact = text.replace(" ", "")
    for alias in aliases:
        if not alias:
            continue
        for haystack in (text, compact):
            start = 0
            while True:
                index = haystack.find(alias, start)
                if index == -1:
                    break
                left = max(index - radius, 0)
                right = min(index + len(alias) + radius, len(haystack))
                windows.append(haystack[left:right])
                start = index + len(alias)
    return windows


def alias_contexts(text: str, aliases: list[str], radius: int = 8) -> tuple[list[str], list[str]]:
    before_contexts: list[str] = []
    after_contexts: list[str] = []
    compact = text.replace(" ", "")
    for alias in aliases:
        if not alias:
            continue
        for haystack in (text, compact):
            start = 0
            while True:
                index = haystack.find(alias, start)
                if index == -1:
                    break
                before_contexts.append(haystack[max(index - radius, 0):index])
                after_contexts.append(haystack[index + len(alias):min(index + len(alias) + radius, len(haystack))])
                start = index + len(alias)
    return before_contexts, after_contexts


def detect_item_state(reply_text: str, item: dict) -> str:
    aliases = build_keyword_aliases(item)
    normalized = reply_text.lower().strip()
    compact = normalized.replace(" ", "")
    matched = any(alias and (alias in normalized or alias in compact) for alias in aliases)
    if not matched and ("둘 다" in normalized or "둘다" in compact):
        matched = True
    if not matched:
        return "unmentioned"

    relevant_segments = []
    for segment in split_segments(normalized):
        segment_compact = segment.replace(" ", "")
        if "둘 다" in segment or "둘다" in segment_compact:
            relevant_segments.append(segment)
            continue
        if any(alias and (alias in segment or alias in segment_compact) for alias in aliases):
            relevant_segments.append(segment)

    if not relevant_segments:
        relevant_segments = [normalized]

    windows = []
    before_contexts = []
    after_contexts = []
    for segment in relevant_segments:
        windows.extend(local_windows(segment, aliases))
        before, after = alias_contexts(segment, aliases)
        before_contexts.extend(before)
        after_contexts.extend(after)
    scoped_texts = windows or relevant_segments

    has_approve = any(contains_any(segment, APPROVE_HINTS) for segment in scoped_texts)
    has_hold = any(contains_any(segment, HOLD_HINTS) for segment in scoped_texts)
    approve_after = any(contains_any(segment, APPROVE_HINTS) for segment in after_contexts)
    hold_after = any(contains_any(segment, HOLD_HINTS) for segment in after_contexts)
    hold_before = any(contains_any(segment, HOLD_HINTS) for segment in before_contexts)

    if approve_after and not hold_after:
        return "approve"
    if hold_after or (hold_before and not approve_after):
        return "hold"

    if has_approve and not has_hold:
        return "approve"
    if has_hold and not has_approve:
        return "hold"
    if item.get("ready_now") and "먼저" in normalized and not has_hold:
        return "approve"
    return "mentioned"


def detect_recovery_selection(reply_text: str, item: dict) -> bool:
    normalized = reply_text.lower().strip()
    compact = normalized.replace(" ", "")
    aliases = build_keyword_aliases(item)
    recovery_aliases = build_recovery_aliases(item)
    item_matched = any(alias and (alias in normalized or alias in compact) for alias in aliases)
    if not item_matched:
        return False
    if not contains_any(normalized, RECOVERY_HINTS):
        return False
    if recovery_aliases and any(alias and (alias in normalized or alias in compact) for alias in recovery_aliases):
        return True
    return True


def build_plan(reply: str) -> dict:
    inbox = load_json(INBOX_JSON)
    items = inbox.get("items", [])
    states = []
    approved_keywords = []
    held_keywords = []
    mentioned_keywords = []

    for item in items:
        state = detect_item_state(reply, item)
        keyword = item.get("keyword", "")
        recovery_selected = detect_recovery_selection(reply, item)
        effective_keyword = keyword
        effective_title = item.get("title", "")
        effective_mode = "direct"
        if recovery_selected and item.get("recovery_confirm_command"):
            recovery_keyword = item.get("recovery_confirm_command", "").split("--keywords", 1)[-1].strip().split()[0]
            if recovery_keyword:
                effective_keyword = recovery_keyword
                effective_title = item.get("recovery_title", effective_title)
                effective_mode = item.get("recovery_mode", "recovery")
                if state == "mentioned":
                    state = "approve"
        states.append(
            {
                "keyword": keyword,
                "title": item.get("title", ""),
                "ready_now": item.get("ready_now", False),
                "state": state,
                "effective_keyword": effective_keyword,
                "effective_title": effective_title,
                "selection_mode": effective_mode,
            }
        )
        if state == "approve" and effective_keyword:
            approved_keywords.append(effective_keyword)
        elif state == "hold" and keyword:
            held_keywords.append(keyword)
        elif state == "mentioned" and keyword:
            mentioned_keywords.append(keyword)

    approved_keywords = list(dict.fromkeys(approved_keywords))

    clear = bool(approved_keywords) and not mentioned_keywords
    command = ""
    if approved_keywords:
        command = f"python3 {SET_APPROVALS} --keywords {' '.join(approved_keywords)} --notes {json.dumps(reply, ensure_ascii=False)}"

    return {
        "reply": reply,
        "clear_enough_to_apply": clear,
        "approved_keywords": approved_keywords,
        "held_keywords": held_keywords,
        "mentioned_but_ambiguous_keywords": mentioned_keywords,
        "item_states": states,
        "set_review_approvals_command": command,
        "safety_note": "애매한 답변이면 apply 하지 않고 preview 로 멈춥니다.",
    }


def write_markdown(plan: dict) -> None:
    lines = []
    lines.append("# User Approval Reply Plan")
    lines.append("")
    lines.append(f"- reply: `{plan.get('reply', '')}`")
    lines.append(f"- clear_enough_to_apply: `{plan.get('clear_enough_to_apply', False)}`")
    lines.append(f"- approved_keywords: `{', '.join(plan.get('approved_keywords', [])) or 'none'}`")
    lines.append(f"- held_keywords: `{', '.join(plan.get('held_keywords', [])) or 'none'}`")
    lines.append(
        f"- mentioned_but_ambiguous_keywords: `{', '.join(plan.get('mentioned_but_ambiguous_keywords', [])) or 'none'}`"
    )
    lines.append(f"- safety_note: {plan.get('safety_note', '')}")
    lines.append("")
    lines.append("## Item States")
    lines.append("")
    for item in plan.get("item_states", []):
        lines.append(
            f"- `{item.get('keyword', '')}` / {item.get('title', '')} / ready_now `{item.get('ready_now', False)}` / state `{item.get('state', '')}` / effective `{item.get('effective_keyword', '')}` / mode `{item.get('selection_mode', '')}`"
        )
    lines.append("")
    if plan.get("set_review_approvals_command"):
        lines.append("## Next Command")
        lines.append("")
        lines.append(f"- `{plan.get('set_review_approvals_command', '')}`")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def maybe_apply(plan: dict) -> dict:
    if not plan.get("clear_enough_to_apply") or not plan.get("set_review_approvals_command"):
        return {"applied": False, "reason": "reply_not_clear_enough"}
    completed = subprocess.run(
        plan["set_review_approvals_command"],
        cwd=ROOT,
        shell=True,
        capture_output=True,
        text=True,
    )
    return {
        "applied": completed.returncode == 0,
        "returncode": completed.returncode,
        "stdout": completed.stdout.strip(),
        "stderr": completed.stderr.strip(),
    }


def main() -> int:
    args = parse_args()
    plan = build_plan(args.reply)
    if args.apply:
        plan["apply_result"] = maybe_apply(plan)
    OUTPUT_JSON.write_text(json.dumps(plan, ensure_ascii=False, indent=2))
    write_markdown(plan)
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
