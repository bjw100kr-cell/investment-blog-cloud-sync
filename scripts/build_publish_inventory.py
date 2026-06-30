#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PUBLISH_QUEUE_JSON = ROOT / "outputs/latest/publish-queue.json"
SEO_PUBLISH_READY_JSON = ROOT / "outputs/latest/seo-publish-ready-report.json"
SEO_BACKLOG_JSON = ROOT / "outputs/latest/seo-backlog.json"
PUBLISH_READY_REPORT_JSON = ROOT / "outputs/latest/publish-ready-report.json"
OUTPUT_JSON = ROOT / "outputs/latest/publish-inventory.json"
OUTPUT_MD = ROOT / "outputs/latest/publish-inventory.md"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def build_seo_backlog_lookup(seo_backlog: dict) -> dict:
    return {item.get("title"): item for item in seo_backlog.get("items", [])}


def build_main_items(publish_queue: dict) -> list[dict]:
    items = []
    for item in publish_queue.get("items", []):
        items.append(
            {
                "inventory_type": "main_post",
                "keyword": item.get("keyword", ""),
                "source_keyword": item.get("keyword", ""),
                "title": item.get("title", ""),
                "role": item.get("role", ""),
                "post_type": item.get("post_type", ""),
                "ready_to_upload": bool(item.get("ready_to_upload")),
                "recommended_publish_date": item.get("recommended_publish_date", ""),
                "publish_bucket": item.get("publish_bucket", ""),
                "priority_score": item.get("publish_priority_score", 0),
                "search_intent": item.get("search_intent", ""),
                "revenue_objective": item.get("revenue_objective", ""),
                "cta_focus": item.get("cta_focus", ""),
                "html_path": item.get("html_path", ""),
                "manifest_path": item.get("manifest_path", ""),
                "upload_sequence_hint": item.get("upload_sequence", 999),
            }
        )
    return items


def build_seo_items(seo_publish_ready: dict, seo_lookup: dict) -> list[dict]:
    items = []
    for index, item in enumerate(seo_publish_ready.get("items", []), start=1):
        backlog = seo_lookup.get(item.get("title", ""), {})
        items.append(
            {
                "inventory_type": "seo_followup",
                "keyword": item.get("keyword", ""),
                "source_keyword": backlog.get("source_keyword", item.get("source_keyword", "")),
                "title": item.get("title", ""),
                "role": backlog.get("role", ""),
                "post_type": backlog.get("post_type", ""),
                "ready_to_upload": bool(item.get("ready")),
                "recommended_publish_date": item.get("recommended_publish_date", ""),
                "publish_bucket": "seo_backlog",
                "priority_score": backlog.get("priority_score", 0),
                "search_intent": backlog.get("search_intent", ""),
                "revenue_objective": backlog.get("monetization_goal", ""),
                "cta_focus": backlog.get("cta_focus", ""),
                "html_path": item.get("html_path", ""),
                "manifest_path": item.get("manifest_path", ""),
                "upload_sequence_hint": 100 + index,
            }
        )
    return items


def inventory_sort_key(item: dict) -> tuple:
    inventory_rank = 0 if item.get("inventory_type") == "main_post" else 1
    ready_rank = 0 if item.get("ready_to_upload") else 1
    bucket_rank = {
        "today_or_overdue": 0,
        "tomorrow": 1,
        "this_week": 2,
        "later": 3,
        "seo_backlog": 4,
    }.get(item.get("publish_bucket"), 9)
    return (
        ready_rank,
        inventory_rank,
        bucket_rank,
        -float(item.get("priority_score", 0)),
        item.get("title", ""),
    )


def build_inventory() -> dict:
    publish_queue = load_json(PUBLISH_QUEUE_JSON)
    seo_publish_ready = load_json(SEO_PUBLISH_READY_JSON)
    publish_ready_report = load_json(PUBLISH_READY_REPORT_JSON)
    seo_backlog = load_json(SEO_BACKLOG_JSON)
    seo_lookup = build_seo_backlog_lookup(seo_backlog)

    items = build_main_items(publish_queue) + build_seo_items(seo_publish_ready, seo_lookup)
    items.sort(key=inventory_sort_key)

    generated_at_candidates = [
        publish_queue.get("generated_at", ""),
        seo_publish_ready.get("generated_at", ""),
        publish_ready_report.get("generated_at", ""),
    ]
    generated_at = max(
        generated_at_candidates,
        key=lambda v: v or "",
    )

    for index, item in enumerate(items, start=1):
        item["inventory_sequence"] = index

    return {
        "generated_at": generated_at,
        "summary": {
            "inventory_count": len(items),
            "ready_count": sum(1 for item in items if item.get("ready_to_upload")),
            "main_post_count": sum(1 for item in items if item.get("inventory_type") == "main_post"),
            "seo_followup_count": sum(1 for item in items if item.get("inventory_type") == "seo_followup"),
        },
        "items": items,
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# 발행 재고판")
    lines.append("")
    lines.append(f"- 생성 시각: `{report.get('generated_at', '')}`")
    lines.append(f"- 전체 발행 후보: `{report.get('summary', {}).get('inventory_count', 0)}`")
    lines.append(f"- 업로드 가능 글 수: `{report.get('summary', {}).get('ready_count', 0)}`")
    lines.append(f"- 메인 글 수: `{report.get('summary', {}).get('main_post_count', 0)}`")
    lines.append(f"- SEO 후속 글 수: `{report.get('summary', {}).get('seo_followup_count', 0)}`")
    lines.append("")
    for item in report.get("items", []):
        lines.append(f"## {item['inventory_sequence']}. {item['title']}")
        lines.append("")
        lines.append(f"- inventory_type: {item['inventory_type']}")
        lines.append(f"- keyword: {item['keyword']}")
        lines.append(f"- source_keyword: {item['source_keyword']}")
        lines.append(f"- role/type: {item['role']} / {item['post_type']}")
        lines.append(f"- ready_to_upload: {item['ready_to_upload']}")
        lines.append(f"- publish_date: {item['recommended_publish_date'] or '미정'} / bucket: {item['publish_bucket']}")
        lines.append(f"- priority_score: {item['priority_score']}")
        lines.append(f"- revenue_objective: {item['revenue_objective']}")
        if item.get("search_intent"):
            lines.append(f"- search_intent: {item['search_intent']}")
        if item.get("cta_focus"):
            lines.append(f"- cta_focus: {item['cta_focus']}")
        lines.append("")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def main() -> int:
    report = build_inventory()
    OUTPUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    write_markdown(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
