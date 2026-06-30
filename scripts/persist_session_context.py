#!/usr/bin/env python3
"""Persist a compact session memory document for long-running sessions.

Purpose:
- save the latest durable facts to a small file
- keep a chronological memory log for handoff
- support context-window-safe resumption without scanning chat history
"""

from __future__ import annotations

import argparse
import json
import re
from collections import OrderedDict
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "outputs" / "latest"
SUMMARY_PATH = ROOT / "CONVERSATION_SUMMARY.md"
CONTEXT_MD = OUTPUT_DIR / "context_checkpoint.md"
CONTEXT_JSON = OUTPUT_DIR / "context_checkpoint.json"
MEMO_DIR = OUTPUT_DIR / "session_memos"
MEMO_DIR.mkdir(parents=True, exist_ok=True)
MEMO_LOG = MEMO_DIR / "session_memories.md"
MEMO_JSON = MEMO_DIR / "session_memories.jsonl"

POLICY_PATH = ROOT / "CONTEXT_PROTOCOL.md"


def _load_json(path: Path) -> dict[str, Any]:
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


def _inventory_count() -> int:
    raw_inventory = _load_json(OUTPUT_DIR / "publish-inventory.json")
    if not raw_inventory:
        return 0

    items = raw_inventory.get("items")
    if isinstance(items, list):
        return len(items)

    items = raw_inventory.get("summaries") or raw_inventory.get("posts")
    if isinstance(items, list):
        return len(items)

    summary_total = raw_inventory.get("summary", {}).get("total")
    if isinstance(summary_total, int):
        return summary_total
    return 0


def _extract_actions_from_handoff() -> list[str]:
    handoff = _read_text(ROOT / "HANDOFF.md")
    if not handoff:
        return []

    active = False
    actions: list[str] = []
    for line in handoff.splitlines():
        if "다음 하이프리오리티 액션" in line:
            active = True
            continue
        if active:
            if re.match(r"^## ", line):
                break
            text = line.strip()
            if text.startswith("- ") or re.match(r"^\d+\.", text):
                clean = text.lstrip("- ").strip()
                if clean:
                    actions.append(clean)
            if len(actions) >= 6:
                break
    return actions


def _korea_now() -> str:
    kst = datetime.now(timezone.utc) + timedelta(hours=9)
    return kst.strftime("%Y-%m-%d %H:%M:%S KST")


def _build_memory(note: str) -> dict[str, Any]:
    checkpoint = _load_json(CONTEXT_JSON)
    blog_summary = checkpoint.get("blogger", {}).get("report_summary", {})
    verification = checkpoint.get("verification", {})
    state = checkpoint.get("blogger", {}).get("state_summary", {})
    inventory = checkpoint.get("inventory", {})
    approvals = checkpoint.get("approvals", {})

    report = OrderedDict()
    report["generated_at_kst"] = _korea_now()
    report["note"] = note or "manual"
    report["goal"] = checkpoint.get("goal", "주식/코인/세계경제 투자 블로그 운영")
    report["uploaded_published_count"] = state.get("published_count", 0)
    report["latest_upload_processed_count"] = blog_summary.get("processed_count", 0)
    report["latest_synced_at"] = state.get("latest_synced_at", "")
    report["last_inventory_count"] = _inventory_count() or inventory.get("inventory_summary", {}).get("total", 0)
    report["all_core_checks_passed"] = verification.get("all_core_checks_passed", False)
    report["review_status_safe"] = verification.get("review_approval_state_is_safe", "")
    report["approved_keywords"] = approvals.get("approved_keywords", [])
    report["top_next_actions"] = _extract_actions_from_handoff()
    report["checkpoint_file"] = str(CONTEXT_JSON)
    report["policy_file"] = str(POLICY_PATH)
    return report


def _render_summary_md(memory: dict[str, Any]) -> str:
    actions = memory.get("top_next_actions", [])
    return "\n".join(
        [
            "# 대화 및 작업 요약 (자동 압축)",
            "",
            f"생성일: {memory['generated_at_kst']}",
            "",
            "## 목표",
            f"- {memory['goal']}",
            "",
            "## 현재 상태",
            f"- 저장된 published 수: `{memory['uploaded_published_count']}`",
            f"- 최신 업로드 처리 건수(processed_count): `{memory['latest_upload_processed_count']}`",
            f"- 마지막 동기화 시각: `{memory['latest_synced_at']}`",
            f"- 최근 소스 후보 수: `{memory['last_inventory_count']}`",
            f"- 핵심 체크 통과 여부: `{memory['all_core_checks_passed']}`",
            f"- 승인 상태 안전성: `{memory['review_status_safe']}`",
            f"- 승인 키워드: `{', '.join(memory.get('approved_keywords', [])) if memory.get('approved_keywords') else '없음'}`",
            "",
            "## 다음 우선순위",
        ]
        + [f"- {item}" for item in actions]
        + [
            "",
            "## 확인용 명령",
            "- `python3 scripts/emit_context_checkpoint.py`",
            "- `python3 scripts/run_pipeline.sh`",
            "- `python3 scripts/prepare_launch_bundle.py`",
            "",
            f"- 최근 노트: `{memory['note']}`",
        ]
    ) + "\n"


