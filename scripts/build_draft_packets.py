#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BRIEF_JSON = ROOT / "outputs/latest/daily-post-brief.json"
PACKET_JSON = ROOT / "outputs/latest/draft-packets.json"
PACKET_MD = ROOT / "outputs/latest/draft-packets.md"
GROWTH_RULES_JSON = ROOT / "config/growth_rules.json"
VOICE_RULES_JSON = ROOT / "config/human_voice_rules.json"
VOICE_EXAMPLES_JSON = ROOT / "config/human_voice_examples.json"
REFERENCE_PATTERNS_JSON = ROOT / "config/current_editorial_reference_patterns.json"


DISCLAIMER = (
    "이 글은 정보 제공 및 학습용 정리이며, 특정 자산에 대한 투자 권유나 자문이 아닙니다. "
    "시장 데이터와 제도는 작성 시점 이후 달라질 수 있으므로 실제 투자 전에는 최신 공식 자료를 다시 확인해야 합니다."
)


FACT_CHECK_MAP = {
    "fomc": [
        "FOMC 성명서 원문 날짜와 발표 시각 확인",
        "점도표/경제전망 최신 버전 확인",
        "달러, 미국채 금리, 나스닥 관련 수치 재확인",
    ],
    "cpi": [
        "CPI headline/core 수치 재확인",
        "발표 월 기준과 전년동월/전월 비교 구분 확인",
        "나스닥, 달러, 미국채 반응 수치 재확인",
    ],
    "pce": [
        "PCE headline/core 수치 재확인",
        "Personal Income and Outlays 원문 링크 확인",
        "연준 경로와 연결 문장 과장 여부 점검",
    ],
    "jobs": [
        "비농업고용, 실업률, 임금 수치 재확인",
        "발표 날짜/시간 기준 확인",
        "금리 기대 변화 문장 교차 검증",
    ],
    "treasury_yields": [
        "미국채 2년/10년 금리 수치 재확인",
        "기준 시각과 비교 기준 명시",
        "주식/코인 반응 인과관계 과장 여부 점검",
    ],
    "dollar": [
        "DXY 또는 환율 수치 재확인",
        "달러 강세/약세 기간 기준 명시",
        "원화/금/코인 연계 문장 점검",
    ],
    "oil": [
        "WTI/Brent 수치 재확인",
        "공급 뉴스 원문 출처 확인",
        "인플레이션/금리 연결 문장 점검",
    ],
    "bitcoin": [
        "BTC 가격 기준 시각 재확인",
        "ETF 자금 유입 여부 공식/신뢰 소스 재확인",
        "단정적 가격 전망 문장 제거",
    ],
    "ethereum": [
        "ETH 가격 기준 시각 재확인",
        "재단/ETF/규제 관련 원문 링크 확인",
        "과장된 강세 표현 제거",
    ],
    "crypto_etf": [
        "ETF 승인/심사 상태 공식 문서 재확인",
        "SEC/Federal Register 최신 문서 링크 확인",
        "승인 기대를 확정처럼 쓰지 않기",
    ],
    "china": [
        "정책 발표 또는 인터뷰 원문 여부 확인",
        "중국 관련 2차 해설을 사실처럼 단정하지 않기",
        "한국/미국 시장 영향은 시나리오형으로 서술",
    ],
    "tariffs_trade": [
        "관세/무역 조치 공식 문서나 발표문 확인",
        "시장 영향은 조건형 문장으로 서술",
        "정치적 해석 과잉 여부 점검",
    ],
    "ai_semiconductors": [
        "기업 실적/가이던스 수치 원문 확인",
        "반도체 섹터 전반 일반화 과장 여부 점검",
        "대표 종목 티커와 실적 날짜 재확인",
    ],
    "us_index_flow": [
        "나스닥/S&P/미국 증시 수치와 기준 시각 재확인",
        "지수 하락/상승 원인을 한 문장으로 단정하지 않기",
        "채권·달러·빅테크와의 연결 문장 교차 점검",
    ],
    "us_big_tech": [
        "대표 종목 가격 변동률과 기준 시각 재확인",
        "실적/가격 인상/공급망 뉴스 원문 링크 확인",
        "개별 종목 이슈를 시장 전체 흐름처럼 과장하지 않기",
    ],
    "ai_growth_stocks": [
        "팔란티어/AI 성장주 관련 수치와 날짜 재확인",
        "단기 검색 급증과 중장기 펀더멘털을 구분해 서술",
        "섹터 자금 흐름 연결 문장 과장 여부 점검",
    ],
}


CTA_MAP = {
    "macro_explainer": "이런 거시 이벤트 해설을 꾸준히 받고 싶다면 다음 글도 이어서 확인해 보세요.",
    "crypto_analysis": "비트코인과 이더리움 흐름을 계속 추적하고 싶다면 다음 코인 해설 글도 함께 보세요.",
    "sector_analysis": "반도체와 AI 섹터 흐름이 이어질지 궁금하다면 다음 실적/섹터 글도 참고해 보세요.",
    "analysis": "비슷한 해설형 글을 더 보고 싶다면 다음 글도 이어서 확인해 보세요.",
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def build_packet(brief: dict, voice_rules: dict, voice_examples: dict) -> dict:
    keyword = brief["keyword"]
    fmt = brief.get("format", "analysis")
    format_profile = voice_rules.get("format_profiles", {}).get(fmt, voice_rules.get("format_profiles", {}).get("analysis", {}))
    example_profile = voice_examples.get(fmt, voice_examples.get("analysis", {}))
    packet = {
        "keyword": keyword,
        "recommended_title": brief["title_candidates"][0],
        "alternate_titles": brief["title_candidates"][1:],
        "summary_angle": brief["reason"],
        "outline": brief["outline"],
        "reference_takeaways": brief.get("reference_takeaways", []),
        "fact_checks": FACT_CHECK_MAP.get(keyword, ["핵심 숫자와 날짜 재확인", "과장 표현 점검", "최신 공식 출처 확인"]),
        "disclaimer": DISCLAIMER,
        "cta": CTA_MAP.get(fmt, CTA_MAP["analysis"]),
        "source_names": brief["source_names"],
        "reference_headlines": brief["sample_headlines"],
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
            "closing_example": example_profile.get("closing_example", "")
        },
        "score_breakdown": {
            "total_score": brief["total_score"],
            "search_score": brief["search_score"],
            "timeliness_score": brief["timeliness_score"],
            "explanatory_score": brief["explanatory_score"],
            "monetization_score": brief["monetization_score"],
            "risk_score": brief["risk_score"],
        },
    }
    return packet


