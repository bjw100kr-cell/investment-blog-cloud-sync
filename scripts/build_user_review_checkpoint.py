#!/usr/bin/env python3
import html
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CURRENT_REVIEW_FOCUS_JSON = ROOT / "outputs/latest/current-review-focus.json"
USER_APPROVAL_INBOX_JSON = ROOT / "outputs/latest/user-approval-inbox.json"
REVIEW_APPROVALS_JSON = ROOT / "outputs/latest/review-approvals.json"
PLATFORM_PUBLISH_PLAN_JSON = ROOT / "outputs/latest/platform-publish-plan.json"
SOURCE_FRESHNESS_BOARD_HTML = ROOT / "outputs/latest/source-freshness-board.html"
OUTPUT_JSON = ROOT / "outputs/latest/user-review-checkpoint.json"
OUTPUT_MD = ROOT / "outputs/latest/user-review-checkpoint.md"
OUTPUT_HTML = ROOT / "outputs/latest/user-review-checkpoint.html"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def pick_reply_example(inbox: dict, keyword: str) -> str:
    for item in inbox.get("reply_examples", []):
        if keyword and keyword in item:
            return item
    examples = inbox.get("reply_examples", [])
    return examples[0] if examples else "`fomc` 글 먼저 진행"


def build_report() -> dict:
    focus = load_json(CURRENT_REVIEW_FOCUS_JSON)
    inbox = load_json(USER_APPROVAL_INBOX_JSON)
    approvals = load_json(REVIEW_APPROVALS_JSON)
    publish_plan = load_json(PLATFORM_PUBLISH_PLAN_JSON)

    focus_items = focus.get("focus_items", [])
    top_item = focus_items[0] if focus_items else {}
    approved_keywords = approvals.get("user_confirmed_keywords", approvals.get("approved_keywords", []))
    confirmed_all = approvals.get("user_confirmed_all", approvals.get("approved_all", False))

    return {
        "guardrail": "게시 전에는 제가 먼저 초안을 보여드리고, 사용자가 확인한 글만 다음 단계로 넘깁니다.",
        "posting_blocked_until_user_confirmation": bool(
            approvals.get("user_final_confirmation_required", True) and not confirmed_all and not approved_keywords
        ),
        "approved_keywords": approved_keywords,
        "approved_ready_count": publish_plan.get("approved_ready_count", 0),
        "next_review": {
            "keyword": top_item.get("keyword", ""),
            "title": top_item.get("title", ""),
            "ready_now": top_item.get("ready_now", False),
            "quality_status": top_item.get("quality_status", ""),
            "draft_path": top_item.get("draft_path", ""),
            "html_path": top_item.get("html_path", ""),
            "preview": top_item.get("preview", [])[:2],
            "excerpt": top_item.get("excerpt", [])[:3],
            "retention_cta_enabled": top_item.get("retention_cta_enabled", False),
            "retention_cta": top_item.get("retention_cta", {}),
            "freshness_status": top_item.get("freshness_status", ""),
            "newest_evidence_age_days": top_item.get("newest_evidence_age_days", ""),
            "freshness_summary": top_item.get("freshness_summary", ""),
            "freshness_recommendation": top_item.get("freshness_recommendation", ""),
            "next_action": top_item.get("next_action", ""),
            "hard_blocking_checks": top_item.get("hard_blocking_checks", []),
            "confirm_command": top_item.get("confirm_command", ""),
            "reply_example": pick_reply_example(inbox, top_item.get("keyword", "")),
        },
        "secondary_review": [
            {
                "keyword": item.get("keyword", ""),
                "title": item.get("title", ""),
                "ready_now": item.get("ready_now", False),
                "quality_status": item.get("quality_status", ""),
                "freshness_status": item.get("freshness_status", ""),
                "next_action": item.get("next_action", ""),
                "hard_blocking_checks": item.get("hard_blocking_checks", []),
                "draft_path": item.get("draft_path", ""),
                "html_path": item.get("html_path", ""),
            }
            for item in focus_items[1:3]
        ],
        "related_paths": {
            "current_review_focus_html": str(ROOT / "outputs/latest/current-review-focus.html"),
            "user_approval_inbox_html": str(ROOT / "outputs/latest/user-approval-inbox.html"),
            "full_draft_review_sheet_md": str(ROOT / "outputs/latest/full-draft-review-sheet.md"),
            "source_freshness_board_html": str(SOURCE_FRESHNESS_BOARD_HTML),
        },
    }


