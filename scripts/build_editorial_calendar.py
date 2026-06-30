#!/usr/bin/env python3
import json
from datetime import date, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BRIEF_JSON = ROOT / "outputs/latest/daily-post-brief.json"
FRESHNESS_JSON = ROOT / "outputs/latest/source-freshness-board.json"
REVIEW_PACKET_JSON = ROOT / "outputs/latest/review-packet.json"
PERFORMANCE_JSON = ROOT / "outputs/latest/performance-feedback.json"
RULES_JSON = ROOT / "config/growth_rules.json"
TEMPLATE_JSON = ROOT / "config/editorial_calendar_templates.json"
OUTPUT_JSON = ROOT / "outputs/latest/editorial-calendar.json"
OUTPUT_MD = ROOT / "outputs/latest/editorial-calendar.md"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def load_optional_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def brand_lane_from_cluster(cluster: dict) -> str:
    text = f"{cluster.get('keyword', '')} {cluster.get('working_title', '')}".lower()
    if any(token in text for token in ["bitcoin", "crypto", "이더리움", "비트코인", "코인"]):
        return "crypto"
    if any(token in text for token in ["big_tech", "미국 증시", "빅테크", "반도체", "ai 성장주", "나스닥"]):
        return "us-stocks"
    if any(token in text for token in ["china", "관세", "무역", "중국"]):
        return "world-flow"
    return "macro"


def build_freshness_lookup(payload: dict) -> dict[str, dict]:
    lookup: dict[str, dict] = {}
    for item in payload.get("items", []):
        keyword = item.get("keyword", "")
        if keyword:
            lookup[keyword] = item
    return lookup


def build_review_lookup(payload: dict) -> dict[str, dict]:
    return {item.get("keyword", ""): item for item in payload.get("items", []) if item.get("keyword")}


def freshness_rank(status: str) -> int:
    return {"fresh": 0, "aging": 1, "unknown": 2, "stale": 3}.get(status, 2)


def build_breaking_candidate(brief: dict, freshness: dict, review_lookup: dict[str, dict]) -> dict:
    keyword = brief.get("keyword", "")
    review = review_lookup.get(keyword, {})
    return {
        "mode": "direct",
        "keyword": keyword,
        "working_title": review.get("title") or brief.get("title_candidates", [""])[0],
        "angle": brief.get("reason", ""),
        "brand_lane": brief.get("brand_lane", "macro"),
        "source_basis": brief.get("source_names", []),
        "internal_link_targets": brief.get("source_names", []),
        "search_intent": "당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자",
        "monetization_path": "시의성 유입 확보 후 설명형 글과 내부링크로 체류 확대",
        "freshness_status": freshness.get("freshness_status", "unknown"),
        "priority_score": brief.get("total_score", 0),
        "publish_note": freshness.get("recommendation", "당일 이슈 해설형 글"),
    }


def build_recovery_candidate(brief: dict, freshness: dict, review_lookup: dict[str, dict]) -> dict:
    recovery_keyword = freshness.get("recovery_keyword", "")
    review = review_lookup.get(recovery_keyword, {})
    working_title = review.get("title") or freshness.get("recovery_title") or brief.get("title_candidates", [""])[0]
    return {
        "mode": "recovery",
        "keyword": recovery_keyword or brief.get("keyword", ""),
        "working_title": working_title,
        "angle": freshness.get("recovery_summary", "") or freshness.get("recommendation", ""),
        "brand_lane": brief.get("brand_lane", "macro"),
        "source_basis": [brief.get("keyword", "")],
        "internal_link_targets": [brief.get("keyword", "")],
        "search_intent": "당일 이슈를 따라가되 날짜가 지난 뉴스보다 구조를 이해하고 싶은 독자",
        "monetization_path": "검색형 후속 글로 전환해 시의성 하락 리스크를 줄이고 누적 유입 확보",
        "freshness_status": freshness.get("freshness_status", "stale"),
        "priority_score": brief.get("total_score", 0),
        "publish_note": "직접 뉴스 발행 대신 evergreen salvage 경로로 전환",
    }


