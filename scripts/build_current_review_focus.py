#!/usr/bin/env python3
import html
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SHORTLIST_JSON = ROOT / "outputs/latest/user-review-shortlist.json"
ACTION_BOARD_JSON = ROOT / "outputs/latest/shortlist-publish-action-board.json"
EVIDENCE_JSON = ROOT / "outputs/latest/approval-evidence-sheet.json"
FULL_DRAFT_JSON = ROOT / "outputs/latest/full-draft-review-sheet.json"
FRESHNESS_JSON = ROOT / "outputs/latest/source-freshness-board.json"
FIRST_APPROVAL_PATH = ROOT / "outputs/latest/first-approval-path.json"
OUTPUT_JSON = ROOT / "outputs/latest/current-review-focus.json"
OUTPUT_MD = ROOT / "outputs/latest/current-review-focus.md"
OUTPUT_HTML = ROOT / "outputs/latest/current-review-focus.html"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def to_uri(path: Path) -> str:
    if not path.exists():
        return ""
    return path.resolve().as_uri()


def item_lookup(items: list[dict]) -> dict[str, dict]:
    return {item.get("keyword", ""): item for item in items if item.get("keyword")}


def build_excerpt(full_draft_text: str) -> list[str]:
    excerpt: list[str] = []
    for line in full_draft_text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        excerpt.append(stripped)
        if len(excerpt) == 4:
            break
    return excerpt


