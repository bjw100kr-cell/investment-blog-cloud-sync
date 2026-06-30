#!/usr/bin/env python3
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

ROOT = Path(__file__).resolve().parents[1]
SETUP_JSON = ROOT / "outputs/latest/setup-check-report.json"
PUBLISH_INVENTORY_JSON = ROOT / "outputs/latest/publish-inventory.json"
APPROVALS_JSON = ROOT / "outputs/latest/review-approvals.json"
QUALITY_GATE_JSON = ROOT / "outputs/latest/pre-publish-quality-gate.json"
PLATFORM_PUBLISH_PLAN_JSON = ROOT / "outputs/latest/platform-publish-plan.json"
OUTPUT_JSON = ROOT / "outputs/latest/cross-platform-publish-pack.json"
OUTPUT_MD = ROOT / "outputs/latest/cross-platform-publish-pack.md"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def integration_lookup(setup: dict) -> dict:
    return {item.get("name"): item for item in setup.get("integrations", [])}


def normalized_confirmations(approvals: dict) -> tuple[bool, list[str]]:
    confirmed_all = bool(approvals.get("user_confirmed_all", approvals.get("approved_all", False)))
    confirmed_keywords = approvals.get("user_confirmed_keywords", approvals.get("approved_keywords", []))
    return confirmed_all, [item for item in confirmed_keywords if item]


def is_approved(item: dict, approvals: dict) -> bool:
    confirmed_all, confirmed_keywords = normalized_confirmations(approvals)
    if confirmed_all:
        return True
    approved = set(confirmed_keywords)
    candidates = {
        item.get("keyword", ""),
        item.get("source_keyword", ""),
        Path(item.get("html_path", "")).stem,
    }
    return any(candidate in approved for candidate in candidates if candidate)


def build_quality_lookup() -> dict[str, str]:
    if not QUALITY_GATE_JSON.exists():
        return {}
    payload = load_json(QUALITY_GATE_JSON)
    lookup = {}
    for entry in payload.get("items", []):
        status = entry.get("status", "")
        keyword = entry.get("keyword", "")
        html_path = entry.get("html_path", "")
        source_group = entry.get("source_group", "")
        if keyword and status:
            lookup[keyword] = status
            if source_group:
                lookup[f"{keyword}:{source_group}"] = status
        if html_path:
            lookup[Path(html_path).stem] = status
    return lookup


def is_quality_ready(item: dict, quality_lookup: dict[str, str]) -> bool:
    if not quality_lookup:
        return True
    keyword = item.get("keyword", "")
    html_path = item.get("html_path", "")
    source_group = "seo" if item.get("inventory_type") == "seo_followup" else "main"
    status = quality_lookup.get(keyword) or quality_lookup.get(f"{keyword}:{source_group}") or quality_lookup.get(
        Path(html_path).stem if html_path else ""
    )
    if not status:
        return True
    return status == "pass"


def summarize_selected_items(require_quality: bool = True) -> list[dict]:
    inventory = load_json(PUBLISH_INVENTORY_JSON)
    approvals = load_json(APPROVALS_JSON)
    quality_lookup = build_quality_lookup()
    selected = []
    for item in inventory.get("items", []):
        if not item.get("ready_to_upload"):
            continue
        if not is_approved(item, approvals):
            continue
        if require_quality and not is_quality_ready(item, quality_lookup):
            continue
        selected.append(item)
    return selected


def build_platform_channels(items: list[dict], setup: dict) -> list[dict]:
    integrations = integration_lookup(setup)
    return [
        {
            "name": "blogger",
            "label": "Blogger (자동)",
            "ready": integrations.get("blogger_upload", {}).get("ready", False),
            "mode": "auto",
            "command": "python3 scripts/upload_blogger_drafts.py",
            "ready_item_count": len(items),
            "items": [to_pack_item(item) for item in items],
        },
        {
            "name": "wordpress",
            "label": "WordPress (자동)",
            "ready": integrations.get("wordpress_upload", {}).get("ready", False),
            "mode": "auto",
            "command": "python3 scripts/upload_wordpress_drafts.py",
            "ready_item_count": len(items),
            "items": [to_pack_item(item) for item in items],
        },
    ]


