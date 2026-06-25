#!/usr/bin/env python3
import json
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BRIEF_JSON = ROOT / "outputs/latest/daily-post-brief.json"
CALENDAR_JSON = ROOT / "outputs/latest/editorial-calendar.json"
PUBLISHING_JSON = ROOT / "outputs/latest/publishing-assets.json"
PUBLISH_READY_JSON = ROOT / "outputs/latest/publish-ready-report.json"
SEARCH_DEMAND_JSON = ROOT / "outputs/latest/search-demand-report.json"
PLAYBOOK_JSON = ROOT / "config/monetization_playbook.json"
OUTPUT_JSON = ROOT / "outputs/latest/publish-queue.json"
OUTPUT_MD = ROOT / "outputs/latest/publish-queue.md"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def build_brief_lookup(brief_data: dict) -> dict:
    return {item.get("keyword"): item for item in brief_data.get("top_briefs", [])}


def build_calendar_lookup(calendar_data: dict) -> dict:
    lookup = {}
    for item in calendar_data.get("schedule", []):
        target = item.get("target_keyword")
        if target and target not in lookup:
            lookup[target] = item
        for source_keyword in item.get("source_basis", []):
            if source_keyword and source_keyword not in lookup:
                lookup[source_keyword] = item
    return lookup


def build_ready_lookup(publish_ready: dict) -> dict:
    lookup = {}
    for item in publish_ready.get("items", []):
        lookup[item.get("keyword")] = item
    return lookup


def build_demand_lookup(search_demand: dict) -> dict:
    return {item.get("keyword"): item for item in search_demand.get("ranked_keyword_demand", [])}


def days_until(target_date: str) -> int:
    if not target_date:
        return 99
    try:
        y, m, d = [int(part) for part in target_date.split("-")]
        target = date(y, m, d)
    except Exception:  # noqa: BLE001
        return 99
    return (target - date.today()).days


def publish_bucket(target_date: str) -> str:
    delta = days_until(target_date)
    if delta <= 0:
        return "today_or_overdue"
    if delta == 1:
        return "tomorrow"
    if delta <= 3:
        return "this_week"
    return "later"