def build_report() -> dict:
    shortlist = load_json(SHORTLIST_JSON)
    action_board = load_json(ACTION_BOARD_JSON)
    evidence_sheet = load_json(EVIDENCE_JSON)
    full_draft_sheet = load_json(FULL_DRAFT_JSON)
    first_approval = load_json(FIRST_APPROVAL_PATH)

    action_lookup = item_lookup(action_board.get("items", []))
    evidence_lookup = item_lookup(evidence_sheet.get("items", []))
    draft_lookup = item_lookup(full_draft_sheet.get("items", []))
    freshness_lookup = item_lookup(load_json(FRESHNESS_JSON).get("items", []))
    recommended_keyword = (first_approval.get("recommended_single") or {}).get("keyword", "")

    shortlist_items = shortlist.get("shortlist", [])
    if recommended_keyword:
        shortlist_items = sorted(
            shortlist_items,
            key=lambda item: 0 if item.get("keyword") == recommended_keyword else 1,
        )

    focus_items = []
    for order, item in enumerate(shortlist_items[:2], start=1):
        keyword = item.get("keyword", "")
        action = action_lookup.get(keyword, {})
        evidence = evidence_lookup.get(keyword, {})
        draft = draft_lookup.get(keyword, {})
        freshness = freshness_lookup.get(keyword, {})
        focus_items.append(
            {
                "display_order": order,
                "keyword": keyword,
                "title": item.get("title", ""),
                "publish_date": item.get("publish_date", ""),
                "priority_score": item.get("priority_score", 0),
                "review_verdict": item.get("review_verdict", ""),
                "quality_status": item.get("quality_status", ""),
                "hero_image_selected": item.get("hero_image_selected", False),
                "ready_now": item.get("ready_now", False),
                "cta_focus": item.get("cta_focus", ""),
                "intent": item.get("intent", ""),
                "preview": item.get("preview", [])[:2],
                "draft_path": draft.get("draft_path", ""),
                "html_path": draft.get("html_path", ""),
                "excerpt": build_excerpt(draft.get("full_draft_text", "")),
                "retention_cta_enabled": draft.get("retention_cta_enabled", False),
                "retention_cta": draft.get("retention_cta", {}),
                "freshness_status": freshness.get("freshness_status", ""),
                "newest_evidence_age_days": freshness.get("newest_evidence_age_days", ""),
                "freshness_summary": freshness.get("summary_line", ""),
                "freshness_recommendation": freshness.get("recommendation", ""),
                "recent_evidence": evidence.get("recent_evidence", [])[:3],
                "source_names": evidence.get("source_names", [])[:3],
                "demand_signal_score": evidence.get("demand_signal_score", 0),
                "fallback_source": evidence.get("fallback_source", ""),
                "confirm_command": action.get("confirm_command", ""),
                "next_action": action.get("next_action", ""),
                "next_command": action.get("next_command", ""),
                "helper_preview_command": action.get("helper_preview_command", ""),
                "helper_apply_command": action.get("helper_apply_command", ""),
                "recovery_mode": action.get("recovery_mode", ""),
                "recovery_title": action.get("recovery_title", ""),
                "recovery_confirm_command": action.get("recovery_confirm_command", ""),
                "recovery_image_search_url": action.get("recovery_image_search_url", ""),
                "recovery_image_search_query": action.get("recovery_image_search_query", ""),
                "recovery_image_apply_helper": action.get("recovery_image_apply_helper", ""),
                "hard_blocking_checks": action.get("hard_blocking_checks", []),
                "advisory_checks": action.get("advisory_checks", []),
                "hero_image_search_url": item.get("hero_image_search_url", ""),
                "hero_image_search_query": item.get("hero_image_search_query", ""),
                "hero_image_apply_helper": item.get("hero_image_apply_helper", ""),
            }
        )

    top_focus = focus_items[0] if focus_items else {}
    return {
        "focus_count": len(focus_items),
        "guardrail": "제가 먼저 이 화면으로 초안을 보여드리고, 사용자 최종 확인 전에는 실제 업로드가 계속 차단됩니다.",
        "recommended_first_keyword": top_focus.get("keyword", ""),
        "recommended_first_title": top_focus.get("title", ""),
        "focus_items": focus_items,
        "related_paths": {
            "review_shortlist_md": str(ROOT / "outputs/latest/user-review-shortlist.md"),
            "full_draft_review_sheet_md": str(ROOT / "outputs/latest/full-draft-review-sheet.md"),
            "approval_briefing_board_html": str(ROOT / "outputs/latest/approval-briefing-board.html"),
            "shortlist_launchpad_html": str(ROOT / "outputs/latest/shortlist-launchpad.html"),
            "source_freshness_board_html": str(ROOT / "outputs/latest/source-freshness-board.html"),
        },
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# Current Review Focus")
    lines.append("")
    lines.append("지금 사용자에게 먼저 보여줄 글만 다시 줄인 검토 카드입니다.")
    lines.append(f"- 발행 안전 원칙: {report.get('guardrail', '')}")
    if report.get("recommended_first_title"):
        lines.append(
            f"- 지금 1순위로 읽을 글: `{report.get('recommended_first_title', '')}` / keyword `{report.get('recommended_first_keyword', '')}`"
        )
    lines.append(f"- shortlist: `{report.get('related_paths', {}).get('review_shortlist_md', '')}`")
    lines.append(f"- full draft review sheet: `{report.get('related_paths', {}).get('full_draft_review_sheet_md', '')}`")
    lines.append(f"- approval briefing board: `{report.get('related_paths', {}).get('approval_briefing_board_html', '')}`")
    lines.append(f"- shortlist launchpad: `{report.get('related_paths', {}).get('shortlist_launchpad_html', '')}`")
    lines.append(f"- source freshness board: `{report.get('related_paths', {}).get('source_freshness_board_html', '')}`")
    lines.append("")
    for item in report.get("focus_items", []):
        lines.append(f"## {item.get('display_order', 0)}. {item.get('title', '')}")
        lines.append("")
        lines.append(f"- keyword: `{item.get('keyword', '')}`")
        lines.append(f"- ready_now: `{item.get('ready_now', False)}`")
        lines.append(f"- quality_status: `{item.get('quality_status', '')}`")
        lines.append(f"- hero_image_selected: `{item.get('hero_image_selected', False)}`")
        lines.append(f"- intent: {item.get('intent', '')}")
        lines.append(f"- CTA focus: {item.get('cta_focus', '')}")
        if item.get("retention_cta_enabled"):
            retention_cta = item.get("retention_cta", {})
            lines.append(f"- final retention CTA: {retention_cta.get('inline_cta_now', '')}")
            if retention_cta.get("telegram_cta_later"):
                lines.append(f"- later revisit CTA: {retention_cta.get('telegram_cta_later', '')}")
        lines.append(f"- demand_signal_score: `{item.get('demand_signal_score', 0)}`")
        if item.get("freshness_status"):
            lines.append(
                f"- freshness: `{item.get('freshness_status', '')}` / newest evidence age `{item.get('newest_evidence_age_days', '')}` days"
            )
        if item.get("freshness_summary"):
            lines.append(f"- freshness_summary: {item.get('freshness_summary', '')}")
        if item.get("freshness_recommendation"):
            lines.append(f"- freshness_recommendation: {item.get('freshness_recommendation', '')}")
        if item.get("source_names"):
            lines.append(f"- sources: {', '.join(item.get('source_names', []))}")
        if item.get("hard_blocking_checks"):
            lines.append(f"- hard_blocking_checks: {', '.join(item.get('hard_blocking_checks', []))}")
        if item.get("advisory_checks"):
            lines.append(f"- advisory_checks: {', '.join(item.get('advisory_checks', []))}")
        if item.get("next_action"):
            lines.append(f"- next_action: {item.get('next_action', '')}")
        if item.get("confirm_command"):
            lines.append(f"- confirm_command: `{item.get('confirm_command', '')}`")
        if item.get("helper_preview_command"):
            lines.append(f"- helper_preview_command: `{item.get('helper_preview_command', '')}`")
        if item.get("helper_apply_command"):
            lines.append(f"- helper_apply_command: `{item.get('helper_apply_command', '')}`")
        for paragraph in item.get("excerpt", []):
            lines.append(f"- excerpt: {paragraph}")
        for preview in item.get("preview", []):
            lines.append(f"- preview: {preview}")
        for evidence in item.get("recent_evidence", []):
            lines.append(
                f"- evidence: {evidence.get('source_name', '')} / {evidence.get('published_iso', '')} / {evidence.get('title', '')}"
            )
        if item.get("hero_image_search_url"):
            lines.append(
                f"- hero_image_search: `{item.get('hero_image_search_query', '')}` / {item.get('hero_image_search_url', '')}"
            )
        if item.get("hero_image_apply_helper"):
            lines.append(f"- hero_image_apply_helper: `{item.get('hero_image_apply_helper', '')}`")
        if item.get("draft_path"):
            lines.append(f"- draft_path: `{item.get('draft_path', '')}`")
        if item.get("html_path"):
            lines.append(f"- html_path: `{item.get('html_path', '')}`")
        lines.append("")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def render_evidence_list(evidence_items: list[dict]) -> str:
    if not evidence_items:
        return "<li>최근 근거가 아직 정리되지 않았습니다.</li>"
    return "".join(
        f"<li><strong>{html.escape(item.get('source_name', ''))}</strong> · {html.escape(item.get('published_iso', ''))}<br>{html.escape(item.get('title', ''))}</li>"
        for item in evidence_items
    )


def render_paragraphs(items: list[str], fallback: str) -> str:
    if not items:
        return f"<p class='muted'>{html.escape(fallback)}</p>"
    return "".join(f"<p>{html.escape(item)}</p>" for item in items)


def write_html(report: dict) -> None:
    cards = []
    for item in report.get("focus_items", []):
        blockers = item.get("hard_blocking_checks", [])
        advisory = item.get("advisory_checks", [])
        readiness = "ready now" if item.get("ready_now") else "needs final prep"
        cards.append(
            f"""
            <article class="card">
              <div class="top">
                <span class="badge">{html.escape(item.get('keyword', ''))}</span>
                <span class="badge alt">{html.escape(readiness)}</span>
              </div>
              <h2>{html.escape(item.get('display_order', 0).__str__())}. {html.escape(item.get('title', ''))}</h2>
              <p class="meta">quality `{html.escape(item.get('quality_status', ''))}` · hero `{html.escape(str(item.get('hero_image_selected', False)))}` · demand `{html.escape(str(item.get('demand_signal_score', 0)))}`</p>
              <p class="lead">{html.escape(item.get('intent', ''))}</p>
              {f"<div class='callout'><strong>신선도</strong><p>{html.escape(item.get('freshness_status', ''))} · newest evidence age {html.escape(str(item.get('newest_evidence_age_days', '')))} days</p><p>{html.escape(item.get('freshness_recommendation', ''))}</p></div>" if item.get('freshness_status') else ""}
              {f"<div class='callout alt'><strong>최종 CTA</strong><p>{html.escape((item.get('retention_cta') or {}).get('inline_cta_now', ''))}</p></div>" if item.get('retention_cta_enabled') and (item.get('retention_cta') or {}).get('inline_cta_now') else ""}
              <div class="callout">
                <strong>다음 액션</strong>
                <p>{html.escape(item.get('next_action', ''))}</p>
              </div>
              <div class="commands">
                {f"<code>{html.escape(item.get('confirm_command', ''))}</code>" if item.get('confirm_command') else ""}
                {f"<code>{html.escape(item.get('helper_preview_command', ''))}</code>" if item.get('helper_preview_command') else ""}
              </div>
              <h3>초안 핵심 문단</h3>
              {render_paragraphs(item.get("excerpt", []), "초안 발췌가 아직 없습니다.")}
              <h3>미리보기 포인트</h3>
              {render_paragraphs(item.get("preview", []), "미리보기 포인트가 아직 없습니다.")}
              <h3>최근 근거</h3>
              <ul>{render_evidence_list(item.get("recent_evidence", []))}</ul>
              <h3>체크 상태</h3>
              <p><strong>Hard blockers:</strong> {html.escape(', '.join(blockers) if blockers else 'none')}</p>
              <p><strong>Advisory:</strong> {html.escape(', '.join(advisory) if advisory else 'none')}</p>
              {f"<p><strong>이미지 검색:</strong> <a href='{html.escape(item.get('hero_image_search_url', ''))}' target='_blank' rel='noreferrer'>{html.escape(item.get('hero_image_search_query', ''))}</a></p>" if item.get('hero_image_search_url') else ""}
              {f"<code>{html.escape(item.get('hero_image_apply_helper', ''))}</code>" if item.get('hero_image_apply_helper') else ""}
              <p class="paths">draft: {html.escape(item.get('draft_path', ''))}</p>
              <p class="paths">html: {html.escape(item.get('html_path', ''))}</p>
            </article>
            """
        )

    html_text = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Current Review Focus</title>
  <style>
    :root {{
      --bg: #f4efe6;
      --panel: rgba(255, 251, 244, 0.94);
      --ink: #1b1a16;
      --muted: #615f57;
      --line: #ddd3c4;
      --accent: #8f352d;
      --accent-soft: #f6e0d8;
      --accent-alt: #285c58;
      --accent-alt-soft: #dff2ee;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: "Avenir Next", "Pretendard", "Apple SD Gothic Neo", sans-serif;
      color: var(--ink);
      background:
        radial-gradient(circle at top left, rgba(143, 53, 45, 0.08), transparent 26%),
        radial-gradient(circle at bottom right, rgba(40, 92, 88, 0.08), transparent 24%),
        linear-gradient(180deg, #faf7f1 0%, var(--bg) 100%);
    }}
    main {{
      max-width: 1240px;
      margin: 0 auto;
      padding: 28px 18px 56px;
    }}
    .hero, .card {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 24px;
      box-shadow: 0 18px 40px rgba(32, 24, 12, 0.07);
    }}
    .hero {{
      padding: 24px;
      margin-bottom: 18px;
    }}
    h1 {{
      margin: 0 0 10px;
      font-size: clamp(2rem, 4vw, 3.5rem);
      letter-spacing: -0.05em;
      line-height: 0.95;
    }}
    p {{
      line-height: 1.62;
    }}
    .muted, .meta, .paths {{
      color: var(--muted);
    }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 18px;
    }}
    .card {{
      padding: 20px;
    }}
    .top {{
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }}
    .badge {{
      display: inline-flex;
      align-items: center;
      padding: 5px 10px;
      border-radius: 999px;
      font-size: 0.76rem;
      font-weight: 700;
      background: var(--accent-soft);
      color: var(--accent);
    }}
    .badge.alt {{
      background: var(--accent-alt-soft);
      color: var(--accent-alt);
    }}
    .callout {{
      margin: 14px 0;
      padding: 14px;
      border-radius: 16px;
      background: #fcf8f2;
      border: 1px solid var(--line);
    }}
    h2 {{
      margin: 12px 0 8px;
      font-size: 1.35rem;
      line-height: 1.15;
    }}
    h3 {{
      margin: 18px 0 10px;
      font-size: 0.98rem;
    }}
    ul {{
      margin: 0;
      padding-left: 18px;
    }}
    code {{
      display: block;
      margin-top: 10px;
      padding: 12px 14px;
      border-radius: 14px;
      background: #171915;
      color: #f8f3ea;
      overflow-wrap: anywhere;
      font-family: "SFMono-Regular", Consolas, monospace;
    }}
    a {{
      color: var(--accent-alt);
    }}
    @media (max-width: 960px) {{
      .grid {{
        grid-template-columns: 1fr;
      }}
    }}
  </style>
</head>
<body>
  <main>
    <section class="hero">
      <h1>Current Review Focus</h1>
      <p class="muted">지금 사용자에게 먼저 보여줄 글만 1순위, 2순위로 줄여 둔 검토 시작 화면입니다.</p>
      <p><strong>발행 안전 원칙:</strong> {html.escape(report.get('guardrail', ''))}</p>
      <p><strong>지금 먼저 읽을 글:</strong> {html.escape(report.get('recommended_first_title', '없음'))}</p>
      <p class="paths">shortlist launchpad: {html.escape(to_uri(ROOT / 'outputs/latest/shortlist-launchpad.html'))}</p>
      <p class="paths">approval briefing board: {html.escape(to_uri(ROOT / 'outputs/latest/approval-briefing-board.html'))}</p>
    </section>
    <section class="grid">
      {''.join(cards) if cards else "<article class='card'><p>검토 카드가 아직 없습니다.</p></article>"}
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
    print(OUTPUT_HTML)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
