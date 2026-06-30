#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SEARCH_DEMAND_JSON = ROOT / "outputs/latest/search-demand-report.json"
DAILY_POST_BRIEF_JSON = ROOT / "outputs/latest/daily-post-brief.json"
REFERENCE_PATTERNS_JSON = ROOT / "config/current_editorial_reference_patterns.json"
OUTPUT_JSON = ROOT / "outputs/latest/keyword-capture-strategy.json"
OUTPUT_MD = ROOT / "outputs/latest/keyword-capture-strategy.md"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def choose_pattern(keyword: str, title: str) -> str:
    text = f"{keyword} {title}".lower()
    if any(token in text for token in ["fomc", "cpi", "pce", "jobs", "bitcoin", "ethereum", "etf", "규제"]):
        return "news_what_it_means"
    if any(token in text for token in ["faq", "체크포인트", "가이드", "정리"]):
        return "followup_checklist"
    return "search_explainer"


def choose_capture_route(keyword: str, title: str) -> str:
    text = f"{keyword} {title}".lower()
    if any(token in text for token in ["fomc", "cpi", "pce", "jobs", "bitcoin"]):
        return "breaking_to_evergreen"
    if any(token in text for token in ["big_tech", "big tech", "semiconductor", "반도체", "ai"]):
        return "sector_hub_to_followups"
    return "search_entry_to_internal_links"


def capture_route_description(route: str) -> str:
    mapping = {
        "breaking_to_evergreen": "당일 해설 글로 유입을 먼저 받고, 바로 evergreen 설명글과 FAQ형 후속 글로 내부링크를 넘깁니다.",
        "sector_hub_to_followups": "섹터 메인 해설 글을 허브로 두고 대표 종목, 공급망, ETF/지수 후속 글로 퍼뜨립니다.",
        "search_entry_to_internal_links": "검색형 진입 글에서 정의와 기준점을 설명한 뒤 관련 허브 글로 내부링크를 넘깁니다.",
    }
    return mapping.get(route, "검색형 진입 글에서 관련 해설 글로 내부링크를 넘깁니다.")


def build_report() -> dict:
    demand = load_json(SEARCH_DEMAND_JSON)
    brief = load_json(DAILY_POST_BRIEF_JSON)
    reference = load_json(REFERENCE_PATTERNS_JSON)

    demand_lookup = {
        item.get("keyword"): item for item in demand.get("ranked_keyword_demand", []) if item.get("keyword")
    }
    operating_patterns = reference.get("operating_patterns", {})

    items = []
    for post in brief.get("top_briefs", [])[:6]:
        keyword = post.get("keyword", "")
        title = (post.get("title_candidates") or [""])[0]
        pattern_name = choose_pattern(keyword, title)
        route = choose_capture_route(keyword, title)
        demand_item = demand_lookup.get(keyword, {})
        items.append(
            {
                "keyword": keyword,
                "recommended_title": title,
                "pattern_name": pattern_name,
                "pattern_rules": operating_patterns.get(pattern_name, {}),
                "capture_route": route,
                "capture_route_description": capture_route_description(route),
                "demand_signal_score": demand_item.get("demand_signal_score", 0),
                "trend_queries": demand_item.get("trend_queries", []),
                "source_names": post.get("source_names", []),
                "search_intent_angle": post.get("reason", ""),
                "outline": post.get("outline", []),
            }
        )

    return {
        "generated_at": brief.get("generated_at", demand.get("generated_at", "")),
        "items": items,
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# Keyword Capture Strategy")
    lines.append("")
    lines.append("현재 잡힌 키워드를 어떤 글 타입과 내부링크 경로로 받아먹을지 정리한 운영 카드입니다.")
    lines.append("")
    lines.append(f"- generated_at: `{report.get('generated_at', '')}`")
    lines.append("")
    for index, item in enumerate(report.get("items", []), start=1):
        lines.append(f"## {index}. {item.get('keyword', '')}")
        lines.append("")
        lines.append(f"- recommended_title: {item.get('recommended_title', '')}")
        lines.append(f"- pattern_name: `{item.get('pattern_name', '')}`")
        lines.append(f"- capture_route: `{item.get('capture_route', '')}`")
        lines.append(f"- route_description: {item.get('capture_route_description', '')}")
        lines.append(f"- demand_signal_score: `{item.get('demand_signal_score', 0)}`")
        if item.get("trend_queries"):
            lines.append(f"- trend_queries: {', '.join(item.get('trend_queries', []))}")
        lines.append(f"- search_intent_angle: {item.get('search_intent_angle', '')}")
        lines.append("- pattern_must_have:")
        for rule in item.get("pattern_rules", {}).get("must_have", []):
            lines.append(f"  - {rule}")
        lines.append("- recommended_outline:")
        for part in item.get("outline", []):
            lines.append(f"  - {part}")
        lines.append("- sources:")
        for source in item.get("source_names", [])[:5]:
            lines.append(f"  - {source}")
        lines.append("")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def main() -> int:
    report = build_report()
    OUTPUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    write_markdown(report)
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
