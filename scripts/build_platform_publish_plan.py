#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SETUP_JSON = ROOT / "outputs/latest/setup-check-report.json"
PUBLISH_INVENTORY_JSON = ROOT / "outputs/latest/publish-inventory.json"
APPROVALS_JSON = ROOT / "outputs/latest/review-approvals.json"
AUTOMATION_SCOPE_JSON = ROOT / "outputs/latest/automation-scope.json"
OUTPUT_JSON = ROOT / "outputs/latest/platform-publish-plan.json"
OUTPUT_MD = ROOT / "outputs/latest/platform-publish-plan.md"
QUALITY_GATE_JSON = ROOT / "outputs/latest/pre-publish-quality-gate.json"
SOURCE_FRESHNESS_JSON = ROOT / "outputs/latest/source-freshness-board.json"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def integration_lookup(setup: dict) -> dict:
    return {item.get("name"): item for item in setup.get("integrations", [])}


def normalized_confirmations(approvals: dict) -> tuple[bool, list[str]]:
    confirmed_all = bool(approvals.get("user_confirmed_all", approvals.get("approved_all", False)))
    confirmed_keywords = approvals.get("user_confirmed_keywords", approvals.get("approved_keywords", []))
    return confirmed_all, [item for item in confirmed_keywords if item]


def is_approved(item: dict, approvals: dict) -> bool:
    confirmed_all, confirmed_keywords = normalized_confirmations(approvals)
    if confirmed_all:
        return True
    approved = set(confirmed_keywords)
    candidates = {item.get("keyword", ""), Path(item.get("html_path", "")).stem}
    return any(candidate in approved for candidate in candidates if candidate)


def build_quality_lookup() -> dict[str, str]:
    if not QUALITY_GATE_JSON.exists():
        return {}
    payload = load_json(QUALITY_GATE_JSON)
    lookup = {}
    for entry in payload.get("items", []):
        status = entry.get("status", "")
        keyword = entry.get("keyword", "")
        html_path = entry.get("html_path", "")
        source_group = entry.get("source_group", "")
        if keyword and status:
            lookup[keyword] = status
            lookup[f"{keyword}:{source_group}"] = status
        if html_path:
            lookup[Path(html_path).stem] = status
    return lookup


def build_freshness_lookup() -> dict[str, str]:
    if not SOURCE_FRESHNESS_JSON.exists():
        return {}
    payload = load_json(SOURCE_FRESHNESS_JSON)
    lookup = {}
    for entry in payload.get("items", []):
        keyword = entry.get("keyword", "")
        status = entry.get("freshness_status", "")
        if keyword and status:
            lookup[keyword] = status
    return lookup


def is_quality_ready(item: dict, quality_lookup: dict[str, str]) -> bool:
    if not quality_lookup:
        return True
    keyword = item.get("keyword", "")
    html_path = item.get("manifest_path", "")
    source_group = item.get("inventory_type", "")
    source_group_key = "seo" if source_group == "seo_followup" else "main"
    status = quality_lookup.get(keyword) or quality_lookup.get(f"{keyword}:{source_group_key}") or quality_lookup.get(
        Path(html_path).stem if html_path else ""
    )
    if not status:
        return True
    return status == "pass"


def is_freshness_ready(item: dict, freshness_lookup: dict[str, str]) -> bool:
    if not freshness_lookup:
        return True
    status = freshness_lookup.get(item.get("keyword", ""))
    if not status:
        return True
    return status != "stale"


def build_channel(name: str, ready: bool, command: str, items: list[dict]) -> dict:
    approved_ready = [item for item in items if item.get("ready_to_upload")]
    return {
        "name": name,
        "ready": ready,
        "command": command,
        "ready_item_count": len(approved_ready),
        "first_item": approved_ready[0] if approved_ready else {},
        "items": approved_ready[:5],
    }


