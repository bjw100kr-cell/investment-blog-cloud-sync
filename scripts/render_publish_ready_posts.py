#!/usr/bin/env python3
import argparse
import json
import os
from datetime import datetime, timezone
from html import escape
from pathlib import Path

import markdown


ROOT = Path(__file__).resolve().parents[1]
RENDER_CONFIG_JSON = ROOT / "config/blog_rendering.json"
DEFAULT_PACKETS_JSON = ROOT / "outputs/latest/draft-packets.json"
DEFAULT_PUBLISHING_JSON = ROOT / "outputs/latest/publishing-assets.json"
DEFAULT_DRAFTS_DIR = ROOT / "outputs/latest/drafts"
DEFAULT_OUTPUT_DIR = ROOT / "outputs/latest/publish-ready"
DEFAULT_OUTPUT_JSON = ROOT / "outputs/latest/publish-ready-report.json"
DEFAULT_OUTPUT_MD = ROOT / "outputs/latest/publish-ready-report.md"


def slugify(text: str) -> str:
    out = []
    for ch in text.lower():
        if ch.isalnum():
            out.append(ch)
        elif ch in {" ", "-", "_"}:
            out.append("-")
    slug = "".join(out).strip("-")
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug or "draft"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render publish-ready HTML documents from generated drafts and publishing assets.")
    parser.add_argument("--packets-json", type=Path, default=DEFAULT_PACKETS_JSON, help="Draft packets JSON file.")
    parser.add_argument("--publishing-json", type=Path, default=DEFAULT_PUBLISHING_JSON, help="Publishing assets JSON file.")
    parser.add_argument("--drafts-dir", type=Path, default=DEFAULT_DRAFTS_DIR, help="Directory containing markdown drafts.")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR, help="Directory to write publish-ready HTML and manifests.")
    parser.add_argument("--output-json", type=Path, default=DEFAULT_OUTPUT_JSON, help="Publish-ready report JSON path.")
    parser.add_argument("--output-md", type=Path, default=DEFAULT_OUTPUT_MD, help="Publish-ready report markdown path.")
    return parser.parse_args()


def resolve_link(link: str, base_url: str, link_map: dict) -> str:
    target = link_map.get(link, link)
    if target.startswith("http://") or target.startswith("https://"):
        return target
    if not base_url:
        return target
    return f"{base_url.rstrip('/')}{target}"


def extract_title_and_body(markdown_text: str, fallback: str) -> tuple[str, str]:
    lines = markdown_text.splitlines()
    title = fallback
    body_lines = lines
    for idx, line in enumerate(lines):
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            title = stripped.lstrip("#").strip()
            body_lines = lines[idx + 1 :]
        else:
            title = stripped[:120]
            body_lines = lines[idx + 1 :]
        break
    body = "\n".join(body_lines).strip()
    return title, body


def markdown_to_html(text: str) -> str:
    return markdown.markdown(text, extensions=["extra", "nl2br", "tables"])


def replace_first(text: str, old: str, new: str) -> str:
    if old not in text:
        return text
    return text.replace(old, new, 1)


def resolve_canonical_url(base_url: str, slug: str) -> str:
    if not base_url:
        return ""
    return f"{base_url.rstrip('/')}/{slug}.html"


def extract_faq_items(markdown_text: str) -> list[dict]:
    lines = markdown_text.splitlines()
    items = []
    current_question = ""
    current_answer: list[str] = []

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("### "):
            if current_question and current_answer:
                items.append(
                    {
                        "question": current_question,
                        "answer": " ".join(part.strip() for part in current_answer if part.strip()),
                    }
                )
            current_question = stripped[4:].strip()
            current_answer = []
            continue
        if current_question:
            if stripped.startswith("## "):
                if current_answer:
                    items.append(
                        {
                            "question": current_question,
                            "answer": " ".join(part.strip() for part in current_answer if part.strip()),
                        }
                    )
                current_question = ""
                current_answer = []
                continue
            if stripped:
                current_answer.append(stripped)

    if current_question and current_answer:
        items.append(
            {
                "question": current_question,
                "answer": " ".join(part.strip() for part in current_answer if part.strip()),
            }
        )

    return items


