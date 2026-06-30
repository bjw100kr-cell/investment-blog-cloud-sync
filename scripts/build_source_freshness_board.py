#!/usr/bin/env python3
import html
import json
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Optional


ROOT = Path(__file__).resolve().parents[1]
APPROVAL_EVIDENCE_JSON = ROOT / "outputs/latest/approval-evidence-sheet.json"
USER_REVIEW_SHORTLIST_JSON = ROOT / "outputs/latest/user-review-shortlist.json"
SOURCE_SNAPSHOT_JSON = ROOT / "outputs/latest/source-snapshot.json"
PUBLISH_INVENTORY_JSON = ROOT / "outputs/latest/publish-inventory.json"
REVIEW_PACKET_JSON = ROOT / "outputs/latest/review-packet.json"
SAFE_IMAGE_SUGGESTIONS_JSON = ROOT / "outputs/latest/safe-image-suggestions.json"
OUTPUT_JSON = ROOT / "outputs/latest/source-freshness-board.json"
OUTPUT_MD = ROOT / "outputs/latest/source-freshness-board.md"
OUTPUT_HTML = ROOT / "outputs/latest/source-freshness-board.html"
APPROVAL_HELPER = ROOT / "scripts/set_review_approvals.py"
IMAGE_HELPER = ROOT / "scripts/set_image_selection.py"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def parse_dt(value: str) -> Optional[datetime]:
    if not value:
        return None
    try:
        parsed = parsedate_to_datetime(value)
        if parsed.tzinfo is None:
            return parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc)
    except (TypeError, ValueError, IndexError):
        pass

    candidate = value.strip().replace("Z", "+00:00")
    try:
        parsed = datetime.fromisoformat(candidate)
        if parsed.tzinfo is None:
            return parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc)
    except ValueError:
        return None


def age_days(reference: datetime, target: Optional[datetime]) -> Optional[float]:
    if target is None:
        return None
    seconds = max((reference - target).total_seconds(), 0.0)
    return round(seconds / 86400, 1)


def freshness_status(days: Optional[float]) -> str:
    if days is None:
        return "unknown"
    if days <= 2:
        return "fresh"
    if days <= 5:
        return "aging"
    return "stale"


def recommendation_for(status: str, quality_status: str, ready_now: bool) -> str:
    if status == "fresh" and ready_now and quality_status == "pass":
        return "사용자 검토만 통과하면 바로 게시 후보로 유지해도 됩니다."
    if status == "fresh":
        return "신선도는 괜찮습니다. 이미지나 품질 게이트만 보완하면 됩니다."
    if status == "aging":
        return "초안은 유지하되 발행 직전에 가격, 수치, headline을 한 번 더 갱신하는 편이 안전합니다."
    if status == "stale":
        return "지금 상태로는 데일리 뉴스형 게시보다 refresh 후 재작성 또는 evergreen 해설형 전환이 더 안전합니다."
    return "최근 근거 시각을 다시 수집해 신선도를 먼저 확인하세요."


def summary_line(status: str, newest_title: str) -> str:
    if status == "fresh":
        return f"최신 근거가 살아 있어 데일리 해설로 다루기 좋은 상태입니다. 대표 근거: {newest_title}"
    if status == "aging":
        return f"아직 쓸 수는 있지만 뉴스 속도는 조금 늦었습니다. 대표 근거: {newest_title}"
    if status == "stale":
        return f"핵심 근거가 이미 오래돼 그대로 올리기에는 위험합니다. 마지막 대표 근거: {newest_title}"
    return "대표 근거 시각을 읽지 못해 판단이 보류되었습니다."


def build_lookup(items: list[dict], key: str) -> dict[str, dict]:
    return {item.get(key, ""): item for item in items if item.get(key)}


def build_image_lookup() -> dict[str, dict]:
    payload = load_json(SAFE_IMAGE_SUGGESTIONS_JSON)
    lookup: dict[str, dict] = {}
    for item in payload.get("items", []):
        keyword = item.get("keyword", "")
        if not keyword:
            continue
        hero = next((image for image in item.get("image_plan", []) if image.get("slot") == "hero"), {})
        if hero:
            lookup[keyword] = {
                "search_query": hero.get("search_query", ""),
                "search_url": hero.get("search_url", ""),
                "provider_name": hero.get("provider_name", ""),
                "license_label": hero.get("license_label", ""),
                "license_url": hero.get("license_url", ""),
                "apply_helper": f'python3 {IMAGE_HELPER} --keyword {keyword} --slot hero --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve',
            }
    return lookup