def build_manual_channels(items: list[dict], quality_lookup: dict[str, str]) -> list[dict]:
    naver_blog_url = os.getenv("NAVER_BLOG_MANAGE_URL", "https://blog.naver.com")
    tistory_url = os.getenv("TISTORY_MANAGE_URL", "https://www.tistory.com/manage")
    packed_items = [to_pack_item(item, quality_lookup) for item in items]
    return [
        {
            "name": "naver_blog",
            "label": "네이버 블로그 (수동)",
            "ready": True,
            "mode": "manual",
            "reason": "운영 정책상 수동 운영 채널로 분리",
            "editor_url": naver_blog_url,
            "recommended_steps": [
                "1) `html_path`에 적힌 파일을 열어 전체 본문을 복사",
                "2) 네이버 블로그 글쓰기 에디터에서 새 글 작성으로 붙여넣기",
                "3) 카테고리/태그: `경제`, `투자`, `주식`, `코인` 중심으로 정리",
                "공개 범위를 확인하고 발행",
                "발행한 뒤 링크에 `출처`를 한 줄 넣고, 수익화 성과 트래킹 시트에 URL 기록",
                "발행 URL을 추후 수동 성과 추적용으로 기록",
                "중복/오타 검수 후 바로 다음 글로 이동",
            ],
            "execution_notes": [
                "네이버는 현재 수동 채널입니다. 동일 후보 글이 여러 개면 한 번에 하나씩 발행하세요.",
                "업로드 대상이 여러 개면 `1번 후보 -> 발행 -> 다음 후보`로 순서 유지가 효율적입니다.",
            ],
            "ready_item_count": len(packed_items),
            "ready_command": f"open {naver_blog_url} and paste html_path content",
            "quality_note": "수동 채널은 품질 게이트 상태와 상관없이 수동 발행 후보로 노출됩니다.",
            "items": packed_items,
        },
        {
            "name": "tistory",
            "label": "티스토리 (수동)",
            "ready": True,
            "mode": "manual",
            "reason": "운영 정책상 수동 운영 채널로 분리",
            "editor_url": tistory_url,
            "recommended_steps": [
                "1) `html_path`에 적힌 파일을 열어 본문을 복사",
                "2) 티스토리 새 글 작성으로 붙여넣기",
                "3) 썸네일/태그/카테고리를 시장 흐름 중심으로 정렬",
                "발행 후 상단 고정 링크와 관련 글 이동 경로를 점검",
                "문단 구분이 깨지면 HTML 보기에서 한 번 더 줄 바꿈 정리",
                "발행 URL과 대표 키워드를 수기 스프레드시트나 텍스트로 저장",
            ],
            "execution_notes": [
                "티스토리는 수동 채널이라 자동 업로드가 없고, 발행은 사용자가 직접 확인해야 합니다.",
                "SEO 글이면 `해시태그`에 핵심 키워드 2~3개만 짧게 넣어 검색 유입을 확보하세요.",
            ],
            "ready_command": f"open {tistory_url} and create a new post with copied html_path content",
            "ready_item_count": len(packed_items),
            "items": packed_items,
        },
    ]


def _quality_entry_for_item(item: dict, quality_lookup: dict[str, str]) -> str:
    keyword = item.get("keyword", "")
    html_path = item.get("html_path", "")
    source_group = "seo" if item.get("inventory_type") == "seo_followup" else "main"
    return (
        quality_lookup.get(keyword)
        or quality_lookup.get(f"{keyword}:{source_group}")
        or quality_lookup.get(Path(html_path).stem if html_path else "")
        or "unknown"
    )


def to_pack_item(item: dict, quality_lookup: Optional[dict[str, str]] = None) -> dict:
    quality_lookup = quality_lookup or {}
    return {
        "inventory_sequence": item.get("inventory_sequence"),
        "inventory_type": item.get("inventory_type"),
        "keyword": item.get("keyword", ""),
        "source_keyword": item.get("source_keyword", ""),
        "title": item.get("title", ""),
        "publish_bucket": item.get("publish_bucket", ""),
        "recommended_publish_date": item.get("recommended_publish_date", ""),
        "priority_score": item.get("priority_score", 0),
        "html_path": item.get("html_path", ""),
        "manifest_path": item.get("manifest_path", ""),
        "quality_status": _quality_entry_for_item(item, quality_lookup),
    }