def render_fact_check_box(packet: dict) -> str:
    fact_checks = packet.get("fact_checks", [])
    source_names = packet.get("source_names", [])
    if not fact_checks and not source_names:
        return ""

    parts = ["<section class='post-fact-check'><h2>발행 전 확인 포인트</h2>"]
    if source_names:
        parts.append(f"<p><strong>참고 소스</strong>: {escape(', '.join(source_names))}</p>")
    if fact_checks:
        items = "".join(f"<li>{escape(item)}</li>" for item in fact_checks)
        parts.append(f"<ul>{items}</ul>")
    parts.append("</section>")
    return "".join(parts)


def render_newsletter_box(config: dict, subscribe_url: str) -> str:
    if not subscribe_url:
        return ""
    return (
        "<section class='post-newsletter-cta'>"
        f"<h2>{escape(config.get('newsletter_heading', '다음 흐름도 이어서 받고 싶다면'))}</h2>"
        f"<p>{escape(config.get('newsletter_description', '업데이트를 이어서 받아볼 수 있는 구독 동선입니다.'))}</p>"
        f"<p><a class='newsletter-button' href=\"{escape(subscribe_url)}\">{escape(config.get('newsletter_button_label', '업데이트 받기'))}</a></p>"
        "</section>"
    )


def render_ad_slot(slot_name: str, config: dict, adsense_publisher_id: str) -> str:
    label_map = config.get("ad_slot_labels", {})
    label = label_map.get(slot_name, slot_name)
    publisher_attr = f" data-adsense-publisher=\"{escape(adsense_publisher_id)}\"" if adsense_publisher_id else ""
    status = "active" if adsense_publisher_id else "placeholder"
    return (
        f"<section class='post-ad-slot' data-slot=\"{escape(slot_name)}\" data-status=\"{status}\"{publisher_attr}>"
        f"<p>광고 슬롯: {escape(label)}</p>"
        "</section>"
    )


def inject_ad_slots(body_html: str, ad_slots: list[str], config: dict, adsense_publisher_id: str) -> str:
    updated = body_html
    for slot in ad_slots:
        snippet = render_ad_slot(slot, config, adsense_publisher_id)
        if slot == "after_intro":
            updated = replace_first(updated, "</p>\n<h2>본문</h2>", f"</p>{snippet}\n<h2>본문</h2>")
        elif slot == "mid_article":
            updated = replace_first(updated, "<h2>4. 앞으로 체크할 변수</h2>", f"{snippet}<h2>4. 앞으로 체크할 변수</h2>")
        elif slot == "before_related_links":
            updated = f"{updated}{snippet}"
        elif slot == "before_faq":
            updated = replace_first(updated, "<h2>FAQ 2개</h2>", f"{snippet}<h2>FAQ 2개</h2>")
        elif slot == "after_supply_chain_section":
            updated = replace_first(updated, "<h2>4. 거시 변수와 연결</h2>", f"{snippet}<h2>4. 거시 변수와 연결</h2>")
        else:
            updated = f"{updated}{snippet}"
    return updated


def render_analytics_meta(ga4_measurement_id: str, canonical_url: str, title: str, category: str) -> str:
    if not ga4_measurement_id:
        return ""
    payload = {
        "ga4_measurement_id": ga4_measurement_id,
        "page_title": title,
        "page_category": category,
        "canonical_url": canonical_url,
    }
    return f"<script type='application/json' class='ga4-page-meta'>{json.dumps(payload, ensure_ascii=False)}</script>"


def build_structured_data(
    config: dict,
    title: str,
    asset: dict,
    canonical_url: str,
    publish_date: str,
    faq_items: list[dict],
) -> str:
    blog_posting = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": title,
        "description": asset.get("meta_description", ""),
        "datePublished": publish_date,
        "dateModified": publish_date,
        "author": {
            "@type": "Organization",
            "name": config.get("author_name", ""),
        },
        "publisher": {
            "@type": "Organization",
            "name": config.get("site_name", ""),
        },
        "keywords": asset.get("labels", []),
        "articleSection": asset.get("category", ""),
    }
    if canonical_url:
        blog_posting["url"] = canonical_url

    graph = [blog_posting]

    if faq_items:
        graph.append(
            {
                "@context": "https://schema.org",
                "@type": "FAQPage",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": item["question"],
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": item["answer"],
                        },
                    }
                    for item in faq_items
                ],
            }
        )

    return f"<script type='application/ld+json'>{json.dumps(graph, ensure_ascii=False)}</script>"


def render_author_box(config: dict, publish_date: str) -> str:
    return (
        f"<section class='post-author-box'>"
        f"<h2>{config['author_box_heading']}</h2>"
        f"<p><strong>{config['author_name']}</strong> · {config['author_role']}</p>"
        f"<p>발행 기준일: {publish_date}</p>"
        f"</section>"
    )


