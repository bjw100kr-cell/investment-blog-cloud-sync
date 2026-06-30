#!/usr/bin/env python3
import argparse
import json
import os
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_PATH = ROOT / "templates/investment_blog_draft_prompt.md"
RESPONSES_URL = "https://api.openai.com/v1/responses"

DEFAULT_PACKETS_JSON = ROOT / "outputs/latest/draft-packets.json"
DEFAULT_PROMPTS_DIR = ROOT / "outputs/latest/prompts"
DEFAULT_DRAFTS_DIR = ROOT / "outputs/latest/drafts"
DEFAULT_REPORT_JSON = ROOT / "outputs/latest/draft-generation-report.json"


def slugify(text: str) -> str:
    out = []
    for ch in text.lower():
        if ch.isalnum():
            out.append(ch)
        elif ch in {" ", "-", "_"}:
            out.append("-")
    slug = "".join(out).strip("-")
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug or "draft"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def load_template(path: Path) -> str:
    return path.read_text()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate investment blog drafts from draft packets.")
    parser.add_argument("--packets-json", type=Path, default=DEFAULT_PACKETS_JSON, help="Path to the source draft packets JSON file.")
    parser.add_argument("--prompts-dir", type=Path, default=DEFAULT_PROMPTS_DIR, help="Directory to write rendered prompt files into.")
    parser.add_argument("--drafts-dir", type=Path, default=DEFAULT_DRAFTS_DIR, help="Directory to write generated markdown drafts into.")
    parser.add_argument("--report-json", type=Path, default=DEFAULT_REPORT_JSON, help="Path to the draft generation summary report JSON file.")
    parser.add_argument("--template-path", type=Path, default=TEMPLATE_PATH, help="Prompt template path.")
    return parser.parse_args()


def render_prompt(template: str, packet: dict) -> str:
    return template.replace("{{DRAFT_PACKET_JSON}}", json.dumps(packet, ensure_ascii=False, indent=2))


def call_openai(prompt: str) -> str:
    import requests

    api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set")

    response = requests.post(
        RESPONSES_URL,
        timeout=120,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": model,
            "input": prompt,
        },
    )
    response.raise_for_status()
    payload = response.json()

    output_text = []
    for item in payload.get("output", []):
        if item.get("type") != "message":
            continue
        for content in item.get("content", []):
            if content.get("type") == "output_text":
                output_text.append(content.get("text", ""))

    return "\n".join(output_text).strip()


def pick_faq_questions(packet: dict) -> list[tuple[str, str]]:
    keyword = packet.get("keyword", "")
    mapping = {
        "fomc": [
            ("FOMC가 왜 주식과 코인에 동시에 영향을 주나요?", "금리 방향이 달러와 유동성 기대를 바꾸기 때문입니다. 그래서 성장주와 코인처럼 유동성에 민감한 자산이 함께 반응하는 경우가 많습니다."),
            ("이번 발표에서 개인 투자자가 가장 먼저 볼 것은 무엇인가요?", "성명서 문구 자체보다 점도표, 기자회견 톤, 그리고 이후 금리 인하 기대가 얼마나 바뀌는지를 함께 보는 편이 더 중요합니다."),
        ],
        "oil": [
            ("유가가 내려가면 무조건 증시에 좋은가요?", "항상 그렇지는 않습니다. 공급 정상화 기대로 내리는 하락과 경기 둔화 우려로 내리는 하락은 시장 해석이 다를 수 있습니다."),
            ("개인 투자자는 유가를 어디까지 연결해서 봐야 하나요?", "원자재 가격 자체보다 인플레이션, 금리 기대, 운송비, 관련 업종 반응까지 연결해서 보는 편이 더 실전적입니다."),
        ],
        "ai_semiconductors": [
            ("AI 반도체는 엔비디아만 보면 되나요?", "그렇게 단순하게 보기는 어렵습니다. 메모리, 파운드리, 네트워크, 서버 공급망까지 같이 봐야 흐름이 더 잘 보입니다."),
            ("섹터 강세가 이어질지 보려면 무엇을 확인해야 하나요?", "실적 숫자, 가이던스, CAPEX, 고객사 주문 흐름처럼 실제 수요가 이어지는 신호가 있는지 확인해야 합니다."),
        ],
    }
    return mapping.get(
        keyword,
        [
            ("이 이슈를 볼 때 가장 먼저 확인할 것은 무엇인가요?", "핵심 숫자와 발표 시점, 그리고 시장이 그 숫자를 어떻게 해석하는지까지 함께 보는 편이 좋습니다."),
            ("개인 투자자는 어떤 식으로 접근해야 하나요?", "단정적으로 결론 내리기보다 시나리오를 나눠 보고, 다음 확인 포인트를 정해 두는 방식이 더 현실적입니다."),
        ],
    )


