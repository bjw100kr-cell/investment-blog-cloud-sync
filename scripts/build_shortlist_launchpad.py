#!/usr/bin/env python3
import html
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
APPROVAL_BRIEFING_BOARD_JSON = ROOT / "outputs/latest/approval-briefing-board.json"
SHORTLIST_PUBLISH_ACTION_BOARD_JSON = ROOT / "outputs/latest/shortlist-publish-action-board.json"
OUTPUT_JSON = ROOT / "outputs/latest/shortlist-launchpad.json"
OUTPUT_MD = ROOT / "outputs/latest/shortlist-launchpad.md"
OUTPUT_HTML = ROOT / "outputs/latest/shortlist-launchpad.html"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def build_lookup(items: list[dict], key: str) -> dict:
    return {item.get(key): item for item in items if item.get(key)}


def to_uri(path_text: str) -> str:
    if not path_text:
        return ""
    path = Path(path_text)
    if not path.exists():
        return ""
    return path.resolve().as_uri()


def build_report() -> dict:
    briefing = load_json(APPROVAL_BRIEFING_BOARD_JSON)
    actions = load_json(SHORTLIST_PUBLISH_ACTION_BOARD_JSON)
    action_lookup = build_lookup(actions.get("items", []), "keyword")

    cards = []
    for item in briefing.get("cards", []):
        action = action_lookup.get(item.get("keyword", ""), {})
        cards.append(
            {
                "keyword": item.get("keyword", ""),
                "title": item.get("title", ""),
                "publish_date": item.get("publish_date", ""),
                "review_verdict": item.get("review_verdict", ""),
                "quality_status": item.get("quality_status", ""),
                "ready_now": item.get("ready_now", False),
                "hero_image_selected": item.get("hero_image_selected", False),
                "reason": item.get("reason", ""),
                "intent": item.get("intent", ""),
                "sample_headlines": item.get("sample_headlines", [])[:3],
                "recent_evidence": item.get("recent_evidence", [])[:3],
                "draft_uri": item.get("draft_uri", ""),
                "html_uri": item.get("html_uri", ""),
                "confirm_command": action.get("confirm_command", ""),
                "next_action": action.get("next_action", ""),
                "next_command": action.get("next_command", ""),
                "followup_commands": action.get("followup_commands", []),
                "helper_preview_command": action.get("helper_preview_command", ""),
                "helper_apply_command": action.get("helper_apply_command", ""),
                "hard_blocking_checks": action.get("hard_blocking_checks", []),
            }
        )

    return {
        "item_count": len(cards),
        "single_approval_command": briefing.get("single_approval_command", ""),
        "batch_approval_command": briefing.get("batch_approval_command", ""),
        "cards": cards,
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# Shortlist Launchpad")
    lines.append("")
    lines.append("shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.")
    lines.append("- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.")
    lines.append(f"- item_count: `{report.get('item_count', 0)}`")
    lines.append("")
    for index, card in enumerate(report.get("cards", []), start=1):
        lines.append(f"## {index}. {card.get('title', '')}")
        lines.append("")
        lines.append(
            f"- keyword `{card.get('keyword', '')}` / publish `{card.get('publish_date', '')}` / verdict `{card.get('review_verdict', '')}` / quality `{card.get('quality_status', '')}`"
        )
        lines.append(f"- ready_now: `{card.get('ready_now', False)}` / hero_image_selected: `{card.get('hero_image_selected', False)}`")
        lines.append(f"- intent: {card.get('intent', '')}")
        lines.append(f"- why_now: {card.get('reason', '')}")
        if card.get("hard_blocking_checks"):
            lines.append(f"- hard_blocking_checks: {', '.join(card.get('hard_blocking_checks', []))}")
        if card.get("sample_headlines"):
            lines.append("- sample_headlines:")
            for headline in card.get("sample_headlines", []):
                lines.append(f"  - {headline}")
        if card.get("recent_evidence"):
            lines.append("- recent_evidence:")
            for evidence in card.get("recent_evidence", []):
                lines.append(
                    f"  - {evidence.get('source_name', '')} | {evidence.get('published_iso', evidence.get('published', ''))} | {evidence.get('title', '')}"
                )
        if card.get("confirm_command"):
            lines.append(f"- confirm_command: `{card.get('confirm_command', '')}`")
        if card.get("next_command"):
            lines.append(f"- next_command: `{card.get('next_command', '')}`")
        if card.get("helper_preview_command"):
            lines.append(f"- helper_preview_command: `{card.get('helper_preview_command', '')}`")
        if card.get("helper_apply_command"):
            lines.append(f"- helper_apply_command: `{card.get('helper_apply_command', '')}`")
        lines.append("")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def render_recent_evidence(items: list[dict]) -> str:
    if not items:
        return "<li>No recent evidence</li>"
    return "".join(
        f"<li><strong>{html.escape(item.get('source_name', ''))}</strong> <span class='tiny'>{html.escape(item.get('published_iso', item.get('published', '')))}</span><br>{html.escape(item.get('title', ''))}</li>"
        for item in items
    )


def render_headlines(items: list[str]) -> str:
    if not items:
        return "<li>No headlines</li>"
    return "".join(f"<li>{html.escape(item)}</li>" for item in items)


def render_commands(card: dict) -> str:
    commands = []
    if card.get("confirm_command"):
        commands.append(f"<code>{html.escape(card.get('confirm_command', ''))}</code>")
    if card.get("next_command"):
        commands.append(f"<code>{html.escape(card.get('next_command', ''))}</code>")
    if card.get("helper_preview_command"):
        commands.append(f"<code>{html.escape(card.get('helper_preview_command', ''))}</code>")
    if card.get("helper_apply_command"):
        commands.append(f"<code>{html.escape(card.get('helper_apply_command', ''))}</code>")
    deduped: list[str] = []
    for command in commands:
        if command not in deduped:
            deduped.append(command)
    return "".join(deduped)


def render_followups(items: list[str]) -> str:
    if not items:
        return "<li>No followup commands</li>"
    return "".join(f"<li><code>{html.escape(item)}</code></li>" for item in items)


def render_card(card: dict) -> str:
    draft_link = (
        f"<a href='{html.escape(card.get('draft_uri', ''))}' target='_blank' rel='noreferrer'>Draft</a>"
        if card.get("draft_uri")
        else ""
    )
    html_link = (
        f"<a href='{html.escape(card.get('html_uri', ''))}' target='_blank' rel='noreferrer'>HTML Preview</a>"
        if card.get("html_uri")
        else ""
    )
    blockers = ", ".join(card.get("hard_blocking_checks", [])) or "none"
    return f"""
    <section class="card">
      <div class="top">
        <div class="pill-row">
          <span class="pill">{html.escape(card.get('keyword', ''))}</span>
          <span class="pill alt">{html.escape(card.get('review_verdict', ''))}</span>
          <span class="pill">{html.escape(card.get('quality_status', ''))}</span>
        </div>
        <h2>{html.escape(card.get('title', ''))}</h2>
        <p><strong>Publish</strong> {html.escape(card.get('publish_date', ''))} / <strong>Ready</strong> {html.escape(str(card.get('ready_now', False)))}</p>
        <p><strong>Hero image</strong> {html.escape(str(card.get('hero_image_selected', False)))} / <strong>Hard blocker</strong> {html.escape(blockers)}</p>
        <p><strong>Why now</strong> {html.escape(card.get('reason', ''))}</p>
        <p><strong>Intent</strong> {html.escape(card.get('intent', ''))}</p>
        <p class="links">{draft_link} {html_link}</p>
      </div>
      <div class="grid">
        <div class="panel">
          <h3>Quick Evidence</h3>
          <ul>{render_recent_evidence(card.get('recent_evidence', []))}</ul>
        </div>
        <div class="panel">
          <h3>Sample Headlines</h3>
          <ul>{render_headlines(card.get('sample_headlines', []))}</ul>
        </div>
      </div>
      <div class="panel">
        <h3>Do This Next</h3>
        <p>{html.escape(card.get('next_action', ''))}</p>
        {render_commands(card)}
      </div>
      <div class="panel">
        <h3>Followup Chain</h3>
        <ul>{render_followups(card.get('followup_commands', []))}</ul>
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
  <title>Shortlist Launchpad</title>
  <style>
    :root {{
      --bg: #f7f1e7;
      --panel: rgba(255, 252, 244, 0.94);
      --ink: #191a17;
      --muted: #61635d;
      --line: #d8cfbe;
      --accent: #8f3b2f;
      --accent-soft: #f1ddd8;
      --accent-alt: #1b5d58;
      --accent-alt-soft: #def0eb;
      --shadow: 0 18px 42px rgba(43, 31, 18, 0.08);
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      color: var(--ink);
      font-family: "Avenir Next", "Pretendard", "Apple SD Gothic Neo", sans-serif;
      background:
        radial-gradient(circle at top left, rgba(143, 59, 47, 0.08), transparent 28%),
        linear-gradient(180deg, #fbf8f1 0%, var(--bg) 100%);
    }}
    .page {{
      max-width: 1420px;
      margin: 0 auto;
      padding: 28px 18px 60px;
    }}
    .hero, .card, .panel {{
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
      font-size: clamp(2.1rem, 4.5vw, 3.8rem);
      line-height: 0.97;
      letter-spacing: -0.05em;
    }}
    h2 {{
      margin: 0 0 10px;
      font-size: 1.45rem;
    }}
    h3 {{
      margin: 0 0 10px;
      font-size: 1rem;
    }}
    p {{ line-height: 1.6; }}
    .muted {{ color: var(--muted); }}
    .card {{
      padding: 20px;
      margin-bottom: 18px;
    }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 14px;
      margin: 14px 0;
    }}
    .panel {{
      padding: 16px;
      border-radius: 18px;
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
    ul {{
      margin: 0;
      padding-left: 18px;
    }}
    .links a {{
      margin-right: 10px;
    }}
    code {{
      display: block;
      margin-top: 10px;
      padding: 12px 14px;
      border-radius: 14px;
      background: #161714;
      color: #f6f1e7;
      overflow-wrap: anywhere;
      font-family: "SFMono-Regular", Consolas, monospace;
    }}
    .tiny {{
      color: var(--muted);
      font-size: 0.8rem;
    }}
    @media (max-width: 980px) {{
      .grid {{
        grid-template-columns: 1fr;
      }}
    }}
  </style>
</head>
<body>
  <main class="page">
    <section class="hero">
      <h1>Shortlist Launchpad</h1>
      <p class="muted">처음엔 이 화면 하나만 보면 됩니다. shortlist 글 2개 기준으로 왜 지금 올리는지, 무엇이 막고 있는지, 바로 쓸 명령이 무엇인지 모아 둔 시작 화면입니다.</p>
      <code>{single or 'single confirmation unavailable'}</code>
      <code>{batch or 'batch confirmation unavailable'}</code>
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