def render_related_links(config: dict, links: list[dict]) -> str:
    if not links:
        return ""
    items = "".join(f"<li><a href=\"{item['url']}\">{item['label']}</a></li>" for item in links)
    return f"<section class='post-related-links'><h2>{config['related_heading']}</h2><ul>{items}</ul></section>"


def render_follow_up_posts(config: dict, posts: list[dict], base_url: str) -> str:
    if not posts:
        return ""
    items = []
    for post in posts:
        slug = post.get("slug", "")
        title = post.get("title", "")
        href = f"{base_url.rstrip('/')}/{slug}.html" if base_url and slug else ""
        intent = post.get("search_intent", "")
        role = post.get("role", "")
        intent_html = f"<p>{escape(intent)}</p>" if intent else ""
        meta_bits = [bit for bit in [role, "발행 예정"] if bit]
        meta_html = f"<p class='follow-up-meta'>{escape(' · '.join(meta_bits))}</p>" if meta_bits else ""
        if href:
            items.append(f"<li><a href=\"{escape(href)}\">{escape(title)}</a>{meta_html}{intent_html}</li>")
        else:
            items.append(f"<li><strong>{escape(title)}</strong>{meta_html}{intent_html}</li>")
    return f"<section class='post-follow-up-links'><h2>{config.get('follow_up_heading', '이어서 준비 중인 글')}</h2><ul>{''.join(items)}</ul></section>"


def build_related_links(asset: dict, config: dict, base_url: str) -> list[dict]:
    link_map = config.get("internal_link_url_map", {})
    links = []
    for link in asset.get("internal_links", []):
        links.append(
            {
                "label": Path(link).stem.replace("-", " "),
                "url": resolve_link(link, base_url, link_map),
            }
        )
    return links


def render_html_document(
    config: dict,
    title: str,
    summary_angle: str,
    body_html: str,
    asset: dict,
    packet: dict,
    related_links: list[dict],
    follow_up_posts: list[dict],
    canonical_url: str,
    faq_items: list[dict],
    newsletter_url: str,
    adsense_publisher_id: str,
    ga4_measurement_id: str,
    ad_slots: list[str],
) -> str:
    publish_date = asset.get("recommended_publish_date") or datetime.now(timezone.utc).date().isoformat()
    tags = ", ".join(asset.get("labels", []))
    author_box = render_author_box(config, publish_date)
    related = render_related_links(config, related_links)
    follow_up = render_follow_up_posts(config, follow_up_posts, canonical_url.rsplit("/", 1)[0] if canonical_url else "")
    fact_check_box = render_fact_check_box(packet)
    newsletter_box = render_newsletter_box(config, newsletter_url)
    body_with_ads = inject_ad_slots(body_html, ad_slots, config, adsense_publisher_id)
    disclosure = (
        f"<section class='post-disclosure'><h2>{config['disclosure_heading']}</h2>"
        f"<p>{asset.get('trust_footer_note', '')}</p></section>"
    )
    canonical_meta = f"<p class='post-canonical'>원문 기준 주소: <a href=\"{canonical_url}\">{canonical_url}</a></p>" if canonical_url else ""
    structured_data = build_structured_data(config, title, asset, canonical_url, publish_date, faq_items)
    analytics_meta = render_analytics_meta(ga4_measurement_id, canonical_url, title, asset.get("category", ""))
    return (
        f"{structured_data}{analytics_meta}<article class='investment-post'>"
        f"<header class='post-header'><h1>{title}</h1>"
        f"<p class='post-summary'>{summary_angle}</p>"
        f"<p class='post-top-notice'>{config['top_notice']}</p>"
        f"<p class='post-meta'>카테고리: {asset.get('category', '')} · 라벨: {tags}</p>"
        f"{canonical_meta}</header>"
        f"{author_box}"
        f"{fact_check_box}"
        f"<section class='post-body'>{body_with_ads}</section>"
        f"{newsletter_box}"
        f"{follow_up}"
        f"{related}"
        f"{disclosure}"
        "</article>"
    )


