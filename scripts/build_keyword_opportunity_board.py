#!/usr/bin/env python3
import json
from pathlib import Path
from typing import Optional


ROOT = Path(__file__).resolve().parents[1]
BRIEF_JSON = ROOT / "outputs/latest/daily-post-brief.json"
SEARCH_DEMAND_JSON = ROOT / "outputs/latest/search-demand-report.json"
SEO_BACKLOG_JSON = ROOT / "outputs/latest/seo-backlog.json"
PUBLISH_QUEUE_JSON = ROOT / "outputs/latest/publish-queue.json"
OUTPUT_JSON = ROOT / "outputs/latest/keyword-opportunity-board.json"
OUTPUT_MD = ROOT / "outputs/latest/keyword-opportunity-board.md"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def build_queue_lookup(queue_data: dict) -> dict:
    return {item.get("keyword"): item for item in queue_data.get("items", [])}


def publish_urgency(queue_item: Optional[dict], index: int) -> str:
    if not queue_item:
        return "watch"
    bucket = queue_item.get("publish_bucket")
    if bucket == "today_or_overdue":
        return "publish_now"
    if bucket == "tomorrow":
        return "prep_today"
    if index <= 2:
        return "watch_closely"
    return "watch"


def action_note(urgency: str, brief: dict) -> str:
    if urgency == "publish_now":
        return "오늘 메인 글로 바로 발행하고, 후속 SEO 글 1~2개로 내부링크를 같이 준비합니다."
    if urgency == "prep_today":
        return "초안과 메타 설명을 오늘 마무리해 두고 다음 발행 슬롯에 올립니다."
    if urgency == "watch_closely":
        return "뉴스 업데이트를 더 보면서 제목만 빠르게 조정할 수 있게 대기합니다."
    if brief.get("trend_queries"):
        return "검색 반응을 더 본 뒤 제목형 후속 글로 빼는 편이 좋습니다."
    return "카테고리 보강용 후보로 계속 추적합니다."


def build_breaking_candidates(brief_data: dict, queue_lookup: dict) -> list[dict]:
    candidates = []
    for index, brief in enumerate(brief_data.get("top_briefs", [])[:5], start=1):
        queue_item = queue_lookup.get(brief.get("keyword"))
        urgency = publish_urgency(queue_item, index)
        candidates.append(
            {
                "rank": index,
                "keyword": brief.get("keyword", ""),
                "suggested_title": (brief.get("title_candidates") or [""])[0],
                "format": brief.get("format", ""),
                "total_score": brief.get("total_score", 0),
                "search_score": brief.get("search_score", 0),
                "demand_signal_score": brief.get("demand_signal_score", 0),
                "trend_queries": brief.get("trend_queries", []),
                "source_names": brief.get("source_names", []),
                "reason": brief.get("reason", ""),
                "urgency": urgency,
                "operator_action": action_note(urgency, brief),
                "queue_title": (queue_item or {}).get("title", ""),
                "queue_publish_date": (queue_item or {}).get("recommended_publish_date", ""),
                "queue_publish_bucket": (queue_item or {}).get("publish_bucket", ""),
                "ready_to_upload": bool((queue_item or {}).get("ready_to_upload")),
            }
        )
    return candidates


def build_seo_followups(seo_data: dict) -> list[dict]:
    items = []
    for index, item in enumerate(seo_data.get("items", [])[:6], start=1):
        items.append(
            {
                "rank": index,
                "source_keyword": item.get("source_keyword", ""),
                "title": item.get("title", ""),
                "role": item.get("role", ""),
                "post_type": item.get("post_type", ""),
                "priority_score": item.get("priority_score", 0),
                "search_intent": item.get("search_intent", ""),
                "monetization_goal": item.get("monetization_goal", ""),
                "cta_focus": item.get("cta_focus", ""),
            }
        )
    return items


def suggested_watch_title(query: str) -> str:
    cleaned = (query or "").strip()
    if not cleaned:
        cleaned = "오늘 급상승 투자 키워드"
    return f"{cleaned} 왜 검색이 급증했나: 투자자 관점 핵심 정리"