def write_markdown(report: dict) -> None:
    next_review = report.get("next_review", {})
    lines = []
    lines.append("# User Review Checkpoint")
    lines.append("")
    lines.append("블로그 업로드 전에 사용자에게 가장 먼저 보여줄 초안과 확인 상태를 한 장에 묶은 체크포인트입니다.")
    lines.append(f"- guardrail: {report.get('guardrail', '')}")
    lines.append(
        f"- posting_blocked_until_user_confirmation: `{report.get('posting_blocked_until_user_confirmation', False)}`"
    )
    lines.append(f"- approved_keywords: `{json.dumps(report.get('approved_keywords', []), ensure_ascii=False)}`")
    lines.append(f"- approved_ready_count: `{report.get('approved_ready_count', 0)}`")
    lines.append(f"- current review focus: `{report.get('related_paths', {}).get('current_review_focus_html', '')}`")
    lines.append(f"- user approval inbox: `{report.get('related_paths', {}).get('user_approval_inbox_html', '')}`")
    lines.append(f"- source freshness board: `{report.get('related_paths', {}).get('source_freshness_board_html', '')}`")
    lines.append("")
    lines.append("## 지금 먼저 보여줄 글")
    lines.append("")
    if next_review.get("title"):
        lines.append(f"- title: `{next_review.get('title', '')}`")
        lines.append(f"- keyword: `{next_review.get('keyword', '')}`")
        lines.append(f"- ready_now: `{next_review.get('ready_now', False)}`")
        lines.append(f"- quality_status: `{next_review.get('quality_status', '')}`")
        lines.append(f"- draft_path: `{next_review.get('draft_path', '')}`")
        lines.append(f"- html_path: `{next_review.get('html_path', '')}`")
        if next_review.get("freshness_status"):
            lines.append(
                f"- freshness: `{next_review.get('freshness_status', '')}` / newest evidence age `{next_review.get('newest_evidence_age_days', '')}` days"
            )
        if next_review.get("freshness_summary"):
            lines.append(f"- freshness_summary: {next_review.get('freshness_summary', '')}")
        if next_review.get("freshness_recommendation"):
            lines.append(f"- freshness_recommendation: {next_review.get('freshness_recommendation', '')}")
        if next_review.get("hard_blocking_checks"):
            lines.append(f"- hard_blocking_checks: {', '.join(next_review.get('hard_blocking_checks', []))}")
        if next_review.get("next_action"):
            lines.append(f"- next_action: {next_review.get('next_action', '')}")
        if next_review.get("retention_cta_enabled"):
            retention_cta = next_review.get("retention_cta", {})
            lines.append(f"- final retention CTA: {retention_cta.get('inline_cta_now', '')}")
            if retention_cta.get("telegram_cta_later"):
                lines.append(f"- later revisit CTA: {retention_cta.get('telegram_cta_later', '')}")
        lines.append(f"- reply_example: {next_review.get('reply_example', '')}")
        if next_review.get("confirm_command"):
            lines.append(f"- confirm_command: `{next_review.get('confirm_command', '')}`")
        for text in next_review.get("excerpt", []):
            lines.append(f"- excerpt: {text}")
        for text in next_review.get("preview", []):
            lines.append(f"- preview: {text}")
    else:
        lines.append("- 아직 사용자에게 보여줄 우선 초안이 없습니다.")
    lines.append("")
    lines.append("## 다음 후보")
    lines.append("")
    for item in report.get("secondary_review", []):
        lines.append(
            f"- `{item.get('title', '')}` / keyword `{item.get('keyword', '')}` / ready `{item.get('ready_now', False)}` / quality `{item.get('quality_status', '')}` / freshness `{item.get('freshness_status', '')}`"
        )
        if item.get("hard_blocking_checks"):
            lines.append(f"  hard blockers: {', '.join(item.get('hard_blocking_checks', []))}")
        if item.get("next_action"):
            lines.append(f"  next action: {item.get('next_action', '')}")
    if not report.get("secondary_review"):
        lines.append("- none")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def render_paragraphs(items: list[str]) -> str:
    return "".join(f"<p>{html.escape(item)}</p>" for item in items)


