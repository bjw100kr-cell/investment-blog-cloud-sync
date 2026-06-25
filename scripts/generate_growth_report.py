#!/usr/bin/env python3
import json
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RULES_JSON = ROOT / "config/growth_rules.json"
BRIEF_JSON = ROOT / "outputs/latest/daily-post-brief.json"
CALENDAR_JSON = ROOT / "outputs/latest/editorial-calendar.json"
PUBLISHING_JSON = ROOT / "outputs/latest/publishing-assets.json"
SEARCH_CONSOLE_JSON = ROOT / "outputs/latest/search-console-conversion-report.json"
PERFORMANCE_JSON = ROOT / "outputs/latest/performance-feedback.json"
TONE_JSON = ROOT / "outputs/latest/human-tone-review.json"
SEARCH_DEMAND_JSON = ROOT / "outputs/latest/search-demand-report.json"
OUTPUT_JSON = ROOT / "outputs/latest/growth-report.json"
OUTPUT_MD = ROOT / "outputs/latest/growth-report.md"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def average(values: list[float]) -> float:
    if not values:
        return 0.0
    return round(sum(values) / len(values), 2)


def build_category_summary(publishing_items: list[dict], top_briefs: list[dict], rules: dict) -> list[dict]:
    category_weights = rules.get("category_value_weights", {})
    brief_by_keyword = {item.get("keyword"): item for item in top_briefs}
    grouped = defaultdict(lambda: {"count": 0, "keywords": [], "score_sum": 0.0})

    for item in publishing_items:
        category = item.get("category", "unknown")
        keyword = item.get("keyword")
        grouped[category]["count"] += 1
        grouped[category]["keywords"].append(keyword)
        grouped[category]["score_sum"] += float(brief_by_keyword.get(keyword, {}).get("monetization_score", 0))

    summary = []
    for category, info in grouped.items():
        base_score = info["score_sum"] / max(info["count"], 1)
        weighted_score = round(base_score * float(category_weights.get(category, 1.0)), 2)
        summary.append(
            {
                "category": category,
                "post_count": info["count"],
                "keywords": info["keywords"],
                "avg_monetization_score": round(base_score, 2),
                "weighted_priority_score": weighted_score,
            }
        )

    return sorted(summary, key=lambda item: item["weighted_priority_score"], reverse=True)


def build_query_watchlist(search_console: dict) -> list[dict]:
    if not search_console.get("available"):
        return []

    watchlist = []
    for item in search_console.get("items", []):
        keyword = item.get("keyword", "")
        clicks = float(item.get("clicks", 0))
        impressions = float(item.get("impressions", 0))
        ctr = round((clicks / impressions) * 100, 2) if impressions else 0.0
        watchlist.append(
            {
                "keyword": keyword,
                "query_examples": item.get("queries", []),
                "clicks": clicks,
                "impressions": impressions,
                "ctr": ctr,
                "angle": "이미 검색 수요가 보여서 제목, FAQ, 입문형 evergreen 글로 확장하기 좋음",
            }
        )

    return sorted(watchlist, key=lambda item: (item["impressions"], item["clicks"]), reverse=True)


def build_trend_watchlist(search_demand: dict) -> list[dict]:
    watchlist = []
    for item in search_demand.get("ranked_keyword_demand", []):
        watchlist.append(
            {
                "keyword": item.get("keyword", ""),
                "trend_queries": item.get("trend_queries", []),
                "trend_count": item.get("trend_count", 0),
                "traffic_score_sum": item.get("traffic_score_sum", 0),
                "regions": item.get("regions", []),
                "angle": "무료 Google Trends 급상승 쿼리 기반으로 먼저 잡은 수요 신호",
            }
        )
    return sorted(watchlist, key=lambda item: (item["traffic_score_sum"], item["trend_count"]), reverse=True)


