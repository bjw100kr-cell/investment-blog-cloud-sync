#!/usr/bin/env python3
import json
from email.utils import parsedate_to_datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
USER_REVIEW_SHORTLIST_JSON = ROOT / "outputs/latest/user-review-shortlist.json"
DAILY_POST_BRIEF_JSON = ROOT / "outputs/latest/daily-post-brief.json"
SEARCH_DEMAND_REPORT_JSON = ROOT / "outputs/latest/search-demand-report.json"
SOURCE_SNAPSHOT_JSON = ROOT / "outputs/latest/source-snapshot.json"
SOURCE_CONFIG_JSON = ROOT / "config/investment_sources.json"
OUTPUT_JSON = ROOT / "outputs/latest/approval-evidence-sheet.json"
OUTPUT_MD = ROOT / "outputs/latest/approval-evidence-sheet.md"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def build_lookup(items: list[dict], key: str) -> dict:
    return {item.get(key): item for item in items if item.get(key)}


def normalize_text(text: str) -> str:
    if not text:
        return ""
    repaired = text
    if "â" in repaired or "Ã" in repaired:
        try:
            repaired = repaired.encode("latin-1").decode("utf-8")
        except (UnicodeEncodeError, UnicodeDecodeError):
            pass
    return " ".join(repaired.split()).strip()


def parse_published(value: str) -> str:
    if not value:
        return ""
    try:
        return parsedate_to_datetime(value).isoformat()
    except (TypeError, ValueError, IndexError):
        return value


def keyword_alias_lookup() -> dict[str, list[str]]:
    payload = load_json(SOURCE_CONFIG_JSON)
    aliases = payload.get("keyword_aliases", {})
    return {
        keyword: [alias.lower() for alias in alias_list if alias]
        for keyword, alias_list in aliases.items()
    }


def recent_evidence_for_keyword(keyword: str, source_items: list[dict], alias_lookup: dict[str, list[str]]) -> list[dict]:
    aliases = alias_lookup.get(keyword, [])
    matches = []
    seen = set()

    for item in source_items:
        title = normalize_text(item.get("title", ""))
        title_lower = title.lower()
        if not title or not any(alias in title_lower for alias in aliases):
            continue
        link = item.get("link", "")
        dedupe_key = (title.lower(), link)
        if dedupe_key in seen:
            continue
        seen.add(dedupe_key)
        matches.append(
            {
                "title": title,
                "source_name": item.get("source_name", ""),
                "published": item.get("published", ""),
                "published_iso": parse_published(item.get("published", "")),
                "link": link,
                "source_type": item.get("source_type", ""),
            }
        )

    def rank(item: dict) -> tuple:
        title_lower = item.get("title", "").lower()
        keyword_boost = 1 if keyword.lower() in title_lower else 0
        official_boost = 1 if item.get("source_name") == "Federal Reserve Monetary Policy Press" else 0
        trend_boost = 1 if item.get("source_name") == "Google Trends KR" else 0
        return (keyword_boost, official_boost, trend_boost, item.get("published_iso", ""), item.get("title", ""))

    matches.sort(key=rank, reverse=True)
    return matches[:5]