def choose_recovery_candidate(keyword: str, inventory_items: list[dict], review_lookup: dict[str, dict]) -> dict:
    candidates = []
    for item in inventory_items:
        if item.get("source_keyword") != keyword:
            continue
        if item.get("inventory_type") != "seo_followup":
            continue
        review_item = review_lookup.get(item.get("keyword", ""), {})
        candidates.append(
            {
                "keyword": item.get("keyword", ""),
                "title": item.get("title", ""),
                "role": item.get("role", ""),
                "priority_score": float(review_item.get("priority_score", 0)),
                "review_verdict": review_item.get("review_verdict", ""),
            }
        )
    if not candidates:
        return {}
    candidates.sort(
        key=lambda item: (
            0 if item.get("role") == "evergreen_seo" else 1,
            0 if item.get("review_verdict") == "approve" else 1,
            -item.get("priority_score", 0),
        )
    )
    return candidates[0]


def recovery_plan_for(
    keyword: str,
    status: str,
    inventory_items: list[dict],
    review_lookup: dict[str, dict],
    image_lookup: dict[str, dict],
) -> dict:
    if status == "fresh":
        return {
            "recovery_mode": "publish_direct",
            "recovery_summary": "현재 신선도가 살아 있어 데일리 해설형으로 바로 검토를 이어가도 됩니다.",
        }
    if status == "aging":
        return {
            "recovery_mode": "refresh_before_publish",
            "recovery_summary": "발행 직전 전체 파이프라인을 다시 돌려 headline과 숫자를 최신 상태로 갱신하는 편이 안전합니다.",
            "recovery_command": "bash scripts/run_pipeline.sh",
        }
    if status == "stale":
        candidate = choose_recovery_candidate(keyword, inventory_items, review_lookup)
        if candidate:
            image = image_lookup.get(candidate.get("keyword", ""), {})
            return {
                "recovery_mode": "evergreen_salvage",
                "recovery_summary": "뉴스형 본문 대신 evergreen 후속 글로 전환하는 편이 더 안전하고 검색형 수익화에도 유리합니다.",
                "recovery_keyword": candidate.get("keyword", ""),
                "recovery_title": candidate.get("title", ""),
                "recovery_confirm_command": f"python3 {APPROVAL_HELPER} --keywords {candidate.get('keyword', '')}",
                "recovery_image_apply_helper": image.get("apply_helper", ""),
                "recovery_image_search_url": image.get("search_url", ""),
                "recovery_image_search_query": image.get("search_query", ""),
            }
        return {
            "recovery_mode": "full_refresh_needed",
            "recovery_summary": "현재 fresh 근거가 없어서 먼저 전체 파이프라인을 다시 돌려 새 소스가 들어오는지 확인해야 합니다.",
            "recovery_command": "bash scripts/run_pipeline.sh",
        }
    return {
        "recovery_mode": "manual_check",
        "recovery_summary": "최근 근거 시각을 먼저 다시 확인한 뒤 다음 액션을 결정하세요.",
    }


