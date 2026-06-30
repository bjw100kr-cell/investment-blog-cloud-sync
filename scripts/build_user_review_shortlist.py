#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REVIEW_PACKET_JSON = ROOT / "outputs/latest/review-packet.json"
FIRST_APPROVAL_PATH_JSON = ROOT / "outputs/latest/first-approval-path.json"
DAILY_REVENUE_FOCUS_JSON = ROOT / "outputs/latest/daily-revenue-focus.json"
QUALITY_GATE_JSON = ROOT / "outputs/latest/pre-publish-quality-gate.json"
SAFE_IMAGE_SUGGESTIONS_JSON = ROOT / "outputs/latest/safe-image-suggestions.json"
DAILY_BRIEF_JSON = ROOT / "outputs/latest/daily-post-brief.json"
GROWTH_RULES_JSON = ROOT / "config/growth_rules.json"
FRESHNESS_JSON = ROOT / "outputs/latest/source-freshness-board.json"
OUTPUT_JSON = ROOT / "outputs/latest/user-review-shortlist.json"
OUTPUT_MD = ROOT / "outputs/latest/user-review-shortlist.md"
REVIEW_BOARD_MD = ROOT / "outputs/latest/review-preview-board.md"
REVIEW_PACKET_MD = ROOT / "outputs/latest/review-packet.md"
IMAGE_HELPER = ROOT / "scripts/set_image_selection.py"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def build_item_lookup(items: list[dict]) -> dict:
    return {item.get("keyword"): item for item in items if item.get("keyword")}


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


def build_quality_lookup() -> dict[str, dict]:
    payload = load_json(QUALITY_GATE_JSON)
    lookup: dict[str, dict] = {}
    for item in payload.get("items", []):
        keyword = item.get("keyword", "")
        if not keyword:
            continue
        hero_image_selected = False
        for check in item.get("checks", []):
            if check.get("name") == "hero_image_selected":
                hero_image_selected = bool(check.get("ok"))
                break
        lookup[keyword] = {
            "quality_status": item.get("status", ""),
            "hero_image_selected": hero_image_selected,
            "ready_now": item.get("status") == "pass" and hero_image_selected,
        }
    return lookup


def build_image_lookup() -> dict[str, dict]:
    payload = load_json(SAFE_IMAGE_SUGGESTIONS_JSON)
    lookup: dict[str, dict] = {}
    for item in payload.get("items", []):
        keyword = item.get("keyword", "")
        if not keyword:
            continue
        hero = {}
        for image in item.get("image_plan", []):
            if image.get("slot") == "hero":
                hero = image
                break
        if hero:
            lookup[keyword] = {
                "provider_name": hero.get("provider_name", ""),
                "search_query": hero.get("search_query", ""),
                "search_url": hero.get("search_url", ""),
                "license_label": hero.get("license_label", ""),
                "license_url": hero.get("license_url", ""),
                "apply_helper": f'python3 {IMAGE_HELPER} --keyword {keyword} --slot hero --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve',
            }
    return lookup


def build_freshness_lookup() -> dict[str, dict]:
    payload = load_json(FRESHNESS_JSON)
    lookup: dict[str, dict] = {}
    for item in payload.get("items", []):
        keyword = item.get("keyword", "")
        if not keyword:
            continue
        lookup[keyword] = {
            "freshness_status": item.get("freshness_status", ""),
            "recommendation": item.get("recommendation", ""),
        }
    return lookup


def shortlist_keywords(first_approval: dict, revenue_focus: dict, daily_brief: dict, freshness_lookup: dict[str, dict]) -> list[str]:
    keywords: list[str] = []

    single = (first_approval.get("recommended_single") or {}).get("keyword", "")
    if single:
        keywords.append(single)

    for item in revenue_focus.get("today_path", []):
        keyword = item.get("keyword", "")
        if keyword and keyword not in keywords:
            keywords.append(keyword)

    for keyword in (first_approval.get("recommended_batch") or {}).get("keywords", []):
        if keyword and keyword not in keywords:
            keywords.append(keyword)

    for item in daily_brief.get("top_briefs", []):
        keyword = item.get("keyword", "")
        if keyword and keyword not in keywords:
            keywords.append(keyword)

    non_stale = [keyword for keyword in keywords if freshness_lookup.get(keyword, {}).get("freshness_status", "unknown") != "stale"]
    if len(non_stale) >= 3:
        return non_stale[:3]
    for keyword in keywords:
        if keyword not in non_stale:
            non_stale.append(keyword)
        if len(non_stale) >= 3:
            break
    return non_stale[:3]


