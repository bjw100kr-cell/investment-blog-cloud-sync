#!/usr/bin/env python3
import html
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FULL_DRAFT_REVIEW_SHEET_JSON = ROOT / "outputs/latest/full-draft-review-sheet.json"
APPROVAL_EVIDENCE_SHEET_JSON = ROOT / "outputs/latest/approval-evidence-sheet.json"
OUTPUT_JSON = ROOT / "outputs/latest/approval-briefing-board.json"
OUTPUT_MD = ROOT / "outputs/latest/approval-briefing-board.md"
OUTPUT_HTML = ROOT / "outputs/latest/approval-briefing-board.html"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def to_uri(path_text: str) -> str:
    if not path_text:
        return ""
    path = Path(path_text)
    if not path.exists():
        return ""
    return path.resolve().as_uri()


def build_lookup(items: list[dict], key: str) -> dict:
    return {item.get(key): item for item in items if item.get(key)}


def build_report() -> dict:
    drafts = load_json(FULL_DRAFT_REVIEW_SHEET_JSON)
    evidence = load_json(APPROVAL_EVIDENCE_SHEET_JSON)
    evidence_lookup = build_lookup(evidence.get("items", []), "keyword")

    cards = []
    for item in drafts.get("items", []):
        keyword = item.get("keyword", "")
        evidence_item = evidence_lookup.get(keyword, {})
        cards.append(
            {
                "keyword": keyword,
                "title": item.get("title", ""),
                "publish_date": item.get("publish_date", ""),
                "priority_score": item.get("priority_score", 0),
                "review_verdict": item.get("review_verdict", ""),
                "review_score": item.get("review_score", 0),
                "quality_status": item.get("quality_status", ""),
                "hero_image_selected": item.get("hero_image_selected", False),
                "ready_now": item.get("ready_now", False),
                "intent": item.get("intent", ""),
                "cta_focus": item.get("cta_focus", ""),
                "draft_path": item.get("draft_path", ""),
                "html_path": item.get("html_path", ""),
                "draft_uri": to_uri(item.get("draft_path", "")),
                "html_uri": to_uri(item.get("html_path", "")),
                "image_slots": item.get("image_slots", []),
                "review_warnings": item.get("review_warnings", []),
                "full_draft_text": item.get("full_draft_text", ""),
                "reason": evidence_item.get("reason", ""),
                "format": evidence_item.get("format", ""),
                "demand_signal_score": evidence_item.get("demand_signal_score", 0),
                "fallback_source": evidence_item.get("fallback_source", ""),
                "source_names": evidence_item.get("source_names", []),
                "sample_headlines": evidence_item.get("sample_headlines", []),
                "recent_evidence": evidence_item.get("recent_evidence", []),
            }
        )

    return {
        "item_count": len(cards),
        "single_approval_command": drafts.get("single_approval_command", ""),
        "batch_approval_command": drafts.get("batch_approval_command", ""),
        "cards": cards,
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# Approval Briefing Board")
    lines.append("")
    lines.append("사용자가 승인 직전에 글 전문, 근거, 이미지 상태, 승인 명령을 한 번에 보는 통합 보드입니다.")
    lines.append("- 원칙: 여기서 읽고 확인한 글만 사용자 최종 확인 대상으로 넘깁니다.")
    lines.append("- 상태: 사용자 최종 확인 전에는 실제 업로드가 차단됩니다.")
    lines.append(f"- item_count: `{report.get('item_count', 0)}`")
    if report.get("single_approval_command"):
        lines.append(f"- single confirmation: `{report.get('single_approval_command', '')}`")
    if report.get("batch_approval_command"):
        lines.append(f"- batch confirmation: `{report.get('batch_approval_command', '')}`")
    lines.append("")

    for index, card in enumerate(report.get("cards", []), start=1):
        lines.append(f"## {index}. {card.get('title', '')}")
        lines.append("")
        lines.append(
            f"- keyword `{card.get('keyword', '')}` / publish `{card.get('publish_date', '')}` / priority `{card.get('priority_score', 0)}`"
        )
        lines.append(
            f"- review `{card.get('review_verdict', '')}` score `{card.get('review_score', 0)}` / quality `{card.get('quality_status', '')}` / ready_now `{card.get('ready_now', False)}`"
        )
        lines.append(f"- intent: {card.get('intent', '')}")
        lines.append(f"- CTA focus: {card.get('cta_focus', '')}")
        lines.append(f"- reason: {card.get('reason', '')}")
        lines.append(
            f"- evidence score: demand `{card.get('demand_signal_score', 0)}` / fallback `{card.get('fallback_source', '')}` / format `{card.get('format', '')}`"
        )
        if card.get("source_names"):
            lines.append(f"- source_names: {', '.join(card.get('source_names', []))}")
        if card.get("sample_headlines"):
            lines.append("- sample_headlines:")
            for headline in card.get("sample_headlines", [])[:4]:
                lines.append(f"  - {headline}")
        if card.get("recent_evidence"):
            lines.append("- recent_evidence:")
            for evidence in card.get("recent_evidence", [])[:4]:
                published = evidence.get("published_iso") or evidence.get("published", "")
                lines.append(
                    f"  - {evidence.get('source_name', '')} | {published} | {evidence.get('title', '')}"
                )
        if card.get("image_slots"):
            lines.append("- image_slots:")
            for image in card.get("image_slots", []):
                lines.append(
                    f"  - {image.get('slot_label', image.get('slot', ''))} / {image.get('provider_name', '')} / `{image.get('search_query', '')}` / {image.get('license_label', '')}"
                )
        lines.append("")
        lines.append("### Draft Body")
        lines.append("")
        lines.append("```md")
        lines.append(card.get("full_draft_text", ""))
        lines.append("```")
        lines.append("")

    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def render_image_slots(image_slots: list[dict]) -> str:
    if not image_slots:
        return "<li>No image tasks</li>"
    items = []
    for image in image_slots:
        search = html.escape(image.get("search_query", ""))
        provider = html.escape(image.get("provider_name", ""))
        slot = html.escape(image.get("slot_label", image.get("slot", "")))
        items.append(f"<li><strong>{slot}</strong> {provider} / <code>{search}</code></li>")
    return "".join(items)


def render_recent_evidence(items: list[dict]) -> str:
    if not items:
        return "<li>No evidence rows</li>"
    rows = []
    for item in items[:4]:
        published = html.escape(item.get("published_iso") or item.get("published", ""))
        source = html.escape(item.get("source_name", ""))
        title = html.escape(item.get("title", ""))
        link = html.escape(item.get("link", ""))
        link_html = f"<a href='{link}' target='_blank' rel='noreferrer'>open</a>" if link else ""
        rows.append(f"<li><strong>{source}</strong> <span class='tiny'>{published}</span><br>{title} {link_html}</li>")
    return "".join(rows)


def render_sample_headlines(items: list[str]) -> str:
    if not items:
        return "<li>No sample headlines</li>"
    return "".join(f"<li>{html.escape(item)}</li>" for item in items[:4])


def render_card(card: dict) -> str:
    title = html.escape(card.get("title", ""))
    keyword = html.escape(card.get("keyword", ""))
    publish_date = html.escape(card.get("publish_date", ""))
    verdict = html.escape(card.get("review_verdict", ""))
    score = html.escape(str(card.get("review_score", 0)))
    quality = html.escape(card.get("quality_status", ""))
    ready = html.escape(str(card.get("ready_now", False)))
    priority = html.escape(str(card.get("priority_score", 0)))
    reason = html.escape(card.get("reason", ""))
    intent = html.escape(card.get("intent", ""))
    cta = html.escape(card.get("cta_focus", ""))
    demand = html.escape(str(card.get("demand_signal_score", 0)))
    fallback = html.escape(card.get("fallback_source", ""))
    draft_link = f"<a href='{html.escape(card.get('draft_uri', ''))}' target='_blank' rel='noreferrer'>Draft</a>" if card.get("draft_uri") else ""
    html_link = f"<a href='{html.escape(card.get('html_uri', ''))}' target='_blank' rel='noreferrer'>HTML</a>" if card.get("html_uri") else ""
    draft_body = html.escape(card.get("full_draft_text", ""))
    return f"""
    <section class="card">
      <div class="summary">
        <div class="pill-row">
          <span class="pill">{keyword}</span>
          <span class="pill alt">{verdict}</span>
          <span class="pill">score {score}</span>
          <span class="pill">priority {priority}</span>
        </div>
        <h2>{title}</h2>
        <p><strong>Publish</strong> {publish_date} / <strong>Quality</strong> {quality} / <strong>Ready</strong> {ready}</p>
        <p><strong>Intent</strong> {intent}</p>
        <p><strong>CTA</strong> {cta}</p>
        <p><strong>Why now</strong> {reason}</p>
        <p><strong>Evidence</strong> demand {demand} / fallback {fallback}</p>
        <p class="links">{draft_link} {html_link}</p>
        <div class="mini-block">
          <h3>Sample Headlines</h3>
          <ul>{render_sample_headlines(card.get("sample_headlines", []))}</ul>
        </div>
        <div class="mini-block">
          <h3>Recent Evidence</h3>
          <ul>{render_recent_evidence(card.get("recent_evidence", []))}</ul>
        </div>
        <div class="mini-block">
          <h3>Image Status</h3>
          <ul>{render_image_slots(card.get("image_slots", []))}</ul>
        </div>
      </div>
      <div class="draft">
        <h3>Draft Body</h3>
        <pre>{draft_body}</pre>
      </div>
    </section>
    """


def write_html(report: dict) -> None:
    cards_html = "\n".join(render_card(card) for card in report.get("cards", []))
    single = html.escape(report.get("single_approval_command", ""))
    batch = html.escape(report.get("batch_approval_command", ""))
    html_text = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Approval Briefing Board</title>
  <style>
    :root {{
      --bg: #f6f1e8;
      --panel: rgba(255, 252, 245, 0.94);
      --ink: #1a1b18;
      --muted: #62645d;
      --line: #d8cfbf;
      --accent: #8f3b2f;
      --accent-soft: #f3ddd7;
      --accent-alt: #1d5f5b;
      --accent-alt-soft: #dff0ec;
      --shadow: 0 18px 40px rgba(39, 28, 17, 0.08);
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      color: var(--ink);
      font-family: "Avenir Next", "Pretendard", "Apple SD Gothic Neo", sans-serif;
      background:
        radial-gradient(circle at top left, rgba(143, 59, 47, 0.08), transparent 26%),
        linear-gradient(180deg, #fbf8f2 0%, var(--bg) 100%);
    }}
    .page {{
      max-width: 1500px;
      margin: 0 auto;
      padding: 28px 18px 64px;
    }}
    .hero, .card {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 24px;
      box-shadow: var(--shadow);
    }}
    .hero {{
      padding: 26px;
      margin-bottom: 22px;
    }}
    h1 {{
      margin: 0 0 10px;
      font-size: clamp(2.2rem, 4.8vw, 4rem);
      line-height: 0.96;
      letter-spacing: -0.05em;
    }}
    h2 {{
      margin: 0 0 12px;
      font-size: 1.45rem;
      letter-spacing: -0.02em;
    }}
    h3 {{
      margin: 0 0 10px;
      font-size: 1rem;
    }}
    p {{ line-height: 1.6; }}
    .muted {{ color: var(--muted); }}
    code, pre {{
      font-family: "SFMono-Regular", Consolas, monospace;
    }}
    .command {{
      display: block;
      padding: 12px 14px;
      border-radius: 14px;
      background: #151714;
      color: #f8f2e7;
      overflow-wrap: anywhere;
      margin-top: 10px;
    }}
    .card {{
      display: grid;
      grid-template-columns: 0.95fr 1.05fr;
      gap: 18px;
      padding: 20px;
      margin-bottom: 20px;
    }}
    .pill-row {{
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      margin-bottom: 10px;
    }}
    .pill {{
      display: inline-flex;
      align-items: center;
      border-radius: 999px;
      padding: 5px 10px;
      font-size: 0.78rem;
      background: var(--accent-soft);
      color: var(--accent);
      font-weight: 700;
    }}
    .pill.alt {{
      background: var(--accent-alt-soft);
      color: var(--accent-alt);
    }}
    .mini-block {{
      margin-top: 16px;
      padding: 14px;
      border-radius: 18px;
      background: #fcf8f0;
      border: 1px solid var(--line);
    }}
    .mini-block ul {{
      margin: 0;
      padding-left: 18px;
    }}
    .draft pre {{
      margin: 0;
      padding: 16px;
      border-radius: 18px;
      background: #141613;
      color: #f6f1e7;
      white-space: pre-wrap;
      line-height: 1.5;
      max-height: 900px;
      overflow: auto;
    }}
    .links a {{
      margin-right: 10px;
    }}
    .tiny {{
      color: var(--muted);
      font-size: 0.8rem;
    }}
    @media (max-width: 1100px) {{
      .card {{
        grid-template-columns: 1fr;
      }}
    }}
  </style>
</head>
<body>
  <main class="page">
    <section class="hero">
      <h1>Approval Briefing Board</h1>
      <p class="muted">승인 직전 필요한 자료를 한 화면에 묶었습니다. 글 전문, 최신 근거, 이미지 상태, 승인 명령을 따로 열지 않고 바로 비교할 수 있습니다.</p>
      <code class="command">{single or 'single confirmation unavailable'}</code>
      <code class="command">{batch or 'batch confirmation unavailable'}</code>
    </section>
    {cards_html}
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
