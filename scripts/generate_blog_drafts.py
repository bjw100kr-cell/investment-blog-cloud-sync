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


def build_fallback_draft(packet: dict) -> str:
    title = packet["recommended_title"]
    outline = packet.get("outline", [])
    takeaways = packet.get("reference_takeaways", [])
    source_names = ", ".join(packet.get("source_names", []))
    headlines = packet.get("reference_headlines", [])
    faq_items = pick_faq_questions(packet)
    fact_checks = packet.get("fact_checks", [])
    today = datetime.now(timezone.utc)
    today_label = f"{today.year}년 {today.month}월 {today.day}일 기준"
    source_focus = source_names or "수집된 공식·언론·해설 소스"

    avoid_phrases = [p for p in packet.get("avoid_phrases", []) if p]
    reader_bridge_phrases = [p for p in packet.get("reader_bridge_phrases", []) if p]
    direct_address_phrases = [p for p in packet.get("direct_address_phrases", []) if p] or [
        "개인 투자자 입장에서는",
        "독자 입장에서 중요한 건",
    ]
    interpretation_markers = [p for p in packet.get("interpretation_markers", []) if p]
    must_include_style_points = [p for p in packet.get("must_include_style_points", []) if p]
    tone_penalties = [p for p in packet.get("tone_penalties", []) if p]

    def _safe_intro(idx: int) -> str:
        return _pick_styled_text(
            reader_bridge_phrases,
            "투자자 입장에서 가장 먼저 보는 건 바로 '왜 지금 이 이슈가 중요해졌는지'입니다.",
            idx,
        )

    summary = f"{packet['summary_angle']} 관점에서, 지금 투자자가 먼저 봐야 할 포인트를 한 번에 정리합니다."
    intro_parts = [
        f"{today_label} {title} 이슈를 정리하는 이유는, 이슈 자체보다 그 다음 연결 고리를 미리 점검하는 데 있습니다.",
        f"{_safe_intro(0)} {title}은 멀어 보여도 {source_focus}를 같이 보면 자산군 간 파급 경로가 보입니다.",
        f"{_safe_intro(1)} 지금 시점에 중요한 건 바로 가격이 아니라, 그 가격 변화가 어떤 해석을 타고 왔는지입니다.",
        f"{_pick_styled_text(direct_address_phrases, '독자 입장에서 중요한 건')} 지금 결론을 단정하기보다, 무엇이 먼저 반응했는지와 무엇이 아직 안 기다려졌는지를 나눠 보는 것입니다.",
    ]
    if headlines:
        intro_parts.append(f"여기서 먼저 봐야 할 건 `{headlines[0]}` 같은 제목 자체보다, 그 발표가 자금 흐름에 어떤 해석을 붙였는지입니다.")

    body_lines = []
    interpretation_marker = _pick_styled_text(interpretation_markers, "시장에서는 이걸 이렇게 해석합니다.", 0).strip()
    interpretation_focus = _normalize_interpretation_focus(interpretation_marker)
    for idx, item in enumerate(outline, start=1):
        body_lines.append(f"## {idx}. {item}")
        body_lines.append("")
        if idx == 1:
            body_lines.append(
                f"이 파트가 중요한 이유는 {packet['summary_angle']}라는 점입니다. {source_focus}에서 같은 성격의 움직임이 반복되면 소음일 가능성보다 흐름이 붙어 있을 확률이 더 높아집니다."
            )
        elif idx == 2:
            first_headline = headlines[0] if headlines else "관련 핵심 뉴스"
            body_lines.append(f"실제 확인된 정보 중 하나는 `{first_headline}` 입니다. 여기서 먼저 봐야 할 건 제목 자체보다 발표 시점, 숫자, 그리고 반응 축이 어떻게 읽히는지입니다. 핵심 해석 포인트는 {interpretation_focus}입니다.")
        elif idx == 3:
            body_lines.append(
                f"결국 같이 봐야 할 건 {interpretation_focus}입니다. 달러, 금리, 주식, 코인, 그리고 섹터 자금 흐름에서 먼저 움직인 축이 무엇인지 보면, 이후 방향을 보는 기준이 달라집니다."
            )
        elif idx == 4:
            body_lines.append(
                "포인트를 한 줄로 줄이면, 후속 이벤트가 나오기 전까지 이슈를 과도하게 매수·매도 신호로 단정하지 않고 검증 신호를 기다리는 방식이 더 안전합니다."
            )
        else:
            body_lines.append("개인 투자자 입장에서는 지금 결론을 세게 내리기보다, 체크포인트를 먼저 만든 뒤 다음 확인 이벤트에서 시나리오를 수정하는 흐름이 현실적입니다.")
        if takeaways:
            body_lines.append("")
            body_lines.append("이 이슈에서 특히 볼 해설 포인트:")
            for takeaway in takeaways[:2]:
                body_lines.append(f"- {takeaway}")
        body_lines.append("")

    checkpoint_lines = [
        "1. 핵심 숫자와 발표 시점을 공식 자료 기준으로 다시 확인하기",
        "2. 달러, 금리, 주식, 코인 중 무엇이 먼저 반응했는지 비교하기",
        "3. 다음 이벤트 전까지 어떤 시나리오가 유효한지 메모해두기",
    ]

    faq_lines = []
    for question, answer in faq_items:
        faq_lines.append(f"### {question}")
        faq_lines.append(answer)
        faq_lines.append("")

    tone_check = []
    if must_include_style_points:
        tone_check.append("## 운영자 체크용 톤 기준")
        tone_check.append("")
        tone_check.append("아래 항목은 본문 점검용 기준입니다.")
        for item in must_include_style_points:
            tone_check.append(f"- {item}")
        tone_check.append("")

    if tone_penalties:
        tone_check.append("## 피해야 할 톤 포인트")
        tone_check.append("")
        for item in tone_penalties:
            tone_check.append(f"- {item}")
        tone_check.append("")

    avoid_note = " ".join([f"`{phrase}`" for phrase in avoid_phrases[:2]])
    if avoid_note:
        intro_parts.append(f"지금 글에서 피해야 할 표현은 {avoid_note} 같은 형태로, 이런 뉘앙스는 기계식 결론으로 받아들여지기 쉽습니다.")

    lines = [
        f"# {title}",
        "",
        f"한 줄 요약: {summary}",
        "",
        "## 도입부",
        "",
        *intro_parts,
        "",
        "## 본문",
        "",
        *body_lines,
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
        *tone_check,
        "",
        "## CTA",
        "",
        packet["cta"],
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
