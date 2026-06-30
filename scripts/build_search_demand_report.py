#!/usr/bin/env python3
import json
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config/investment_sources.json"
GROWTH_RULES_PATH = ROOT / "config/growth_rules.json"
SNAPSHOT_PATH = ROOT / "outputs/latest/source-snapshot.json"
OUTPUT_JSON = ROOT / "outputs/latest/search-demand-report.json"
OUTPUT_MD = ROOT / "outputs/latest/search-demand-report.md"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def find_keywords(text: str, aliases: dict) -> list[str]:
    haystack = text.lower()
    hits = []
    for canonical, variations in aliases.items():
        for variation in variations:
            if variation.lower() in haystack:
                hits.append(canonical)
                break
    return hits


def extract_traffic_score(value: str) -> int:
    digits = re.sub(r"[^0-9]", "", value or "")
    if not digits:
        return 0
    return int(digits)


def source_region(name: str, item: dict) -> str:
    if " KR" in name or item.get("source_id", "").endswith("_kr"):
        return "KR"
    if " US" in name or item.get("source_id", "").endswith("_us"):
        return "US"
    return "unknown"


def normalize_trend_item(item: dict, aliases: dict) -> dict:
    title = (item.get("title") or "").strip()
    hits = find_keywords(f"{title} {item.get('description', '')}", aliases)
    return {
        "query": title,
        "region": source_region(item.get("source_name", ""), item),
        "approx_traffic": item.get("approx_traffic", ""),
        "traffic_score": extract_traffic_score(item.get("approx_traffic", "")),
        "published": item.get("published", ""),
        "matched_keywords": hits,
        "source_name": item.get("source_name", ""),
    }


def market_relevance_score(query: str, market_terms: list[str]) -> int:
    haystack = (query or "").lower()
    score = 0
    for term in market_terms:
        needle = term.lower().strip()
        if not needle:
            continue
        if re.search(r"[a-z0-9]", needle):
            pattern = r"(?<![a-z0-9])" + re.escape(needle) + r"(?![a-z0-9])"
            if re.search(pattern, haystack):
                score += 1
        elif needle in haystack:
            score += 1
    return score


def matches_any_term(query: str, terms: list[str]) -> bool:
    haystack = (query or "").lower()
    return any(term.lower() in haystack for term in terms if term)


def within_brand_identity(query: str, guardrails: dict) -> bool:
    focus_terms = guardrails.get("primary_focus_terms", [])
    equity_terms = guardrails.get("preferred_equity_queries", [])
    return matches_any_term(query, focus_terms) or matches_any_term(query, equity_terms)


def build_weak_trend_fallback_ranked_keywords(snapshot: dict, ranked_keywords: list[dict], matched_keywords: set[str], strategy: dict) -> list[dict]:
    minimum_matches = int(strategy.get("weak_trend_min_matched_keywords", 3))
    if len(matched_keywords) >= minimum_matches:
        return []

    score_min = int(strategy.get("weak_trend_fallback_source_score_min", 8))
    limit = int(strategy.get("weak_trend_fallback_keyword_limit", 4))
    base_demand = int(strategy.get("weak_trend_fallback_demand_base", 1200))
    items_by_keyword = {}
    for item in snapshot.get("items", []):
        items_by_keyword.setdefault(item.get("keyword", ""), []).append(item)

    fallback = []
    for item in ranked_keywords:
        keyword = item.get("keyword", "")
        score = int(item.get("score", 0))
        if not keyword or keyword in matched_keywords or score < score_min:
            continue
        sources = item.get("sources", [])
        sample_titles = item.get("sample_titles", [])
        fallback.append(
            {
                "keyword": keyword,
                "trend_count": 0,
                "traffic_score_sum": 0,
                "max_approx_traffic": 0,
                "trend_queries": [],
                "regions": [],
                "demand_signal_score": base_demand + (score * 100),
                "fallback_source": "source_snapshot_rank",
                "source_snapshot_score": score,
                "source_count": int(item.get("source_count", 0)),
                "source_names": sources[:5],
                "sample_titles": sample_titles[:3],
            }
        )
        if len(fallback) >= limit:
            break
    return fallback


