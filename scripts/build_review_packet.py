#!/usr/bin/env python3
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PUBLISH_INVENTORY_JSON = ROOT / "outputs/latest/publish-inventory.json"
PUBLISH_QUEUE_JSON = ROOT / "outputs/latest/publish-queue.json"
VOICE_RULES_JSON = ROOT / "config/human_voice_rules.json"
OUTPUT_JSON = ROOT / "outputs/latest/review-packet.json"
OUTPUT_MD = ROOT / "outputs/latest/review-packet.md"
APPROVAL_DASHBOARD_JSON = ROOT / "outputs/latest/approval-dashboard.json"
APPROVALS_EXAMPLE_JSON = ROOT / "outputs/latest/review-approvals.example.json"
APPROVALS_JSON = ROOT / "outputs/latest/review-approvals.json"
APPROVAL_HELPER = ROOT / "scripts/set_review_approvals.py"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def resolve_workspace_path(path_text: str) -> Path:
    path = Path(path_text)
    if path.exists():
        return path
    parts = path.parts
    if "outputs" in parts:
        output_index = parts.index("outputs")
        candidate = ROOT / Path(*parts[output_index:])
        if candidate.exists():
            return candidate
    marker = "investment-blog-cloud-sync/"
    if marker in path_text:
        relative = path_text.split(marker, 1)[1]
        return ROOT / relative
    return path


def first_content_paragraphs(text: str, limit: int = 2) -> list[str]:
    paragraphs = []
    for block in text.split("\n\n"):
        compact = " ".join(block.split()).strip()
        if not compact:
            continue
        if compact.startswith("#"):
            continue
        if compact.startswith("## CTA") or compact.startswith("## 면책문구"):
            continue
        paragraphs.append(compact)
        if len(paragraphs) >= limit:
            break
    return paragraphs


def sentence_count(text: str) -> int:
    chunks = re.split(r"[.!?]\s+|\n+", text)
    return len([chunk for chunk in chunks if chunk.strip()])


def build_lookup(items: list[dict], key: str) -> dict:
    return {item.get(key): item for item in items if item.get(key)}


def analyze_text(text: str, voice_rules: dict) -> dict:
    avoid_phrases = voice_rules.get("avoid_phrases", [])
    direct_address = voice_rules.get("direct_address_phrases", [])
    interpretation_markers = voice_rules.get("interpretation_markers", [])
    interpretation_markers = [
        *interpretation_markers,
        "투자자 언어로",
        "뜻에 가깝습니다",
        "시장 해석",
        "뉴스의 질이 달라",
        "왜 시장이 반응",
    ]
    bridge_phrases = voice_rules.get("reader_bridge_phrases", [])

    avoid_hits = [phrase for phrase in avoid_phrases if phrase and phrase in text]
    direct_hits = [phrase for phrase in direct_address if phrase and phrase in text]
    interpretation_hits = [phrase for phrase in interpretation_markers if phrase and phrase in text]
    bridge_hits = [phrase for phrase in bridge_phrases if phrase and phrase in text]
    has_year = bool(re.search(r"20\d{2}", text))
    has_number = bool(re.search(r"\d", text))
    has_balance = any(token in text for token in ["다만", "반면", "변수", "시나리오"])
    paragraphs = [part.strip() for part in text.split("\n\n") if part.strip()]

    score = 100
    score -= len(avoid_hits) * 15
    if not direct_hits:
        score -= 10
    if not interpretation_hits:
        score -= 12
    if not bridge_hits:
        score -= 8
    if not has_year:
        score -= 8
    if not has_number:
        score -= 8
    if not has_balance:
        score -= 8
    if len(paragraphs) < 8:
        score -= 6
    score = max(score, 0)

    verdict = "approve"
    if score < 75 or avoid_hits:
        verdict = "revise"
    elif score < 85:
        verdict = "review_carefully"

    warnings = []
    if avoid_hits:
        warnings.append(f"피해야 할 표현 감지: {', '.join(avoid_hits)}")
    if not direct_hits:
        warnings.append("독자에게 직접 말 거는 문장이 부족함")
    if not interpretation_hits:
        warnings.append("뉴스/숫자의 의미를 풀어주는 해석 문장이 부족함")
    if not bridge_hits:
        warnings.append("문단 전환용 연결 문장이 부족함")
    if not has_year:
        warnings.append("절대 날짜 또는 연도 기준 문장이 부족함")
    if not has_number:
        warnings.append("숫자 근거가 거의 없음")
    if not has_balance:
        warnings.append("다만/반면/변수 같은 균형 문장이 부족함")

    return {
        "score": score,
        "verdict": verdict,
        "warnings": warnings,
        "avoid_hits": avoid_hits,
        "direct_address_hits": direct_hits,
        "interpretation_hits": interpretation_hits,
        "bridge_hits": bridge_hits,
        "has_year": has_year,
        "has_number": has_number,
        "has_balance": has_balance,
        "paragraph_count": len(paragraphs),
        "sentence_count": sentence_count(text),
    }


