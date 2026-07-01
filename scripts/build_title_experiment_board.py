#!/usr/bin/env python3
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DAILY_BRIEF_JSON = ROOT / "outputs/latest/daily-post-brief.json"
KEYWORD_BOARD_JSON = ROOT / "outputs/latest/keyword-opportunity-board.json"
CRYPTO_MARKET_SIGNAL_JSON = ROOT / "outputs/latest/crypto-market-signal.json"
PUBLISH_INVENTORY_JSON = ROOT / "outputs/latest/publish-inventory.json"
BLOGGER_STATE_JSON = ROOT / "outputs/latest/blogger-upload-state.json"
OUTPUT_JSON = ROOT / "outputs/latest/title-experiment-board.json"
OUTPUT_MD = ROOT / "outputs/latest/title-experiment-board.md"


PATTERN_BY_LANE = {
    "macro": [
        "{topic}, 지금 주식과 코인이 같이 흔들리는 이유",
        "{topic} 체크포인트 3가지: 금리, 달러, 위험자산",
        "{topic}을 투자자가 봐야 하는 이유: 오늘 확인할 숫자들",
    ],
    "crypto": [
        "{topic} 가격보다 먼저 볼 것: ETF 자금과 달러 흐름",
        "{topic}, 공포 구간에서 확인할 리스크 체크포인트 5가지",
        "{topic} 투자자가 오늘 놓치면 안 되는 규제와 자금 흐름",
    ],
    "us-stocks": [
        "{topic}, 나스닥과 빅테크가 같이 움직이는 이유",
        "{topic} 체크포인트: 금리, 실적, 섹터 폭을 같이 봐야 하는 이유",
        "{topic}이 내 주식 계좌에 주는 신호 3가지",
    ],
    "world-flow": [
        "{topic}, 환율과 원자재까지 같이 봐야 하는 이유",
        "{topic}이 시장에 번지는 경로: 주식, 코인, 원자재 체크",
        "{topic} 핵심 변수 3가지: 경기부양, 환율, 수요",
    ],
}

PATTERN_BY_KEYWORD = {
    "fomc": [
        "FOMC 이후 시장 체크포인트 3가지: 금리, 달러, 위험자산",
        "FOMC 이후 주식과 코인이 같이 흔들리는 이유",
        "FOMC 이후 투자자가 오늘 확인할 숫자들",
    ],
    "crypto_etf": [
        "코인 ETF 자금 흐름, 공포 구간에서 확인할 리스크 5가지",
        "코인 ETF 자금 유출입이 비트코인과 알트코인에 주는 신호",
        "코인 ETF를 볼 때 가격보다 먼저 확인할 자금 흐름",
    ],
}

TOPIC_BY_KEYWORD = {
    "fomc": "FOMC 이후 시장",
    "bitcoin": "비트코인",
    "us_index_flow": "미국 증시 지수 흐름",
    "china": "중국 변수와 시장 영향",
    "crypto_etf": "코인 ETF 자금 흐름",
}


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def dedupe(items: list[str]) -> list[str]:
    seen = set()
    result = []
    for item in items:
        normalized = " ".join((item or "").split())
        if not normalized or normalized in seen:
            continue
        seen.add(normalized)
        result.append(normalized)
    return result


def clean_topic(title: str, keyword: str) -> str:
    if keyword in TOPIC_BY_KEYWORD:
        return TOPIC_BY_KEYWORD[keyword]
    title = (title or keyword).strip()
    for sep in [":", "?", "|"]:
        if sep in title:
            title = title.split(sep, 1)[0].strip()
    if "," in title:
        title = title.split(",", 1)[0].strip()
    if len(title) > 24:
        title = title[:24].rstrip()
    return title or keyword


def inventory_lookup(inventory: dict) -> dict:
    return {item.get("keyword"): item for item in inventory.get("items", []) if item.get("keyword")}


def state_url_lookup(state: dict) -> dict:
    items = state.get("items", {})
    rows = items.values() if isinstance(items, dict) else items if isinstance(items, list) else []
    return {item.get("keyword"): item.get("url", "") for item in rows if item.get("keyword")}


def score_title(title: str, lane: str, demand_score: int, crypto_sentiment: str) -> int:
    score = 50
    if any(token in title for token in ["이유", "체크포인트", "먼저 볼 것", "확인할"]):
        score += 15
    if any(token in title for token in ["ETF", "달러", "금리", "실적", "환율", "규제"]):
        score += 12
    if any(token in title for token in ["3가지", "5가지"]):
        score += 8
    if lane == "crypto" and crypto_sentiment == "extreme_fear" and any(token in title for token in ["공포", "리스크", "ETF", "달러"]):
        score += 12
    if demand_score >= 5000:
        score += 8
    elif demand_score >= 3000:
        score += 5
    if len(title) > 58:
        score -= 5
    if any(token in title for token in ["급등", "무조건", "매수", "추천"]):
        score -= 20
    return score


def build_variants(item: dict, current_title: str, crypto_signal: dict) -> list[dict]:
    keyword = item.get("keyword", "")
    lane = item.get("brand_lane", "")
    topic = clean_topic(current_title or (item.get("title_candidates") or [""])[0], keyword)
    demand_score = int(item.get("demand_signal_score", 0) or 0)
    crypto_sentiment = crypto_signal.get("market_sentiment", item.get("crypto_market_sentiment", ""))
    base_titles = [current_title] + (item.get("title_candidates") or [])
    patterns = PATTERN_BY_KEYWORD.get(keyword, PATTERN_BY_LANE.get(lane, PATTERN_BY_LANE["macro"]))
    generated = [pattern.format(topic=topic) for pattern in patterns]

    variants = []
    for idx, title in enumerate(dedupe(base_titles + generated), start=1):
        title_score = score_title(title, lane, demand_score, crypto_sentiment)
        variants.append(
            {
                "variant_id": f"{keyword}-v{idx}",
                "title": title,
                "score": title_score,
                "angle": title_angle(title),
                "why": title_reason(title, lane, crypto_sentiment),
            }
        )
    variants.sort(key=lambda row: (-row["score"], len(row["title"]), row["title"]))
    return variants[:5]


