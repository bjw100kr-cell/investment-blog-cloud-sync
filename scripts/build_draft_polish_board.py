#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HUMAN_TONE_JSON = ROOT / "outputs/latest/human-tone-review.json"
FULL_DRAFT_JSON = ROOT / "outputs/latest/full-draft-review-sheet.json"
SHORTLIST_JSON = ROOT / "outputs/latest/user-review-shortlist.json"
OUTPUT_JSON = ROOT / "outputs/latest/draft-polish-board.json"
OUTPUT_MD = ROOT / "outputs/latest/draft-polish-board.md"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def index_by(items: list[dict], key: str) -> dict[str, dict]:
    return {item.get(key, ""): item for item in items if item.get(key)}


def first_body_paragraph(text: str) -> str:
    parts = [part.strip() for part in text.split("\n\n") if part.strip() and not part.startswith("#")]
    return parts[0] if parts else ""


def intro_upgrade(title: str, keyword: str) -> str:
    if keyword == "fomc":
        return f"{title}은 멀게 느껴질 수 있지만, 실제로는 환율과 나스닥, 비트코인까지 같이 흔들 수 있는 변수라서 개인 투자자도 그냥 넘기기 어렵습니다."
    if keyword == "bitcoin":
        return f"{title}에서 중요한 건 오늘 가격이 몇 퍼센트 움직였느냐보다, 그 움직임이 잠깐의 과열인지 다음 흐름의 시작인지를 가려내는 일입니다."
    return f"{title}은 headline만 보면 단순 뉴스처럼 보이지만, 실제 투자 판단에서는 자금 흐름이 어디로 번지는지까지 같이 봐야 의미가 생깁니다."


def interpretation_upgrade(keyword: str) -> str:
    if keyword == "fomc":
        return "이 대목을 투자자 언어로 바꾸면, 금리 자체보다 연준이 앞으로 얼마나 빨리 방향을 바꿀 수 있는지에 대한 기대가 자산 가격을 먼저 흔들고 있다는 뜻입니다."
    if keyword == "bitcoin":
        return "이걸 가격이 아니라 구조로 보면, 비트코인만의 힘으로 오른다기보다 유동성과 위험선호가 같이 살아나는지 여부를 먼저 확인해야 한다는 신호에 가깝습니다."
    return "이 숫자를 그대로 외우는 것보다 더 중요한 건, 시장이 이 재료를 경기 둔화 신호로 읽는지 아니면 위험자산 회복 신호로 읽는지 구분하는 것입니다."


def ending_mix_upgrade(ending: str) -> str:
    if not ending:
        return "짧게 끊는 문장과 질문형 문장을 한두 개 섞어 문장 리듬을 더 자연스럽게 만듭니다."
    return f"`{ending}` 어미가 반복될 때는 한 문장을 짧게 끊거나, `그럼 투자자는 뭘 먼저 봐야 할까` 같은 질문형 문장을 섞어 리듬을 풀어줍니다."


def cta_upgrade(keyword: str) -> str:
    if keyword == "fomc":
        return "다음 글에서는 FOMC 이후 달러, 미국채 금리, 나스닥 가운데 무엇을 먼저 보면 되는지 더 실전적으로 풀어보겠습니다."
    if keyword == "bitcoin":
        return "다음 글에서는 비트코인 흐름을 ETF 자금, 달러, 알트코인 순서로 어떻게 체크하면 되는지 더 쉽게 짚어보겠습니다."
    return "다음 글에서는 이 흐름이 실제 종목이나 자산군 선택으로 어떻게 이어지는지 더 실전적으로 정리해보겠습니다."


def keyword_focus(keyword: str) -> str:
    if keyword == "fomc":
        return "거시 이슈를 내 자산 흐름과 연결해주는 해설 톤"
    if keyword == "bitcoin":
        return "가격 기사보다 한 단계 깊게 읽어주는 코인 해설 톤"
    return "뉴스를 투자자 언어로 다시 번역해주는 해설 톤"


def build_report() -> dict:
    tone = index_by(load_json(HUMAN_TONE_JSON).get("items", []), "keyword")
    drafts = index_by(load_json(FULL_DRAFT_JSON).get("items", []), "keyword")
    shortlist = load_json(SHORTLIST_JSON).get("shortlist", [])

    items = []
    for card in shortlist[:3]:
        keyword = card.get("keyword", "")
        draft = drafts.get(keyword, {})
        tone_item = tone.get(keyword, {})
        full_text = draft.get("full_draft_text", "")
        items.append(
            {
                "keyword": keyword,
                "title": card.get("title", ""),
                "ready_now": card.get("ready_now", False),
                "quality_status": card.get("quality_status", ""),
                "human_tone_score": tone_item.get("score", 0),
                "warnings": tone_item.get("warnings", []),
                "voice_focus": keyword_focus(keyword),
                "first_body_paragraph": first_body_paragraph(full_text),
                "intro_upgrade": intro_upgrade(card.get("title", ""), keyword),
                "interpretation_upgrade": interpretation_upgrade(keyword),
                "ending_mix_upgrade": ending_mix_upgrade(tone_item.get("dominant_sentence_ending", "")),
                "cta_upgrade": cta_upgrade(keyword),
                "draft_path": draft.get("draft_path", ""),
                "html_path": draft.get("html_path", ""),
            }
        )

    return {
        "board_goal": "사용자에게 보여주기 전 초안의 사람 느낌과 해설 톤을 더 자연스럽게 다듬기 위한 보정 보드",
        "item_count": len(items),
        "items": items,
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# Draft Polish Board")
    lines.append("")
    lines.append("사용자에게 글을 보여주기 전에 더 사람답고 친근한 해설 톤으로 다듬기 위한 보정 제안입니다.")
    lines.append(f"- board_goal: {report.get('board_goal', '')}")
    lines.append(f"- item_count: `{report.get('item_count', 0)}`")
    lines.append("")
    for idx, item in enumerate(report.get("items", []), start=1):
        lines.append(f"## {idx}. {item.get('title', '')}")
        lines.append("")
        lines.append(f"- keyword: `{item.get('keyword', '')}`")
        lines.append(f"- ready_now: `{item.get('ready_now', False)}`")
        lines.append(f"- quality_status: `{item.get('quality_status', '')}`")
        lines.append(f"- human_tone_score: `{item.get('human_tone_score', 0)}`")
        lines.append(f"- voice_focus: {item.get('voice_focus', '')}")
        for warning in item.get("warnings", []):
            lines.append(f"- warning: {warning}")
        if item.get("first_body_paragraph"):
            lines.append(f"- current_opening: {item.get('first_body_paragraph', '')}")
        lines.append(f"- intro_upgrade: {item.get('intro_upgrade', '')}")
        lines.append(f"- interpretation_upgrade: {item.get('interpretation_upgrade', '')}")
        lines.append(f"- ending_mix_upgrade: {item.get('ending_mix_upgrade', '')}")
        lines.append(f"- cta_upgrade: {item.get('cta_upgrade', '')}")
        lines.append(f"- draft_path: `{item.get('draft_path', '')}`")
        lines.append(f"- html_path: `{item.get('html_path', '')}`")
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
