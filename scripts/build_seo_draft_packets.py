#!/usr/bin/env python3
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SEO_BACKLOG_JSON = ROOT / "outputs/latest/seo-backlog.json"
GROWTH_RULES_JSON = ROOT / "config/growth_rules.json"
VOICE_RULES_JSON = ROOT / "config/human_voice_rules.json"
VOICE_EXAMPLES_JSON = ROOT / "config/human_voice_examples.json"
OUTPUT_JSON = ROOT / "outputs/latest/seo-draft-packets.json"
OUTPUT_MD = ROOT / "outputs/latest/seo-draft-packets.md"
DRAFT_PACKETS_JSON = ROOT / "outputs/latest/draft-packets.json"


DISCLAIMER = (
    "이 글은 정보 제공 및 학습용 정리이며, 특정 자산에 대한 투자 권유나 자문이 아닙니다. "
    "시장 데이터와 제도는 작성 시점 이후 달라질 수 있으므로 실제 투자 전에는 최신 공식 자료를 다시 확인해야 합니다."
)


FACT_CHECK_BY_CATEGORY = {
    "macro": [
        "관련 공식 발표문과 날짜 재확인",
        "달러, 금리, 주식, 코인 연결 문장이 과장되지 않았는지 점검",
        "초보 독자가 오해할 수 있는 용어에 짧은 설명 추가",
    ],
    "global-sector": [
        "대표 기업명과 티커 재확인",
        "실적/가이던스/공급망 숫자 출처 점검",
        "섹터 전체 일반화 표현 과장 여부 점검",
    ],
    "crypto": [
        "가격 기준 시각과 출처 재확인",
        "ETF/규제 관련 문장을 최신 상태 기준으로 점검",
        "전망 문장이 단정형이 아닌지 확인",
    ],
}


CTA_BY_CATEGORY = {
    "macro": "당일 해설 글과 거시 허브 글을 함께 보면 시장 흐름을 더 입체적으로 볼 수 있습니다.",
    "global-sector": "대표 종목, 실적 일정, 공급망 글까지 이어서 보면 섹터 흐름이 더 잘 보입니다.",
    "crypto": "기초 가이드와 ETF·규제 해설 글까지 이어서 보면 코인 흐름이 더 쉽게 정리됩니다.",
}


VOICE_FORMAT_BY_CATEGORY = {
    "macro": "macro_explainer",
    "global-sector": "sector_analysis",
    "crypto": "crypto_analysis",
}


OUTLINE_BY_POST_TYPE = {
    "evergreen_explainer": [
        "먼저 이 개념을 왜 알아야 하나",
        "핵심 구조를 가장 쉽게 풀어보기",
        "실전 투자에서는 어디를 같이 보면 좋은가",
        "많이 헷갈리는 포인트 정리",
        "다음에 이어서 볼 글",
    ],
    "evergreen_sector_guide": [
        "왜 이 섹터를 따로 봐야 하나",
        "대표 기업과 지수/ETF 먼저 정리",
        "실적과 공급망에서 핵심 포인트 보기",
        "거시 변수와 같이 봐야 할 것",
        "다음 체크포인트",
    ],
    "follow_up_analysis": [
        "이전 메인 글에서 이어지는 핵심 질문",
        "이번에 추가로 확인된 내용",
        "개인 투자자가 체크할 숫자와 일정",
        "강세/약세 시나리오 나눠 보기",
        "다음 후속 글 연결",
    ],
}


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def build_source_name_lookup(draft_packets: dict) -> dict[str, list[str]]:
    lookup: dict[str, list[str]] = {}
    for packet in draft_packets.get("packets", []):
        source_keyword = packet.get("source_keyword", "")
        source_names = packet.get("source_names", [])
        keyword = packet.get("keyword", "")
        if keyword and source_names:
            lookup[keyword] = [name for name in source_names if name]
        if source_keyword and source_names:
            lookup[source_keyword] = [name for name in source_names if name]
    return lookup


def select_backlog_items(items: list[dict], packet_limit: int, per_source_limit: int = 3, demand_capture_min: int = 3) -> list[dict]:
    selected = []
    selected_keys = set()

    demand_capture_items = [item for item in items if item.get("role") == "search_demand_capture"]
    for item in demand_capture_items[:demand_capture_min]:
        if len(selected) >= packet_limit:
            return selected
        selected.append(item)
        selected_keys.add((item.get("source_keyword", ""), item.get("title", "")))

    grouped = {}
    source_order = []
    for item in items:
        item_key = (item.get("source_keyword", ""), item.get("title", ""))
        if item_key in selected_keys:
            continue
        source_keyword = item.get("source_keyword", "")
        if not source_keyword:
            continue
        if source_keyword not in grouped:
            grouped[source_keyword] = []
            source_order.append(source_keyword)
        grouped[source_keyword].append(item)
    for source_keyword in source_order:
        for item in grouped[source_keyword][:per_source_limit]:
            if len(selected) >= packet_limit:
                return selected
            selected.append(item)
    return selected