def title_angle(title: str) -> str:
    if "ETF" in title or "자금" in title:
        return "fund-flow"
    if "달러" in title or "금리" in title or "환율" in title:
        return "macro-link"
    if "리스크" in title or "공포" in title:
        return "risk-check"
    if "실적" in title or "나스닥" in title:
        return "stock-market"
    if "3가지" in title or "5가지" in title:
        return "checklist"
    return "explainer"


def title_reason(title: str, lane: str, crypto_sentiment: str) -> str:
    if lane == "crypto" and crypto_sentiment == "extreme_fear":
        return "공포 구간에서는 가격 예측보다 자금 흐름과 리스크 확인형 제목이 클릭 의도에 더 맞습니다."
    if "체크포인트" in title or "3가지" in title or "5가지" in title:
        return "독자가 글에서 얻을 정보를 제목에서 바로 알 수 있습니다."
    if "이유" in title:
        return "뉴스를 이미 본 독자가 시장 반응의 이유를 확인하려는 검색 의도에 맞습니다."
    return "현재 주제를 설명형 검색어로 받아내기 위한 후보입니다."


def build_report() -> dict:
    daily = load_json(DAILY_BRIEF_JSON)
    keyword_board = load_json(KEYWORD_BOARD_JSON)
    crypto = load_json(CRYPTO_MARKET_SIGNAL_JSON)
    inventory = load_json(PUBLISH_INVENTORY_JSON)
    state = load_json(BLOGGER_STATE_JSON)

    inventory_by_keyword = inventory_lookup(inventory)
    urls = state_url_lookup(state)
    crypto_signals = crypto.get("keyword_signals", {})
    items = []
    for item in daily.get("top_briefs", [])[:8]:
        keyword = item.get("keyword", "")
        inv = inventory_by_keyword.get(keyword, {})
        current_title = inv.get("title") or (item.get("title_candidates") or [""])[0]
        variants = build_variants(item, current_title, crypto_signals.get(keyword, {}))
        if not variants:
            continue
        items.append(
            {
                "keyword": keyword,
                "brand_lane": item.get("brand_lane", ""),
                "current_title": current_title,
                "public_url": urls.get(keyword, ""),
                "demand_signal_score": item.get("demand_signal_score", 0),
                "total_score": item.get("total_score", 0),
                "crypto_market_sentiment": crypto_signals.get(keyword, {}).get("market_sentiment", ""),
                "recommended_title": variants[0]["title"],
                "recommended_angle": variants[0]["angle"],
                "variants": variants,
            }
        )

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "status": "ready_for_manual_title_ab_testing",
        "measurement_note": "Search Console 연결 전에는 실제 CTR 검증이 불가하므로, 검색 의도 기반 후보를 준비합니다.",
        "source_summary": {
            "daily_brief_count": len(daily.get("top_briefs", [])),
            "breaking_candidates": len(keyword_board.get("breaking_candidates", [])),
            "query_watchlist": len(keyword_board.get("query_watchlist", [])),
            "crypto_market_sentiment": crypto.get("market", {}).get("sentiment", ""),
        },
        "items": items,
        "next_actions": [
            "Search Console 연결 전에는 추천 제목을 배포 문구와 내부링크 앵커에 우선 사용합니다.",
            "Search Console 연결 후 노출은 높고 CTR이 낮은 글부터 recommended_title로 교체 테스트합니다.",
            "급등/매수 유도형 제목은 제외하고 체크포인트/이유/자금 흐름 중심으로 테스트합니다.",
        ],
    }


def write_markdown(report: dict) -> None:
    lines = [
        "# Title Experiment Board",
        "",
        "검색 클릭률을 높이기 위한 제목 A/B 후보 보드입니다.",
        "",
        f"- status: `{report.get('status', '')}`",
        f"- measurement_note: {report.get('measurement_note', '')}",
        f"- crypto_market_sentiment: `{report.get('source_summary', {}).get('crypto_market_sentiment', '')}`",
        "",
        "## Next Actions",
        "",
    ]
    for action in report.get("next_actions", []):
        lines.append(f"- {action}")
    for idx, item in enumerate(report.get("items", []), start=1):
        lines.extend(
            [
                "",
                f"## {idx}. {item.get('keyword', '')}",
                "",
                f"- lane: `{item.get('brand_lane', '')}`",
                f"- current_title: {item.get('current_title', '')}",
                f"- recommended_title: {item.get('recommended_title', '')}",
                f"- recommended_angle: `{item.get('recommended_angle', '')}`",
                f"- demand_signal_score: `{item.get('demand_signal_score', 0)}`",
                f"- public_url: {item.get('public_url') or '`missing`'}",
                "",
                "### Variants",
                "",
            ]
        )
        for variant in item.get("variants", []):
            lines.append(
                f"- `{variant.get('variant_id', '')}` score `{variant.get('score', 0)}` angle `{variant.get('angle', '')}`: {variant.get('title', '')}"
            )
            lines.append(f"  - why: {variant.get('why', '')}")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def main() -> int:
    report = build_report()
    OUTPUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    write_markdown(report)
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