def build_schedule_mix(schedule: list[dict]) -> dict:
    role_counter = Counter()
    post_type_counter = Counter()

    for item in schedule:
        role_counter[item.get("role", "unknown")] += 1
        post_type_counter[item.get("post_type", "unknown")] += 1

    return {
        "roles": dict(role_counter),
        "post_types": dict(post_type_counter),
        "days_scheduled": len(schedule),
    }


def infer_next_actions(
    category_summary: list[dict],
    query_watchlist: list[dict],
    tone_items: list[dict],
    rules: dict,
) -> list[str]:
    actions = []
    tone_target = int(rules.get("human_tone_score_target", 75))
    evaluated_tone_items = [item for item in tone_items if item.get("score", 0) > 0]
    avg_tone = average([float(item.get("score", 0)) for item in evaluated_tone_items])

    if category_summary:
        top_category = category_summary[0]["category"]
        actions.append(f"다음 7일은 `{top_category}` 카테고리를 메인 허브로 밀고, 나머지는 보조 내부링크로 묶습니다.")

    if query_watchlist:
        top_query = query_watchlist[0]
        query_label = ", ".join(top_query.get("query_examples", [])) or top_query["keyword"]
        actions.append(f"이미 수요가 잡힌 `{query_label}` 계열은 속보 1개로 끝내지 말고 evergreen 설명 글로 한 번 더 확장합니다.")
    else:
        actions.append("Search Console 데이터가 아직 약하니, Google Trends와 당일 헤드라인으로 1차 주제 발굴을 이어갑니다.")

    if not evaluated_tone_items:
        actions.append("아직 실제 초안이 생성되지 않아 문체 평가는 대기 상태입니다. OPENAI 초안 생성 연결 후 다시 점검합니다.")
    elif avg_tone < tone_target:
        actions.append(f"문체 평균 점수 `{avg_tone}`가 목표 `{tone_target}`보다 낮아, 도입부 독자 문장과 숫자 뒤 해석 문장을 우선 보강합니다.")
    else:
        actions.append(f"문체 평균 점수 `{avg_tone}`로 기준 이상이므로, 이제는 제목 클릭률과 내부링크 동선을 더 키웁니다.")

    actions.append("당일 속보 1개와 검색형 evergreen 1개를 짝으로 묶어, 트래픽과 누적 검색 유입을 동시에 노립니다.")
    return actions