def build_report() -> dict:
    shortlist = load_json(USER_REVIEW_SHORTLIST_JSON)
    brief = load_json(DAILY_POST_BRIEF_JSON)
    demand = load_json(SEARCH_DEMAND_REPORT_JSON)
    source_snapshot = load_json(SOURCE_SNAPSHOT_JSON)
    alias_lookup = keyword_alias_lookup()

    brief_lookup = build_lookup(brief.get("top_briefs", []), "keyword")
    demand_lookup = build_lookup(demand.get("ranked_keyword_demand", []), "keyword")

    items = []
    for card in shortlist.get("shortlist", []):
        keyword = card.get("keyword", "")
        brief_item = brief_lookup.get(keyword, {})
        demand_item = demand_lookup.get(keyword, {})
        sample_headlines = []
        seen_headlines = set()
        for headline in brief_item.get("sample_headlines", []):
            cleaned = normalize_text(headline)
            if not cleaned:
                continue
            dedupe_key = cleaned.lower()
            if dedupe_key in seen_headlines:
                continue
            seen_headlines.add(dedupe_key)
            sample_headlines.append(cleaned)
        items.append(
            {
                "keyword": keyword,
                "title": card.get("title", ""),
                "publish_date": card.get("publish_date", ""),
                "priority_score": card.get("priority_score", 0),
                "ready_now": card.get("ready_now", False),
                "quality_status": card.get("quality_status", ""),
                "reason": brief_item.get("reason", ""),
                "format": brief_item.get("format", ""),
                "source_names": brief_item.get("source_names", []),
                "sample_headlines": sample_headlines[:5],
                "trend_queries": brief_item.get("trend_queries", []),
                "trend_regions": brief_item.get("trend_regions", []),
                "demand_signal_score": demand_item.get("demand_signal_score", brief_item.get("demand_signal_score", 0)),
                "fallback_source": demand_item.get("fallback_source", brief_item.get("fallback_source", "")),
                "source_count": demand_item.get("source_count", len(brief_item.get("source_names", []))),
                "search_score": brief_item.get("search_score", 0),
                "timeliness_score": brief_item.get("timeliness_score", 0),
                "monetization_score": brief_item.get("monetization_score", 0),
                "recent_evidence": recent_evidence_for_keyword(keyword, source_snapshot.get("items", []), alias_lookup),
            }
        )

    return {
        "generated_at": brief.get("generated_at", ""),
        "item_count": len(items),
        "items": items,
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# Approval Evidence Sheet")
    lines.append("")
    lines.append("사용자가 초안을 최종 확인하기 전에, 왜 이 글이 오늘 올라올 가치가 있는지 근거를 빠르게 보는 시트입니다.")
    lines.append("- 원칙: 초안 내용과 함께 근거 소스, 검색 수요, 시의성을 같이 보고 최종 확인합니다.")
    if report.get("generated_at"):
        lines.append(f"- generated_at: `{report.get('generated_at', '')}`")
    lines.append(f"- item_count: `{report.get('item_count', 0)}`")
    lines.append("")

    for index, item in enumerate(report.get("items", []), start=1):
        lines.append(f"## {index}. {item.get('title', '')}")
        lines.append("")
        lines.append(f"- keyword: `{item.get('keyword', '')}`")
        lines.append(f"- publish_date: `{item.get('publish_date', '')}`")
        lines.append(f"- priority_score: `{item.get('priority_score', 0)}`")
        lines.append(f"- ready_now: `{item.get('ready_now', False)}` / quality_status `{item.get('quality_status', '')}`")
        lines.append(f"- reason: {item.get('reason', '')}")
        lines.append(f"- format: `{item.get('format', '')}`")
        lines.append(f"- demand_signal_score: `{item.get('demand_signal_score', 0)}`")
        lines.append(f"- fallback_source: `{item.get('fallback_source', '')}`")
        lines.append(f"- source_count: `{item.get('source_count', 0)}`")
        lines.append(
            f"- score_breakdown: search `{item.get('search_score', 0)}` / timeliness `{item.get('timeliness_score', 0)}` / monetization `{item.get('monetization_score', 0)}`"
        )
        if item.get("trend_queries"):
            lines.append(f"- trend_queries: {', '.join(item.get('trend_queries', []))}")
        if item.get("trend_regions"):
            lines.append(f"- trend_regions: {', '.join(item.get('trend_regions', []))}")
        if item.get("source_names"):
            lines.append(f"- source_names: {', '.join(item.get('source_names', []))}")
        if item.get("sample_headlines"):
            lines.append("- sample_headlines:")
            for headline in item.get("sample_headlines", []):
                lines.append(f"  - {headline}")
        if item.get("recent_evidence"):
            lines.append("- recent_evidence:")
            for evidence in item.get("recent_evidence", []):
                published = evidence.get("published_iso") or evidence.get("published", "")
                lines.append(
                    f"  - {evidence.get('source_name', '')} | {published} | {evidence.get('title', '')} | {evidence.get('link', '')}"
                )
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
