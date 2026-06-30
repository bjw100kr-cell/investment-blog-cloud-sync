#!/usr/bin/env python3
import html
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
USER_REVIEW_SHORTLIST_JSON = ROOT / "outputs/latest/user-review-shortlist.json"
REVIEW_PACKET_JSON = ROOT / "outputs/latest/review-packet.json"
OUTPUT_JSON = ROOT / "outputs/latest/review-preview-board.json"
OUTPUT_MD = ROOT / "outputs/latest/review-preview-board.md"
OUTPUT_HTML = ROOT / "outputs/latest/review-preview-board.html"


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


def build_lookup(items: list[dict]) -> dict:
    return {item.get("keyword"): item for item in items if item.get("keyword")}


def build_report() -> dict:
    shortlist = load_json(USER_REVIEW_SHORTLIST_JSON)
    review_packet = load_json(REVIEW_PACKET_JSON)
    review_lookup = build_lookup(review_packet.get("items", []))

    cards = []
    for item in shortlist.get("shortlist", []):
        keyword = item.get("keyword", "")
        review_item = review_lookup.get(keyword, {})
        cards.append(
            {
                "keyword": keyword,
                "title": item.get("title", ""),
                "publish_date": item.get("publish_date", ""),
                "priority_score": item.get("priority_score", 0),
                "review_verdict": item.get("review_verdict", ""),
                "intent": item.get("intent", ""),
                "cta_focus": item.get("cta_focus", ""),
                "preview": item.get("preview", []),
                "draft_path": review_item.get("draft_path", ""),
                "html_path": review_item.get("html_path", ""),
                "manifest_path": review_item.get("manifest_path", ""),
                "review_score": review_item.get("review_score", 0),
                "review_warnings": review_item.get("review_warnings", []),
                "retention_cta_enabled": review_item.get("retention_cta_enabled", False),
                "retention_cta": review_item.get("retention_cta", {}),
                "image_slots": review_item.get("image_slots", []),
                "image_manual_review_required": review_item.get("image_manual_review_required", False),
                "draft_uri": to_uri(review_item.get("draft_path", "")),
                "html_uri": to_uri(review_item.get("html_path", "")),
                "manifest_uri": to_uri(review_item.get("manifest_path", "")),
            }
        )

    return {
        "card_count": len(cards),
        "single_approval_command": shortlist.get("single_approval_command", ""),
        "batch_approval_command": shortlist.get("batch_approval_command", ""),
        "cards": cards,
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# Review Preview Board")
    lines.append("")
    lines.append("사용자가 업로드 전에 실제 본문 HTML까지 빠르게 읽어보고 최종 확인할 수 있도록 만든 검토 보드입니다.")
    lines.append("")
    if report.get("single_approval_command"):
        lines.append(f"- single approval: `{report['single_approval_command']}`")
    if report.get("batch_approval_command"):
        lines.append(f"- batch approval: `{report['batch_approval_command']}`")
    lines.append("")
    for index, card in enumerate(report.get("cards", []), start=1):
        lines.append(f"## {index}. {card.get('title', '')}")
        lines.append("")
        lines.append(f"- keyword: `{card.get('keyword', '')}`")
        lines.append(f"- publish_date: `{card.get('publish_date', '') or 'unscheduled'}`")
        lines.append(f"- priority_score: `{card.get('priority_score', 0)}`")
        lines.append(f"- review_verdict: `{card.get('review_verdict', '')}` / score `{card.get('review_score', 0)}`")
        lines.append(f"- intent: {card.get('intent', '')}")
        lines.append(f"- CTA focus: {card.get('cta_focus', '')}")
        if card.get("retention_cta_enabled"):
            retention_cta = card.get("retention_cta", {})
            lines.append(f"- final retention CTA: {retention_cta.get('inline_cta_now', '')}")
            if retention_cta.get("telegram_cta_later"):
                lines.append(f"- later revisit CTA: {retention_cta.get('telegram_cta_later', '')}")
        if card.get("draft_path"):
            lines.append(f"- draft: `{card.get('draft_path', '')}`")
        if card.get("html_path"):
            lines.append(f"- html: `{card.get('html_path', '')}`")
        if card.get("image_slots"):
            lines.append(f"- image review required: `{card.get('image_manual_review_required', False)}`")
            for image in card.get("image_slots", []):
                lines.append(
                    f"- image {image.get('slot_label', image.get('slot'))}: {image.get('provider_name', '')} / `{image.get('search_query', '')}` / {image.get('license_label', '')}"
                )
                lines.append(
                    f"- image apply helper: `python3 {ROOT / 'scripts/set_image_selection.py'} --keyword {card.get('keyword', '')} --slot {image.get('slot', '')} --selected-url <IMAGE_URL> --selected-credit \"Photo by ...\" --approve`"
                )
        for warning in card.get("review_warnings", []):
            lines.append(f"- warning: {warning}")
        for paragraph in card.get("preview", []):
            lines.append(f"- preview: {paragraph}")
        lines.append("")
    if not report.get("cards"):
        lines.append("- 검토 카드가 없습니다.")
        lines.append("")
    lines.append(f"- board html: `{OUTPUT_HTML}`")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def render_preview(paragraphs: list[str]) -> str:
    if not paragraphs:
        return "<p class='muted'>Preview unavailable.</p>"
    return "".join(f"<p>{html.escape(paragraph)}</p>" for paragraph in paragraphs)


def render_warnings(warnings: list[str]) -> str:
    if not warnings:
        return "<li>No internal warnings</li>"
    return "".join(f"<li>{html.escape(warning)}</li>" for warning in warnings)


def render_image_slots(image_slots: list[dict]) -> str:
    if not image_slots:
        return "<li>No image suggestions yet</li>"
    items = []
    for image in image_slots:
        search_url = html.escape(image.get("search_url", ""))
        license_url = html.escape(image.get("license_url", ""))
        slot_label = html.escape(image.get("slot_label", image.get("slot", "")))
        provider_name = html.escape(image.get("provider_name", ""))
        search_query = html.escape(image.get("search_query", ""))
        license_label = html.escape(image.get("license_label", ""))
        search_link = f"<a href='{search_url}' target='_blank' rel='noreferrer'>search</a>" if search_url else ""
        license_link = f"<a href='{license_url}' target='_blank' rel='noreferrer'>{license_label}</a>" if license_url else license_label
        items.append(
            f"<li><strong>{slot_label}</strong>: {provider_name} / <code>{search_query}</code> / {search_link} / {license_link}</li>"
        )
    return "".join(items)


def render_card(card: dict) -> str:
    title = html.escape(card.get("title", "Untitled"))
    keyword = html.escape(card.get("keyword", ""))
    verdict = html.escape(card.get("review_verdict", ""))
    publish_date = html.escape(card.get("publish_date", "") or "unscheduled")
    intent = html.escape(card.get("intent", ""))
    cta_focus = html.escape(card.get("cta_focus", ""))
    retention_cta = card.get("retention_cta", {}) or {}
    retention_now = html.escape(retention_cta.get("inline_cta_now", "")) if card.get("retention_cta_enabled") else ""
    retention_later = html.escape(retention_cta.get("telegram_cta_later", "")) if card.get("retention_cta_enabled") else ""
    score = html.escape(str(card.get("review_score", 0)))
    priority_score = html.escape(str(card.get("priority_score", 0)))
    draft_link = f"<a href='{html.escape(card['draft_uri'])}' target='_blank' rel='noreferrer'>Draft markdown</a>" if card.get("draft_uri") else ""
    html_link = f"<a href='{html.escape(card['html_uri'])}' target='_blank' rel='noreferrer'>Rendered HTML</a>" if card.get("html_uri") else ""
    manifest_link = f"<a href='{html.escape(card['manifest_uri'])}' target='_blank' rel='noreferrer'>Manifest</a>" if card.get("manifest_uri") else ""
    links = " ".join(link for link in [draft_link, html_link, manifest_link] if link)
    iframe = (
        f"<iframe src='{html.escape(card['html_uri'])}' loading='lazy' title='{title}'></iframe>"
        if card.get("html_uri")
        else "<div class='empty-frame'>Rendered HTML unavailable.</div>"
    )
    return f"""
    <section class="card">
      <div class="meta">
        <div class="pill-row">
          <span class="pill keyword">{keyword}</span>
          <span class="pill verdict">{verdict}</span>
          <span class="pill score">score {score}</span>
          <span class="pill priority">priority {priority_score}</span>
        </div>
        <h2>{title}</h2>
        <p><strong>Publish date:</strong> {publish_date}</p>
        <p><strong>Intent:</strong> {intent}</p>
        <p><strong>CTA focus:</strong> {cta_focus}</p>
        {f"<p><strong>Final retention CTA:</strong> {retention_now}</p>" if retention_now else ""}
        {f"<p><strong>Later revisit CTA:</strong> {retention_later}</p>" if retention_later else ""}
        <div class="preview">
          {render_preview(card.get("preview", []))}
        </div>
        <div class="links">{links}</div>
        <div class="warnings">
          <h3>Safe image suggestions</h3>
          <ul>{render_image_slots(card.get("image_slots", []))}</ul>
        </div>
        <div class="warnings">
          <h3>Internal review warnings</h3>
          <ul>{render_warnings(card.get("review_warnings", []))}</ul>
        </div>
      </div>
      <div class="frame-wrap">
        {iframe}
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
  <title>Review Preview Board</title>
  <style>
    :root {{
      --bg: #f5f1e8;
      --ink: #1e1f1d;
      --muted: #5a5b56;
      --card: #fffdf8;
      --line: #d9cfbf;
      --accent: #9d3c2b;
      --accent-soft: #f2ddd5;
      --accent-alt: #1f5f5b;
      --shadow: 0 18px 40px rgba(48, 36, 22, 0.08);
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: "Iowan Old Style", "Palatino Linotype", "Noto Serif KR", serif;
      background:
        radial-gradient(circle at top left, rgba(157, 60, 43, 0.10), transparent 28%),
        linear-gradient(180deg, #f9f5ed 0%, var(--bg) 100%);
      color: var(--ink);
    }}
    .page {{
      max-width: 1400px;
      margin: 0 auto;
      padding: 32px 20px 64px;
    }}
    .hero {{
      background: rgba(255, 253, 248, 0.86);
      border: 1px solid var(--line);
      box-shadow: var(--shadow);
      padding: 24px;
      border-radius: 24px;
      margin-bottom: 24px;
    }}
    h1, h2, h3 {{ margin: 0 0 12px; }}
    h1 {{
      font-size: clamp(2rem, 4vw, 3.5rem);
      line-height: 1.02;
      letter-spacing: -0.04em;
    }}
    .hero p {{
      margin: 10px 0;
      color: var(--muted);
      font-size: 1.02rem;
    }}
    .command {{
      display: block;
      padding: 12px 14px;
      border-radius: 14px;
      background: #faf6ef;
      border: 1px dashed var(--line);
      font-family: "SFMono-Regular", Consolas, monospace;
      overflow-wrap: anywhere;
      margin-top: 10px;
    }}
    .card {{
      display: grid;
      grid-template-columns: minmax(280px, 420px) 1fr;
      gap: 20px;
      align-items: start;
      background: rgba(255, 253, 248, 0.92);
      border: 1px solid var(--line);
      box-shadow: var(--shadow);
      border-radius: 24px;
      padding: 20px;
      margin-bottom: 22px;
    }}
    .pill-row {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 14px;
    }}
    .pill {{
      display: inline-flex;
      align-items: center;
      border-radius: 999px;
      padding: 6px 12px;
      font-size: 0.84rem;
      border: 1px solid transparent;
    }}
    .keyword {{ background: var(--accent-soft); color: var(--accent); }}
    .verdict {{ background: #eef6f5; color: var(--accent-alt); }}
    .score, .priority {{ background: #f4efe7; color: var(--muted); border-color: var(--line); }}
    .meta p {{
      margin: 8px 0;
      line-height: 1.6;
    }}
    .preview {{
      margin-top: 16px;
      padding: 16px;
      border-left: 4px solid var(--accent);
      background: #fcf7f1;
      border-radius: 0 14px 14px 0;
    }}
    .preview p {{
      margin: 0 0 12px;
    }}
    .preview p:last-child {{ margin-bottom: 0; }}
    .links {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 16px;
    }}
    .links a {{
      color: var(--accent);
      text-decoration: none;
      font-weight: 700;
    }}
    .warnings code {{
      display: inline;
      padding: 2px 6px;
      border-radius: 8px;
      background: #141613;
      color: #f6f1e7;
    }}
    .warnings {{
      margin-top: 18px;
      padding-top: 16px;
      border-top: 1px solid var(--line);
    }}
    .warnings ul {{
      padding-left: 18px;
      margin: 8px 0 0;
    }}
    .frame-wrap {{
      min-height: 700px;
      background: #f3ede2;
      border-radius: 18px;
      border: 1px solid var(--line);
      overflow: hidden;
    }}
    iframe, .empty-frame {{
      width: 100%;
      height: 700px;
      border: 0;
      background: white;
    }}
    .empty-frame {{
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--muted);
      padding: 24px;
      text-align: center;
    }}
    .muted {{ color: var(--muted); }}
    @media (max-width: 980px) {{
      .card {{
        grid-template-columns: 1fr;
      }}
      .frame-wrap, iframe, .empty-frame {{
        height: 520px;
      }}
    }}
  </style>
</head>
<body>
  <main class="page">
    <section class="hero">
      <h1>Review Preview Board</h1>
      <p>업로드 전에 읽어볼 글을 짧게 고르고, 같은 화면에서 실제 렌더링까지 확인할 수 있게 만든 검토 보드입니다.</p>
      <p>검토 후 승인할 때는 아래 명령만 쓰면 됩니다.</p>
      <code class="command">{single or 'single approval command unavailable'}</code>
      <code class="command">{batch or 'batch approval command unavailable'}</code>
    </section>
    {cards_html or "<p class='muted'>No review cards available.</p>"}
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
