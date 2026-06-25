#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RULES_JSON = ROOT / "config/publishing_rules.json"
PLAYBOOK_JSON = ROOT / "config/monetization_playbook.json"
DEFAULT_PACKETS_JSON = ROOT / "outputs/latest/draft-packets.json"
DEFAULT_CALENDAR_JSON = ROOT / "outputs/latest/editorial-calendar.json"
DEFAULT_SEO_BACKLOG_JSON = ROOT / "outputs/latest/seo-backlog.json"
DEFAULT_OUTPUT_JSON = ROOT / "outputs/latest/publishing-assets.json"
DEFAULT_OUTPUT_MD = ROOT / "outputs/latest/publishing-assets.md"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate publishing asset metadata from draft packets.")
    parser.add_argument("--packets-json", type=Path, default=DEFAULT_PACKETS_JSON, help="Source draft packets JSON file.")
    parser.add_argument("--calendar-json", type=Path, default=DEFAULT_CALENDAR_JSON, help="Editorial calendar JSON file.")
    parser.add_argument("--seo-backlog-json", type=Path, default=DEFAULT_SEO_BACKLOG_JSON, help="SEO backlog JSON file.")
    parser.add_argument("--output-json", type=Path, default=DEFAULT_OUTPUT_JSON, help="Output publishing assets JSON file.")
    parser.add_argument("--output-md", type=Path, default=DEFAULT_OUTPUT_MD, help="Output publishing assets markdown report.")
    return parser.parse_args()


def slugify(text: str) -> str:
    text = text.lower()
    parts = []
    for ch in text:
        if ch.isalnum():
            parts.append(ch)
        elif ch in {" ", "-", "_", "·", ":", ","}:
            parts.append("-")
    slug = "".join(parts)
    slug = re.sub(r"-{2,}", "-", slug).strip("-")
    return slug or "post"


def dedupe(items: list[str]) -> list[str]:
    seen = set()
    out = []
    for item in items:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out


def normalize_title_topic(title: str) -> str:
    topic = title.strip()
    for suffix in [" 해설", " 정리", " 분석"]:
        if topic.endswith(suffix):
            topic = topic[: -len(suffix)].strip()
    return topic or title


def build_calendar_lookup(calendar: dict) -> dict[str, dict]:
    lookup = {}
    for item in calendar.get("schedule", []):
        target = item.get("target_keyword", "")
        if target and target not in lookup:
            lookup[target] = item
        for source_keyword in item.get("source_basis", []):
            if source_keyword and source_keyword not in lookup:
                lookup[source_keyword] = item
    return lookup


def build_followup_lookup(seo_backlog: dict) -> dict[str, list[dict]]:
    lookup: dict[str, list[dict]] = {}
    for item in seo_backlog.get("items", []):
        source_keyword = item.get("source_keyword", "")
        if not source_keyword:
            continue
        lookup.setdefault(source_keyword, []).append(item)
    return lookup


def build_followup_posts(keyword: str, title: str, followup_lookup: dict[str, list[dict]]) -> list[dict]:
    items = []
    for item in followup_lookup.get(keyword, [])[:3]:
        if item.get("title") == title:
            continue
        items.append(
            {
                "title": item.get("title", ""),
                "slug": item.get("slug", ""),
                "role": item.get("role", ""),
                "post_type": item.get("post_type", ""),
                "search_intent": item.get("search_intent", ""),
                "monetization_goal": item.get("monetization_goal", ""),
                "cta_focus": item.get("cta_focus", ""),
            }
        )
    return items