def build_item(manifest: dict, inventory_item: dict, queue_item: dict, voice_rules: dict) -> dict:
    draft_path = resolve_workspace_path(manifest.get("draft_path", ""))
    draft_text = draft_path.read_text() if draft_path.exists() else ""
    analysis = analyze_text(draft_text, voice_rules) if draft_text else {
        "score": 0,
        "verdict": "revise",
        "warnings": ["draft file missing"],
        "avoid_hits": [],
        "direct_address_hits": [],
        "interpretation_hits": [],
        "bridge_hits": [],
        "has_year": False,
        "has_number": False,
        "has_balance": False,
        "paragraph_count": 0,
        "sentence_count": 0,
    }
    preview = first_content_paragraphs(draft_text)
    image_plan = manifest.get("image_plan", [])[:2]
    return {
        "keyword": manifest.get("keyword", ""),
        "title": manifest.get("title", ""),
        "inventory_type": inventory_item.get("inventory_type", ""),
        "role": inventory_item.get("role", ""),
        "recommended_publish_date": manifest.get("recommended_publish_date", ""),
        "priority_score": inventory_item.get("priority_score", 0),
        "search_intent": inventory_item.get("search_intent", ""),
        "cta_focus": inventory_item.get("cta_focus", ""),
        "draft_path": manifest.get("draft_path", ""),
        "html_path": manifest.get("html_path", ""),
        "manifest_path": manifest.get("manifest_path", ""),
        "review_preview": preview,
        "review_score": analysis["score"],
        "review_verdict": analysis["verdict"],
        "review_warnings": analysis["warnings"],
        "paragraph_count": analysis["paragraph_count"],
        "sentence_count": analysis["sentence_count"],
        "queue_bucket": queue_item.get("publish_bucket", inventory_item.get("publish_bucket", "")),
        "retention_cta_enabled": manifest.get("retention_cta_enabled", False),
        "retention_cta": manifest.get("retention_cta", {}),
        "image_manual_review_required": manifest.get("image_manual_review_required", False),
        "image_slots": [
            {
                "slot": image.get("slot", ""),
                "slot_label": image.get("slot_label", ""),
                "provider_name": image.get("provider_name", ""),
                "search_query": image.get("search_query", ""),
                "search_url": image.get("search_url", ""),
                "license_label": image.get("license_label", ""),
                "license_url": image.get("license_url", ""),
                "alt_text": image.get("alt_text", ""),
            }
            for image in image_plan
        ],
    }


def load_review_helper_command() -> str:
    dashboard = load_json(APPROVAL_DASHBOARD_JSON)
    batches = dashboard.get("batches", [])
    helper = ""
    for batch in batches:
        if batch.get("id") == "due_soon_main":
            helper = batch.get("confirmation_command", "")
            break
    if not helper:
        helper = "python3 {APPROVAL_HELPER} --all".format(APPROVAL_HELPER=APPROVAL_HELPER)
    return helper