def build_watchlist(search_demand: dict) -> list[dict]:
    watchlist = []
    for item in search_demand.get("ranked_keyword_demand", [])[:5]:
        trend_queries = item.get("trend_queries", [])
        top_query = trend_queries[0] if trend_queries else item.get("keyword", "")
        watchlist.append(
            {
                "query": top_query,
                "mapped_keyword": item.get("keyword", ""),
                "query_type": "mapped_keyword_demand",
                "demand_signal_score": item.get("demand_signal_score", 0),
                "regions": item.get("regions", []),
                "suggested_title": suggested_watch_title(top_query),
                "note": "기존 핵심 키워드와 연결되어 있어 검색형 후속 글로 전환하기 좋습니다.",
            }
        )

    for item in search_demand.get("unmatched_market_trends", [])[:5]:
        watchlist.append(
            {
                "query": item.get("query", ""),
                "mapped_keyword": "",
                "query_type": "unmatched_market_trend",
                "demand_signal_score": item.get("traffic_score", 0),
                "regions": [item.get("region", "")] if item.get("region") else [],
                "suggested_title": suggested_watch_title(item.get("query", "")),
                "note": item.get("note", "시장성은 있지만 현재 핵심 키워드 묶음에 직접 연결되지 않았습니다."),
            }
        )

    watchlist.sort(
        key=lambda item: (
            0 if item.get("query_type") == "mapped_keyword_demand" else 1,
            -float(item.get("demand_signal_score", 0)),
            item.get("query", ""),
        )
    )
    return watchlist[:8]


def build_board() -> dict:
    brief_data = load_json(BRIEF_JSON)
    search_demand = load_json(SEARCH_DEMAND_JSON)
    seo_data = load_json(SEO_BACKLOG_JSON)
    queue_data = load_json(PUBLISH_QUEUE_JSON)
    queue_lookup = build_queue_lookup(queue_data)

    breaking_candidates = build_breaking_candidates(brief_data, queue_lookup)
    seo_followups = build_seo_followups(seo_data)
    query_watchlist = build_watchlist(search_demand)

    return {
        "generated_at": brief_data.get("generated_at", search_demand.get("generated_at", "")),
        "summary": {
            "breaking_candidate_count": len(breaking_candidates),
            "seo_followup_count": len(seo_followups),
            "watchlist_count": len(query_watchlist),
        },
        "breaking_candidates": breaking_candidates,
        "seo_followups": seo_followups,
        "query_watchlist": query_watchlist,
    }


def write_markdown(board: dict) -> None:
    lines = []
    lines.append("# 오늘의 키워드 기회판")
    lines.append("")
    lines.append(f"- 생성 시각: `{board.get('generated_at', '')}`")
    lines.append(f"- 당일 브레이킹 후보: `{board.get('summary', {}).get('breaking_candidate_count', 0)}`")
    lines.append(f"- SEO 후속 후보: `{board.get('summary', {}).get('seo_followup_count', 0)}`")
    lines.append(f"- 검색어 워치리스트: `{board.get('summary', {}).get('watchlist_count', 0)}`")
    lines.append("")
    lines.append("## 오늘 바로 볼 브레이킹 후보")
    lines.append("")
    for item in board.get("breaking_candidates", []):
        lines.append(f"### {item['rank']}. {item['suggested_title']}")
        lines.append("")
        lines.append(f"- keyword: {item['keyword']}")
        lines.append(f"- urgency: {item['urgency']}")
        lines.append(f"- score: {item['total_score']} / search {item['search_score']} / demand {item['demand_signal_score']}")
        lines.append(f"- ready_to_upload: {item['ready_to_upload']}")
        lines.append(f"- queue_publish: {item['queue_publish_date'] or '미정'} ({item['queue_publish_bucket'] or 'queue 없음'})")
        if item.get("trend_queries"):
            lines.append(f"- trend_queries: {', '.join(item['trend_queries'])}")
        lines.append(f"- reason: {item['reason']}")
        lines.append(f"- action: {item['operator_action']}")
        lines.append("")

    lines.append("## 검색형 후속 SEO 후보")
    lines.append("")
    for item in board.get("seo_followups", []):
        lines.append(f"### {item['rank']}. {item['title']}")
        lines.append("")
        lines.append(f"- source_keyword: {item['source_keyword']}")
        lines.append(f"- role/type: {item['role']} / {item['post_type']}")
        lines.append(f"- priority_score: {item['priority_score']}")
        lines.append(f"- search_intent: {item['search_intent']}")
        lines.append(f"- monetization_goal: {item['monetization_goal']}")
        lines.append(f"- cta_focus: {item['cta_focus']}")
        lines.append("")

    lines.append("## 검색어 워치리스트")
    lines.append("")
    for item in board.get("query_watchlist", []):
        lines.append(f"- `{item['query']}`: type {item['query_type']} / mapped {item['mapped_keyword'] or 'none'} / demand {item['demand_signal_score']} / regions {', '.join(item['regions']) or 'unknown'}")
        lines.append(f"  - suggested_title: {item['suggested_title']}")
        lines.append(f"  - note: {item['note']}")
    lines.append("")

    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def main() -> int:
    board = build_board()
    OUTPUT_JSON.write_text(json.dumps(board, ensure_ascii=False, indent=2))
    write_markdown(board)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