def packet_for_item(item: dict, voice_rules: dict, voice_examples: dict, source_name_lookup: dict[str, list[str]]) -> dict:
    category = item.get("category", "")
    fmt = VOICE_FORMAT_BY_CATEGORY.get(category, "analysis")
    format_profile = voice_rules.get("format_profiles", {}).get(fmt, voice_rules.get("format_profiles", {}).get("analysis", {}))
    example_profile = voice_examples.get(fmt, voice_examples.get("analysis", {}))
    outline = OUTLINE_BY_POST_TYPE.get(item.get("post_type"), OUTLINE_BY_POST_TYPE["evergreen_explainer"])
    title = item.get("title", "")
    source_keyword = item.get("source_keyword", "")

    return {
        "keyword": f"seo_{source_keyword}_{item.get('backlog_sequence')}",
        "source_keyword": source_keyword,
        "recommended_title": title,
        "alternate_titles": [
            f"{title}: 초보 투자자 기준으로 다시 보기",
            f"{title}: 지금 읽어야 하는 이유",
        ],
        "summary_angle": f"{item.get('source_title')}에서 이어지는 후속 글로, {item.get('search_intent')}",
        "outline": outline,
        "reference_takeaways": [
            f"메인 연결 글: {item.get('source_title')}",
            f"검색 의도: {item.get('search_intent')}",
            f"수익화 목표: {item.get('monetization_goal')}",
            f"검색어 후보: {', '.join(item.get('reader_search_queries', [])[:4]) or title}",
            f"수요 신뢰도: {item.get('demand_confidence', '')} - {item.get('demand_confidence_note', '')}",
        ],
        "fact_checks": FACT_CHECK_BY_CATEGORY.get(category, ["핵심 숫자와 날짜 재확인", "과장 표현 점검", "최신 공식 출처 확인"]),
        "disclaimer": DISCLAIMER,
        "cta": CTA_BY_CATEGORY.get(category, "관련 허브 글과 메인 해설 글을 이어서 보면 이해가 더 쉬워집니다."),
        "source_names": source_name_lookup.get(
            source_keyword,
            item.get("source_names") or [item.get("source_title", ""), item.get("source_keyword", "")],
        ),
        "reference_headlines": [item.get("title", "")],
        "voice_profile": format_profile.get("voice_goal", "쉽고 신뢰감 있는 설명형 톤"),
        "human_touch_requirements": voice_rules.get("human_touch_requirements", []),
        "reader_bridge_phrases": voice_rules.get("reader_bridge_phrases", []),
        "direct_address_phrases": voice_rules.get("direct_address_phrases", []),
        "interpretation_markers": voice_rules.get("interpretation_markers", []),
        "avoid_phrases": voice_rules.get("avoid_phrases", []),
        "tone_penalties": voice_rules.get("tone_penalties", []),
        "sentence_rhythm_targets": voice_rules.get("sentence_rhythm_targets", {}),
        "must_include_style_points": format_profile.get("must_include", []),
        "voice_examples": {
            "intro_example": example_profile.get("intro_example", ""),
            "analysis_example": example_profile.get("analysis_example", ""),
            "closing_example": example_profile.get("closing_example", ""),
        },
        "score_breakdown": {
            "total_score": item.get("priority_score", 0),
            "search_score": item.get("priority_score", 0),
            "timeliness_score": 0,
            "explanatory_score": 0,
            "monetization_score": 0,
            "risk_score": 0,
        },
        "internal_link_plan": {
            "primary": item.get("primary_internal_link_target", ""),
            "secondary": item.get("secondary_internal_link_targets", []),
        },
        "labels": item.get("labels", []),
        "search_intent": item.get("search_intent", ""),
        "monetization_goal": item.get("monetization_goal", ""),
        "reader_search_queries": item.get("reader_search_queries", []),
        "demand_confidence": item.get("demand_confidence", ""),
        "demand_confidence_note": item.get("demand_confidence_note", ""),
    }


def main() -> int:
    backlog = load_json(SEO_BACKLOG_JSON)
    growth_rules = load_json(GROWTH_RULES_JSON)
    voice_rules = load_json(VOICE_RULES_JSON)
    voice_examples = load_json(VOICE_EXAMPLES_JSON)
    packet_limit = int(growth_rules.get("daily_execution_targets", {}).get("ideal_posts_per_day", 2)) * 3 + 3
    selected_items = select_backlog_items(backlog.get("items", []), packet_limit)
    draft_packets = load_json(DRAFT_PACKETS_JSON)
    source_name_lookup = build_source_name_lookup(draft_packets)
    packets = [packet_for_item(item, voice_rules, voice_examples, source_name_lookup) for item in selected_items]

    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "count": len(packets),
        "packets": packets,
    }
    OUTPUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2))

    lines = []
    lines.append("# SEO 후속 글 Draft Packets")
    lines.append("")
    lines.append(f"- packet_count: `{len(packets)}`")
    lines.append("")
    for idx, packet in enumerate(packets, start=1):
        lines.append(f"## {idx}. {packet['recommended_title']}")
        lines.append("")
        lines.append(f"- source_keyword: {packet['source_keyword']}")
        lines.append(f"- search_intent: {packet['search_intent']}")
        lines.append(f"- monetization_goal: {packet['monetization_goal']}")
        lines.append(f"- voice_profile: {packet['voice_profile']}")
        lines.append(f"- primary_internal_link: {packet['internal_link_plan']['primary']}")
        lines.append(f"- secondary_internal_links: {', '.join(packet['internal_link_plan']['secondary'])}")
        lines.append("- outline:")
        for item in packet["outline"]:
            lines.append(f"  - {item}")
        lines.append("")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
