#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PUBLISH_INVENTORY_JSON = ROOT / "outputs/latest/publish-inventory.json"
OUTPUT_JSON = ROOT / "outputs/latest/distribution-pack.json"
OUTPUT_MD = ROOT / "outputs/latest/distribution-pack.md"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def short_role(role: str) -> str:
    mapping = {
        "breaking_primary": "속보형",
        "breaking_secondary": "보완형",
        "weekly_recap": "주간정리형",
        "evergreen_seo": "검색형",
        "follow_up": "후속형",
    }
    return mapping.get(role, role or "일반형")


def build_snippets(item: dict) -> dict:
    title = item.get("title", "")
    search_intent = item.get("search_intent", "")
    cta_focus = item.get("cta_focus", "")
    revenue_objective = item.get("revenue_objective", "")
    role_label = short_role(item.get("role", ""))

    x_post = (
        f"{title}\n\n"
        f"오늘 시장을 볼 때 핵심은 이것입니다.\n"
        f"- 독자 관점: {search_intent}\n"
        f"- 한 줄 포인트: {cta_focus}\n\n"
        f"짧고 이해하기 쉽게 정리했습니다."
    )
    telegram_post = (
        f"[{role_label}] {title}\n"
        f"오늘 체크해야 할 흐름을 초보자도 이해하기 쉽게 정리했습니다.\n"
        f"핵심 포인트: {cta_focus}"
    )
    community_post = (
        f"{title}\n\n"
        f"이번 글은 '{search_intent}'에 맞춰 정리한 해설입니다. "
        f"읽고 나면 {cta_focus} 흐름까지 같이 이어서 보기 좋게 설계했습니다."
    )
    newsletter_subject = f"[오늘의 투자 브리핑] {title}"
    newsletter_preview = f"{revenue_objective} 관점에서 꼭 봐야 할 포인트를 짧게 정리했습니다."

    return {
        "hook_line": f"{title} | {search_intent}",
        "x_post": x_post,
        "telegram_post": telegram_post,
        "community_post": community_post,
        "newsletter_subject": newsletter_subject,
        "newsletter_preview": newsletter_preview,
    }


def build_pack() -> dict:
    inventory = load_json(PUBLISH_INVENTORY_JSON)
    items = []
    for entry in inventory.get("items", []):
        if not entry.get("ready_to_upload"):
            continue
        snippets = build_snippets(entry)
        items.append(
            {
                "inventory_sequence": entry.get("inventory_sequence"),
                "inventory_type": entry.get("inventory_type"),
                "keyword": entry.get("keyword"),
                "source_keyword": entry.get("source_keyword"),
                "title": entry.get("title"),
                "publish_bucket": entry.get("publish_bucket"),
                "priority_score": entry.get("priority_score"),
                "snippets": snippets,
            }
        )
    return {
        "generated_at": inventory.get("generated_at", ""),
        "item_count": len(items),
        "items": items,
    }


def write_markdown(pack: dict) -> None:
    lines = []
    lines.append("# Distribution Pack")
    lines.append("")
    lines.append(f"- item_count: `{pack.get('item_count', 0)}`")
    lines.append("")
    for item in pack.get("items", []):
        lines.append(f"## {item.get('inventory_sequence')}. {item.get('title')}")
        lines.append("")
        lines.append(f"- inventory_type: `{item.get('inventory_type')}`")
        lines.append(f"- publish_bucket: `{item.get('publish_bucket')}`")
        lines.append(f"- priority_score: `{item.get('priority_score')}`")
        lines.append(f"- hook_line: {item.get('snippets', {}).get('hook_line', '')}")
        lines.append("")
        lines.append("### X / Threads")
        lines.append("")
        lines.append(item.get("snippets", {}).get("x_post", ""))
        lines.append("")
        lines.append("### Telegram / Kakao Channel")
        lines.append("")
        lines.append(item.get("snippets", {}).get("telegram_post", ""))
        lines.append("")
        lines.append("### Community")
        lines.append("")
        lines.append(item.get("snippets", {}).get("community_post", ""))
        lines.append("")
        lines.append("### Newsletter")
        lines.append("")
        lines.append(f"- subject: {item.get('snippets', {}).get('newsletter_subject', '')}")
        lines.append(f"- preview: {item.get('snippets', {}).get('newsletter_preview', '')}")
        lines.append("")
    OUTPUT_MD.write_text("\n".join(lines))


def main() -> int:
    pack = build_pack()
    OUTPUT_JSON.write_text(json.dumps(pack, ensure_ascii=False, indent=2))
    write_markdown(pack)
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
