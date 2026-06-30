#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
KEYWORD_BOARD_JSON = ROOT / "outputs/latest/keyword-opportunity-board.json"
FIRST_APPROVAL_PATH_JSON = ROOT / "outputs/latest/first-approval-path.json"
PUBLISH_QUEUE_JSON = ROOT / "outputs/latest/publish-queue.json"
MONETIZATION_JSON = ROOT / "outputs/latest/monetization-readiness-report.json"
DAILY_BRIEF_JSON = ROOT / "outputs/latest/daily-post-brief.json"
FRESHNESS_JSON = ROOT / "outputs/latest/source-freshness-board.json"
REVIEW_PACKET_JSON = ROOT / "outputs/latest/review-packet.json"
GROWTH_RULES_JSON = ROOT / "config/growth_rules.json"
OUTPUT_JSON = ROOT / "outputs/latest/daily-revenue-focus.json"
OUTPUT_MD = ROOT / "outputs/latest/daily-revenue-focus.md"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def build_queue_lookup(queue_data: dict) -> dict:
    return {item.get("keyword"): item for item in queue_data.get("items", [])}


def build_review_lookup(review_data: dict) -> dict:
    return {item.get("keyword"): item for item in review_data.get("items", []) if item.get("keyword")}


def build_freshness_lookup(payload: dict) -> dict[str, dict]:
    return {item.get("keyword", ""): item for item in payload.get("items", []) if item.get("keyword")}


def build_brand_lane_lookup() -> tuple[dict[str, str], dict[str, str]]:
    brief = load_json(DAILY_BRIEF_JSON)
    growth_rules = load_json(GROWTH_RULES_JSON)
    lane_labels = ((growth_rules.get("topic_mix_policy") or {}).get("brand_lane_labels") or {})
    lookup: dict[str, str] = {}
    for item in brief.get("top_briefs", []):
        keyword = item.get("keyword", "")
        lane = item.get("brand_lane", "")
        if keyword and lane:
            lookup[keyword] = lane
    fallback = {
        "fomc": "macro",
        "cpi": "macro",
        "pce": "macro",
        "jobs": "macro",
        "treasury_yields": "macro",
        "dollar": "macro",
        "oil": "macro",
        "bitcoin": "crypto",
        "ethereum": "crypto",
        "crypto_etf": "crypto",
        "ai_semiconductors": "us-stocks",
        "us_index_flow": "us-stocks",
        "us_big_tech": "us-stocks",
        "ai_growth_stocks": "us-stocks",
        "china": "world-flow",
        "tariffs_trade": "world-flow",
    }
    for keyword, lane in fallback.items():
        lookup.setdefault(keyword, lane)
    return lookup, lane_labels


def revenue_angle(item: dict) -> str:
    objective = item.get("revenue_objective", "")
    if objective:
        return objective
    urgency = item.get("urgency", "")
    if urgency == "publish_now":
        return "당일 검색/소셜 유입을 먼저 확보해 초기 페이지뷰를 만드는 역할"
    if urgency == "prep_today":
        return "내일 발행 슬롯 선점으로 연속 유입을 이어가는 역할"
    return "카테고리 보강과 내부링크 확장으로 장기 검색 유입 기반을 만드는 역할"


def candidate_title(item: dict) -> str:
    return item.get("title", "") or item.get("suggested_title", "")


def candidate_lane(item: dict, lane_lookup: dict[str, str]) -> str:
    return lane_lookup.get(item.get("keyword", "") or item.get("source_keyword", ""), "macro")


def freshness_rank(status: str) -> int:
    return {"fresh": 0, "aging": 1, "unknown": 2, "stale": 3}.get(status, 2)