def _pick_styled_text(items: list, fallback: str, idx: int = 0) -> str:
    if not items:
        return fallback
    return items[min(idx, len(items) - 1)]


def _normalize_interpretation_focus(text: str) -> str:
    phrase = text.strip().rstrip(".")
    mapping = {
        "이 숫자의 의미는": "이 숫자가 시장 기대를 얼마나 바꾸는지",
        "시장에서는 이걸 이렇게 해석합니다": "시장이 이 이슈를 어떤 방향으로 읽고 있는지",
        "결국 핵심은": "결국 무엇이 실제 변수로 남는지",
        "포인트를 한 줄로 줄이면": "복잡한 뉴스 속에서 결국 남는 한 가지 포인트가 무엇인지",
        "다음으로 연결해서 보면": "이 이슈가 다음 이벤트와 어떻게 연결되는지",
    }
    if phrase in mapping:
        return mapping[phrase]
    if phrase.endswith(("다", "요")):
        return phrase
    if phrase.endswith(("은", "는", "이", "가")):
        return f"{phrase} 무엇인지"
    return phrase


def _compact_text(text: str) -> str:
    return " ".join(str(text).split()).strip()


def _voice_example(packet: dict, key: str, fallback: str) -> str:
    examples = packet.get("voice_examples", {}) or {}
    value = _compact_text(examples.get(key, ""))
    return value or fallback


def _takeaway_lines(packet: dict) -> list[str]:
    takeaways = [_compact_text(item) for item in packet.get("reference_takeaways", []) if _compact_text(item)]
    return takeaways[:2]


def _human_interpretation_line(keyword: str, interpretation_focus: str) -> str:
    if "fomc" in keyword:
        return "이 대목을 투자자 언어로 바꾸면, 금리 자체보다 연준이 앞으로 얼마나 빨리 방향을 바꿀 수 있는지에 대한 기대가 먼저 가격을 흔들고 있다는 뜻에 가깝습니다."
    if "bitcoin" in keyword:
        return "이걸 가격이 아니라 구조로 보면, 비트코인만의 힘으로 움직인다기보다 유동성과 위험선호가 같이 살아나는지 여부를 먼저 확인해야 한다는 쪽에 가깝습니다."
    if "us_big_tech" in keyword:
        return "투자자 언어로 다시 풀면, headline보다 실제 자금이 대형주에 몰리는지 아니면 공급망 전반으로 퍼지는지를 보는 게 더 중요하다는 뜻입니다."
    return f"투자자 언어로 다시 풀면, 결국 중요한 건 {interpretation_focus} 쪽이 실제 자산 가격에 얼마나 빨리 반영되는지입니다."


def _question_mix_line(keyword: str) -> str:
    if "fomc" in keyword:
        return "그럼 개인 투자자는 뭘 먼저 봐야 할까. 달러와 미국채 금리, 그리고 나스닥 반응 순서를 같이 놓고 보면 생각보다 그림이 빨리 잡힙니다."
    if "bitcoin" in keyword:
        return "그럼 여기서 먼저 확인할 건 뭘까. ETF 자금과 달러 흐름, 그리고 알트코인 반응이 같은 방향으로 가는지부터 보는 편이 훨씬 현실적입니다."
    return "그럼 여기서 먼저 봐야 할 건 뭘까. 숫자 하나보다 그 숫자 뒤에서 같이 움직이는 자산군과 다음 일정까지 같이 놓고 보는 편이 더 실전적입니다."


