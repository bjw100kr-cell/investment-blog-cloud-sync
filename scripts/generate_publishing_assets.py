#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path
from urllib.parse import quote_plus


ROOT = Path(__file__).resolve().parents[1]
RULES_JSON = ROOT / "config/publishing_rules.json"
PLAYBOOK_JSON = ROOT / "config/monetization_playbook.json"
SAFE_IMAGE_RULES_JSON = ROOT / "config/safe_image_rules.json"
DEFAULT_PACKETS_JSON = ROOT / "outputs/latest/draft-packets.json"
DEFAULT_CALENDAR_JSON = ROOT / "outputs/latest/editorial-calendar.json"
DEFAULT_SEO_BACKLOG_JSON = ROOT / "outputs/latest/seo-backlog.json"
DEFAULT_OUTPUT_JSON = ROOT / "outputs/latest/publishing-assets.json"
DEFAULT_OUTPUT_MD = ROOT / "outputs/latest/publishing-assets.md"
STABLE_SLUG_BY_KEYWORD = {
    "fomc": "fomc-이후-시장-해설",
    "bitcoin": "비트코인-핵심-흐름-해설",
    "us_index_flow": "미국-증시-지수-흐름-해설",
    "china": "중국-변수와-시장-영향-해설",
}


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


def stable_slug(keyword: str, source_keyword: str, title: str) -> str:
    return STABLE_SLUG_BY_KEYWORD.get(keyword) or slugify(title)


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


def provider_search_url(provider: dict, query: str) -> str:
    return provider.get("search_url_template", "").replace("{query}", quote_plus(query))


def image_query(source_keyword: str, category: str, slot: str, image_rules: dict) -> str:
    keyword_override = image_rules.get("keyword_overrides", {}).get(source_keyword, {})
    if keyword_override.get(slot):
        return keyword_override[slot]
    category_queries = image_rules.get("category_query_presets", {}).get(category, {})
    if category_queries.get(slot):
        return category_queries[slot]
    return image_rules.get("category_query_presets", {}).get("default", {}).get(slot, "finance abstract")


def build_image_plan(source_keyword: str, category: str, title_topic: str, image_rules: dict) -> list[dict]:
    provider_order = image_rules.get("provider_priority_by_category", {}).get(
        category,
        image_rules.get("provider_priority_by_category", {}).get("default", ["unsplash", "pexels"]),
    )
    providers = image_rules.get("providers", {})
    slot_labels = image_rules.get("slot_labels", {})
    slot_notes = image_rules.get("slot_notes", {})
    plans = []

    for index, slot in enumerate(["hero", "inline"]):
        provider_key = provider_order[min(index, len(provider_order) - 1)]
        provider = providers.get(provider_key, {})
        query = image_query(source_keyword, category, slot, image_rules)
        alt_text = (
            f"{title_topic} 내용을 설명하는 대표 금융 분위기 이미지"
            if slot == "hero"
            else f"{title_topic} 설명을 보조하는 데이터 또는 산업 분위기 이미지"
        )
        plans.append(
            {
                "slot": slot,
                "slot_label": slot_labels.get(slot, slot),
                "placement_note": slot_notes.get(slot, ""),
                "provider_key": provider_key,
                "provider_name": provider.get("display_name", provider_key),
                "license_label": provider.get("license_label", ""),
                "license_url": provider.get("license_url", ""),
                "search_query": query,
                "search_url": provider_search_url(provider, query),
                "alt_text": alt_text,
                "caption_guidance": "출처 표기를 남기고 시장 흐름 설명을 보조하는 분위기 컷으로 사용",
                "selected_url": "",
                "selected_credit": "",
                "selected_photographer": "",
                "approved": False
            }
        )
    return plans


def build_asset(
    packet: dict,
    rules: dict,
    calendar_lookup: dict,
    playbook: dict,
    followup_lookup: dict[str, list[dict]],
    image_rules: dict,
) -> dict:
    keyword = packet["keyword"]
    source_keyword = packet.get("source_keyword", keyword)
    category = rules["category_by_keyword"].get(source_keyword, rules["category_by_keyword"].get(keyword, "macro"))
    title = packet["recommended_title"]
    title_topic = normalize_title_topic(title)
    slug = stable_slug(keyword, source_keyword, title)
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
    image_plan = build_image_plan(source_keyword, category, title_topic, image_rules)

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
        "image_plan": image_plan,
        "image_usage_checklist": image_rules.get("usage_checklist", []),
        "image_blocked_subjects": image_rules.get("blocked_subjects", []),
        "image_manual_review_required": True,
    }


def main() -> int:
    args = parse_args()
    packets = load_json(args.packets_json)
    calendar = load_json(args.calendar_json)
    rules = load_json(RULES_JSON)
    playbook = load_json(PLAYBOOK_JSON)
    image_rules = load_json(SAFE_IMAGE_RULES_JSON)
    seo_backlog = load_json(args.seo_backlog_json)
    calendar_lookup = build_calendar_lookup(calendar)
    followup_lookup = build_followup_lookup(seo_backlog)

    items = [
        build_asset(packet, rules, calendar_lookup, playbook, followup_lookup, image_rules)
        for packet in packets.get("packets", [])
    ]
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
        if item.get("image_plan"):
            image_summary = ", ".join(
                f"{image['slot_label']}({image['provider_name']} / {image['search_query']})"
                for image in item["image_plan"]
            )
            lines.append(f"- 이미지 추천: {image_summary}")
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