def resolve_candidate(
    item: dict,
    freshness_lookup: dict[str, dict],
    review_lookup: dict[str, dict],
    lane_lookup: dict[str, str],
) -> dict:
    keyword = item.get("keyword", "")
    freshness = freshness_lookup.get(keyword, {})
    freshness_status = freshness.get("freshness_status", "unknown")
    resolved = dict(item)
    resolved["resolved_keyword"] = keyword
    resolved["freshness_status"] = freshness_status
    resolved["selection_mode"] = "direct"

    if freshness_status == "stale" and freshness.get("recovery_mode") == "evergreen_salvage":
        recovery_keyword = freshness.get("recovery_keyword", "")
        review_item = review_lookup.get(recovery_keyword, {})
        resolved["resolved_keyword"] = recovery_keyword or keyword
        resolved["resolved_title"] = review_item.get("title") or freshness.get("recovery_title") or candidate_title(item)
        resolved["selection_mode"] = "evergreen_salvage"
        resolved["why_revenue_override"] = freshness.get("recovery_summary", "")
        resolved["cta_focus_override"] = review_item.get("cta_focus", "")
        resolved["brand_lane_override"] = lane_lookup.get(keyword, lane_lookup.get(recovery_keyword, "macro"))
        resolved["urgency_override"] = "recover_then_publish"
    return resolved


def choose_next_slot(
    breaking: list[dict],
    first_keyword: str,
    first_lane: str,
    lane_lookup: dict[str, str],
    freshness_lookup: dict[str, dict],
    review_lookup: dict[str, dict],
) -> dict:
    candidates = [item for item in breaking if item.get("keyword") and item.get("keyword") != first_keyword]
    if not candidates:
        return {}
    resolved_candidates = [resolve_candidate(item, freshness_lookup, review_lookup, lane_lookup) for item in candidates]
    different_lane = [
        item
        for item in resolved_candidates
        if item.get("brand_lane_override", candidate_lane(item, lane_lookup)) != first_lane
    ]
    fresh_preferred = [item for item in different_lane if item.get("freshness_status") != "stale"] or [
        item for item in resolved_candidates if item.get("freshness_status") != "stale"
    ]
    preferred = fresh_preferred or different_lane or resolved_candidates
    urgency_rank = {"publish_now": 0, "prep_today": 1, "watch": 2}
    preferred.sort(
        key=lambda item: (
            freshness_rank(item.get("freshness_status", "unknown")),
            0 if item.get("selection_mode") == "direct" else 1,
            urgency_rank.get(item.get("urgency_override", item.get("urgency", "watch")), 9),
            -float(item.get("score", 0) or 0),
            item.get("resolved_keyword", item.get("keyword", "")),
        )
    )
    return preferred[0]