def _cta_upgrade_line(keyword: str, title: str) -> str:
    if "fomc" in keyword:
        return "다음 글에서는 FOMC 이후 달러, 미국채 금리, 나스닥 가운데 무엇을 먼저 보면 되는지 더 실전적으로 풀어보겠습니다."
    if "bitcoin" in keyword:
        return "다음 글에서는 비트코인 흐름을 ETF 자금, 달러, 알트코인 순서로 어떻게 체크하면 되는지 더 쉽게 짚어보겠습니다."
    if "us_big_tech" in keyword:
        return "다음 글에서는 이 흐름이 실제로 어떤 대표 종목과 공급망으로 번지는지 한 단계 더 실전적으로 풀어보겠습니다."
    return f"다음 글에서는 {title} 흐름이 실제 종목이나 자산군 선택으로 어떻게 이어지는지 더 실전적으로 풀어보겠습니다."


def _topic_profile(keyword: str, title: str) -> dict:
    if "fomc" in keyword:
        return {
            "title": "FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지",
            "quick": [
                "FOMC는 금리 결정 한 줄보다 달러, 미국채 금리, 위험자산 심리를 동시에 바꾸는 이벤트입니다.",
                "시장은 발표 결과보다 성명서 문구, 점도표, 기자회견 톤이 다음 금리 경로를 어떻게 바꾸는지에 더 민감하게 반응합니다.",
                "개인 투자자는 발표 직후 방향을 단정하기보다 달러 인덱스, 미국채 2년물/10년물, 나스닥과 비트코인 반응을 같이 확인하는 편이 안전합니다.",
            ],
            "concrete_checks": ["달러 인덱스", "미국채 2년물/10년물 금리", "나스닥과 비트코인 동시 반응", "다음 CPI/PCE/고용지표"],
            "market_reason": "금리 경로가 바뀌면 돈값이 달라지고, 돈값이 달라지면 성장주와 코인처럼 미래 기대를 크게 반영하는 자산의 할인율도 함께 흔들립니다.",
            "investor_angle": "이걸 내 돈 관점에서 보면 FOMC는 매수·매도 신호라기보다 포트폴리오의 위험 노출을 점검하는 날에 가깝습니다.",
            "upside": "달러와 단기금리가 안정되고 나스닥, 비트코인, 반도체 같은 위험자산이 같은 방향으로 반응하면 시장은 완화 기대를 더 강하게 읽을 수 있습니다.",
            "risk": "반대로 연준 발언이 물가 경계 쪽으로 기울거나 다음 물가 지표가 다시 강하게 나오면, 발표 직후 반등은 빠르게 되돌려질 수 있습니다.",
            "mistake": "금리 동결을 곧바로 호재로만 해석하는 것입니다. 시장은 동결 여부보다 앞으로 몇 번, 언제, 어떤 속도로 움직일지를 더 크게 봅니다.",
        }
    if "bitcoin" in keyword:
        return {
            "title": "비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트",
            "quick": [
                "비트코인 흐름은 가격 캔들만 보면 늦습니다. ETF 자금과 달러 흐름, 규제 뉴스가 먼저 분위기를 바꾸는 경우가 많습니다.",
                "강한 상승처럼 보여도 실제 자금 유입이 약하거나 달러가 강하면 흐름이 쉽게 끊길 수 있습니다.",
                "개인 투자자는 비트코인 단독 상승인지, 이더리움·알트코인·나스닥까지 같이 움직이는지를 함께 확인해야 합니다.",
            ],
            "concrete_checks": ["현물 ETF 순유입/순유출", "달러 인덱스와 미국채 금리", "이더리움과 알트코인 확산 여부", "규제 법안·SEC 관련 일정"],
            "market_reason": "코인 시장은 기대가 빠르게 가격에 반영되는 만큼, 실제 유동성이 따라오지 않으면 좋은 뉴스 뒤에도 차익실현이 먼저 나올 수 있습니다.",
            "investor_angle": "독자 입장에서 중요한 건 '비트코인이 올랐다'가 아니라 그 상승이 새 자금의 유입인지, 기존 포지션의 단기 반등인지 구분하는 일입니다.",
            "upside": "ETF 자금이 여러 날 이어지고 달러가 약해지며 알트코인까지 따라오면 시장은 위험선호 회복으로 해석할 가능성이 커집니다.",
            "risk": "ETF 유입이 꺾이거나 규제 뉴스가 부정적으로 바뀌면, 가격이 버티고 있어도 내부 체력은 먼저 약해질 수 있습니다.",
            "mistake": "ETF나 규제 헤드라인 하나를 곧바로 매수 신호로 받아들이는 것입니다. 코인 시장은 호재 선반영과 뉴스 후 되돌림이 자주 나옵니다.",
        }
    if any(marker in keyword for marker in ["us_index_flow", "us_big_tech", "ai_semiconductors"]):
        return {
            "title": f"{title}: 나스닥, 금리, 빅테크 실적을 같이 봐야 하는 이유",
            "quick": [
                "미국 증시 흐름은 지수 등락률만 보면 부족합니다. 금리와 달러, 빅테크 실적 기대가 같이 움직입니다.",
                "나스닥이 강해도 시장 폭이 좁으면 일부 대형주 쏠림일 수 있고, 반대로 섹터 확산이 나오면 추세가 더 단단해질 수 있습니다.",
                "개인 투자자는 지수보다 금리, 반도체·AI 대표주, 실적 가이던스, 거래대금 확산을 함께 보는 편이 좋습니다.",
            ],
            "concrete_checks": ["나스닥과 S&P500 상대 강도", "미국채 10년물 금리", "엔비디아·마이크로소프트 등 빅테크 실적 가이던스", "반도체 ETF와 시장 폭"],
            "market_reason": "미국 지수는 대형 기술주의 비중이 크기 때문에 금리가 내려가면 밸류에이션 부담이 줄고, 실적 기대가 강하면 지수가 더 쉽게 버팁니다.",
            "investor_angle": "이걸 내 돈 관점에서 보면 지수가 올랐다는 사실보다 어떤 업종이 끌고 갔는지, 그리고 그 흐름이 넓어지는지가 더 중요합니다.",
            "upside": "금리가 안정되고 빅테크 실적 전망이 유지되며 반도체와 소프트웨어까지 같이 오르면 상승의 질이 좋아질 수 있습니다.",
            "risk": "소수 대형주만 버티고 중소형주나 경기민감주가 약하면, 지수 상승이 생각보다 얇은 흐름일 수 있습니다.",
            "mistake": "나스닥 상승을 모든 주식에 좋은 신호로 해석하는 것입니다. 실제로는 몇 개 대형주가 지수를 밀어 올리는 장면도 많습니다.",
        }
    if "china" in keyword:
        return {
            "title": "중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유",
            "quick": [
                "중국 변수는 중국 증시만의 문제가 아니라 원자재, 환율, 한국 수출주, 글로벌 위험심리로 번질 수 있습니다.",
                "정책 부양 뉴스가 나와도 실제 소비와 부동산, 위안화 흐름이 따라오는지 확인해야 합니다.",
                "개인 투자자는 중국 관련 ETF나 소재·산업재만 보지 말고 달러/위안, 구리·유가, 한국 수출주 반응을 같이 보는 편이 좋습니다.",
            ],
            "concrete_checks": ["달러/위안 환율", "중국 부동산·소비 지표", "구리와 유가", "한국 수출주와 소재·산업재 반응"],
            "market_reason": "중국은 글로벌 수요의 큰 축이기 때문에 경기 기대가 바뀌면 원자재와 아시아 증시, 달러 흐름까지 같이 움직일 수 있습니다.",
            "investor_angle": "독자 입장에서 중요한 건 중국 뉴스 자체보다 그 뉴스가 실제 수요 회복으로 이어지는지 확인하는 일입니다.",
            "upside": "부양책과 소비 지표가 같은 방향으로 개선되고 위안화가 안정되면 중국 관련 자산의 해석이 좋아질 수 있습니다.",
            "risk": "정책 기대만 앞서고 부동산·소비 지표가 따라오지 않으면 시장은 다시 실망 쪽으로 기울 수 있습니다.",
            "mistake": "부양책 발표를 곧바로 경기 회복으로 보는 것입니다. 시장은 발표보다 집행 속도와 실제 지표를 더 냉정하게 봅니다.",
        }
    return {
        "title": f"{title}: 오늘 시장이 반응한 이유와 확인할 3가지",
        "quick": [
            f"{title}은 제목만 보면 단순 뉴스처럼 보이지만, 실제로는 자금 흐름과 투자심리를 같이 건드릴 수 있는 이슈입니다.",
            "핵심은 발표 자체보다 시장이 그 발표를 어떤 방향으로 해석했는지입니다.",
            "개인 투자자는 가격 반응, 관련 자산 확산, 다음 공식 일정을 함께 확인하는 편이 좋습니다.",
        ],
        "concrete_checks": ["공식 발표 날짜와 핵심 문구", "달러·금리·주식·코인 중 먼저 반응한 자산", "거래량과 자금 흐름", "다음 경제지표 또는 정책 일정"],
        "market_reason": "시장은 뉴스의 좋고 나쁨보다 그 뉴스가 다음 기대를 얼마나 바꾸는지에 먼저 반응합니다.",
        "investor_angle": "이걸 내 돈 관점에서 보면 지금 필요한 건 예측보다 체크리스트입니다.",
        "upside": "관련 자산들이 같은 방향으로 움직이고 후속 데이터가 확인되면 시장 해석은 더 빠르게 굳어질 수 있습니다.",
        "risk": "반응이 한 자산에만 머물거나 다음 지표가 반대로 나오면 초기 해석은 쉽게 흔들릴 수 있습니다.",
        "mistake": "헤드라인 하나만 보고 방향을 단정하는 것입니다.",
    }