def select_diverse_keywords(
    candidate_keywords: list[str],
    review_lookup: dict[str, dict],
    quality_lookup: dict[str, dict],
    freshness_lookup: dict[str, dict],
    brand_lane_lookup: dict[str, str],
    limit: int = 3,
) -> list[str]:
    candidates: list[dict] = []
    for position, keyword in enumerate(candidate_keywords):
        review_item = review_lookup.get(keyword, {})
        if not review_item:
            continue
        quality = quality_lookup.get(keyword, {})
        candidates.append(
            {
                "keyword": keyword,
                "lane": brand_lane_lookup.get(keyword, "macro"),
                "ready_now": quality.get("ready_now", False),
                "quality_status": quality.get("quality_status", ""),
                "freshness_status": freshness_lookup.get(keyword, {}).get("freshness_status", "unknown"),
                "priority_score": float(review_item.get("priority_score", 0)),
                "position": position,
            }
        )

    freshness_rank = {"fresh": 0, "aging": 1, "unknown": 2, "stale": 3}
    candidates.sort(
        key=lambda item: (
            0 if item.get("ready_now") else 1,
            freshness_rank.get(item.get("freshness_status", "unknown"), 2),
            0 if item.get("quality_status") == "pass" else 1,
            -item.get("priority_score", 0),
            item.get("position", 999),
        )
    )

    selected: list[str] = []
    used_lanes: set[str] = set()
    for item in candidates:
        if item["lane"] in used_lanes:
            continue
        selected.append(item["keyword"])
        used_lanes.add(item["lane"])
        if len(selected) >= limit:
            return selected

    for item in candidates:
        if item["keyword"] in selected:
            continue
        selected.append(item["keyword"])
        if len(selected) >= limit:
            break
    return selected