def _append_memo_log(memory: dict[str, Any]) -> None:
    line = json.dumps(memory, ensure_ascii=False)
    with MEMO_JSON.open("a", encoding="utf-8") as f:
        f.write(line + "\n")

    header = f"- [{memory['generated_at_kst']}] {memory['note']}"
    bullet = (
        f" - published={memory['uploaded_published_count']} / processed={memory['latest_upload_processed_count']} / "
        f"inventory={memory['last_inventory_count']} / all_core_checks_passed={memory['all_core_checks_passed']}"
    )
    if not MEMO_LOG.exists():
        MEMO_LOG.write_text(
            "# Session Memory Log\n\n- auto-run memory entries\n",
            encoding="utf-8",
        )
    with MEMO_LOG.open("a", encoding="utf-8") as f:
        f.write(header + "\n")
        f.write(bullet + "\n")

    _dedupe_memo_lines()
    _prune_memo_log(max_entries=80)
    _prune_memo_jsonl(max_entries=80)


def _dedupe_memo_lines() -> None:
    if not MEMO_LOG.exists():
        return

    lines = MEMO_LOG.read_text(encoding="utf-8").splitlines()
    if len(lines) <= 3:
        return

    deduped: list[str] = [lines[0], lines[1]]
    i = 2
    while i < len(lines):
        line = lines[i]
        if line.startswith("# ... truncated - recent entries kept") and (len(deduped) > 2 and deduped[-1] == line):
            i += 1
            continue
        if line.startswith("- [") and i + 1 < len(lines):
            bullet = lines[i + 1]
            if (
                len(deduped) >= 2
                and deduped[-2] == line
                and deduped[-1] == bullet
            ):
                i += 2
                continue
            deduped.append(line)
            if bullet.startswith(" - "):
                deduped.append(bullet)
                i += 2
            else:
                i += 1
            continue
        if line == deduped[-1]:
            i += 1
            continue
        deduped.append(line)
        i += 1

    # remove accidental duplicated truncated banner at top
    filtered: list[str] = []
    for item in deduped:
        if item.startswith("# ... truncated - recent entries kept") and filtered and filtered[-1].startswith("# ... truncated - recent entries kept"):
            continue
        filtered.append(item)
    deduped = filtered

    MEMO_LOG.write_text("\n".join(deduped) + "\n", encoding="utf-8")


def _prune_memo_jsonl(max_entries: int) -> None:
    if max_entries <= 0 or not MEMO_JSON.exists():
        return

    raw_lines = [line for line in MEMO_JSON.read_text(encoding="utf-8").splitlines() if line.strip()]
    lines: list[str] = []
    for item in raw_lines:
        if lines and item == lines[-1]:
            continue
        lines.append(item)
    if len(lines) <= max_entries:
        return

    lines = lines[-max_entries:]
    MEMO_JSON.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _prune_memo_log(max_entries: int) -> None:
    if max_entries <= 0 or not MEMO_LOG.exists():
        return

    lines = MEMO_LOG.read_text(encoding="utf-8").splitlines()
    if len(lines) <= max_entries + 2:
        return

    # Preserve header and keep only the most recent entries.
    header = lines[:2]
    entries = lines[2:]
    entries = entries[-(max_entries * 2):]
    if entries:
        entries.insert(0, "# ... truncated - recent entries kept")
    MEMO_LOG.write_text("\n".join(header + entries) + "\n", encoding="utf-8")


def write_all(memory: dict[str, Any]) -> None:
    SUMMARY_PATH.write_text(_render_summary_md(memory), encoding="utf-8")
    _append_memo_log(memory)
    CONTEXT_MD.touch(exist_ok=True)
    CONTEXT_JSON.touch(exist_ok=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--note", default="manual", help="Short note to describe this checkpoint")
    args = parser.parse_args()

    memory = _build_memory(note=args.note)
    write_all(memory)

    print(f"Session memory persisted: {SUMMARY_PATH}")
    print(f"Session memory log: {MEMO_LOG}")


if __name__ == "__main__":
    main()
