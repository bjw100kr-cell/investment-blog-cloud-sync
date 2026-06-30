#!/usr/bin/env python3
import html
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CURRENT_REVIEW_FOCUS_JSON = ROOT / "outputs/latest/current-review-focus.json"
FIRST_APPROVAL_PATH_JSON = ROOT / "outputs/latest/first-approval-path.json"
OUTPUT_JSON = ROOT / "outputs/latest/user-approval-inbox.json"
OUTPUT_MD = ROOT / "outputs/latest/user-approval-inbox.md"
OUTPUT_HTML = ROOT / "outputs/latest/user-approval-inbox.html"
REPLY_HELPER = ROOT / "scripts/apply_user_approval_reply.py"
REPLY_FLOW_HELPER = ROOT / "scripts/run_user_approval_reply_flow.py"
REHEARSAL_HELPER = ROOT / "scripts/rehearse_user_approval_reply.py"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def to_uri(path: Path) -> str:
    if not path.exists():
        return ""
    return path.resolve().as_uri()


def decision_label(item: dict) -> str:
    if "source_freshness_stale" in item.get("hard_blocking_checks", []):
        return "이 글은 지금 바로 뉴스형 승인보다, FOMC SEO 후속 글 같은 대체 경로가 더 안전합니다."
    if item.get("ready_now"):
        return "이 글은 내용만 괜찮으면 바로 승인 후보입니다."
    return "이 글은 내용 확인 후 대표 이미지 보완이 먼저 필요합니다."