def build_report() -> dict:
    config = load_json(CONFIG_PATH)
    growth_rules = load_json(GROWTH_RULES_PATH)
    snapshot = load_json(SNAPSHOT_PATH)
    aliases = config.get("keyword_aliases", {})
    guardrails = config.get("brand_identity_guardrails", {})
    search_strategy = growth_rules.get("search_first_strategy", {})
    market_terms = config.get(
        "trend_market_terms",
        [
            "stock",
            "stocks",
            "market",
            "mortgage",
            "rate",
            "rates",
            "oil",
            "crude",
            "bitcoin",
            "ethereum",
            "coin",
            "crypto",
            "fed",
            "federal reserve",
            "jp모건",
            "jpmorgan",
            "trade",
            "tariff",
            "china",
            "semiconductor",
            "chip",
            "ai",
            "anthropic",
            "유조선",
            "원유",
            "달러",
            "금리",
            "환율",
            "비트코인",
            "이더리움",
            "반도체",
            "엔비디아",
            "중국",
            "관세",
            "무역",
            "증시",
            "주식",
        ],
    )

    trend_items = [
        normalize_trend_item(item, aliases)
        for item in snapshot.get("items", [])
        if item.get("source_category") == "keyword_trends"
    ]

    per_keyword = defaultdict(
        lambda: {
            "trend_count": 0,
            "traffic_score_sum": 0,
            "max_approx_traffic": 0,
            "trend_queries": [],
            "regions": set(),
        }
    )
    unmatched_market_trends = []

    for item in trend_items:
        if item["matched_keywords"]:
            for keyword in item["matched_keywords"]:
                entry = per_keyword[keyword]
                entry["trend_count"] += 1
                entry["traffic_score_sum"] += item["traffic_score"]
                entry["max_approx_traffic"] = max(entry["max_approx_traffic"], item["traffic_score"])
                entry["regions"].add(item["region"])
                if item["query"] not in entry["trend_queries"]:
                    entry["trend_queries"].append(item["query"])
        else:
            relevance = market_relevance_score(item["query"], market_terms)
            if (
                relevance >= int(guardrails.get("minimum_unmatched_market_relevance", 1))
                and item["traffic_score"] >= int(guardrails.get("minimum_unmatched_traffic_score", 0))
                and within_brand_identity(item["query"], guardrails)
            ):
                unmatched_market_trends.append(
                    {
                        "query": item["query"],
                        "region": item["region"],
                        "approx_traffic": item["approx_traffic"],
                        "traffic_score": item["traffic_score"],
                        "market_relevance_score": relevance,
                        "brand_identity_match": True,
                        "note": "시장/투자 관련 가능성이 있지만 현재 키워드 묶음에 직접 매핑되지 않음",
                    }
                )

    ranked_keywords = []
    for keyword, info in per_keyword.items():
        ranked_keywords.append(
            {
                "keyword": keyword,
                "trend_count": info["trend_count"],
                "traffic_score_sum": info["traffic_score_sum"],
                "max_approx_traffic": info["max_approx_traffic"],
                "trend_queries": info["trend_queries"][:5],
                "regions": sorted(info["regions"]),
                "demand_signal_score": info["traffic_score_sum"] + (info["trend_count"] * 200),
                "fallback_source": "trend_match",
            }
        )

    ranked_keywords.sort(
        key=lambda item: (-item["demand_signal_score"], -item["traffic_score_sum"], item["keyword"])
    )
    weak_trend_fallback = build_weak_trend_fallback_ranked_keywords(
        snapshot,
        snapshot.get("ranked_keywords", []),
        {item["keyword"] for item in ranked_keywords},
        search_strategy,
    )
    ranked_keywords.extend(weak_trend_fallback)
    unmatched_market_trends.sort(
        key=lambda item: (-item["market_relevance_score"], -item["traffic_score"], item["query"])
    )

    return {
        "generated_at": snapshot.get("generated_at", ""),
        "summary": {
            "trend_item_count": len(trend_items),
            "matched_keyword_count": len(ranked_keywords),
            "unmatched_market_trend_count": len(unmatched_market_trends),
            "weak_trend_fallback_count": len(weak_trend_fallback),
        },
        "ranked_keyword_demand": ranked_keywords,
        "unmatched_market_trends": unmatched_market_trends[:10],
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# 검색 수요 신호 리포트")
    lines.append("")
    lines.append(f"- 생성 시각: `{report.get('generated_at', '')}`")
    lines.append(f"- 트렌드 아이템 수: `{report.get('summary', {}).get('trend_item_count', 0)}`")
    lines.append(f"- 매칭된 키워드 수: `{report.get('summary', {}).get('matched_keyword_count', 0)}`")
    lines.append(f"- 약한 트렌드 fallback 수: `{report.get('summary', {}).get('weak_trend_fallback_count', 0)}`")
    lines.append("")
    lines.append("## 키워드별 트렌드 수요")
    lines.append("")
    if report.get("ranked_keyword_demand"):
        for item in report["ranked_keyword_demand"]:
            lines.append(
                f"- `{item['keyword']}`: demand {item['demand_signal_score']} / trend_count {item['trend_count']} / traffic_sum {item['traffic_score_sum']} / regions {', '.join(item['regions'])}"
            )
            if item.get("fallback_source") == "source_snapshot_rank":
                lines.append(
                    f"  - fallback: source snapshot score {item.get('source_snapshot_score', 0)} / sources {', '.join(item.get('source_names', []))}"
                )
            for query in item.get("trend_queries", []):
                lines.append(f"  - trend query: {query}")
    else:
        lines.append("- 현재 직접 매칭된 트렌드 쿼리가 없음")
    lines.append("")
    lines.append("## 아직 못 주운 시장성 트렌드")
    lines.append("")
    if report.get("unmatched_market_trends"):
        for item in report["unmatched_market_trends"]:
            lines.append(
                f"- `{item['query']}` ({item['region']}): traffic {item['approx_traffic']} / relevance {item['market_relevance_score']}"
            )
    else:
        lines.append("- 현재 추가 분류가 필요한 시장성 트렌드가 없음")
    lines.append("")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def main() -> int:
    report = build_report()
    OUTPUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    write_markdown(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