def queue_priority(item: dict, role_weight: int) -> float:
    brief = item.get("brief", {})
    demand = item.get("demand", {})
    ready_bonus = 5 if item.get("ready_to_upload") else -10
    date_bonus = {
        "today_or_overdue": 12,
        "tomorrow": 8,
        "this_week": 4,
        "later": 1,
    }.get(item.get("publish_bucket"), 0)
    trend_bonus = min(int(demand.get("demand_signal_score", 0)) // 250, 8)
    return round(
        float(brief.get("total_score", 0))
        + float(brief.get("monetization_score", 0))
        + role_weight
        + date_bonus
        + trend_bonus
        + ready_bonus,
        2,
    )


def build_queue() -> dict:
    brief_data = load_json(BRIEF_JSON)
    calendar_data = load_json(CALENDAR_JSON)
    publishing_data = load_json(PUBLISHING_JSON)
    publish_ready = load_json(PUBLISH_READY_JSON)
    search_demand = load_json(SEARCH_DEMAND_JSON)
    playbook = load_json(PLAYBOOK_JSON)

    brief_lookup = build_brief_lookup(brief_data)
    calendar_lookup = build_calendar_lookup(calendar_data)
    ready_lookup = build_ready_lookup(publish_ready)
    demand_lookup = build_demand_lookup(search_demand)

    role_weights = playbook.get("role_priority_weights", {})
    revenue_objectives = playbook.get("revenue_objective_by_role", {})
    cta_focus_map = playbook.get("cta_focus_by_category", {})
    ad_slots_map = playbook.get("ad_slot_recommendations_by_post_type", {})
    readiness_checklist = playbook.get("readiness_checklist", [])

    queue_items = []
    for asset in publishing_data.get("items", []):
        keyword = asset.get("keyword", "")
        brief = brief_lookup.get(keyword, {})
        schedule = calendar_lookup.get(keyword, {})
        ready = ready_lookup.get(keyword, {})
        demand = demand_lookup.get(keyword, {})
        if not demand and brief:
            demand_signal = brief.get("demand_signal_score", 0)
            if demand_signal:
                demand = {"trend_queries": brief.get("trend_queries", []), "demand_signal_score": demand_signal}
        role = schedule.get("role", "unplanned")
        post_type = schedule.get("post_type", "breaking_explainer")
        bucket = publish_bucket(asset.get("recommended_publish_date", ""))
        role_weight = int(role_weights.get(role, 3))
        item = {
            "keyword": keyword,
            "title": asset.get("title", ""),
            "slug": asset.get("slug", ""),
            "category": asset.get("category", ""),
            "recommended_publish_date": asset.get("recommended_publish_date", ""),
            "publish_bucket": bucket,
            "role": role,
            "post_type": post_type,
            "ready_to_upload": bool(ready.get("ready")),
            "html_path": ready.get("html_path", ""),
            "manifest_path": ready.get("manifest_path", ""),
            "revenue_objective": revenue_objectives.get(role, "페이지뷰와 체류시간 균형 확보"),
            "cta_focus": cta_focus_map.get(asset.get("category", ""), "관련 허브와 다음 글로 연결"),
            "ad_slot_recommendations": ad_slots_map.get(post_type, ["after_intro", "mid_article", "before_related_links"]),
            "internal_link_targets": asset.get("internal_links", []),
            "trend_queries": demand.get("trend_queries", []),
            "demand_signal_score": demand.get("demand_signal_score", 0),
            "search_intent": schedule.get("search_intent", ""),
            "publish_note": schedule.get("publish_note", ""),
            "monetization_path": schedule.get("monetization_path", ""),
            "readiness_checklist": readiness_checklist,
            "brief": brief,
            "demand": demand,
        }
        item["publish_priority_score"] = queue_priority(item, role_weight)
        queue_items.append(item)

    queue_items.sort(
        key=lambda item: (
            not item["ready_to_upload"],
            {"today_or_overdue": 0, "tomorrow": 1, "this_week": 2, "later": 3}.get(item["publish_bucket"], 9),
            -item["publish_priority_score"],
            item["keyword"],
        )
    )

    for idx, item in enumerate(queue_items, start=1):
        item["upload_sequence"] = idx
        item.pop("brief", None)
        item.pop("demand", None)

    return {
        "generated_at": publishing_data.get("generated_at", brief_data.get("generated_at", "")),
        "summary": {
            "queue_count": len(queue_items),
            "ready_count": sum(1 for item in queue_items if item.get("ready_to_upload")),
        },
        "items": queue_items,
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# 발행 우선순위 큐")
    lines.append("")
    lines.append(f"- 생성 시각: `{report.get('generated_at', '')}`")
    lines.append(f"- 큐 개수: `{report.get('summary', {}).get('queue_count', 0)}`")
    lines.append(f"- 업로드 가능 글 수: `{report.get('summary', {}).get('ready_count', 0)}`")
    lines.append("")
    for item in report.get("items", []):
        lines.append(f"## {item['upload_sequence']}. {item['keyword']}")
        lines.append("")
        lines.append(f"- 제목: {item['title']}")
        lines.append(f"- 우선순위 점수: {item['publish_priority_score']}")
        lines.append(f"- 발행일: {item['recommended_publish_date'] or '미정'} / 버킷: {item['publish_bucket']}")
        lines.append(f"- 역할: {item['role']} / 타입: {item['post_type']}")
        lines.append(f"- 업로드 가능: {item['ready_to_upload']}")
        lines.append(f"- 수익화 목표: {item['revenue_objective']}")
        lines.append(f"- CTA 초점: {item['cta_focus']}")
        lines.append(f"- 광고 슬롯 추천: {', '.join(item['ad_slot_recommendations'])}")
        if item.get("trend_queries"):
            lines.append(f"- 트렌드 쿼리: {', '.join(item['trend_queries'])}")
        lines.append(f"- 발행 메모: {item['publish_note']}")
        lines.append(f"- 수익화 경로: {item['monetization_path']}")
        lines.append(f"- 내부링크: {', '.join(item.get('internal_link_targets', []))}")
        lines.append("")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def main() -> int:
    report = build_queue()
    OUTPUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    write_markdown(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
