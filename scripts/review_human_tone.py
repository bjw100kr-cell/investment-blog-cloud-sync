#!/usr/bin/env python3
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKETS_JSON = ROOT / "outputs/latest/draft-packets.json"
DRAFTS_DIR = ROOT / "outputs/latest/drafts"
OUTPUT_JSON = ROOT / "outputs/latest/human-tone-review.json"
OUTPUT_MD = ROOT / "outputs/latest/human-tone-review.md"
VOICE_RULES_JSON = ROOT / "config/human_voice_rules.json"

UNCERTAINTY_MARKERS = [
    "가능성",
    "시나리오",
    "다만",
    "반면",
    "변수",
]


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
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def split_sentences(text: str) -> list[str]:
    chunks = re.split(r"(?<=[.!?])\s+|(?<=[다요죠]\.)\s+|\n+", text)
    return [chunk.strip() for chunk in chunks if chunk.strip()]


def dominant_ending_ratio(sentences: list[str]) -> tuple[str, float]:
    endings = []
    for sentence in sentences:
        compact = sentence.rstrip(" .!?\"'")
        match = re.search(r"([가-힣]{2,6})$", compact)
        if match:
            endings.append(match.group(1))

    if not endings:
        return "", 0.0

    counts = {}
    for ending in endings:
        counts[ending] = counts.get(ending, 0) + 1

    dominant = max(counts, key=counts.get)
    return dominant, counts[dominant] / len(endings)


def extract_intro_preview(text: str) -> str:
    marker = "## 도입부"
    if marker not in text:
        paragraphs = [part.strip() for part in text.split("\n\n") if part.strip()]
        return "\n\n".join(paragraphs[:2])

    intro_part = text.split(marker, 1)[1]
    if "\n## " in intro_part:
        intro_part = intro_part.split("\n## ", 1)[0]
    paragraphs = [part.strip() for part in intro_part.split("\n\n") if part.strip()]
    return "\n\n".join(paragraphs[:2])