def _profit_title(packet: dict) -> str:
    profile = _topic_profile(packet.get("keyword", ""), packet["recommended_title"])
    return profile["title"]


def _check_label(text: str) -> str:
    return text.strip().rstrip(".")


def _has_reference_source_names(source_names: str) -> bool:
    haystack = source_names.lower()
    markers = [
        "rss",
        "news",
        "press",
        "youtube",
        "google trends",
        "marketwatch",
        "coindesk",
        "reuters",
        "cnbc",
        "federal reserve",
        "investing.com",
        "financial times",
    ]
    return any(marker in haystack for marker in markers)


def _describe_source_context(source_names: list[str]) -> str:
    haystack = " ".join(source_names).lower()
    labels = []
    if any(marker in haystack for marker in ["federal reserve", "official", "press"]):
        labels.append("공식 발표 자료")
    if any(marker in haystack for marker in ["reuters", "cnbc", "financial times", "marketwatch"]):
        labels.append("해외 주요 매체 보도")
    if any(marker in haystack for marker in ["coindesk", "cointelegraph", "coinness", "investing.com crypto"]):
        labels.append("코인 전문 매체 기사")
    if any(marker in haystack for marker in ["youtube", "trade king", "tradeking"]):
        labels.append("유튜브 해설")
    if any(marker in haystack for marker in ["google trends", "trend"]):
        labels.append("실시간 검색 흐름")
    if not labels:
        return "관련 해설 글과 핵심 키워드"
    return ", ".join(dict.fromkeys(labels))


