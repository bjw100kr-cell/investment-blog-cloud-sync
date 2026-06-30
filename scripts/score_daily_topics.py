#!/usr/bin/env python3
import json
import re
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Dict, List, Optional


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config/investment_sources.json"
SNAPSHOT_PATH = ROOT / "outputs/latest/source-snapshot.json"
PERFORMANCE_PATH = ROOT / "outputs/latest/performance-feedback.json"
SEARCH_DEMAND_PATH = ROOT / "outputs/latest/search-demand-report.json"
CRYPTO_MARKET_SIGNAL_PATH = ROOT / "outputs/latest/crypto-market-signal.json"
OUTPUT_JSON = ROOT / "outputs/latest/daily-post-brief.json"
OUTPUT_MD = ROOT / "outputs/latest/daily-post-brief.md"


KEYWORD_PROFILES = {
    "fomc": {"explanatory": 19, "monetization": 14, "risk": 8, "format": "macro_explainer"},
    "cpi": {"explanatory": 18, "monetization": 13, "risk": 8, "format": "macro_explainer"},
    "pce": {"explanatory": 17, "monetization": 12, "risk": 8, "format": "macro_explainer"},
    "jobs": {"explanatory": 17, "monetization": 12, "risk": 8, "format": "macro_explainer"},
    "treasury_yields": {"explanatory": 18, "monetization": 13, "risk": 8, "format": "macro_explainer"},
    "dollar": {"explanatory": 16, "monetization": 11, "risk": 8, "format": "macro_explainer"},
    "oil": {"explanatory": 16, "monetization": 12, "risk": 7, "format": "macro_explainer"},
    "bitcoin": {"explanatory": 16, "monetization": 14, "risk": 5, "format": "crypto_analysis"},
    "ethereum": {"explanatory": 15, "monetization": 13, "risk": 5, "format": "crypto_analysis"},
    "crypto_etf": {"explanatory": 17, "monetization": 14, "risk": 6, "format": "crypto_analysis"},
    "tariffs_trade": {"explanatory": 18, "monetization": 13, "risk": 7, "format": "macro_explainer"},
    "china": {"explanatory": 17, "monetization": 12, "risk": 7, "format": "macro_explainer"},
    "ai_semiconductors": {"explanatory": 17, "monetization": 15, "risk": 7, "format": "sector_analysis"},
    "us_index_flow": {"explanatory": 18, "monetization": 14, "risk": 8, "format": "sector_analysis"},
    "us_big_tech": {"explanatory": 16, "monetization": 15, "risk": 7, "format": "sector_analysis"},
    "ai_growth_stocks": {"explanatory": 16, "monetization": 15, "risk": 7, "format": "sector_analysis"},
}

CATEGORY_BY_KEYWORD = {
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
    "tariffs_trade": "global-sector",
    "china": "global-sector",
    "ai_semiconductors": "global-sector",
    "us_index_flow": "global-sector",
    "us_big_tech": "global-sector",
    "ai_growth_stocks": "global-sector",
}

BRAND_LANE_BY_KEYWORD = {
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
    "tariffs_trade": "world-flow",
    "china": "world-flow",
    "ai_semiconductors": "us-stocks",
    "us_index_flow": "us-stocks",
    "us_big_tech": "us-stocks",
    "ai_growth_stocks": "us-stocks",
}

UNMATCHED_FALLBACK_LIMIT = 3

UNMATCHED_MARKET_STOPWORDS = {
    "of",
    "and",
    "the",
    "to",
    "for",
    "in",
    "on",
    "with",
    "as",
    "at",
    "what",
    "how",
    "is",
    "are",
    "a",
    "an",
    "by",
    "vs",
    "또",
    "그리고",
    "오늘",
    "이슈",
    "이란",
    "무엇",
    "시장",
    "경제",
    "뉴스",
    "핫",
    "핫이슈",
}


HTML_TAG_RE = re.compile(r"<[^>]+>")


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def load_optional_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def clean_text(value: str) -> str:
    value = HTML_TAG_RE.sub(" ", value or "")
    return re.sub(r"\s+", " ", value).strip()