def build_cluster_candidate(cluster: dict, performance_lookup: dict) -> dict:
    bonus = 0.0
    for related in cluster.get("related_keywords", []):
        bonus = max(bonus, float(performance_lookup.get(related, {}).get("bonus", 0)))
    note = "성과 데이터가 있는 키워드와 연결된 설명형 글" if bonus > 0 else "검색 저변을 넓히는 설명형 글"
    return {
        "mode": "evergreen",
        "keyword": cluster.get("keyword", ""),
        "working_title": cluster.get("working_title", ""),
        "angle": cluster.get("angle", ""),
        "brand_lane": brand_lane_from_cluster(cluster),
        "source_basis": cluster.get("related_keywords", []),
        "internal_link_targets": cluster.get("internal_link_targets", []),
        "search_intent": cluster.get("search_intent", ""),
        "monetization_path": cluster.get("monetization_path", ""),
        "freshness_status": "evergreen",
        "priority_score": bonus,
        "publish_note": note,
        "post_type": cluster.get("post_type", "evergreen_explainer"),
    }


def choose_best_by_lane(briefs: list[dict], freshness_lookup: dict[str, dict], review_lookup: dict[str, dict]) -> dict[str, dict]:
    grouped: dict[str, list[dict]] = {}
    for brief in briefs:
        lane = brief.get("brand_lane", "macro")
        freshness = freshness_lookup.get(brief.get("keyword", ""), {})
        candidate = build_breaking_candidate(brief, freshness, review_lookup)
        if freshness.get("freshness_status") == "stale" and freshness.get("recovery_mode") == "evergreen_salvage":
            candidate = build_recovery_candidate(brief, freshness, review_lookup)
        grouped.setdefault(lane, []).append(candidate)

    best: dict[str, dict] = {}
    for lane, items in grouped.items():
        ranked = sorted(
            items,
            key=lambda item: (
                freshness_rank(item.get("freshness_status", "unknown")),
                0 if item.get("mode") == "direct" else 1,
                -float(item.get("priority_score", 0) or 0),
            ),
        )
        best[lane] = ranked[0]
    return best


def choose_clusters_by_lane(clusters: list[dict], performance_lookup: dict) -> dict[str, list[dict]]:
    grouped: dict[str, list[dict]] = {}
    for cluster in clusters:
        candidate = build_cluster_candidate(cluster, performance_lookup)
        grouped.setdefault(candidate["brand_lane"], []).append(candidate)
    for lane, items in grouped.items():
        items.sort(key=lambda item: (-float(item.get("priority_score", 0) or 0), item.get("keyword", "")))
    return grouped


def make_schedule_entry(day: date, slot: int, role: str, candidate: dict) -> dict:
    post_type = candidate.get("post_type")
    if not post_type:
        post_type = "breaking_explainer" if candidate.get("mode") in {"direct", "recovery"} else "evergreen_explainer"
    return {
        "date": day.isoformat(),
        "slot": slot,
        "role": role,
        "post_type": post_type,
        "target_keyword": candidate.get("keyword", ""),
        "working_title": candidate.get("working_title", ""),
        "angle": candidate.get("angle", ""),
        "search_intent": candidate.get("search_intent", ""),
        "monetization_path": candidate.get("monetization_path", ""),
        "internal_link_targets": candidate.get("internal_link_targets", []),
        "source_basis": candidate.get("source_basis", []),
        "publish_note": candidate.get("publish_note", ""),
        "brand_lane": candidate.get("brand_lane", "macro"),
        "freshness_status": candidate.get("freshness_status", ""),
        "planning_mode": candidate.get("mode", ""),
    }