def main() -> int:
    inventory = load_json(PUBLISH_INVENTORY_JSON)
    queue = load_json(PUBLISH_QUEUE_JSON)
    voice_rules = load_json(VOICE_RULES_JSON)
    queue_lookup = build_lookup(queue.get("items", []), "keyword")
    items = []

    for inventory_item in inventory.get("items", []):
        manifest_path = resolve_workspace_path(inventory_item.get("manifest_path", ""))
        if not manifest_path.exists():
            continue
        manifest = load_json(manifest_path)
        queue_item = queue_lookup.get(inventory_item.get("source_keyword")) or queue_lookup.get(inventory_item.get("keyword")) or {}
        items.append(build_item(manifest, inventory_item, queue_item, voice_rules))

    payload = {
        "summary": {
            "item_count": len(items),
            "approve_count": sum(1 for item in items if item["review_verdict"] == "approve"),
            "review_carefully_count": sum(1 for item in items if item["review_verdict"] == "review_carefully"),
            "revise_count": sum(1 for item in items if item["review_verdict"] == "revise"),
        },
        "items": items,
        "approval_file": str(APPROVALS_JSON),
    }
    OUTPUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2))

    lines = [
        "# Review Packet",
        "",
        "업로드 전에 운영자와 사용자가 함께 확인할 글 검토 패킷입니다.",
        "",
        f"- 사용자 최종 확인 파일: `{APPROVALS_JSON}`",
        f"- 사용자 확인 헬퍼: `{load_review_helper_command() or f'python3 {APPROVAL_HELPER} --all'}` 또는 `python3 {APPROVAL_HELPER} --all`",
        f"- 총 검토 대상: `{payload['summary']['item_count']}`",
        f"- 바로 최종 확인 가능: `{payload['summary']['approve_count']}`",
        f"- 주의 검토: `{payload['summary']['review_carefully_count']}`",
        f"- 수정 권장: `{payload['summary']['revise_count']}`",
        "",
    ]

    for item in items:
        lines.append(f"## {item['title']}")
        lines.append("")
        lines.append(f"- keyword: `{item['keyword']}`")
        lines.append(f"- type: `{item['inventory_type']}` / role `{item['role']}`")
        lines.append(f"- publish date: `{item['recommended_publish_date'] or 'unscheduled'}`")
        lines.append(f"- priority: `{item['priority_score']}`")
        lines.append(f"- internal review: `{item['review_verdict']}` / score `{item['review_score']}`")
        lines.append(f"- intent: {item['search_intent']}")
        lines.append(f"- CTA focus: {item['cta_focus']}")
        if item.get("retention_cta_enabled"):
            retention_cta = item.get("retention_cta", {})
            lines.append(f"- final retention CTA: {retention_cta.get('inline_cta_now', '')}")
            if retention_cta.get("telegram_cta_later"):
                lines.append(f"- later revisit CTA: {retention_cta.get('telegram_cta_later', '')}")
        lines.append(f"- draft: `{item['draft_path']}`")
        lines.append(f"- rendered html: `{item['html_path']}`")
        if item.get("image_slots"):
            lines.append(f"- image review required: `{item.get('image_manual_review_required', False)}`")
            for image in item["image_slots"]:
                lines.append(
                    f"- image {image.get('slot_label', image.get('slot'))}: {image.get('provider_name', '')} / query `{image.get('search_query', '')}` / license {image.get('license_label', '')}"
                )
                lines.append(
                    f"- image apply helper: `python3 {ROOT / 'scripts/set_image_selection.py'} --keyword {item['keyword']} --slot {image.get('slot', '')} --selected-url <IMAGE_URL> --selected-credit \"Photo by ...\" --approve`"
                )
        for warning in item["review_warnings"]:
            lines.append(f"- warning: {warning}")
        if item["review_preview"]:
            lines.append("- preview:")
            for paragraph in item["review_preview"]:
                lines.append(f"  {paragraph}")
        lines.append("")

    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")

    APPROVALS_EXAMPLE_JSON.write_text(
        json.dumps(
            {
                "user_final_confirmation_required": True,
                "user_confirmed_all": False,
                "user_confirmed_keywords": [],
                "approved_all": False,
                "approved_keywords": [],
                "notes": "복사해서 review-approvals.json 으로 만든 뒤 user_confirmed_keywords 에 내가 최종 확인한 keyword 를 넣습니다.",
            },
            ensure_ascii=False,
            indent=2,
        )
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