def choose_editorial_pattern(keyword: str, fmt: str) -> str:
    if fmt == "macro_explainer":
        return "news_what_it_means"
    if fmt == "crypto_analysis":
        return "news_what_it_means" if keyword in {"bitcoin", "ethereum", "crypto_etf"} else "followup_checklist"
    if fmt == "sector_analysis":
        return "search_explainer"
    return "search_explainer"


def main() -> int:
    brief_data = load_json(BRIEF_JSON)
    growth_rules = load_json(GROWTH_RULES_JSON)
    voice_rules = load_json(VOICE_RULES_JSON)
    voice_examples = load_json(VOICE_EXAMPLES_JSON)
    reference_patterns = load_json(REFERENCE_PATTERNS_JSON)
    packet_limit = int(growth_rules.get("daily_execution_targets", {}).get("ideal_posts_per_day", 2)) + 2
    packets = []
    for brief in brief_data.get("top_briefs", [])[:packet_limit]:
        packet = build_packet(brief, voice_rules, voice_examples)
        editorial_pattern_name = choose_editorial_pattern(brief["keyword"], brief.get("format", "analysis"))
        packet["reference_editorial_pattern_name"] = editorial_pattern_name
        packet["reference_editorial_pattern"] = (reference_patterns.get("operating_patterns") or {}).get(editorial_pattern_name, {})
        packet["reference_editorial_sources"] = reference_patterns.get("sources", [])
        packet["style_translation_rules"] = reference_patterns.get("style_translation_rules", [])
        packets.append(packet)

    payload = {
        "generated_at": brief_data.get("generated_at"),
        "packets": packets,
    }
    PACKET_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2))

    lines = []
    lines.append("# 초안 생성 패킷")
    lines.append("")
    lines.append(f"- 생성 시각: `{payload['generated_at']}`")
    lines.append("")
    for idx, packet in enumerate(packets, start=1):
        lines.append(f"## {idx}. {packet['keyword']}")
        lines.append("")
        lines.append(f"- 추천 제목: {packet['recommended_title']}")
        lines.append(f"- 각도: {packet['summary_angle']}")
        lines.append(f"- 점수: {packet['score_breakdown']['total_score']}")
        lines.append(f"- 톤 목표: {packet['voice_profile']}")
        lines.append(f"- 편집 패턴: {packet.get('reference_editorial_pattern_name', '')}")
        lines.append("- 대체 제목:")
        for title in packet["alternate_titles"]:
            lines.append(f"  - {title}")
        lines.append("- 글 구조:")
        for item in packet["outline"]:
            lines.append(f"  - {item}")
        if packet["reference_takeaways"]:
            lines.append("- 유튜브/해설 참고 포인트:")
            for item in packet["reference_takeaways"]:
                lines.append(f"  - {item}")
        lines.append("- 사람 느낌 규칙:")
        for item in packet["human_touch_requirements"]:
            lines.append(f"  - {item}")
        lines.append("- 독자에게 직접 말 거는 표현 후보:")
        for item in packet["direct_address_phrases"]:
            lines.append(f"  - {item}")
        lines.append("- 해석 문장 장치:")
        for item in packet["interpretation_markers"]:
            lines.append(f"  - {item}")
        lines.append("- 반드시 살릴 말투 포인트:")
        for item in packet["must_include_style_points"]:
            lines.append(f"  - {item}")
        lines.append("- 현재 레퍼런스 기반 구조 규칙:")
        for item in packet.get("reference_editorial_pattern", {}).get("must_have", []):
            lines.append(f"  - {item}")
        lines.append("- 구조 참고 소스:")
        for source in packet.get("reference_editorial_sources", [])[:3]:
            lines.append(f"  - {source.get('name', '')}: {source.get('focus', '')}")
        lines.append("- 피해야 할 어색한 톤:")
        for item in packet["tone_penalties"]:
            lines.append(f"  - {item}")
        lines.append("- 참고할 사람 느낌 예시:")
        lines.append(f"  - 도입: {packet['voice_examples']['intro_example']}")
        lines.append(f"  - 해설: {packet['voice_examples']['analysis_example']}")
        lines.append(f"  - 마무리: {packet['voice_examples']['closing_example']}")
        lines.append("- 팩트체크:")
        for item in packet["fact_checks"]:
            lines.append(f"  - {item}")
        lines.append(f"- CTA: {packet['cta']}")
        lines.append(f"- 면책문구: {packet['disclaimer']}")
        lines.append("- 참고 헤드라인:")
        for item in packet["reference_headlines"]:
            lines.append(f"  - {item}")
        lines.append("")

    PACKET_MD.write_text("\n".join(lines).strip() + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