def analyze_draft(text: str, packet: dict, voice_rules: dict) -> dict:
    robotic_phrases = voice_rules.get("avoid_phrases", [])
    bridge_phrases = voice_rules.get("reader_bridge_phrases", [])
    direct_address_phrases = voice_rules.get("direct_address_phrases", [])
    interpretation_markers = voice_rules.get("interpretation_markers", [])
    rhythm_targets = voice_rules.get("sentence_rhythm_targets", {})

    robotic_hits = [phrase for phrase in robotic_phrases if phrase in text]
    bridge_hits = [phrase for phrase in bridge_phrases if phrase in text]
    direct_address_hits = [phrase for phrase in direct_address_phrases if phrase in text]
    interpretation_hits = [phrase for phrase in interpretation_markers if phrase in text]
    uncertainty_hits = [phrase for phrase in UNCERTAINTY_MARKERS if phrase in text]
    year_anchor = bool(re.search(r"20\d{2}", text))
    number_anchor = bool(re.search(r"\d", text))
    paragraphs = [part.strip() for part in text.split("\n\n") if part.strip()]
    short_paragraphs = sum(1 for part in paragraphs if len(part) <= 120)
    long_paragraphs = sum(1 for part in paragraphs if len(part) >= 260)
    intro_preview = extract_intro_preview(text)
    intro_direct_address = any(phrase in intro_preview for phrase in direct_address_phrases + bridge_phrases)
    sentences = split_sentences(text)
    dominant_ending, ending_ratio = dominant_ending_ratio(sentences)

    max_dominant_ratio = float(rhythm_targets.get("max_dominant_ending_ratio", 0.72))
    min_direct_address_hits = int(rhythm_targets.get("minimum_direct_address_hits", 2))
    min_interpretation_hits = int(rhythm_targets.get("minimum_interpretation_hits", 2))

    score = 100
    score -= len(robotic_hits) * 12
    if not bridge_hits:
        score -= 12
    if len(direct_address_hits) < min_direct_address_hits:
        score -= 8
    if len(interpretation_hits) < min_interpretation_hits:
        score -= 8
    if not uncertainty_hits:
        score -= 10
    if not year_anchor:
        score -= 8
    if not number_anchor:
        score -= 8
    if not short_paragraphs:
        score -= 6
    if not long_paragraphs:
        score -= 4
    if not intro_direct_address:
        score -= 8
    if ending_ratio > max_dominant_ratio:
        score -= 10
    score = max(score, 0)

    warnings = []
    if robotic_hits:
        warnings.append(f"AI스러운 관용 문구 감지: {', '.join(robotic_hits)}")
    if not bridge_hits:
        warnings.append("독자에게 말 걸듯 연결하는 문장이 부족함")
    if len(direct_address_hits) < min_direct_address_hits:
        warnings.append("독자 관점에서 직접 말 거는 문장이 부족함")
    if len(interpretation_hits) < min_interpretation_hits:
        warnings.append("숫자/뉴스의 의미를 풀어주는 해석 문장이 부족함")
    if not uncertainty_hits:
        warnings.append("시나리오/조건형 문장이 부족함")
    if not year_anchor:
        warnings.append("절대 날짜 또는 연도 기준 문장이 보이지 않음")
    if not number_anchor:
        warnings.append("숫자나 구체 근거가 부족해 보일 수 있음")
    if not intro_direct_address:
        warnings.append("도입부에서 독자가 왜 지금 읽어야 하는지 직접 잡아주지 못함")
    if ending_ratio > max_dominant_ratio:
        warnings.append(f"문장 끝 어미가 `{dominant_ending}` 쪽으로 과하게 반복됨")

    return {
        "keyword": packet.get("keyword", ""),
        "recommended_title": packet.get("recommended_title", ""),
        "score": score,
        "robotic_phrase_hits": robotic_hits,
        "reader_bridge_hits": bridge_hits,
        "direct_address_hits": direct_address_hits,
        "interpretation_hits": interpretation_hits,
        "uncertainty_hits": uncertainty_hits,
        "warnings": warnings,
        "paragraph_count": len(paragraphs),
        "short_paragraphs": short_paragraphs,
        "long_paragraphs": long_paragraphs,
        "intro_direct_address": intro_direct_address,
        "dominant_sentence_ending": dominant_ending,
        "dominant_sentence_ending_ratio": round(ending_ratio, 3),
    }


def main() -> int:
    packets = load_json(PACKETS_JSON).get("packets", [])
    voice_rules = load_json(VOICE_RULES_JSON)
    results = []

    for idx, packet in enumerate(packets, start=1):
        draft_path = DRAFTS_DIR / f"{idx:02d}-{slugify(packet['keyword'])}.md"
        if not draft_path.exists():
            results.append(
                {
                    "keyword": packet["keyword"],
                    "score": 0,
                    "warnings": ["draft file not found"],
                }
            )
            continue

        text = draft_path.read_text()
        if text.startswith("# Draft not generated"):
            results.append(
                {
                    "keyword": packet["keyword"],
                    "score": 0,
                    "warnings": ["draft not generated because OPENAI_API_KEY is missing"],
                }
            )
            continue

        results.append(analyze_draft(text, packet, voice_rules))

    payload = {"items": results}
    OUTPUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2))

    lines = []
    lines.append("# 사람 느낌 문체 점검")
    lines.append("")
    for item in results:
        lines.append(f"## {item['keyword']}")
        lines.append("")
        lines.append(f"- 점수: {item['score']}")
        if "dominant_sentence_ending" in item:
            lines.append(
                f"- 어미 반복: `{item['dominant_sentence_ending']}` / 비중 {item['dominant_sentence_ending_ratio']}"
            )
        for warning in item.get("warnings", []):
            lines.append(f"- 경고: {warning}")
        lines.append("")

    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