def find_keywords(text: str, aliases: Dict[str, List[str]]) -> List[str]:
    haystack = text.lower()
    hits = []
    for canonical, variations in aliases.items():
        for variant in variations:
            if variant.lower() in haystack:
                hits.append(canonical)
                break
    return hits


def parse_datetime(value: str):
    if not value:
        return None
    try:
        return parsedate_to_datetime(value)
    except Exception:  # noqa: BLE001
        return None


def clamp(value: int, low: int, high: int) -> int:
    return max(low, min(high, value))


def title_from_keyword(keyword: str) -> str:
    mapping = {
        "fomc": "FOMC 이후 시장 해설",
        "cpi": "CPI 발표 이후 시장 해설",
        "pce": "PCE 발표 이후 시장 해설",
        "jobs": "고용지표 이후 시장 해설",
        "treasury_yields": "미국채 금리 변화 해설",
        "dollar": "달러 흐름 해설",
        "oil": "유가 흐름 해설",
        "bitcoin": "비트코인 핵심 흐름 해설",
        "ethereum": "이더리움 핵심 흐름 해설",
        "crypto_etf": "크립토 ETF 이슈 해설",
        "tariffs_trade": "관세와 무역 이슈 해설",
        "china": "중국 변수와 시장 영향 해설",
        "ai_semiconductors": "AI·반도체 섹터 흐름 해설",
        "us_index_flow": "미국 증시 지수 흐름 해설",
        "us_big_tech": "미국 빅테크 흐름 해설",
        "ai_growth_stocks": "AI 성장주 흐름 해설",
    }
    return mapping.get(keyword, f"{keyword} 관련 시장 해설")


def market_context_title(base: str) -> str:
    if base.endswith(("해설", "정리")):
        return f"{base}로 보는 주식·코인 흐름"
    return f"{base}와 주식·코인 흐름 함께 보기"


def make_fallback_keyword(value: str, used: set) -> str:
    cleaned = re.sub(r"[^0-9A-Za-z가-힣 ]", " ", value.lower())
    tokens = [token for token in cleaned.split() if token not in UNMATCHED_MARKET_STOPWORDS]
    if not tokens:
        base = "market_trend"
    elif len(tokens) <= 3:
        base = "_".join(tokens)
    else:
        base = "_".join(tokens[:3])

    candidate = base
    suffix = 2
    while candidate in used:
        candidate = f"{base}_{suffix}"
        suffix += 1
    return candidate


def detect_keyword_profile(value: str) -> dict:
    text = value.lower()
    if any(token in text for token in ["bitcoin", "btc", "eth", "ethereum", "crypto", "coindesk", "코인", "비트코인", "이더리움"]):
        return KEYWORD_PROFILES.get("bitcoin", {"explanatory": 16, "monetization": 14, "risk": 5, "format": "crypto_analysis"})
    if any(token in text for token in ["nasdaq", "spy", "qqq", "s&p", "stock market", "미국 증시", "나스닥"]):
        return KEYWORD_PROFILES.get("us_index_flow", {"explanatory": 18, "monetization": 14, "risk": 8, "format": "sector_analysis"})
    if any(token in text for token in ["palantir", "pltr"]):
        return KEYWORD_PROFILES.get("ai_growth_stocks", {"explanatory": 16, "monetization": 15, "risk": 7, "format": "sector_analysis"})
    if any(token in text for token in ["apple", "aapl", "microsoft", "msft", "amazon", "amzn", "meta", "tesla", "dell"]):
        return KEYWORD_PROFILES.get("us_big_tech", {"explanatory": 16, "monetization": 15, "risk": 7, "format": "sector_analysis"})
    if any(token in text for token in ["반도체", "semiconduct", "chip", "ai", "nvidia", "tsmc", "amd", "gpu", "엔비디아", "하이퍼스케일"]):
        return KEYWORD_PROFILES.get("ai_semiconductors", {"explanatory": 17, "monetization": 15, "risk": 7, "format": "sector_analysis"})
    return KEYWORD_PROFILES.get("fomc", {"explanatory": 14, "monetization": 10, "risk": 7, "format": "analysis"})