def build_report() -> dict:
    rules = load_json(RULES_JSON)
    brief_data = load_json(BRIEF_JSON)
    calendar_data = load_json(CALENDAR_JSON)
    publishing_data = load_json(PUBLISHING_JSON)
    search_console = load_json(SEARCH_CONSOLE_JSON)
    performance = load_json(PERFORMANCE_JSON)
    tone_data = load_json(TONE_JSON)
    search_demand = load_json(SEARCH_DEMAND_JSON)

    top_briefs = brief_data.get("top_briefs", [])
    schedule = calendar_data.get("schedule", [])
    publishing_items = publishing_data.get("items", [])
    tone_items = tone_data.get("items", [])
    evaluated_tone_items = [item for item in tone_items if item.get("score", 0) > 0]

    category_summary = build_category_summary(publishing_items, top_briefs, rules)
    query_watchlist = build_query_watchlist(search_console)
    trend_watchlist = build_trend_watchlist(search_demand)
    schedule_mix = build_schedule_mix(schedule)
    avg_tone_score = average([float(item.get("score", 0)) for item in evaluated_tone_items])

    top_opportunities = []
    for brief in top_briefs[:3]:
        top_opportunities.append(
            {
                "keyword": brief.get("keyword"),
                "recommended_title": brief.get("title_candidates", [""])[0],
                "reason": brief.get("reason", ""),
                "total_score": brief.get("total_score", 0),
                "monetization_score": brief.get("monetization_score", 0),
                "source_names": brief.get("source_names", []),
            }
        )

    return {
        "generated_at": brief_data.get("generated_at"),
        "daily_execution_targets": rules.get("daily_execution_targets", {}),
        "content_mix_targets": rules.get("content_mix_targets", {}),
        "top_opportunities": top_opportunities,
        "category_summary": category_summary,
        "query_watchlist": query_watchlist[:5],
        "trend_watchlist": trend_watchlist[:5],
        "schedule_mix": schedule_mix,
        "tone_review": {
            "average_score": avg_tone_score,
            "target_score": rules.get("human_tone_score_target", 75),
            "evaluated_count": len(evaluated_tone_items),
            "skipped_count": max(len(tone_items) - len(evaluated_tone_items), 0),
            "items": tone_items,
        },
        "performance_feedback_available": performance.get("available", False),
        "next_actions": infer_next_actions(category_summary, query_watchlist, tone_items, rules),
        "monetization_ladders": rules.get("monetization_ladders", {}),
        "trust_stack": rules.get("trust_requirements", []),
        "human_style_checkpoints": rules.get("human_style_checkpoints", []),
        "official_guidance_links": rules.get("official_guidance_links", []),
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# 성장 전략 리포트")
    lines.append("")
    lines.append(f"- 생성 시각: `{report.get('generated_at', '')}`")
    lines.append("")
    lines.append("## 지금 가장 먼저 밀 주제")
    lines.append("")
    for item in report.get("top_opportunities", []):
        lines.append(f"- `{item['keyword']}`: {item['recommended_title']} / 점수 {item['total_score']} / 수익화 {item['monetization_score']}")
        lines.append(f"  - 이유: {item['reason']}")
        lines.append(f"  - 근거 소스: {', '.join(item.get('source_names', []))}")
    lines.append("")
    lines.append("## 카테고리 우선순위")
    lines.append("")
    for item in report.get("category_summary", []):
        lines.append(
            f"- `{item['category']}`: 우선순위 {item['weighted_priority_score']} / 게시 예정 {item['post_count']}개 / 키워드 {', '.join(item['keywords'])}"
        )
    lines.append("")
    lines.append("## 검색 수요 감지 키워드")
    lines.append("")
    if report.get("query_watchlist"):
        for item in report["query_watchlist"]:
            queries = ", ".join(item.get("query_examples", []))
            lines.append(
                f"- `{item['keyword']}`: impressions {item['impressions']}, clicks {item['clicks']}, CTR {item['ctr']}% / 예시 쿼리 {queries}"
            )
    else:
        lines.append("- Search Console 기반 쿼리 데이터가 아직 충분하지 않음")
    if report.get("trend_watchlist"):
        lines.append("")
        lines.append("## 무료 트렌드 수요 신호")
        lines.append("")
        for item in report["trend_watchlist"]:
            queries = ", ".join(item.get("trend_queries", []))
            regions = ", ".join(item.get("regions", []))
            lines.append(
                f"- `{item['keyword']}`: trend_count {item['trend_count']}, traffic_sum {item['traffic_score_sum']}, regions {regions} / 쿼리 {queries}"
            )
    lines.append("")
    lines.append("## 다음 7일 실행 포인트")
    lines.append("")
    for action in report.get("next_actions", []):
        lines.append(f"- {action}")
    lines.append("")
    lines.append("## 사람 느낌 문체 체크")
    lines.append("")
    if report.get("tone_review", {}).get("evaluated_count", 0):
        lines.append(
            f"- 평균 점수: {report.get('tone_review', {}).get('average_score', 0)} / 목표 {report.get('tone_review', {}).get('target_score', 75)}"
        )
    else:
        lines.append("- 평균 점수: 평가 가능한 실제 초안이 아직 없음")
    for checkpoint in report.get("human_style_checkpoints", []):
        lines.append(f"- {checkpoint}")
    lines.append("")
    lines.append("## 신뢰 신호 체크리스트")
    lines.append("")
    for item in report.get("trust_stack", []):
        lines.append(f"- {item}")
    lines.append("")
    lines.append("## 공식 가이드 참고")
    lines.append("")
    for item in report.get("official_guidance_links", []):
        lines.append(f"- [{item['label']}]({item['url']})")
    lines.append("")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def main() -> int:
    report = build_report()
    OUTPUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    write_markdown(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