def build_fallback_draft(packet: dict) -> str:
    title = _profit_title(packet)
    original_title = packet["recommended_title"]
    outline = packet.get("outline", [])
    takeaways = _takeaway_lines(packet)
    source_names = ", ".join(packet.get("source_names", []))
    source_context = _describe_source_context(packet.get("source_names", []))
    headlines = packet.get("reference_headlines", [])
    faq_items = pick_faq_questions(packet)
    fact_checks = packet.get("fact_checks", [])
    today = datetime.now(timezone.utc)
    today_label = f"{today.year}년 {today.month}월 {today.day}일 기준"
    source_focus = source_names or "수집된 공식·언론·해설 소스"
    source_bridge = source_context if _has_reference_source_names(source_focus) else "관련 해설 글과 핵심 키워드"

    avoid_phrases = [p for p in packet.get("avoid_phrases", []) if p]
    reader_bridge_phrases = [p for p in packet.get("reader_bridge_phrases", []) if p]
    direct_address_phrases = [p for p in packet.get("direct_address_phrases", []) if p] or [
        "개인 투자자 입장에서는",
        "독자 입장에서 중요한 건",
    ]
    interpretation_markers = [p for p in packet.get("interpretation_markers", []) if p]
    must_include_style_points = [p for p in packet.get("must_include_style_points", []) if p]

    def _safe_intro(idx: int) -> str:
        return _pick_styled_text(
            reader_bridge_phrases,
            "투자자 입장에서 가장 먼저 보는 건 바로 '왜 지금 이 이슈가 중요해졌는지'입니다.",
            idx,
        )

    intro_example = _voice_example(
        packet,
        "intro_example",
        "표면적으로는 단순한 뉴스처럼 보여도, 투자자 입장에서는 그 한 줄이 자산 흐름을 꽤 크게 바꿀 때가 있습니다.",
    )
    analysis_example = _voice_example(
        packet,
        "analysis_example",
        "쉽게 말해 시장은 헤드라인보다 그 다음 연결 고리를 먼저 가격에 반영하려고 합니다.",
    )
    closing_example = _voice_example(
        packet,
        "closing_example",
        "결국 지금 단계에서는 방향을 단정하기보다 다음 확인 포인트를 미리 정해두는 편이 현실적입니다.",
    )
    human_interpretation = _human_interpretation_line(packet.get("keyword", ""), interpretation_focus="")

    profile = _topic_profile(packet.get("keyword", ""), original_title)
    checks = [_check_label(item) for item in profile["concrete_checks"]]
    primary_headline = headlines[0] if headlines else original_title
    summary = f"`{checks[0]}`, `{checks[1]}`, `{checks[2]}` 세 지표를 같이 봐야 {original_title}이 단기 뉴스인지 실제 흐름인지 구분할 수 있습니다."
    intro_parts = [
        f"{today_label}, 이 이슈를 그냥 뉴스 하나로 넘기기엔 아깝습니다.",
        intro_example,
        f"{_pick_styled_text(direct_address_phrases, '독자 입장에서 중요한 건')} 지금 당장 방향을 맞히는 것보다 `{checks[0]}`, `{checks[1]}`, `{checks[2]}` 세 가지가 같은 쪽을 가리키는지 확인하는 일입니다.",
        f"{_safe_intro(0)} {source_bridge}를 같이 보면 headline 뒤에 있는 자금 흐름과 심리 변화를 더 빨리 잡을 수 있습니다.",
    ]
    if headlines:
        intro_parts.append(f"예를 들어 `{primary_headline}` 같은 제목은 출발점일 뿐입니다. 중요한 건 이 뉴스가 실제로 어떤 자산을 먼저 움직였는지입니다.")

    body_lines = []
    interpretation_marker = _pick_styled_text(interpretation_markers, "시장에서는 이걸 이렇게 해석합니다.", 0).strip()
    interpretation_focus = _normalize_interpretation_focus(interpretation_marker)
    human_interpretation = _human_interpretation_line(packet.get("keyword", ""), interpretation_focus)
    body_sections = [
        (
            "지금 무슨 일이 있었나",
            [
                f"이번 글의 출발점은 `{primary_headline}`입니다. 다만 제목만 읽고 끝내면 가장 중요한 부분을 놓치기 쉽습니다.",
                f"여기서 봐야 할 건 사건 자체보다 시장 해석이 달라지는 두 축입니다. 하나는 `{checks[0]}`, 다른 하나는 `{checks[1]}`입니다.",
                f"{analysis_example} 그래서 같은 뉴스라도 발표 직후 반응과 다음 거래일 반응이 다르게 나올 수 있습니다.",
            ],
        ),
        (
            "왜 시장이 반응했나",
            [
                profile["market_reason"],
                human_interpretation,
                f"특히 `{checks[0]}` 쪽 변화가 먼저 나오고 `{checks[1]}` 흐름이 따라오는지, 아니면 가격만 먼저 튀는지를 나눠 보면 뉴스의 질이 달라 보입니다.",
            ],
        ),
        (
            "개인 투자자가 바로 확인할 지표",
            [
                f"첫째로 볼 것은 `{checks[0]}`입니다. 이 지표가 같은 방향으로 며칠 이어지면 단순 반응보다 흐름일 가능성이 커집니다.",
                f"둘째는 `{checks[1]}`입니다. 거시 환경이 받쳐주지 않으면 좋은 뉴스도 오래 버티기 어렵습니다.",
                f"셋째는 `{checks[2]}`입니다. 한 자산만 움직이는지, 관련 자산으로 확산되는지에 따라 해석이 완전히 달라집니다.",
                f"추가로 `{checks[3]}`까지 확인하면 다음 글감과 투자 판단의 기준선이 더 선명해집니다.",
            ],
        ),
        (
            "내 포트폴리오와 연결해서 보는 법",
            [
                profile["investor_angle"],
                "예를 들어 이미 관련 자산 비중이 높다면 새로 맞히는 것보다 변동성이 커질 때 어느 구간에서 흔들릴지 먼저 생각해야 합니다.",
                "반대로 아직 관망 중이라면 지금 당장 따라가기보다 다음 확인 지표가 같은 방향으로 쌓이는지 보는 편이 더 실전적입니다.",
            ],
        ),
    ]
    for idx, (heading, paragraphs) in enumerate(body_sections, start=1):
        body_lines.append(f"## {idx}. {heading}")
        body_lines.append("")
        body_lines.extend(paragraphs)
        if takeaways and idx == 1:
            body_lines.append("")
            body_lines.append("참고로 영상·해설 자료에서 반복된 관찰 포인트는 이런 쪽이었습니다:")
            for takeaway in takeaways:
                body_lines.append(f"- {takeaway}")
        body_lines.append("")

    checkpoint_lines = [
        f"1. `{checks[0]}`: 발표 직후뿐 아니라 다음 거래일에도 같은 방향인지 확인하기",
        f"2. `{checks[1]}`와 `{checks[2]}`: 서로 엇갈리는지, 같이 움직이는지 비교하기",
        f"3. `{checks[3]}` 전까지 상승 시나리오와 리스크 시나리오를 따로 메모해두기",
    ]

    faq_lines = []
    for question, answer in faq_items:
        faq_lines.append(f"### {question}")
        faq_lines.append(answer)
        faq_lines.append("")

    style_points = []
    if must_include_style_points:
        style_points.append("## 이 글에서 같이 봐야 할 관점")
        style_points.append("")
        for item in must_include_style_points:
            style_points.append(f"- {item}")
        style_points.append("")

    lines = [
        f"# {title}",
        "",
        f"한 줄 요약: {summary}",
        "",
        "## 오늘 핵심 3줄",
        "",
        *[f"- {item}" for item in profile["quick"]],
        "",
        "## 도입부",
        "",
        *intro_parts,
        "",
        "## 본문",
        "",
        *body_lines,
        "## 상승 시나리오와 리스크",
        "",
        f"- 상승 시나리오: {profile['upside']}",
        f"- 리스크 시나리오: {profile['risk']}",
        "",
        "## 자주 하는 오해",
        "",
        profile["mistake"],
        "",
        "## 체크포인트 3개",
        "",
        *checkpoint_lines,
        "",
        "## FAQ 2개",
        "",
        *faq_lines,
        "## 출처 체크",
        "",
        f"- 주요 참고 소스: {source_names or '수집된 공식/언론/해설 소스'}",
        *[f"- 발행 전 재확인: {item}" for item in fact_checks],
        "",
        *style_points,
        "",
        "## CTA",
        "",
        packet["cta"],
        _cta_upgrade_line(packet.get("keyword", ""), title),
        "",
        "## 면책문구",
        "",
        packet["disclaimer"],
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    packets_data = load_json(args.packets_json)
    template = load_template(args.template_path)
    args.prompts_dir.mkdir(parents=True, exist_ok=True)
    args.drafts_dir.mkdir(parents=True, exist_ok=True)
    for old_file in args.prompts_dir.glob("*.md"):
        old_file.unlink()
    for old_file in args.drafts_dir.glob("*.md"):
        old_file.unlink()

    has_api_key = bool(os.getenv("OPENAI_API_KEY"))
    summary = []

    for idx, packet in enumerate(packets_data.get("packets", []), start=1):
        slug = f"{idx:02d}-{slugify(packet['keyword'])}"
        prompt = render_prompt(template, packet)
        prompt_path = args.prompts_dir / f"{slug}.md"
        prompt_path.write_text(prompt)

        draft_path = args.drafts_dir / f"{slug}.md"
        if has_api_key:
            draft_text = call_openai(prompt)
            draft_path.write_text(draft_text + ("\n" if not draft_text.endswith("\n") else ""))
            summary.append({"keyword": packet["keyword"], "prompt": str(prompt_path), "draft": str(draft_path), "generated": True, "mode": "openai"})
        else:
            fallback = build_fallback_draft(packet)
            draft_path.write_text(fallback + ("\n" if not fallback.endswith("\n") else ""))
            summary.append(
                {
                    "keyword": packet["keyword"],
                    "prompt": str(prompt_path),
                    "draft": str(draft_path),
                    "generated": True,
                    "mode": "fallback_template",
                }
            )

    report = {
        "generated_at": packets_data.get("generated_at"),
        "packets_json": str(args.packets_json),
        "prompts_dir": str(args.prompts_dir),
        "drafts_dir": str(args.drafts_dir),
        "openai_enabled": has_api_key,
        "items": summary,
    }
    args.report_json.parent.mkdir(parents=True, exist_ok=True)
    args.report_json.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