def build_report() -> dict:
    setup = load_json(SETUP_JSON)
    platform_plan = load_json(PLATFORM_PUBLISH_PLAN_JSON)
    selected = summarize_selected_items(require_quality=True)
    manual_selected = summarize_selected_items(require_quality=False)
    quality_lookup = build_quality_lookup()

    publish_date = datetime.now(timezone.utc).isoformat()
    auto_channels = build_platform_channels(selected, setup)
    manual_channels = build_manual_channels(manual_selected, quality_lookup)

    return {
        "generated_at": publish_date,
        "automation_policy": platform_plan.get("automation_policy", "automation-first"),
        "primary_channel": platform_plan.get("primary_channel", "blogger"),
        "secondary_channel": platform_plan.get("secondary_channel", "wordpress"),
        "selected_count": len(selected),
        "manual_selected_count": len(manual_selected),
        "manual_channels": manual_channels,
        "auto_channels": auto_channels,
    }


def to_md_line(item: dict) -> str:
    return (
        f"- [{item.get('inventory_sequence')}] {item.get('title', '')} "
        f"| keyword={item.get('keyword', '')} "
        f"| score={item.get('priority_score', 0)} "
        f"| quality={item.get('quality_status', 'unknown')} "
        f"| date={item.get('recommended_publish_date', '')}"
    )


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# Cross-Platform Publish Pack")
    lines.append("")
    lines.append(f"- generated_at: `{report.get('generated_at', '')}`")
    lines.append(f"- selected_count: `{report.get('selected_count', 0)}`")
    lines.append(f"- manual_selected_count: `{report.get('manual_selected_count', 0)}`")
    lines.append(f"- automation_policy: `{report.get('automation_policy', '')}`")
    lines.append(f"- primary_channel: `{report.get('primary_channel', 'blogger')}`")
    lines.append(f"- secondary_channel: `{report.get('secondary_channel', 'wordpress')}`")
    lines.append("")

    lines.append("## 자동 채널")
    lines.append("")
    for channel in report.get("auto_channels", []):
        lines.append(f"### {channel.get('label', channel.get('name', ''))}")
        lines.append(f"- mode: `{channel.get('mode', '')}`")
        lines.append(f"- ready: `{channel.get('ready', False)}`")
        lines.append(f"- ready_item_count: `{channel.get('ready_item_count', 0)}`")
        lines.append(f"- command: `{channel.get('command', '')}`")
        if channel.get("ready", False):
            lines.append("- status: `ready_to_publish_candidates`")
        else:
            lines.append("- status: `waiting_for_credentials`")
        lines.append("")
        lines.append("#### 후보 글")
        if channel.get("items"):
            for item in channel.get("items", []):
                lines.append(to_md_line(item))
                if item.get("html_path"):
                    lines.append(f"  - html_path: `{item.get('html_path')}`")
        else:
            lines.append("- 후보 글이 없습니다.")
        lines.append("")

    lines.append("## 수동 채널")
    lines.append("")
    for channel in report.get("manual_channels", []):
        lines.append(f"### {channel.get('label', channel.get('name', ''))}")
        lines.append(f"- reason: {channel.get('reason', '')}")
        lines.append(f"- editor_url: `{channel.get('editor_url', '')}`")
        lines.append(f"- ready: `{channel.get('ready', False)}`")
        lines.append(f"- mode: `{channel.get('mode', '')}`")
        lines.append(f"- ready_item_count: `{channel.get('ready_item_count', 0)}`")
        if not channel.get("ready_item_count"):
            lines.append("- candidate_status: `not ready: 승인/품질 조건이 맞는 후보가 없습니다`")
        if channel.get("ready_command"):
            lines.append(f"- ready_command: `{channel.get('ready_command', '')}`")
        if channel.get("quality_note"):
            lines.append(f"- quality_note: `{channel.get('quality_note', '')}`")
        lines.append("- publishing_steps:")
        for step in channel.get("recommended_steps", []):
            lines.append(f"  - {step}")
        if channel.get("execution_notes"):
            lines.append("- execution_notes:")
            for note in channel.get("execution_notes", []):
                lines.append(f"  - {note}")
        lines.append("")
        lines.append("#### 후보 글 (복사 대상)")
        if channel.get("items"):
            for item in channel.get("items", []):
                lines.append(to_md_line(item))
                if item.get("html_path"):
                    lines.append(f"  - html_path: `{item.get('html_path')}`")
        else:
            lines.append("- 후보 글이 없습니다.")
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