def build_report() -> dict:
    review = load_json(REVIEW_PACKET_JSON)
    first_approval = load_json(FIRST_APPROVAL_PATH_JSON)
    revenue_focus = load_json(DAILY_REVENUE_FOCUS_JSON)
    daily_brief = load_json(DAILY_BRIEF_JSON)
    review_items = review.get("items", [])
    lookup = build_item_lookup(review_items)
    quality_lookup = build_quality_lookup()
    image_lookup = build_image_lookup()
    freshness_lookup = build_freshness_lookup()
    brand_lane_lookup, lane_labels = build_brand_lane_lookup()

    selected_keywords = shortlist_keywords(first_approval, revenue_focus, daily_brief, freshness_lookup)
    selected_keywords = select_diverse_keywords(selected_keywords, lookup, quality_lookup, freshness_lookup, brand_lane_lookup)
    single_keyword = (first_approval.get("recommended_single") or {}).get("keyword", "")
    if single_keyword and selected_keywords:
        selected_keywords = [single_keyword] + [keyword for keyword in selected_keywords if keyword != single_keyword]

    shortlist = []
    for keyword in selected_keywords:
        item = lookup.get(keyword, {})
        if not item:
            continue
        quality = quality_lookup.get(keyword, {})
        image = image_lookup.get(keyword, {})
        freshness = freshness_lookup.get(keyword, {})
        shortlist.append(
            {
                "keyword": item.get("keyword", ""),
                "title": item.get("title", ""),
                "publish_date": item.get("recommended_publish_date", ""),
                "priority_score": item.get("priority_score", 0),
                "review_verdict": item.get("review_verdict", ""),
                "quality_status": quality.get("quality_status", ""),
                "hero_image_selected": quality.get("hero_image_selected", False),
                "ready_now": quality.get("ready_now", False),
                "brand_lane": brand_lane_lookup.get(keyword, "macro"),
                "brand_lane_label": lane_labels.get(brand_lane_lookup.get(keyword, "macro"), brand_lane_lookup.get(keyword, "macro")),
                "freshness_status": freshness.get("freshness_status", ""),
                "freshness_recommendation": freshness.get("recommendation", ""),
                "hero_image_provider": image.get("provider_name", ""),
                "hero_image_search_query": image.get("search_query", ""),
                "hero_image_search_url": image.get("search_url", ""),
                "hero_image_license_label": image.get("license_label", ""),
                "hero_image_license_url": image.get("license_url", ""),
                "hero_image_apply_helper": image.get("apply_helper", ""),
                "cta_focus": item.get("cta_focus", ""),
                "intent": item.get("search_intent", ""),
                "preview": item.get("review_preview", [])[:2],
            }
        )

    return {
        "selected_keywords": selected_keywords,
        "shortlist_policy": "ready_now 우선, 같은 브랜드 레인 중복 최소화, 높은 priority_score 우선",
        "shortlist": shortlist,
        "review_board_path": str(REVIEW_BOARD_MD),
        "review_packet_path": str(REVIEW_PACKET_MD),
        "single_approval_command": (first_approval.get("recommended_single") or {}).get("approval_command", ""),
        "batch_approval_command": (first_approval.get("recommended_batch") or {}).get("approval_command", ""),
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# User Review Shortlist")
    lines.append("")
    lines.append("사용자가 길게 읽지 않아도 오늘 먼저 확인하면 되는 글만 짧게 추린 검토 카드입니다.")
    lines.append("- 발행 원칙: 제가 먼저 초안을 보여드리고, 사용자가 내용을 확인한 글만 다음 업로드 단계로 넘깁니다.")
    lines.append("- 발행 전 상태: 사용자 최종 확인이 없으면 실제 업로드는 계속 차단됩니다.")
    lines.append(f"- shortlist_policy: {report.get('shortlist_policy', '')}")
    lines.append(f"- 빠른 검토 보드: `{report.get('review_board_path', '')}`")
    lines.append(f"- 상세 검토 패킷: `{report.get('review_packet_path', '')}`")
    lines.append("- 원칙: 여기서 먼저 읽고 확인한 글만 업로드 후보로 넘깁니다.")
    lines.append("")
    lines.append("")
    for index, item in enumerate(report.get("shortlist", []), start=1):
        lines.append(f"## {index}. {item.get('title', '')}")
        lines.append("")
        lines.append(f"- keyword: `{item.get('keyword', '')}`")
        lines.append(f"- brand_lane: `{item.get('brand_lane', '')}` ({item.get('brand_lane_label', '')})")
        lines.append(f"- publish_date: `{item.get('publish_date', '') or 'unscheduled'}`")
        lines.append(f"- priority_score: `{item.get('priority_score', 0)}`")
        lines.append(f"- review_verdict: `{item.get('review_verdict', '')}`")
        lines.append(f"- freshness_status: `{item.get('freshness_status', '')}`")
        lines.append(f"- quality_status: `{item.get('quality_status', '')}`")
        lines.append(f"- hero_image_selected: `{item.get('hero_image_selected', False)}`")
        lines.append(f"- ready_now: `{item.get('ready_now', False)}`")
        lines.append(f"- intent: {item.get('intent', '')}")
        lines.append(f"- CTA focus: {item.get('cta_focus', '')}")
        if item.get("ready_now"):
            lines.append("- recommendation: 지금 이 글부터 확인하면 바로 발행 후보로 넘기기 가장 쉽습니다.")
        elif item.get("quality_status") == "review_before_publish":
            lines.append("- recommendation: 내용 검토는 가능하지만, 대표 이미지나 최종 발행 준비를 먼저 보완해야 합니다.")
            if item.get("hero_image_search_url"):
                lines.append(
                    f"- next_image_search: {item.get('hero_image_provider', '')} / query `{item.get('hero_image_search_query', '')}` / {item.get('hero_image_search_url', '')}"
                )
            if item.get("hero_image_license_url"):
                lines.append(
                    f"- next_image_license: {item.get('hero_image_license_label', '')} / {item.get('hero_image_license_url', '')}"
                )
            if item.get("hero_image_apply_helper"):
                lines.append(f"- next_image_apply_helper: `{item.get('hero_image_apply_helper', '')}`")
        if item.get("freshness_recommendation"):
            lines.append(f"- freshness_note: {item.get('freshness_recommendation', '')}")
        for preview in item.get("preview", []):
            lines.append(f"- preview: {preview}")
        lines.append("")
    lines.append("## User Confirmation Commands")
    lines.append("")
    if report.get("single_approval_command"):
        lines.append(f"- single: `{report.get('single_approval_command', '')}`")
    if report.get("batch_approval_command"):
        lines.append(f"- batch: `{report.get('batch_approval_command', '')}`")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def main() -> int:
    report = build_report()
    OUTPUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    write_markdown(report)
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