def make_weekly_recap_entry(day: date, slot: int, chosen_entries: list[dict]) -> dict:
    keywords = [item.get("target_keyword", "") for item in chosen_entries if item.get("target_keyword")][:3]
    return {
        "date": day.isoformat(),
        "slot": slot,
        "role": "weekly_recap",
        "post_type": "weekly_macro_recap",
        "target_keyword": ", ".join(keywords),
        "working_title": "이번 주 주식·코인·거시 흐름 한 번에 정리",
        "angle": "상위 이슈 3개를 한 글에서 연결해 재방문 독자와 체류 시간을 늘리는 회고형 글",
        "search_intent": "이번 주 시장 흐름을 짧게 복기하고 다음 주 포인트를 잡고 싶은 독자",
        "monetization_path": "주간 회고형 콘텐츠로 페이지뷰 누적과 내부 링크 허브 역할",
        "internal_link_targets": keywords,
        "source_basis": keywords,
        "publish_note": "주간 정리형 글로 카테고리 허브 역할 수행",
        "brand_lane": "macro",
        "freshness_status": "mixed",
        "planning_mode": "recap",
    }


def build_schedule(briefs: list[dict], lane_order: list[str], lane_targets: dict, clusters_by_lane: dict[str, list[dict]], best_by_lane: dict[str, dict]) -> tuple[list[dict], list[dict]]:
    today = date.today()
    schedule: list[dict] = []
    planning_notes: list[dict] = []
    used_keywords: set[str] = set()
    used_lanes: list[str] = []

    for idx, lane in enumerate(lane_order[:4], start=1):
        candidate = best_by_lane.get(lane)
        source = "direct_or_recovery"
        if candidate and candidate.get("keyword") in used_keywords:
            candidate = None
        if candidate is None:
            options = clusters_by_lane.get(lane, [])
            candidate = next((item for item in options if item.get("keyword") not in used_keywords), None)
            source = "evergreen_fallback"
        if candidate is None:
            continue
        schedule.append(make_schedule_entry(today + timedelta(days=idx - 1), idx, f"lane_focus_{lane}", candidate))
        used_keywords.add(candidate.get("keyword", ""))
        used_lanes.append(lane)
        planning_notes.append(
            {
                "lane": lane,
                "target_share": lane_targets.get(lane, 0),
                "selected_keyword": candidate.get("keyword", ""),
                "selected_mode": candidate.get("mode", source),
                "freshness_status": candidate.get("freshness_status", ""),
            }
        )

    remaining_candidates: list[dict] = []
    for lane, candidate in best_by_lane.items():
        if candidate.get("keyword") not in used_keywords:
            remaining_candidates.append(candidate)
    for lane, items in clusters_by_lane.items():
        for candidate in items:
            if candidate.get("keyword") not in used_keywords:
                remaining_candidates.append(candidate)
    remaining_candidates.sort(
        key=lambda item: (
            0 if item.get("brand_lane") not in used_lanes else 1,
            freshness_rank(item.get("freshness_status", "unknown")),
            0 if item.get("mode") == "direct" else 1,
            -float(item.get("priority_score", 0) or 0),
        )
    )

    slot_roles = {5: "evergreen_support", 6: "secondary_lane_support"}
    next_slot = len(schedule) + 1
    for candidate in remaining_candidates:
        if next_slot > 6:
            break
        schedule.append(make_schedule_entry(today + timedelta(days=next_slot - 1), next_slot, slot_roles.get(next_slot, "support"), candidate))
        used_keywords.add(candidate.get("keyword", ""))
        used_lanes.append(candidate.get("brand_lane", "macro"))
        next_slot += 1

    schedule.append(make_weekly_recap_entry(today + timedelta(days=6), 7, schedule))
    return schedule, planning_notes


def build_coverage_summary(schedule: list[dict], lane_labels: dict[str, str], lane_targets: dict) -> list[dict]:
    total_slots = max(len([item for item in schedule if item.get("role") != "weekly_recap"]), 1)
    counts: dict[str, int] = {}
    for item in schedule:
        if item.get("role") == "weekly_recap":
            continue
        lane = item.get("brand_lane", "macro")
        counts[lane] = counts.get(lane, 0) + 1

    summary = []
    for lane, target in lane_targets.items():
        count = counts.get(lane, 0)
        actual = round(count / total_slots, 2)
        summary.append(
            {
                "brand_lane": lane,
                "label": lane_labels.get(lane, lane),
                "target_share": target,
                "scheduled_count": count,
                "actual_share": actual,
                "status": "covered" if count > 0 else "gap",
            }
        )
    return summary