def build_report() -> dict:
    setup = load_json(SETUP_JSON)
    inventory = load_json(PUBLISH_INVENTORY_JSON)
    approvals = load_json(APPROVALS_JSON)
    automation_scope = load_json(AUTOMATION_SCOPE_JSON)
    integrations = integration_lookup(setup)
    quality_lookup = build_quality_lookup()
    freshness_lookup = build_freshness_lookup()
    items = inventory.get("items", [])

    for item in items:
        item["approved_for_upload"] = is_approved(item, approvals)
        item["quality_pass"] = is_quality_ready(item, quality_lookup)
        item["freshness_status"] = freshness_lookup.get(item.get("keyword", ""), "")
        item["freshness_pass"] = is_freshness_ready(item, freshness_lookup)

    approved_items = [
        item
        for item in items
        if item.get("approved_for_upload") and item.get("quality_pass") and item.get("freshness_pass")
    ]
    quality_ready_count = len(
        [item for item in items if item.get("quality_pass") and item.get("freshness_pass") and item.get("ready_to_upload")]
    )

    channels = [
        build_channel(
            "blogger",
            integrations.get("blogger_upload", {}).get("ready", False),
            "python3 scripts/upload_blogger_drafts.py",
            approved_items,
        ),
        build_channel(
            "wordpress",
            integrations.get("wordpress_upload", {}).get("ready", False),
            "python3 scripts/upload_wordpress_drafts.py",
            approved_items,
        ),
    ]

    confirmed_all, confirmed_keywords = normalized_confirmations(approvals)

    return {
        "automation_policy": automation_scope.get("automation_policy", "automation-first"),
        "primary_channel": automation_scope.get("primary_channel", {}).get("name", "blogger"),
        "secondary_channel": automation_scope.get("secondary_channel", {}).get("name", "wordpress"),
        "user_final_confirmation_required": True,
        "user_confirmed_all": confirmed_all,
        "user_confirmed_keywords": confirmed_keywords,
        "approved_all": approvals.get("approved_all", False),
        "approved_keywords": approvals.get("approved_keywords", []),
        "approved_ready_count": len([item for item in approved_items if item.get("ready_to_upload")]),
        "quality_ready_count": quality_ready_count,
        "channels": channels,
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# Platform Publish Plan")
    lines.append("")
    lines.append(f"- automation_policy: `{report.get('automation_policy', '')}`")
    lines.append(f"- primary_channel: `{report.get('primary_channel', '')}`")
    lines.append(f"- secondary_channel: `{report.get('secondary_channel', '')}`")
    lines.append("- user confirmation policy: `upload blocked until you confirm the draft`")
    lines.append(f"- user_confirmed_all: `{report.get('user_confirmed_all', False)}`")
    lines.append(f"- user_confirmed_keywords: `{json.dumps(report.get('user_confirmed_keywords', []), ensure_ascii=False)}`")
    lines.append(f"- user_confirmed_ready_count: `{report.get('approved_ready_count', 0)}`")
    lines.append(f"- quality_ready_count: `{report.get('quality_ready_count', 0)}`")
    lines.append("- freshness policy: `stale source evidence is excluded from upload candidates until refreshed`")
    lines.append("")
    for channel in report.get("channels", []):
        lines.append(f"## {channel.get('name')}")
        lines.append("")
        lines.append(f"- ready: `{channel.get('ready')}`")
        lines.append(f"- ready_item_count: `{channel.get('ready_item_count', 0)}`")
        lines.append(f"- command: `{channel.get('command', '')}`")
        first_item = channel.get("first_item", {})
        if first_item:
            lines.append(f"- first_item: `{first_item.get('title', '')}`")
            lines.append(f"- first_keyword: `{first_item.get('keyword', '')}`")
        else:
            lines.append("- first_item: 없음")
        lines.append("")
        for item in channel.get("items", []):
            lines.append(
                f"- `{item.get('keyword', '')}`: {item.get('title', '')} / {item.get('inventory_type', '')} / score {item.get('priority_score', '')} / quality={item.get('quality_pass', False)} / freshness=`{item.get('freshness_status', '')}` / user_confirmed={item.get('approved_for_upload', False)}"
            )
        if not channel.get("items"):
            lines.append("- 사용자 최종 확인을 마친 업로드 후보가 아직 없습니다.")
        lines.append("")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def main() -> int:
    report = build_report()
    OUTPUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    write_markdown(report)
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