def build_report() -> dict:
    board = load_json(KEYWORD_BOARD_JSON)
    first_approval = load_json(FIRST_APPROVAL_PATH_JSON)
    queue = load_json(PUBLISH_QUEUE_JSON)
    monetization = load_json(MONETIZATION_JSON)
    freshness = load_json(FRESHNESS_JSON)
    review = load_json(REVIEW_PACKET_JSON)
    queue_lookup = build_queue_lookup(queue)
    review_lookup = build_review_lookup(review)
    freshness_lookup = build_freshness_lookup(freshness)
    brand_lane_lookup, lane_labels = build_brand_lane_lookup()

    breaking = board.get("breaking_candidates", [])
    seo_followups = board.get("seo_followups", [])
    first_single = (first_approval.get("recommended_single") or {})
    first_keyword = first_single.get("keyword", "")

    first_breaking = next((item for item in breaking if item.get("keyword") == first_keyword), breaking[0] if breaking else {})
    first_lane = brand_lane_lookup.get(first_keyword, "macro")
    second_breaking = choose_next_slot(
        breaking,
        first_keyword,
        first_lane,
        brand_lane_lookup,
        freshness_lookup,
        review_lookup,
    )
    first_seo = next((item for item in seo_followups if item.get("source_keyword") == first_keyword), seo_followups[0] if seo_followups else {})

    first_queue_item = queue_lookup.get(first_keyword, {})

    today_path = []
    if first_keyword:
        today_path.append(
            {
                "step": "main_post",
                "keyword": first_keyword,
                "title": first_single.get("title", "") or first_breaking.get("suggested_title", ""),
                "why_revenue": revenue_angle(first_queue_item or first_breaking or first_single),
                "cta_focus": first_queue_item.get("cta_focus", ""),
                "urgency": first_breaking.get("urgency", "publish_now"),
                "brand_lane": first_lane,
                "brand_lane_label": lane_labels.get(first_lane, first_lane),
            }
        )
    if first_seo:
        seo_lane = brand_lane_lookup.get(first_seo.get("source_keyword", ""), first_lane)
        today_path.append(
            {
                "step": "seo_followup",
                "keyword": first_seo.get("source_keyword", ""),
                "title": first_seo.get("title", ""),
                "why_revenue": first_seo.get("monetization_goal", ""),
                "cta_focus": first_seo.get("cta_focus", ""),
                "urgency": "follow_after_main",
                "brand_lane": seo_lane,
                "brand_lane_label": lane_labels.get(seo_lane, seo_lane),
            }
        )
    if second_breaking:
        resolved_keyword = second_breaking.get("resolved_keyword", second_breaking.get("keyword", ""))
        second_queue_item = queue_lookup.get(resolved_keyword, queue_lookup.get(second_breaking.get("keyword", ""), {}))
        second_lane = second_breaking.get("brand_lane_override", brand_lane_lookup.get(resolved_keyword, "macro"))
        today_path.append(
            {
                "step": "next_slot",
                "keyword": resolved_keyword,
                "title": second_breaking.get("resolved_title", candidate_title(second_breaking)),
                "why_revenue": second_breaking.get("why_revenue_override") or revenue_angle(second_queue_item or second_breaking),
                "cta_focus": second_breaking.get("cta_focus_override") or second_queue_item.get("cta_focus", ""),
                "urgency": second_breaking.get("urgency_override", second_breaking.get("urgency", "")),
                "brand_lane": second_lane,
                "brand_lane_label": lane_labels.get(second_lane, second_lane),
                "selection_mode": second_breaking.get("selection_mode", "direct"),
                "freshness_status": second_breaking.get("freshness_status", "unknown"),
            }
        )

    weak_stages = [stage.get("name") for stage in monetization.get("stages", []) if not stage.get("ready")]
    approval_batch = (first_approval.get("recommended_batch") or {}).get("approval_command", "")
    approval_single = (first_approval.get("recommended_single") or {}).get("approval_command", "")

    return {
        "generated_at": board.get("generated_at", ""),
        "today_path": today_path,
        "approval_commands": {
            "batch": approval_batch,
            "single": approval_single,
        },
        "monetization_gaps": weak_stages,
        "operator_summary": {
            "main_post_first": today_path[0]["title"] if today_path else "",
            "seo_followup_after": first_seo.get("title", ""),
            "next_slot_title": candidate_title(second_breaking) if second_breaking else "",
        },
        "path_policy": "main post는 현재 최적 단건 후보를 유지하고, next slot은 가능하면 다른 브랜드 레인에서 선택",
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# Daily Revenue Focus")
    lines.append("")
    lines.append("오늘 어떤 글 순서로 올려야 수익화에 더 유리한지 보여주는 운영 카드입니다.")
    lines.append("")
    lines.append(f"- generated_at: `{report.get('generated_at', '')}`")
    lines.append(f"- path_policy: {report.get('path_policy', '')}")
    lines.append("")
    lines.append("## Today Path")
    lines.append("")
    for item in report.get("today_path", []):
        lines.append(f"- `{item.get('step', '')}` / `{item.get('title', '')}`")
        lines.append(f"  - keyword: {item.get('keyword', '')}")
        lines.append(f"  - brand_lane: {item.get('brand_lane', '')} ({item.get('brand_lane_label', '')})")
        lines.append(f"  - urgency: {item.get('urgency', '')}")
        lines.append(f"  - why_revenue: {item.get('why_revenue', '')}")
        lines.append(f"  - cta_focus: {item.get('cta_focus', '')}")
    if not report.get("today_path"):
        lines.append("- 오늘 추천 경로가 아직 없습니다.")
    lines.append("")
    lines.append("## Approval Commands")
    lines.append("")
    if report.get("approval_commands", {}).get("single"):
        lines.append(f"- single: `{report['approval_commands']['single']}`")
    if report.get("approval_commands", {}).get("batch"):
        lines.append(f"- batch: `{report['approval_commands']['batch']}`")
    if not report.get("approval_commands", {}).get("single") and not report.get("approval_commands", {}).get("batch"):
        lines.append("- 승인 명령이 아직 생성되지 않았습니다.")
    lines.append("")
    lines.append("## Monetization Gaps")
    lines.append("")
    for gap in report.get("monetization_gaps", []):
        lines.append(f"- `{gap}`")
    if not report.get("monetization_gaps"):
        lines.append("- 현재 정의된 수익화 단계는 모두 준비 상태입니다.")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def main() -> int:
    report = build_report()
    OUTPUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    write_markdown(report)
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