def detect_category(keyword: str, title_candidates: Optional[List[str]] = None) -> str:
    if keyword in CATEGORY_BY_KEYWORD:
        return CATEGORY_BY_KEYWORD[keyword]
    joined = " ".join(title_candidates or []).lower()
    if any(token in joined for token in ["비트코인", "이더리움", "crypto", "코인", "etf"]):
        return "crypto"
    if any(token in joined for token in ["나스닥", "빅테크", "반도체", "ai", "미국 증시", "섹터"]):
        return "global-sector"
    return "macro"


def detect_brand_lane(keyword: str, title_candidates: Optional[List[str]] = None) -> str:
    if keyword in BRAND_LANE_BY_KEYWORD:
        return BRAND_LANE_BY_KEYWORD[keyword]
    joined = " ".join(title_candidates or []).lower()
    if any(token in joined for token in ["비트코인", "이더리움", "crypto", "코인", "etf"]):
        return "crypto"
    if any(token in joined for token in ["중국", "관세", "무역", "trade", "tariff", "china", "유럽", "중동", "원자재"]):
        return "world-flow"
    if any(token in joined for token in ["나스닥", "빅테크", "반도체", "ai", "미국 증시", "섹터", "s&p", "stock", "지수"]):
        return "us-stocks"
    return "macro"


def brief_sort_key(brief: dict, use_demand_tiebreaker: bool) -> tuple:
    if use_demand_tiebreaker:
        return (-brief["total_score"], -brief["demand_signal_score"], -brief["search_score"], brief["keyword"])
    return (-brief["total_score"], -brief["search_score"], brief["keyword"])


def select_balanced_top_briefs(briefs: List[dict], mix_policy: dict, use_demand_tiebreaker: bool) -> List[dict]:
    max_items = int(mix_policy.get("top_brief_max_items", 5))
    if not briefs or max_items <= 0:
        return briefs[:max_items]

    ordered = sorted(briefs, key=lambda item: brief_sort_key(item, use_demand_tiebreaker))
    preferred_categories = [item for item in mix_policy.get("top_brief_diversity_order", []) if item]
    diversity_key = mix_policy.get("top_brief_diversity_key", "category")
    lane_caps = mix_policy.get("top_brief_lane_caps", {}) or {}

    selected: List[dict] = []
    selected_keywords = set()
    selected_by_lane: dict[str, int] = {}

    def lane_ok(item: dict) -> bool:
        lane = item.get(diversity_key, "")
        cap = lane_caps.get(lane)
        if cap is None:
            return True
        return selected_by_lane.get(lane, 0) < int(cap)

    for category in preferred_categories:
        candidate = next(
            (
                item
                for item in ordered
                if item.get(diversity_key) == category and item.get("keyword") not in selected_keywords and lane_ok(item)
            ),
            None,
        )
        if candidate is None:
            continue
        selected.append(candidate)
        selected_keywords.add(candidate.get("keyword"))
        selected_by_lane[candidate.get(diversity_key)] = selected_by_lane.get(candidate.get(diversity_key), 0) + 1
        if len(selected) >= max_items:
            return selected

    for item in ordered:
        keyword = item.get("keyword")
        if keyword in selected_keywords:
            continue
        if not lane_ok(item):
            continue
        selected.append(item)
        selected_keywords.add(keyword)
        selected_by_lane[item.get(diversity_key)] = selected_by_lane.get(item.get(diversity_key), 0) + 1
        if len(selected) >= max_items:
            break

    return selected