def build_report() -> dict:
    approval = load_json(APPROVAL_EVIDENCE_JSON)
    shortlist = load_json(USER_REVIEW_SHORTLIST_JSON)
    snapshot = load_json(SOURCE_SNAPSHOT_JSON)
    inventory = load_json(PUBLISH_INVENTORY_JSON)
    review_packet = load_json(REVIEW_PACKET_JSON)
    image_lookup = build_image_lookup()
    review_lookup = build_lookup(review_packet.get("items", []), "keyword")

    now = datetime.now(timezone.utc)
    shortlist_lookup = {item.get("keyword", ""): item for item in shortlist.get("shortlist", []) if item.get("keyword")}
    snapshot_dt = parse_dt(snapshot.get("generated_at", ""))
    snapshot_days = age_days(now, snapshot_dt)

    items = []
    counts = {"fresh": 0, "aging": 0, "stale": 0, "unknown": 0}
    for item in approval.get("items", []):
        keyword = item.get("keyword", "")
        shortlist_item = shortlist_lookup.get(keyword, {})
        evidence = item.get("recent_evidence", [])
        evidence_dts = [parse_dt(entry.get("published_iso") or entry.get("published", "")) for entry in evidence]
        evidence_dts = [entry for entry in evidence_dts if entry is not None]
        newest_dt = max(evidence_dts) if evidence_dts else None
        oldest_dt = min(evidence_dts) if evidence_dts else None
        newest_days = age_days(now, newest_dt)
        status = freshness_status(newest_days)
        counts[status] = counts.get(status, 0) + 1
        newest_title = evidence[0].get("title", "") if evidence else ""
        recovery = recovery_plan_for(keyword, status, inventory.get("items", []), review_lookup, image_lookup)

        items.append(
            {
                "keyword": keyword,
                "title": item.get("title", ""),
                "quality_status": item.get("quality_status", ""),
                "ready_now": item.get("ready_now", False),
                "publish_date": item.get("publish_date", ""),
                "freshness_status": status,
                "newest_evidence_iso": newest_dt.isoformat() if newest_dt else "",
                "oldest_evidence_iso": oldest_dt.isoformat() if oldest_dt else "",
                "newest_evidence_age_days": newest_days,
                "source_count": item.get("source_count", 0),
                "demand_signal_score": item.get("demand_signal_score", 0),
                "summary_line": summary_line(status, newest_title),
                "recommendation": recommendation_for(
                    status,
                    item.get("quality_status", ""),
                    bool(shortlist_item.get("ready_now", item.get("ready_now", False))),
                ),
                **recovery,
                "recent_evidence": evidence[:3],
            }
        )

    items.sort(
        key=lambda entry: (
            {"stale": 0, "aging": 1, "unknown": 2, "fresh": 3}.get(entry.get("freshness_status", "unknown"), 2),
            -(entry.get("newest_evidence_age_days") or -999),
        )
    )

    return {
        "generated_at": now.isoformat(),
        "snapshot_generated_at": snapshot.get("generated_at", ""),
        "snapshot_age_days": snapshot_days,
        "snapshot_status": freshness_status(snapshot_days),
        "item_count": len(items),
        "counts": counts,
        "items": items,
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# Source Freshness Board")
    lines.append("")
    lines.append("사용자에게 초안을 보여주기 전에, 근거 소스가 지금 시점에도 충분히 신선한지 확인하는 보드입니다.")
    lines.append(f"- generated_at: `{report.get('generated_at', '')}`")
    lines.append(f"- snapshot_generated_at: `{report.get('snapshot_generated_at', '')}`")
    lines.append(f"- snapshot_age_days: `{report.get('snapshot_age_days', '')}`")
    lines.append(f"- snapshot_status: `{report.get('snapshot_status', '')}`")
    lines.append(
        f"- counts: fresh `{report.get('counts', {}).get('fresh', 0)}` / aging `{report.get('counts', {}).get('aging', 0)}` / stale `{report.get('counts', {}).get('stale', 0)}` / unknown `{report.get('counts', {}).get('unknown', 0)}`"
    )
    lines.append("")
    for index, item in enumerate(report.get("items", []), start=1):
        lines.append(f"## {index}. {item.get('title', '')}")
        lines.append("")
        lines.append(f"- keyword: `{item.get('keyword', '')}`")
        lines.append(f"- freshness_status: `{item.get('freshness_status', '')}`")
        lines.append(f"- newest_evidence_age_days: `{item.get('newest_evidence_age_days', '')}`")
        lines.append(f"- newest_evidence_iso: `{item.get('newest_evidence_iso', '')}`")
        lines.append(f"- quality_status: `{item.get('quality_status', '')}` / ready_now `{item.get('ready_now', False)}`")
        lines.append(f"- summary: {item.get('summary_line', '')}")
        lines.append(f"- recommendation: {item.get('recommendation', '')}")
        if item.get("recovery_mode"):
            lines.append(f"- recovery_mode: `{item.get('recovery_mode', '')}`")
        if item.get("recovery_summary"):
            lines.append(f"- recovery_summary: {item.get('recovery_summary', '')}")
        if item.get("recovery_title"):
            lines.append(f"- recovery_title: {item.get('recovery_title', '')}")
        if item.get("recovery_confirm_command"):
            lines.append(f"- recovery_confirm_command: `{item.get('recovery_confirm_command', '')}`")
        if item.get("recovery_command"):
            lines.append(f"- recovery_command: `{item.get('recovery_command', '')}`")
        if item.get("recovery_image_search_url"):
            lines.append(
                f"- recovery_image_search: `{item.get('recovery_image_search_query', '')}` / {item.get('recovery_image_search_url', '')}"
            )
        if item.get("recovery_image_apply_helper"):
            lines.append(f"- recovery_image_apply_helper: `{item.get('recovery_image_apply_helper', '')}`")
        for evidence in item.get("recent_evidence", []):
            lines.append(
                f"- evidence: {evidence.get('source_name', '')} / {evidence.get('published_iso', '') or evidence.get('published', '')} / {evidence.get('title', '')}"
            )
        lines.append("")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def write_html(report: dict) -> None:
    cards = []
    for item in report.get("items", []):
        tone = item.get("freshness_status", "unknown")
        cards.append(
            f"""
            <article class="card {html.escape(tone)}">
              <div class="top">
                <span class="badge">{html.escape(item.get('keyword', ''))}</span>
                <span class="badge alt">{html.escape(tone)}</span>
              </div>
              <h2>{html.escape(item.get('title', ''))}</h2>
              <p class="meta">newest evidence age {html.escape(str(item.get('newest_evidence_age_days', '')))} days · quality {html.escape(item.get('quality_status', ''))}</p>
              <p>{html.escape(item.get('summary_line', ''))}</p>
              <p><strong>권장 액션</strong> {html.escape(item.get('recommendation', ''))}</p>
              <ul>
                {''.join(f"<li><strong>{html.escape(e.get('source_name', ''))}</strong> · {html.escape(e.get('published_iso', '') or e.get('published', ''))}<br>{html.escape(e.get('title', ''))}</li>" for e in item.get('recent_evidence', [])) or '<li>최근 근거 없음</li>'}
              </ul>
            </article>
            """
        )

    html_text = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Source Freshness Board</title>
  <style>
    :root {{
      --bg: #f4efe6;
      --panel: rgba(255, 251, 244, 0.95);
      --ink: #1b1a16;
      --muted: #615f57;
      --line: #ddd3c4;
      --fresh: #24594f;
      --fresh-soft: #dff2ee;
      --aging: #8b5e18;
      --aging-soft: #f6ead0;
      --stale: #8f352d;
      --stale-soft: #f6e0d8;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: "Avenir Next", "Pretendard", "Apple SD Gothic Neo", sans-serif;
      color: var(--ink);
      background: linear-gradient(180deg, #fbf8f2 0%, var(--bg) 100%);
    }}
    main {{ max-width: 1080px; margin: 0 auto; padding: 28px 18px 60px; }}
    .hero, .card {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 24px;
      padding: 22px;
      box-shadow: 0 18px 40px rgba(36, 28, 18, 0.06);
    }}
    .hero {{ margin-bottom: 18px; }}
    .grid {{ display: grid; gap: 16px; }}
    h1 {{ margin: 0 0 12px; font-size: clamp(2rem, 4vw, 3.1rem); line-height: 0.96; letter-spacing: -0.04em; }}
    h2 {{ margin: 10px 0; font-size: 1.35rem; }}
    .top {{ display: flex; gap: 8px; flex-wrap: wrap; }}
    .badge {{
      display: inline-flex;
      padding: 7px 11px;
      border-radius: 999px;
      background: #f3ede3;
      font-size: 0.9rem;
      font-weight: 700;
    }}
    .alt {{ background: #ece4d6; }}
    .meta, .muted {{ color: var(--muted); }}
    .fresh .alt {{ background: var(--fresh-soft); color: var(--fresh); }}
    .aging .alt {{ background: var(--aging-soft); color: var(--aging); }}
    .stale .alt {{ background: var(--stale-soft); color: var(--stale); }}
    ul {{ padding-left: 20px; }}
  </style>
</head>
<body>
  <main>
    <section class="hero">
      <h1>Source Freshness Board</h1>
      <p>사용자에게 초안을 보여주기 전, 근거 뉴스가 지금 시점에도 충분히 살아 있는지 먼저 확인합니다.</p>
      <p class="muted">snapshot generated {html.escape(str(report.get('snapshot_generated_at', '')))} · snapshot age {html.escape(str(report.get('snapshot_age_days', '')))} days · status {html.escape(report.get('snapshot_status', ''))}</p>
      <p class="muted">fresh {html.escape(str(report.get('counts', {}).get('fresh', 0)))} / aging {html.escape(str(report.get('counts', {}).get('aging', 0)))} / stale {html.escape(str(report.get('counts', {}).get('stale', 0)))} / unknown {html.escape(str(report.get('counts', {}).get('unknown', 0)))}</p>
    </section>
    <section class="grid">
      {''.join(cards)}
    </section>
  </main>
</body>
</html>
"""
    OUTPUT_HTML.write_text(html_text)


def main() -> int:
    report = build_report()
    OUTPUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    write_markdown(report)
    write_html(report)
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