def write_html(report: dict) -> None:
    next_review = report.get("next_review", {})
    secondary_items = report.get("secondary_review", [])
    secondary = "".join(
        f"<li><strong>{html.escape(item.get('title', ''))}</strong> · {html.escape(item.get('keyword', ''))} · ready {html.escape(str(item.get('ready_now', False)))}</li>"
        for item in secondary_items
    ) or "<li>다음 후보 없음</li>"

    html_text = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>User Review Checkpoint</title>
  <style>
    :root {{
      --bg: #f6f1e9;
      --panel: rgba(255, 252, 247, 0.95);
      --ink: #181714;
      --muted: #666258;
      --line: #ddd2c2;
      --accent: #8c3b31;
      --accent-soft: #f8e2db;
      --ok: #24594f;
      --ok-soft: #e0efea;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      color: var(--ink);
      font-family: "Avenir Next", "Pretendard", "Apple SD Gothic Neo", sans-serif;
      background:
        radial-gradient(circle at top left, rgba(140, 59, 49, 0.08), transparent 28%),
        radial-gradient(circle at bottom right, rgba(36, 89, 79, 0.08), transparent 24%),
        linear-gradient(180deg, #fbf8f2 0%, var(--bg) 100%);
    }}
    main {{
      max-width: 980px;
      margin: 0 auto;
      padding: 28px 18px 54px;
    }}
    .panel {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 24px;
      box-shadow: 0 18px 40px rgba(36, 28, 18, 0.07);
      padding: 22px;
      margin-bottom: 18px;
    }}
    h1 {{
      margin: 0 0 12px;
      font-size: clamp(2rem, 4vw, 3.2rem);
      line-height: 0.96;
      letter-spacing: -0.05em;
    }}
    .pill {{
      display: inline-flex;
      padding: 7px 12px;
      border-radius: 999px;
      font-size: 0.92rem;
      font-weight: 700;
      margin-right: 8px;
      margin-bottom: 8px;
    }}
    .blocked {{ background: var(--accent-soft); color: var(--accent); }}
    .open {{ background: var(--ok-soft); color: var(--ok); }}
    .paths, .muted {{ color: var(--muted); }}
    code {{
      display: block;
      padding: 12px 14px;
      border-radius: 14px;
      background: #fbf7f1;
      border: 1px solid var(--line);
      overflow-wrap: anywhere;
      font-size: 0.93rem;
    }}
    ul {{ padding-left: 20px; }}
  </style>
</head>
<body>
  <main>
    <section class="panel">
      <h1>User Review Checkpoint</h1>
      <p>{html.escape(report.get('guardrail', ''))}</p>
      <span class="pill {'blocked' if report.get('posting_blocked_until_user_confirmation') else 'open'}">
        {'posting blocked until you confirm' if report.get('posting_blocked_until_user_confirmation') else 'ready for next confirmed step'}
      </span>
      <span class="pill open">approved ready {html.escape(str(report.get('approved_ready_count', 0)))}</span>
      <p class="paths">current review focus: {html.escape(report.get('related_paths', {}).get('current_review_focus_html', ''))}</p>
      <p class="paths">user approval inbox: {html.escape(report.get('related_paths', {}).get('user_approval_inbox_html', ''))}</p>
      <p class="paths">source freshness board: {html.escape(report.get('related_paths', {}).get('source_freshness_board_html', ''))}</p>
    </section>
    <section class="panel">
      <h2>지금 먼저 보여줄 글</h2>
      <p><strong>{html.escape(next_review.get('title', '초안 없음'))}</strong> · {html.escape(next_review.get('keyword', ''))}</p>
      <p class="muted">ready {html.escape(str(next_review.get('ready_now', False)))} · quality {html.escape(next_review.get('quality_status', ''))}</p>
      {f"<p><strong>freshness</strong> · {html.escape(next_review.get('freshness_status', ''))} · newest evidence age {html.escape(str(next_review.get('newest_evidence_age_days', '')))} days</p>" if next_review.get('freshness_status') else ""}
      {f"<p class='muted'>{html.escape(next_review.get('freshness_recommendation', ''))}</p>" if next_review.get('freshness_recommendation') else ""}
      {f"<p><strong>next action</strong> · {html.escape(next_review.get('next_action', ''))}</p>" if next_review.get('next_action') else ""}
      {f"<p class='muted'>hard blockers · {html.escape(', '.join(next_review.get('hard_blocking_checks', [])))}</p>" if next_review.get('hard_blocking_checks') else ""}
      {f"<p><strong>final retention CTA</strong> · {html.escape((next_review.get('retention_cta') or {}).get('inline_cta_now', ''))}</p>" if next_review.get('retention_cta_enabled') and (next_review.get('retention_cta') or {}).get('inline_cta_now') else ""}
      {render_paragraphs(next_review.get("excerpt", []))}
      {render_paragraphs(next_review.get("preview", []))}
      <p><strong>reply example</strong></p>
      <code>{html.escape(next_review.get('reply_example', ''))}</code>
      {f"<p><strong>confirm command</strong></p><code>{html.escape(next_review.get('confirm_command', ''))}</code>" if next_review.get('confirm_command') else ""}
      <p class="paths">draft: {html.escape(next_review.get('draft_path', ''))}</p>
      <p class="paths">html: {html.escape(next_review.get('html_path', ''))}</p>
    </section>
    <section class="panel">
      <h2>다음 후보</h2>
      <ul>{secondary}</ul>
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