def build_report() -> dict:
    focus = load_json(CURRENT_REVIEW_FOCUS_JSON)
    approval_path = load_json(FIRST_APPROVAL_PATH_JSON)
    focus_items = focus.get("focus_items", [])
    items = []
    top_keyword = (approval_path.get("recommended_single") or {}).get("keyword", "")
    for item in focus_items:
        keyword = item.get("keyword", "")
        items.append(
            {
                "keyword": keyword,
                "title": item.get("title", ""),
                "ready_now": item.get("ready_now", False),
                "quality_status": item.get("quality_status", ""),
                "decision_note": decision_label(item),
                "intent": item.get("intent", ""),
                "cta_focus": item.get("cta_focus", ""),
                "retention_cta_enabled": item.get("retention_cta_enabled", False),
                "retention_cta": item.get("retention_cta", {}),
                "freshness_status": item.get("freshness_status", ""),
                "freshness_recommendation": item.get("freshness_recommendation", ""),
                "next_action": item.get("next_action", ""),
                "hard_blocking_checks": item.get("hard_blocking_checks", []),
                "excerpt": item.get("excerpt", [])[:3],
                "preview": item.get("preview", [])[:2],
                "recent_evidence": item.get("recent_evidence", [])[:2],
                "confirm_command": item.get("confirm_command", ""),
                "next_command": item.get("next_command", ""),
                "recovery_mode": item.get("recovery_mode", ""),
                "recovery_title": item.get("recovery_title", ""),
                "recovery_confirm_command": item.get("recovery_confirm_command", ""),
                "recovery_image_apply_helper": item.get("recovery_image_apply_helper", ""),
                "helper_preview_command": item.get("helper_preview_command", ""),
                "hero_image_apply_helper": item.get("hero_image_apply_helper", ""),
                "draft_path": item.get("draft_path", ""),
                "html_path": item.get("html_path", ""),
            }
        )

    default_keyword = top_keyword or (items[0].get("keyword", "") if items else "bitcoin")
    reply_examples = [
        f"`{default_keyword}` 글 먼저 진행",
        "`bitcoin` 먼저 검토, 이미지 보완 후 업로드 준비",
        "`FOMC 메인 말고 SEO 후속 글로 전환`",
        "둘 다 보류, 제목 톤만 조금 더 부드럽게 수정",
    ]

    return {
        "guardrail": focus.get(
            "guardrail",
            "제가 먼저 초안을 보여드리고, 사용자 최종 확인 전에는 실제 업로드가 계속 차단됩니다.",
        ),
        "item_count": len(items),
        "items": items,
        "reply_examples": reply_examples,
        "reply_helper_examples": [
            f'python3 {REPLY_HELPER} --reply "{default_keyword} 글 먼저 진행"',
            f'python3 {REPLY_HELPER} --reply "bitcoin 먼저 검토, 이미지 보완 후 업로드 준비"',
            f'python3 {REPLY_HELPER} --reply "{default_keyword} 글 먼저 진행" --apply',
        ],
        "reply_flow_examples": [
            f'python3 {REPLY_FLOW_HELPER} --reply "{default_keyword} 글 먼저 진행"',
            f'python3 {REPLY_FLOW_HELPER} --reply "{default_keyword} 글 먼저 진행" --apply',
        ],
        "reply_rehearsal_examples": [
            f'python3 {REHEARSAL_HELPER} --reply "{default_keyword} 글 먼저 진행"',
            f'python3 {REHEARSAL_HELPER} --reply "FOMC 메인 말고 SEO 후속 글로 전환"',
        ],
        "related_paths": {
            "current_review_focus_html": str(ROOT / "outputs/latest/current-review-focus.html"),
            "shortlist_launchpad_html": str(ROOT / "outputs/latest/shortlist-launchpad.html"),
            "approval_briefing_board_html": str(ROOT / "outputs/latest/approval-briefing-board.html"),
        },
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# User Approval Inbox")
    lines.append("")
    lines.append("사용자가 글을 읽고 승인 여부만 빠르게 답할 수 있게 만든 확인 전용 인박스입니다.")
    lines.append(f"- 안전 원칙: {report.get('guardrail', '')}")
    lines.append(f"- current review focus: `{report.get('related_paths', {}).get('current_review_focus_html', '')}`")
    lines.append(f"- shortlist launchpad: `{report.get('related_paths', {}).get('shortlist_launchpad_html', '')}`")
    lines.append(f"- approval briefing board: `{report.get('related_paths', {}).get('approval_briefing_board_html', '')}`")
    lines.append("")
    lines.append("## 어떻게 답하면 되는가")
    lines.append("")
    for example in report.get("reply_examples", []):
        lines.append(f"- {example}")
    lines.append("")
    lines.append("## 답변을 승인 파일로 바꾸는 헬퍼")
    lines.append("")
    for example in report.get("reply_helper_examples", []):
        lines.append(f"- `{example}`")
    lines.append("")
    lines.append("## 답변에서 다음 실행 흐름까지 이어보기")
    lines.append("")
    for example in report.get("reply_flow_examples", []):
        lines.append(f"- `{example}`")
    lines.append("")
    lines.append("## 업로드 없이 안전하게 리허설하기")
    lines.append("")
    for example in report.get("reply_rehearsal_examples", []):
        lines.append(f"- `{example}`")
    lines.append("")
    for idx, item in enumerate(report.get("items", []), start=1):
        lines.append(f"## {idx}. {item.get('title', '')}")
        lines.append("")
        lines.append(f"- keyword: `{item.get('keyword', '')}`")
        lines.append(f"- ready_now: `{item.get('ready_now', False)}`")
        lines.append(f"- quality_status: `{item.get('quality_status', '')}`")
        lines.append(f"- decision_note: {item.get('decision_note', '')}")
        if item.get("freshness_status"):
            lines.append(f"- freshness_status: `{item.get('freshness_status', '')}`")
        if item.get("freshness_recommendation"):
            lines.append(f"- freshness_recommendation: {item.get('freshness_recommendation', '')}")
        if item.get("hard_blocking_checks"):
            lines.append(f"- hard_blocking_checks: {', '.join(item.get('hard_blocking_checks', []))}")
        if item.get("next_action"):
            lines.append(f"- next_action: {item.get('next_action', '')}")
        lines.append(f"- reader_intent: {item.get('intent', '')}")
        lines.append(f"- CTA focus: {item.get('cta_focus', '')}")
        if item.get("retention_cta_enabled"):
            retention_cta = item.get("retention_cta", {})
            lines.append(f"- final retention CTA: {retention_cta.get('inline_cta_now', '')}")
            if retention_cta.get("telegram_cta_later"):
                lines.append(f"- later revisit CTA: {retention_cta.get('telegram_cta_later', '')}")
        for excerpt in item.get("excerpt", []):
            lines.append(f"- excerpt: {excerpt}")
        for preview in item.get("preview", []):
            lines.append(f"- preview: {preview}")
        for evidence in item.get("recent_evidence", []):
            lines.append(
                f"- evidence: {evidence.get('source_name', '')} / {evidence.get('published_iso', '')} / {evidence.get('title', '')}"
            )
        if item.get("confirm_command"):
            lines.append(f"- confirm_command: `{item.get('confirm_command', '')}`")
        if item.get("next_command"):
            lines.append(f"- next_command: `{item.get('next_command', '')}`")
        if item.get("recovery_mode"):
            lines.append(f"- recovery_mode: `{item.get('recovery_mode', '')}`")
        if item.get("recovery_title"):
            lines.append(f"- recovery_title: {item.get('recovery_title', '')}")
        if item.get("recovery_confirm_command"):
            lines.append(f"- recovery_confirm_command: `{item.get('recovery_confirm_command', '')}`")
        if item.get("recovery_image_apply_helper"):
            lines.append(f"- recovery_image_apply_helper: `{item.get('recovery_image_apply_helper', '')}`")
        if item.get("helper_preview_command"):
            lines.append(f"- helper_preview_command: `{item.get('helper_preview_command', '')}`")
        if item.get("hero_image_apply_helper"):
            lines.append(f"- hero_image_apply_helper: `{item.get('hero_image_apply_helper', '')}`")
        lines.append(f"- draft_path: `{item.get('draft_path', '')}`")
        lines.append(f"- html_path: `{item.get('html_path', '')}`")
        lines.append("")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def render_text_blocks(items: list[str]) -> str:
    return "".join(f"<p>{html.escape(item)}</p>" for item in items)


def render_evidence(items: list[dict]) -> str:
    if not items:
        return "<li>근거 요약이 아직 없습니다.</li>"
    return "".join(
        f"<li><strong>{html.escape(item.get('source_name', ''))}</strong> · {html.escape(item.get('published_iso', ''))}<br>{html.escape(item.get('title', ''))}</li>"
        for item in items
    )


def write_html(report: dict) -> None:
    cards = []
    for item in report.get("items", []):
        cards.append(
            f"""
            <article class="card">
              <div class="top">
                <span class="badge">{html.escape(item.get('keyword', ''))}</span>
                <span class="badge alt">{'ready now' if item.get('ready_now') else 'needs prep'}</span>
              </div>
              <h2>{html.escape(item.get('title', ''))}</h2>
              <p class="decision">{html.escape(item.get('decision_note', ''))}</p>
              <p class="meta">quality `{html.escape(item.get('quality_status', ''))}`</p>
              {f"<p class='meta'>freshness `{html.escape(item.get('freshness_status', ''))}`</p>" if item.get('freshness_status') else ""}
              {f"<p class='meta'>{html.escape(item.get('freshness_recommendation', ''))}</p>" if item.get('freshness_recommendation') else ""}
              {f"<p class='meta'>next action · {html.escape(item.get('next_action', ''))}</p>" if item.get('next_action') else ""}
              <h3>이 글을 읽는 사람</h3>
              <p>{html.escape(item.get('intent', ''))}</p>
              {f"<h3>최종 CTA</h3><p>{html.escape((item.get('retention_cta') or {}).get('inline_cta_now', ''))}</p>" if item.get('retention_cta_enabled') and (item.get('retention_cta') or {}).get('inline_cta_now') else ""}
              <h3>초안 핵심</h3>
              {render_text_blocks(item.get('excerpt', []))}
              <h3>읽기 전 체크</h3>
              {render_text_blocks(item.get('preview', []))}
              <h3>최근 근거</h3>
              <ul>{render_evidence(item.get('recent_evidence', []))}</ul>
              {f"<code>{html.escape(item.get('confirm_command', ''))}</code>" if item.get('confirm_command') else ""}
              {f"<code>{html.escape(item.get('recovery_confirm_command', ''))}</code>" if item.get('recovery_confirm_command') else ""}
              {f"<code>{html.escape(item.get('recovery_image_apply_helper', ''))}</code>" if item.get('recovery_image_apply_helper') else ""}
              {f"<code>{html.escape(item.get('hero_image_apply_helper', ''))}</code>" if item.get('hero_image_apply_helper') else ""}
            </article>
            """
        )

    html_text = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>User Approval Inbox</title>
  <style>
    :root {{
      --bg: #f5efe7;
      --panel: rgba(255, 252, 246, 0.95);
      --ink: #171714;
      --muted: #636158;
      --line: #ddd4c6;
      --accent: #8a362f;
      --accent-soft: #f6e2dd;
      --accent-alt: #285e58;
      --accent-alt-soft: #e2f0ed;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      color: var(--ink);
      font-family: "Avenir Next", "Pretendard", "Apple SD Gothic Neo", sans-serif;
      background:
        radial-gradient(circle at top left, rgba(138, 54, 47, 0.08), transparent 28%),
        radial-gradient(circle at bottom right, rgba(40, 94, 88, 0.08), transparent 24%),
        linear-gradient(180deg, #fbf8f2 0%, var(--bg) 100%);
    }}
    main {{
      max-width: 1180px;
      margin: 0 auto;
      padding: 28px 18px 54px;
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
      font-size: clamp(2rem, 4vw, 3.4rem);
      line-height: 0.96;
      letter-spacing: -0.05em;
    }}
    .muted, .meta {{
      color: var(--muted);
    }}
    .reply-list {{
      display: grid;
      gap: 10px;
      margin-top: 14px;
    }}
    .reply-item {{
      padding: 12px 14px;
      border: 1px solid var(--line);
      border-radius: 14px;
      background: #fcf8f2;
      font-weight: 600;
    }}
    .grid {{
      display: grid;
      gap: 18px;
      grid-template-columns: repeat(2, minmax(0, 1fr));
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
    .decision {{
      font-weight: 700;
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
    p {{
      line-height: 1.62;
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
    @media (max-width: 920px) {{
      .grid {{
        grid-template-columns: 1fr;
      }}
    }}
  </style>
</head>
<body>
  <main>
    <section class="hero">
      <h1>User Approval Inbox</h1>
      <p class="muted">이 화면은 사용자가 글을 읽고 승인 여부만 빠르게 답할 수 있도록 만든 확인 전용 인박스입니다.</p>
      <p><strong>안전 원칙:</strong> {html.escape(report.get('guardrail', ''))}</p>
      <div class="reply-list">
        {''.join(f"<div class='reply-item'>{html.escape(example)}</div>" for example in report.get('reply_examples', []))}
      </div>
      <div class="reply-list">
        {''.join(f"<div class='reply-item'><code>{html.escape(example)}</code></div>" for example in report.get('reply_helper_examples', []))}
      </div>
      <div class="reply-list">
        {''.join(f"<div class='reply-item'><code>{html.escape(example)}</code></div>" for example in report.get('reply_flow_examples', []))}
      </div>
      <p class="muted">current review focus: {html.escape(to_uri(ROOT / 'outputs/latest/current-review-focus.html'))}</p>
    </section>
    <section class="grid">
      {''.join(cards) if cards else "<article class='card'><p>승인 인박스 항목이 아직 없습니다.</p></article>"}
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