def main() -> int:
    brief_data = load_json(BRIEF_JSON)
    freshness_data = load_json(FRESHNESS_JSON)
    review_data = load_json(REVIEW_PACKET_JSON)
    performance = load_optional_json(PERFORMANCE_JSON)
    templates = load_json(TEMPLATE_JSON)
    rules = load_optional_json(RULES_JSON)

    briefs = brief_data.get("top_briefs", [])
    freshness_lookup = build_freshness_lookup(freshness_data)
    review_lookup = build_review_lookup(review_data)
    performance_lookup = (performance or {}).get("keyword_feedback", {})
    topic_mix = (rules.get("topic_mix_policy") or {})
    lane_order = topic_mix.get("top_brief_diversity_order", ["macro", "crypto", "us-stocks", "world-flow"])
    lane_targets = topic_mix.get("weekly_mix_targets", {})
    lane_labels = topic_mix.get("brand_lane_labels", {})

    best_by_lane = choose_best_by_lane(briefs, freshness_lookup, review_lookup)
    clusters_by_lane = choose_clusters_by_lane(templates.get("evergreen_clusters", []), performance_lookup)
    schedule, planning_notes = build_schedule(briefs, lane_order, lane_targets, clusters_by_lane, best_by_lane)
    coverage_summary = build_coverage_summary(schedule, lane_labels, lane_targets)

    payload = {
        "generated_at": brief_data.get("generated_at"),
        "lane_order": lane_order,
        "coverage_summary": coverage_summary,
        "planning_notes": planning_notes,
        "schedule": schedule,
    }
    OUTPUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2))

    lines = []
    lines.append("# 7일 편집 캘린더")
    lines.append("")
    lines.append(f"- 생성 시각: `{payload.get('generated_at', '')}`")
    lines.append("- 목적: stale 뉴스는 직접 발행에서 빼고, 거시경제·코인·미국주식·세계 흐름 레인을 주간 단위로 균형 있게 유지")
    lines.append("")
    lines.append("## 레인 커버리지")
    lines.append("")
    for item in coverage_summary:
        lines.append(
            f"- `{item['label']}` / target `{item['target_share']}` / scheduled_count `{item['scheduled_count']}` / actual_share `{item['actual_share']}` / status `{item['status']}`"
        )
    lines.append("")
    lines.append("## 이번 주 배치 메모")
    lines.append("")
    for note in planning_notes:
        lines.append(
            f"- lane `{note['lane']}` / keyword `{note['selected_keyword']}` / mode `{note['selected_mode']}` / freshness `{note['freshness_status']}` / target_share `{note['target_share']}`"
        )
    lines.append("")
    for item in schedule:
        lines.append(f"## Day {item['slot']} · {item['date']} · {item['role']}")
        lines.append("")
        lines.append(f"- 브랜드 레인: {lane_labels.get(item.get('brand_lane', ''), item.get('brand_lane', ''))}")
        lines.append(f"- planning_mode: {item.get('planning_mode', '')}")
        lines.append(f"- freshness_status: {item.get('freshness_status', '')}")
        lines.append(f"- 포스트 유형: {item['post_type']}")
        lines.append(f"- 타깃 키워드: {item['target_keyword']}")
        lines.append(f"- 작업 제목: {item['working_title']}")
        lines.append(f"- 글 각도: {item['angle']}")
        lines.append(f"- 검색 의도: {item['search_intent']}")
        lines.append(f"- 수익화 경로: {item['monetization_path']}")
        lines.append(f"- 내부링크 대상: {', '.join(item['internal_link_targets'])}")
        lines.append(f"- 근거 소스/연결 키워드: {', '.join(item['source_basis'])}")
        lines.append(f"- 발행 메모: {item['publish_note']}")
        lines.append("")

    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
