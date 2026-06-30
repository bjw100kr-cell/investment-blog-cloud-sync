#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONFIG_JSON = ROOT / "config/current_editorial_reference_patterns.json"
GROWTH_RULES_JSON = ROOT / "config/growth_rules.json"
OUTPUT_JSON = ROOT / "outputs/latest/current-reference-strategy.json"
OUTPUT_MD = ROOT / "outputs/latest/current-reference-strategy.md"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def write_markdown(payload: dict) -> None:
    lines = []
    lines.append("# Current Reference Strategy")
    lines.append("")
    lines.append("현재 잘 나가는 투자/코인 매체들의 공통 패턴을 우리 자동화 글 구조로 번역한 운영 문서입니다.")
    lines.append("")
    lines.append(f"- updated_at: `{payload.get('updated_at', '')}`")
    lines.append("")
    topic_mix = payload.get("topic_mix_policy", {})
    if topic_mix:
        lines.append("## Topic Mix Policy")
        lines.append("")
        if topic_mix.get("identity_statement"):
            lines.append(f"- identity_statement: {topic_mix.get('identity_statement', '')}")
        if topic_mix.get("top_brief_diversity_key"):
            lines.append(f"- diversity_key: `{topic_mix.get('top_brief_diversity_key', '')}`")
        for lane, label in (topic_mix.get("brand_lane_labels") or {}).items():
            lines.append(f"- brand_lane `{lane}`: `{label}`")
        for lane, weight in (topic_mix.get("weekly_mix_targets") or {}).items():
            lines.append(f"- weekly_mix_target `{lane}`: `{weight}`")
        for item in topic_mix.get("selection_rules", []):
            lines.append(f"- selection_rule: {item}")
        lines.append("")
    lines.append("## Source Patterns")
    lines.append("")
    for source in payload.get("sources", []):
        lines.append(f"### {source.get('name', '')}")
        lines.append("")
        lines.append(f"- focus: {source.get('focus', '')}")
        for item in source.get("evidence", []):
            lines.append(f"- evidence: {item}")
        for item in source.get("transferable_strengths", []):
            lines.append(f"- transferable_strength: {item}")
        lines.append("")
    lines.append("## Operating Patterns")
    lines.append("")
    for name, block in (payload.get("operating_patterns") or {}).items():
        lines.append(f"### {name}")
        lines.append("")
        for item in block.get("when_to_use", []):
            lines.append(f"- when_to_use: {item}")
        for item in block.get("must_have", []):
            lines.append(f"- must_have: {item}")
        lines.append("")
    lines.append("## Style Translation Rules")
    lines.append("")
    for item in payload.get("style_translation_rules", []):
        lines.append(f"- {item}")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def main() -> int:
    payload = load_json(CONFIG_JSON)
    payload["topic_mix_policy"] = load_json(GROWTH_RULES_JSON).get("topic_mix_policy", {})
    OUTPUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    write_markdown(payload)
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