def build_asset(packet: dict, rules: dict, calendar_lookup: dict, playbook: dict, followup_lookup: dict[str, list[dict]]) -> dict:
    keyword = packet["keyword"]
    source_keyword = packet.get("source_keyword", keyword)
    category = rules["category_by_keyword"].get(source_keyword, rules["category_by_keyword"].get(keyword, "macro"))
    title = packet["recommended_title"]
    title_topic = normalize_title_topic(title)
    slug = slugify(title)
    labels = dedupe(rules["base_labels"] + rules["keyword_labels"].get(source_keyword, rules["keyword_labels"].get(keyword, [])))
    meta_template = rules["meta_description_templates"].get(category, "{title}를 투자자 관점에서 쉽게 정리합니다.")
    meta_description = meta_template.format(title=title_topic)
    calendar_entry = calendar_lookup.get(keyword, calendar_lookup.get(source_keyword, {}))
    publish_date = calendar_entry.get("date", "")
    internal_links = [
        rules["category_hub_paths"].get(category, ""),
        "site-foundation/about.md",
        "site-foundation/disclosure.md",
        "site-foundation/privacy-policy.md",
        "site-foundation/editorial-policy.md",
    ]
    internal_links = [item for item in internal_links if item]
    post_type = calendar_entry.get("post_type", "breaking_explainer")
    ad_slots = playbook.get("ad_slot_recommendations_by_post_type", {}).get(
        post_type,
        ["after_intro", "mid_article", "before_related_links"],
    )
    follow_up_posts = build_followup_posts(source_keyword, title, followup_lookup)

    return {
        "keyword": keyword,
        "source_keyword": source_keyword,
        "category": category,
        "title": title,
        "title_topic": title_topic,
        "slug": slug,
        "meta_title": title[:60],
        "meta_description": meta_description[:155],
        "labels": labels,
        "recommended_publish_date": publish_date,
        "internal_links": internal_links,
        "ad_slot_recommendations": ad_slots,
        "follow_up_posts": follow_up_posts,
        "cta": packet.get("cta", ""),
        "trust_footer_note": rules["trust_footer_note"],
        "summary_angle": packet.get("summary_angle", ""),
    }


def main() -> int:
    args = parse_args()
    packets = load_json(args.packets_json)
    calendar = load_json(args.calendar_json)
    rules = load_json(RULES_JSON)
    playbook = load_json(PLAYBOOK_JSON)
    seo_backlog = load_json(args.seo_backlog_json)
    calendar_lookup = build_calendar_lookup(calendar)
    followup_lookup = build_followup_lookup(seo_backlog)

    items = [build_asset(packet, rules, calendar_lookup, playbook, followup_lookup) for packet in packets.get("packets", [])]
    payload = {
        "generated_at": packets.get("generated_at"),
        "packets_json": str(args.packets_json),
        "items": items,
    }
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_md.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(payload, ensure_ascii=False, indent=2))

    lines = []
    lines.append("# 퍼블리싱 자산")
    lines.append("")
    lines.append(f"- 생성 시각: `{payload['generated_at']}`")
    lines.append("")
    for idx, item in enumerate(items, start=1):
        lines.append(f"## {idx}. {item['keyword']}")
        lines.append("")
        lines.append(f"- 제목: {item['title']}")
        lines.append(f"- slug: `{item['slug']}`")
        lines.append(f"- meta title: {item['meta_title']}")
        lines.append(f"- meta description: {item['meta_description']}")
        lines.append(f"- 카테고리: {item['category']}")
        lines.append(f"- 추천 발행일: {item['recommended_publish_date'] or '미정'}")
        lines.append(f"- labels: {', '.join(item['labels'])}")
        lines.append(f"- 내부링크: {', '.join(item['internal_links'])}")
        if item.get("follow_up_posts"):
            lines.append(f"- 후속 글 후보: {', '.join(post['title'] for post in item['follow_up_posts'])}")
        lines.append(f"- 광고 슬롯: {', '.join(item['ad_slot_recommendations'])}")
        lines.append(f"- CTA: {item['cta']}")
        lines.append(f"- 신뢰 메모: {item['trust_footer_note']}")
        lines.append("")

    args.output_md.write_text("\n".join(lines).strip() + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