def main() -> int:
    args = parse_args()
    packets = load_json(args.packets_json).get("packets", [])
    publishing_items = load_json(args.publishing_json).get("items", [])
    config = load_json(RENDER_CONFIG_JSON)
    args.output_dir.mkdir(parents=True, exist_ok=True)

    base_url = os.getenv("BLOG_BASE_URL", config.get("default_base_url", "")).strip()
    newsletter_url = os.getenv("NEWSLETTER_SUBSCRIBE_URL", "").strip()
    adsense_publisher_id = os.getenv("ADSENSE_PUBLISHER_ID", "").strip()
    ga4_measurement_id = os.getenv("GA4_MEASUREMENT_ID", "").strip()
    packet_lookup = {packet["keyword"]: packet for packet in packets}
    rendered_items = []

    for idx, asset in enumerate(publishing_items, start=1):
        keyword = asset["keyword"]
        draft_path = args.drafts_dir / f"{idx:02d}-{slugify(keyword)}.md"
        html_path = args.output_dir / f"{idx:02d}-{asset['slug']}.html"
        manifest_path = args.output_dir / f"{idx:02d}-{asset['slug']}.json"
        item_payload = {
            "keyword": keyword,
            "title": asset["title"],
            "slug": asset["slug"],
            "meta_title": asset["meta_title"],
            "meta_description": asset["meta_description"],
            "labels": asset.get("labels", []),
            "category": asset.get("category", ""),
            "recommended_publish_date": asset.get("recommended_publish_date", ""),
            "html_path": str(html_path),
            "manifest_path": str(manifest_path),
            "draft_path": str(draft_path),
            "ready": False,
            "reason": "",
        }

        if not draft_path.exists():
            item_payload["reason"] = "draft_file_missing"
            manifest_path.write_text(json.dumps(item_payload, ensure_ascii=False, indent=2))
            rendered_items.append(item_payload)
            continue

        markdown_text = draft_path.read_text()
        if markdown_text.startswith("# Draft not generated"):
            item_payload["reason"] = "draft_not_generated"
            manifest_path.write_text(json.dumps(item_payload, ensure_ascii=False, indent=2))
            rendered_items.append(item_payload)
            continue

        packet = packet_lookup.get(keyword, {})
        title, body_md = extract_title_and_body(markdown_text, asset["title"])
        body_html = markdown_to_html(body_md)
        related_links = build_related_links(asset, config, base_url)
        follow_up_posts = asset.get("follow_up_posts", [])
        canonical_url = resolve_canonical_url(base_url, asset["slug"])
        faq_items = extract_faq_items(markdown_text)
        ad_slots = asset.get("ad_slot_recommendations", [])
        full_html = render_html_document(
            config,
            title,
            asset.get("summary_angle", ""),
            body_html,
            asset,
            packet,
            related_links,
            follow_up_posts,
            canonical_url,
            faq_items,
            newsletter_url,
            adsense_publisher_id,
            ga4_measurement_id,
            ad_slots,
        )

        item_payload.update(
            {
                "ready": True,
                "reason": "ok",
                "author_name": config.get("author_name", ""),
                "related_links": related_links,
                "follow_up_posts": follow_up_posts,
                "cta": asset.get("cta", ""),
                "summary_angle": asset.get("summary_angle", ""),
                "voice_profile": packet.get("voice_profile", ""),
                "trust_footer_note": asset.get("trust_footer_note", ""),
                "canonical_url": canonical_url,
                "structured_data_types": ["BlogPosting"] + (["FAQPage"] if faq_items else []),
                "newsletter_enabled": bool(newsletter_url),
                "adsense_enabled": bool(adsense_publisher_id),
                "ga4_enabled": bool(ga4_measurement_id),
                "ad_slot_recommendations": ad_slots,
            }
        )
        html_path.write_text(full_html)
        manifest_path.write_text(json.dumps(item_payload, ensure_ascii=False, indent=2))
        rendered_items.append(item_payload)

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "base_url": base_url,
        "packets_json": str(args.packets_json),
        "publishing_json": str(args.publishing_json),
        "items": rendered_items,
    }
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_md.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(report, ensure_ascii=False, indent=2))

    lines = []
    lines.append("# Publish Ready Report")
    lines.append("")
    lines.append(f"- generated_at: `{report['generated_at']}`")
    lines.append("")
    for item in rendered_items:
        lines.append(f"## {item['keyword']}")
        lines.append("")
        lines.append(f"- ready: {item['ready']}")
        lines.append(f"- reason: {item['reason']}")
        lines.append(f"- html_path: {item['html_path']}")
        lines.append(f"- meta_title: {item['meta_title']}")
        lines.append(f"- meta_description: {item['meta_description']}")
        lines.append(f"- follow_up_post_count: {len(item.get('follow_up_posts', []))}")
        lines.append("")
    args.output_md.write_text("\n".join(lines).strip() + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