def compute_scores(
    keyword: str,
    items: List[dict],
    ranked_lookup: Dict[str, dict],
    naver_lookup: Dict[str, dict],
    performance_lookup: Dict[str, dict],
    demand_lookup: Dict[str, dict],
    crypto_signal_lookup: Optional[Dict[str, dict]] = None,
    strategy: Optional[dict] = None,
    profile: Optional[dict] = None,
) -> dict:
    strategy = strategy or {}
    if profile is None:
        profile = KEYWORD_PROFILES.get(keyword, {"explanatory": 14, "monetization": 10, "risk": 7, "format": "analysis"})
    source_categories = {item["source_category"] for item in items}
    official_count = sum(1 for item in items if item["source_category"] == "macro_official")
    source_count = len({item["source_name"] for item in items})
    trend_count = sum(1 for item in items if item["source_category"] == "keyword_trends")
    demand_item = demand_lookup.get(keyword, {})
    crypto_signal_item = (crypto_signal_lookup or {}).get(keyword, {})
    demand_score = int(demand_item.get("demand_signal_score", 0))
    demand_trend_count = int(demand_item.get("trend_count", 0))
    demand_bonus_divisor = int(strategy.get("demand_bonus_divisor", 250))
    max_demand_bonus = int(strategy.get("max_demand_bonus", 8))
    trend_count_weight = int(strategy.get("trend_count_weight", 3))
    trend_bonus_cap = int(strategy.get("trend_bonus_cap", 6))
    source_count_weight = int(strategy.get("source_count_weight", 2))
    source_bonus_cap = int(strategy.get("source_bonus_cap", 6))
    naver_bonus = int(strategy.get("naver_bonus", 4))
    high_demand_threshold = int(strategy.get("high_demand_threshold", 0))
    high_demand_extra_boost = int(strategy.get("high_demand_extra_boost", 0))
    demand_bonus = min(demand_score // max(demand_bonus_divisor, 1), max_demand_bonus)

    ranked_item = ranked_lookup.get(keyword, {})
    base_search = min(int(ranked_item.get("score", 0) * 0.8), 18)
    search_bonus = min(source_count * source_count_weight, source_bonus_cap) + min(trend_count * trend_count_weight, trend_bonus_cap)
    if keyword in naver_lookup:
        search_bonus += naver_bonus
    search_bonus += demand_bonus
    if high_demand_threshold and demand_score >= high_demand_threshold:
        search_bonus += high_demand_extra_boost
    search_score = clamp(base_search + search_bonus, 0, 30)

    recency_points = 0
    for item in items:
        dt = parse_datetime(item.get("published", ""))
        if dt is None:
            continue
        recency_points += 3
    timeliness_score = clamp(min(recency_points, 12) + official_count * 4 + min(source_count * 2, 9), 0, 25)

    explanatory_score = clamp(profile["explanatory"] + min(len(source_categories), 3) - (0 if official_count else 1), 0, 20)
    monetization_score = clamp(
        profile["monetization"] + min(source_count, 3) - (0 if trend_count else 1) + min(demand_trend_count, 2),
        0,
        15,
    )
    risk_score = clamp(profile["risk"] - (2 if "crypto_media" in source_categories and official_count == 0 else 0), 0, 10)
    performance_bonus = float(performance_lookup.get(keyword, {}).get("bonus", 0))
    crypto_signal_bonus = int(crypto_signal_item.get("signal_score_bonus", 0))
    total = search_score + timeliness_score + explanatory_score + monetization_score + risk_score + performance_bonus
    total += crypto_signal_bonus
    return {
        "search_score": search_score,
        "timeliness_score": timeliness_score,
        "explanatory_score": explanatory_score,
        "monetization_score": monetization_score,
        "risk_score": risk_score,
        "performance_bonus": performance_bonus,
        "search_demand_bonus": demand_bonus,
        "crypto_market_signal_bonus": crypto_signal_bonus,
        "crypto_market_sentiment": crypto_signal_item.get("market_sentiment", ""),
        "crypto_market_signal_notes": crypto_signal_item.get("market_signal_notes", []),
        "demand_signal_score": demand_score,
        "total_score": round(total, 2),
        "format": profile["format"],
    }


def summarize_reason(keyword: str, items: List[dict], scores: dict, demand_item: dict) -> str:
    sources = sorted({item["source_name"] for item in items})
    reason_parts = []
    if any(item["source_category"] == "macro_official" for item in items):
        reason_parts.append("공식 소스 기반 확인 가능")
    if any(item["source_category"] == "keyword_trends" for item in items):
        reason_parts.append("검색 트렌드 반응 존재")
    if len(sources) >= 2:
        reason_parts.append(f"복수 소스 교차 확인 가능 ({len(sources)}개)")
    if keyword in {"bitcoin", "ethereum", "crypto_etf"}:
        reason_parts.append("코인 독자 유입과 재방문 가능성")
        if scores.get("crypto_market_signal_bonus", 0) > 0:
            sentiment = scores.get("crypto_market_sentiment") or "market signal"
            reason_parts.append(f"코인 시장 신호 반영 ({sentiment})")
    if keyword in {"fomc", "cpi", "pce", "jobs", "treasury_yields", "dollar", "oil"}:
        reason_parts.append("거시 해설형 글로 전환 가치 높음")
    if keyword in {"ai_semiconductors", "china", "tariffs_trade"}:
        reason_parts.append("섹터/세계 흐름 연결 해설 가능")
    if keyword in {"us_index_flow", "us_big_tech", "ai_growth_stocks"}:
        reason_parts.append("검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능")
    if any(item.get("transcript_available") for item in items):
        reason_parts.append("유튜브 해설 맥락까지 확보 가능")
    trend_queries = demand_item.get("trend_queries", [])
    if trend_queries:
        reason_parts.append(f"실제 급상승 검색어 반영 ({', '.join(trend_queries[:2])})")
    if not reason_parts:
        reason_parts.append("설명형 시장 글로 전환 가능")
    return ", ".join(reason_parts)


def extract_reference_takeaways(items: List[dict], limit: int = 4) -> List[str]:
    strong_keywords = (
        "비트코인",
        "이더리움",
        "코인",
        "btc",
        "etf",
        "유동성",
        "금리",
        "달러",
        "연준",
        "fomc",
        "cpi",
        "증시",
        "주식",
        "반도체",
        "관세",
        "무역",
        "규제",
        "온체인",
        "자금",
        "수급",
    )
    weak_markers = (
        "오늘 조금 다른 얘기",
        "허니팟",
        "저 더 안 하잖아요",
        "잠깐만",
        "모자",
        "앞머리",
        "구독하시는 분",
        "썰을",
        "살 수 있는데",
        "어떡하죠",
    )

    takeaways = []
    seen = set()
    for item in items:
        for point in item.get("transcript_digest_points", []):
            normalized = point.strip()
            if not normalized or normalized in seen:
                continue
            lowered = normalized.lower()
            if len(normalized) < 14:
                continue
            if any(marker in normalized for marker in weak_markers):
                continue
            if not any(keyword in lowered for keyword in strong_keywords):
                continue
            seen.add(normalized)
            takeaways.append(normalized)
            if len(takeaways) >= limit:
                return takeaways
    return takeaways


def build_outline(keyword: str, scores: dict) -> List[str]:
    if scores["format"] == "macro_explainer":
        return [
            "왜 지금 이 이슈가 중요한가",
            "실제로 발표되거나 벌어진 일",
            "주식·코인·달러·금리에 주는 영향",
            "앞으로 체크할 변수",
            "개인 투자자가 볼 포인트",
        ]
    if scores["format"] == "crypto_analysis":
        return [
            "오늘 코인 시장 핵심 변화",
            "가격이 아니라 구조상 중요한 포인트",
            "ETF/유동성/규제/온체인과의 연결",
            "강세 시나리오와 리스크",
            "내일 확인할 체크포인트",
        ]
    if scores["format"] == "sector_analysis":
        return [
            "지금 이 섹터가 왜 움직이는가",
            "핵심 뉴스와 시장 반응",
            "대표 종목과 자금 흐름",
            "거시 변수와 연결",
            "다음 실적/정책 이벤트",
        ]
    return [
        "무슨 일이 있었나",
        "왜 중요한가",
        "시장 반응은 무엇인가",
        "앞으로 볼 변수",
        "독자 체크포인트",
    ]


def build_synthetic_fallback_items(trend_item: dict) -> List[dict]:
    return [
        {
            "title": trend_item.get("query", ""),
            "description": "",
            "transcript_excerpt": "",
            "transcript_digest_points": [],
            "source_name": f"{trend_item.get('source_name', 'trends')} ({trend_item.get('region', 'global')})",
            "source_category": "keyword_trends",
            "published": trend_item.get("published", ""),
            "transcript_available": False,
        }
    ]


def build_fallback_title_candidates(raw_query: str) -> List[str]:
    base = raw_query.strip()[:48] if raw_query else "금융 시장"
    if not base:
        base = "금융 시장"
    return [
        f"{base} 관련 시장 해설",
        f"{base}와 주식·코인 영향 체크",
        f"{base} 핵심 포인트 정리",
    ]


def make_title_candidates(keyword: str) -> List[str]:
    base = title_from_keyword(keyword)
    return [
        base,
        f"{base}: 지금 시장이 반응하는 이유",
        market_context_title(base),
    ]


def main() -> int:
    config = load_json(CONFIG_PATH)
    snapshot = load_json(SNAPSHOT_PATH)
    performance = load_optional_json(PERFORMANCE_PATH)
    search_demand = load_optional_json(SEARCH_DEMAND_PATH)
    crypto_market_signal = load_optional_json(CRYPTO_MARKET_SIGNAL_PATH)
    aliases = config["keyword_aliases"]
    unmatched_fallback = (search_demand or {}).get("unmatched_market_trends", [])

    keyword_items = {}
    for candidate in snapshot["topic_candidates"]:
        keyword = candidate["keyword"]
        matches = []
        for item in snapshot["items"]:
            hits = find_keywords(f"{item['title']} {item.get('description', '')} {item.get('transcript_excerpt', '')}", aliases)
            if keyword in hits:
                matches.append(item)
        keyword_items[keyword] = matches

    ranked_lookup = {item["keyword"]: item for item in snapshot["ranked_keywords"]}
    naver_lookup = {item["keyword"]: item for item in (snapshot.get("naver_datalab") or {}).get("ranked", [])}
    performance_lookup = (performance or {}).get("keyword_feedback", {})
    demand_lookup = {item["keyword"]: item for item in (search_demand or {}).get("ranked_keyword_demand", [])}
    crypto_signal_lookup = (crypto_market_signal or {}).get("keyword_signals", {})
    growth_rules = load_optional_json(ROOT / "config/growth_rules.json")
    search_strategy = growth_rules.get("search_first_strategy", {})
    topic_mix_policy = growth_rules.get("topic_mix_policy", {})
    brand_lane_labels = topic_mix_policy.get("brand_lane_labels", {})

    briefs = []
    used_keywords = set()
    for keyword, items in keyword_items.items():
        if not items:
            continue
        scores = compute_scores(
            keyword,
            items,
            ranked_lookup,
            naver_lookup,
            performance_lookup,
            demand_lookup,
            crypto_signal_lookup,
            strategy=search_strategy,
        )
        demand_item = demand_lookup.get(keyword, {})
        briefs.append(
            {
                "keyword": keyword,
                "category": detect_category(keyword, make_title_candidates(keyword)),
                "brand_lane": detect_brand_lane(keyword, make_title_candidates(keyword)),
                "title_candidates": make_title_candidates(keyword),
                "reason": summarize_reason(keyword, items, scores, demand_item),
                "outline": build_outline(keyword, scores),
                "sample_headlines": [clean_text(item["title"]) for item in items[:5]],
                "reference_takeaways": extract_reference_takeaways(items),
                "source_names": sorted({item["source_name"] for item in items}),
                "trend_queries": demand_item.get("trend_queries", []),
                "trend_regions": demand_item.get("regions", []),
                "fallback_source": "mapped_candidate",
                "demand_signal_score": demand_item.get("demand_signal_score", 0),
                **scores,
            }
        )
        used_keywords.add(keyword)

    if len(briefs) < 5 and unmatched_fallback:
        for unmatched in unmatched_fallback:
            if len(briefs) >= 5:
                break
            query = unmatched.get("query", "")
            if not query:
                continue
            synthetic_keyword = make_fallback_keyword(query, used_keywords)
            items = build_synthetic_fallback_items(unmatched)
            profile = detect_keyword_profile(query)
            synthetic_demand = {
                "trend_queries": [query],
                "regions": [unmatched.get("region", "global")],
                "demand_signal_score": unmatched.get("traffic_score", 0) + 200,
                "max_approx_traffic": unmatched.get("traffic_score", 0),
            }
            scores = compute_scores(
                synthetic_keyword,
                items,
                ranked_lookup,
                naver_lookup,
                performance_lookup,
                {synthetic_keyword: synthetic_demand},
                crypto_signal_lookup,
                strategy=search_strategy,
                profile=profile,
            )
            briefs.append(
                {
                    "keyword": synthetic_keyword,
                    "category": detect_category(synthetic_keyword, build_fallback_title_candidates(query)),
                    "brand_lane": detect_brand_lane(synthetic_keyword, build_fallback_title_candidates(query)),
                    "title_candidates": build_fallback_title_candidates(query),
                    "reason": f"급상승 검색어 직접 감지: {query}",
                    "outline": build_outline(synthetic_keyword, scores),
                    "sample_headlines": [query],
                    "reference_takeaways": [],
                    "source_names": [items[0]["source_name"]],
                    "trend_queries": [query],
                    "trend_regions": [unmatched.get("region", "global")],
                    "fallback_source": "unmatched_market_trend",
                    "demand_signal_score": synthetic_demand["demand_signal_score"],
                    **scores,
                }
            )
            used_keywords.add(synthetic_keyword)
            if len(briefs) >= 5:
                break

    if not briefs and unmatched_fallback:
        query = unmatched_fallback[0].get("query", "")
        synthetic_keyword = make_fallback_keyword(query or "market_overview", used_keywords)
        synthetic_demand = {
            "trend_queries": [query] if query else [],
            "regions": [unmatched_fallback[0].get("region", "global")],
            "demand_signal_score": unmatched_fallback[0].get("traffic_score", 0) + 100,
            "max_approx_traffic": unmatched_fallback[0].get("traffic_score", 0),
        }
        items = build_synthetic_fallback_items(unmatched_fallback[0]) if unmatched_fallback else []
        scores = compute_scores(
            synthetic_keyword,
            items or [{
                "title": "금융 시장",
                "description": "",
                "transcript_excerpt": "",
                "transcript_digest_points": [],
                "source_name": "trends",
                "source_category": "keyword_trends",
                "published": "",
                "transcript_available": False,
            }],
            ranked_lookup,
            naver_lookup,
            performance_lookup,
            {synthetic_keyword: synthetic_demand},
            strategy=search_strategy,
            profile=KEYWORD_PROFILES.get("fomc"),
        )
        briefs.append(
            {
                "keyword": synthetic_keyword,
                "category": detect_category(synthetic_keyword),
                "brand_lane": detect_brand_lane(synthetic_keyword, ["금융시장 흐름 해설"]),
                "title_candidates": ["금융시장 흐름 해설", "오늘 시장 해설 한 번에 정리", "주식·코인에 바로 쓰일 시장 체크포인트"],
                "reason": f"매칭된 후보가 없어서 급상승 검색 트렌드를 기반으로 기본 해설 글을 준비했습니다: {query or '시장 흐름 정리'}",
                "outline": build_outline(synthetic_keyword, scores),
                "sample_headlines": [query] if query else ["금융시장 최근 동향 요약"],
                "reference_takeaways": [],
                "source_names": [items[0]["source_name"]] if items else ["Google Trends"],
                "trend_queries": synthetic_demand["trend_queries"],
                "trend_regions": synthetic_demand["regions"],
                "fallback_source": "default_trend_backup",
                "demand_signal_score": synthetic_demand["demand_signal_score"],
                **scores,
            }
        )
        used_keywords.add(synthetic_keyword)

    if not briefs:
        emergency_keyword = "market_snapshot"
        emergency_demand = {
            "trend_queries": ["오늘의 시장 흐름 핵심 정리"],
            "regions": ["global"],
            "demand_signal_score": 0,
            "max_approx_traffic": 0,
        }
        emergency_items = [
            {
                "title": "오늘의 시장 흐름 체크",
                "description": "",
                "transcript_excerpt": "",
                "transcript_digest_points": [],
                "source_name": "system_fallback",
                "source_category": "keyword_trends",
                "published": "",
                "transcript_available": False,
            }
        ]
        emergency_scores = compute_scores(
            emergency_keyword,
            emergency_items,
            ranked_lookup,
            naver_lookup,
            performance_lookup,
            {emergency_keyword: emergency_demand},
            crypto_signal_lookup,
            strategy=search_strategy,
            profile=KEYWORD_PROFILES.get("fomc"),
        )
        briefs.append(
            {
                "keyword": emergency_keyword,
                "category": "macro",
                "brand_lane": "macro",
                "title_candidates": ["오늘 시장 흐름 해설", "오늘 주식·코인 핵심 체크포인트", "한눈에 보는 글로벌 투자 이슈"],
                "reason": "데이터 소스가 적은 날의 운영 안정성을 위해 기본 시장 흐름 해설을 준비했습니다.",
                "outline": build_outline(emergency_keyword, emergency_scores),
                "sample_headlines": ["오늘의 글로벌 투자 흐름 정리"],
                "reference_takeaways": [],
                "source_names": ["system_fallback"],
                "trend_queries": emergency_demand["trend_queries"],
                "trend_regions": emergency_demand["regions"],
                "fallback_source": "emergency_default",
                "demand_signal_score": emergency_demand["demand_signal_score"],
                **emergency_scores,
            }
        )

    use_demand_tiebreaker = bool(search_strategy.get("sort_tiebreaker_use_demand", True))
    if use_demand_tiebreaker:
        briefs.sort(key=lambda x: (-x["total_score"], -x["demand_signal_score"], -x["search_score"], x["keyword"]))
    else:
        briefs.sort(key=lambda x: (-x["total_score"], -x["search_score"], x["keyword"]))

    top_briefs = select_balanced_top_briefs(briefs, topic_mix_policy, use_demand_tiebreaker)

    payload = {
        "generated_at": snapshot["generated_at"],
        "topic_mix_policy": topic_mix_policy,
        "top_briefs": top_briefs,
    }
    OUTPUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2))

    lines = []
    lines.append("# 오늘의 포스팅 브리프")
    lines.append("")
    lines.append(f"- 생성 시각: `{snapshot['generated_at']}`")
    lines.append("")
    if topic_mix_policy.get("identity_statement"):
        lines.append(f"- 정체성 규칙: {topic_mix_policy.get('identity_statement', '')}")
        lines.append("")
    for idx, brief in enumerate(payload["top_briefs"], start=1):
        lines.append(f"## {idx}. {brief['keyword']}")
        lines.append("")
        lines.append(f"- 카테고리: `{brief.get('category', 'macro')}`")
        lane_key = brief.get("brand_lane", brief.get("category", "macro"))
        lines.append(f"- 브랜드 레인: `{lane_key}` ({brand_lane_labels.get(lane_key, lane_key)})")
        lines.append(f"- 총점: `{brief['total_score']}`")
        lines.append(
            f"- 점수 구성: 검색성 {brief['search_score']} / 시의성 {brief['timeliness_score']} / 설명가치 {brief['explanatory_score']} / 수익성 {brief['monetization_score']} / 리스크역점수 {brief['risk_score']} / 성과보너스 {brief['performance_bonus']} / 트렌드보너스 {brief['search_demand_bonus']} / 코인시장신호 {brief.get('crypto_market_signal_bonus', 0)}"
        )
        lines.append(f"- 추천 이유: {brief['reason']}")
        if brief.get("crypto_market_signal_notes"):
            lines.append(f"- 코인 시장 신호: {'; '.join(brief['crypto_market_signal_notes'][:3])}")
        lines.append(f"- 소스: {', '.join(brief['source_names'])}")
        if brief.get("trend_queries"):
            lines.append(f"- 트렌드 쿼리: {', '.join(brief['trend_queries'])}")
        lines.append("- 제목 후보:")
        for title in brief["title_candidates"]:
            lines.append(f"  - {title}")
        lines.append("- 글 구조:")
        for line in brief["outline"]:
            lines.append(f"  - {line}")
        lines.append("- 참고 헤드라인:")
        for headline in brief["sample_headlines"]:
            lines.append(f"  - {headline}")
        lines.append("")

    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
