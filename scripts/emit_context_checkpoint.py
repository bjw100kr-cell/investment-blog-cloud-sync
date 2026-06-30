#!/usr/bin/env python3
"""Create a compact checkpoint from durable artifacts to avoid context drift."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "outputs" / "latest"
SNAPSHOT_JSON = OUTPUT_DIR / "context_checkpoint.json"
SNAPSHOT_MD = OUTPUT_DIR / "context_checkpoint.md"


def _load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _read_text(path: Path) -> str:
    if not path.exists():
        return ""
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return ""


def _parse_markdown_section(path: Path, heading: str, max_lines: int = 12) -> list[str]:
    text = _read_text(path)
    if not text:
        return []
    lines = text.splitlines()
    start = None
    heading_re = re.compile(rf"^#{{1,3}}\s+.*{re.escape(heading)}|^-+\s*{re.escape(heading)}")
    for idx, line in enumerate(lines):
        if heading_re.match(line):
            start = idx + 1
            break
    if start is None:
        return []

    out: list[str] = []
    for line in lines[start:]:
        if line.startswith("## "):
            break
        text_line = line.strip()
        if text_line:
            out.append(text_line)
        if len(out) >= max_lines:
            break
    return out


def _blogger_metrics() -> dict:
    report = _load_json(OUTPUT_DIR / "blogger-upload-report.json")
    state = _load_json(OUTPUT_DIR / "blogger-upload-state.json")

    summary = report.get("summary", {})
    items = report.get("items", [])
    if not isinstance(items, list):
        items = []
    reason_counts = Counter()
    for item in items:
        reason = item.get("reason") or ""
        reason_counts[reason] += 1

    state_items = state.get("items", {}) if isinstance(state, dict) else {}
    if isinstance(state_items, dict):
        state_list = list(state_items.values())
    elif isinstance(state_items, list):
        state_list = state_items
    else:
        state_list = []
    published_count = 0
    latest_synced_at = ""
    for item in state_list:
        if not isinstance(item, dict):
            continue
        if item.get("published"):
            published_count += 1
        synced = item.get("last_synced_at", "")
        if synced and (not latest_synced_at or synced > latest_synced_at):
            latest_synced_at = synced

    return {
        "report_summary": {
            "manifest_candidate_count": summary.get("manifest_candidate_count"),
            "processed_count": summary.get("processed_count"),
            "reason_counts": dict(reason_counts),
            "last_reason": items[0].get("reason") if items else "",
            "top_item_slug": items[0].get("slug") if items else "",
        },
        "state_summary": {
            "item_count": len(state_list),
            "published_count": published_count,
            "latest_synced_at": latest_synced_at,
        },
    }


def _inventory_metrics() -> dict:
    publish_inventory = _load_json(OUTPUT_DIR / "publish-inventory.json")
    publish_queue = _load_json(OUTPUT_DIR / "publish-queue.json")
    return {
        "inventory_summary": publish_inventory.get("summary", {}),
        "queue_summary": publish_queue.get("summary", {}),
    }


def _verification_metrics() -> dict:
    verify = _load_json(OUTPUT_DIR / "first-cloud-run-verification.json")
    if not isinstance(verify, dict):
        return {}
    return {
        "all_core_checks_passed": verify.get("all_core_checks_passed"),
        "review_approval_state_is_safe": verify.get("review_approval_state_is_safe"),
        "approval_mode": verify.get("approval_mode"),
    }


def _approval_metrics() -> dict:
    approvals = _load_json(OUTPUT_DIR / "review-approvals.json")
    if not isinstance(approvals, dict):
        return {}
    return {
        "approved_all": approvals.get("user_confirmed_all") or approvals.get("approved_all"),
        "approved_keywords": approvals.get("user_confirmed_keywords") or approvals.get("approved_keywords", []),
    }


def _next_actions() -> list[str]:
    handoff = _read_text(ROOT / "HANDOFF.md")
    if not handoff:
        return []
    out = []
    capture = False
    for line in handoff.splitlines():
        if "다음 하이프리오리티 액션" in line:
            capture = True
            continue
        if capture:
            if re.match(r"^## ", line):
                break
            if re.match(r"^\s*1\\.", line) or line.strip().startswith("- "):
                out.append(line.strip("- ").strip())
            if len(out) >= 6:
                break
    return out


def make_checkpoint(note: str = "") -> dict:
    data = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "goal": "주식/코인/세계경제 투자 블로그 자동화 운영 지속 및 수익화",
        "blogger": _blogger_metrics(),
        "inventory": _inventory_metrics(),
        "verification": _verification_metrics(),
        "approvals": _approval_metrics(),
        "next_actions": _next_actions(),
        "source_notes": _parse_markdown_section(ROOT / "CONVERSATION_SUMMARY.md", "최근 확인된 병목", max_lines=6),
    }
    if note:
        data["note"] = note
    return data


def write_files(snapshot: dict) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    SNAPSHOT_JSON.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2), encoding="utf-8")

    md = [
        "# Context Snapshot",
        "",
        f"생성 시각(UTC): `{snapshot.get('generated_at_utc')}`",
        "",
        f"- 목표: {snapshot.get('goal')}",
        "",
        "## 핵심 상태",
        f"- published_count: `{snapshot['blogger']['state_summary'].get('published_count')}`",
        f"- upload processed_count: `{snapshot['blogger']['report_summary'].get('processed_count')}`",
        f"- latest_synced_at: `{snapshot['blogger']['state_summary'].get('latest_synced_at')}`",
        f"- all_core_checks_passed: `{snapshot['verification'].get('all_core_checks_passed')}`",
        "",
    ]
    if snapshot.get("note"):
        md += ["## 이번 체크포인트 노트", f"- {snapshot['note']}", ""]

    md += [
        "## 최근 병목 요약",
    ]
    source_notes = snapshot.get("source_notes") or []
    if source_notes:
        for line in source_notes:
            cleaned = line.lstrip("- ").strip()
            md.append(f"- {cleaned}")
    else:
        md.append("- 최근 병목이 기록되지 않았습니다.")

    md += ["", "## 다음 액션"]
    for action in snapshot.get("next_actions", []):
        md.append(f"- {action}")
    if not snapshot.get("next_actions"):
        md.append("- 다음 액션은 HANDOFF.md의 '다음 하이프리오리티 액션' 섹션을 확인하세요.")

    md += [
        "",
        "## 즉시 재개 커맨드",
        "- `python3 scripts/run_pipeline.sh`",
        "- `python3 scripts/emit_context_checkpoint.py`",
        "- `jq '.summary.processed_count,.summary.review_required,.items[0:4]' outputs/latest/blogger-upload-report.json`",
    ]
    SNAPSHOT_MD.write_text("\n".join(md) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--note", default="", help="Optional checkpoint note for recovery sessions")
    args = parser.parse_args()
    snapshot = make_checkpoint(note=args.note)
    write_files(snapshot)
    print(f"Context checkpoint written: {SNAPSHOT_JSON}")


if __name__ == "__main__":
    main()
