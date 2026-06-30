#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
APPROVAL_HELPER = ROOT / "scripts/set_review_approvals.py"
USER_REVIEW_SHORTLIST_JSON = ROOT / "outputs/latest/user-review-shortlist.json"
PRE_PUBLISH_QUALITY_GATE_JSON = ROOT / "outputs/latest/pre-publish-quality-gate.json"
PLATFORM_PUBLISH_PLAN_JSON = ROOT / "outputs/latest/platform-publish-plan.json"
IMAGE_SELECTIONS_JSON = ROOT / "outputs/latest/image-selections.json"
FIRST_PUBLISH_OPERATOR_RUN_JSON = ROOT / "outputs/latest/first-publish-operator-run.json"
FIRST_APPROVAL_PATH_JSON = ROOT / "outputs/latest/first-approval-path.json"
FRESHNESS_JSON = ROOT / "outputs/latest/source-freshness-board.json"
OUTPUT_JSON = ROOT / "outputs/latest/shortlist-publish-action-board.json"
OUTPUT_MD = ROOT / "outputs/latest/shortlist-publish-action-board.md"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def build_lookup(items: list[dict], key: str) -> dict:
    return {item.get(key): item for item in items if item.get(key)}


def selected_image_lookup() -> set[str]:
    payload = load_json(IMAGE_SELECTIONS_JSON)
    selected = set()
    for item in payload.get("items", []):
        if item.get("slot") == "hero" and item.get("approved") and item.get("selected_url"):
            selected.add(item.get("keyword", ""))
    return selected


def build_report() -> dict:
    shortlist = load_json(USER_REVIEW_SHORTLIST_JSON)
    quality_gate = load_json(PRE_PUBLISH_QUALITY_GATE_JSON)
    publish_plan = load_json(PLATFORM_PUBLISH_PLAN_JSON)
    operator_run = load_json(FIRST_PUBLISH_OPERATOR_RUN_JSON)
    approval_path = load_json(FIRST_APPROVAL_PATH_JSON)
    freshness_board = load_json(FRESHNESS_JSON)

    quality_lookup = build_lookup(quality_gate.get("items", []), "keyword")
    freshness_lookup = build_lookup(freshness_board.get("items", []), "keyword")
    selected_images = selected_image_lookup()
    blogger = next((channel for channel in publish_plan.get("channels", []) if channel.get("name") == "blogger"), {})
    single_recommended_keyword = (approval_path.get("recommended_single") or {}).get("keyword", "")
    single_confirm_command = (approval_path.get("recommended_single") or {}).get("approval_command", "") or shortlist.get("single_approval_command", "")
    batch_confirm_command = shortlist.get("batch_approval_command", "")
    planned_commands = operator_run.get("planned_commands", [])
    after_confirm_commands = planned_commands[1:] if len(planned_commands) > 1 else []

    items = []
    for card in shortlist.get("shortlist", []):
        keyword = card.get("keyword", "")
        quality_item = quality_lookup.get(keyword, {})
        failed_checks = [check for check in quality_item.get("checks", []) if not check.get("ok")]
        failed_names = [check.get("name", "") for check in failed_checks]
        hard_blocking_names = []
        if quality_item.get("status") == "review_before_publish":
            for name in failed_names:
                if name == "hero_image_selected":
                    hard_blocking_names.append(name)
        freshness = freshness_lookup.get(keyword, {})
        freshness_status = freshness.get("freshness_status", "")
        if freshness_status == "stale":
            hard_blocking_names.append("source_freshness_stale")

        item_single_confirm_command = f"python3 {APPROVAL_HELPER} --keywords {keyword}" if keyword else ""
        confirm_command = item_single_confirm_command
        if not confirm_command and keyword == single_recommended_keyword:
            confirm_command = single_confirm_command
        if not confirm_command and batch_confirm_command and keyword == single_recommended_keyword:
            confirm_command = batch_confirm_command

        next_action = "사용자 최종 확인 후 업로드"
        next_command = confirm_command
        followup_commands = after_confirm_commands

        if freshness_status == "stale":
            next_action = "데일리 뉴스형 대신 evergreen 후속 글 또는 refresh 경로로 전환"
            next_command = freshness.get("recovery_confirm_command", "") or freshness.get("recovery_command", "")
            followup_commands = [command for command in [freshness.get("recovery_image_apply_helper", ""), "bash scripts/run_pipeline.sh"] if command]
        elif "hero_image_selected" in hard_blocking_names:
            next_action = "대표 이미지 먼저 선택"
            next_command = card.get("hero_image_apply_helper", "")
            followup_commands = [
                "bash scripts/run_pipeline.sh",
                confirm_command,
            ] + after_confirm_commands
        elif quality_item.get("status") == "pass":
            next_action = "사용자 최종 확인 후 Blogger draft 업로드"
            next_command = confirm_command

        items.append(
            {
                "keyword": keyword,
                "title": card.get("title", ""),
                "publish_date": card.get("publish_date", ""),
                "quality_status": quality_item.get("status", card.get("quality_status", "")),
                "ready_now": card.get("ready_now", False),
                "hero_image_selected": keyword in selected_images or card.get("hero_image_selected", False),
                "freshness_status": freshness_status,
                "freshness_recommendation": freshness.get("recommendation", ""),
                "recovery_mode": freshness.get("recovery_mode", ""),
                "recovery_title": freshness.get("recovery_title", ""),
                "recovery_confirm_command": freshness.get("recovery_confirm_command", ""),
                "recovery_image_search_url": freshness.get("recovery_image_search_url", ""),
                "recovery_image_search_query": freshness.get("recovery_image_search_query", ""),
                "recovery_image_apply_helper": freshness.get("recovery_image_apply_helper", ""),
                "hard_blocking_checks": hard_blocking_names,
                "advisory_checks": [name for name in failed_names if name not in hard_blocking_names],
                "confirm_command": confirm_command,
                "next_action": next_action,
                "next_command": next_command,
                "followup_commands": followup_commands,
                "helper_preview_command": f"python3 scripts/run_shortlist_keyword_flow.py --keyword {keyword}",
                "helper_apply_command": (
                    f"python3 scripts/run_shortlist_keyword_flow.py --keyword {keyword} --image-url <IMAGE_URL> --image-credit \"Photo by ...\" --apply"
                    if "hero_image_selected" in hard_blocking_names
                    else f"python3 scripts/run_shortlist_keyword_flow.py --keyword {keyword} --apply"
                ),
                "blogger_ready": blogger.get("ready", False),
            }
        )

    return {
        "item_count": len(items),
        "blogger_ready": blogger.get("ready", False),
        "user_confirmed_keywords": publish_plan.get("user_confirmed_keywords", []),
        "items": items,
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# Shortlist Publish Action Board")
    lines.append("")
    lines.append("shortlist 글 기준으로 지금 남은 blocker와 다음 한 줄 실행만 따로 뽑은 보드입니다.")
    lines.append(f"- blogger_ready: `{report.get('blogger_ready', False)}`")
    lines.append(f"- user_confirmed_keywords: `{json.dumps(report.get('user_confirmed_keywords', []), ensure_ascii=False)}`")
    lines.append(f"- item_count: `{report.get('item_count', 0)}`")
    lines.append("")

    for index, item in enumerate(report.get("items", []), start=1):
        lines.append(f"## {index}. {item.get('title', '')}")
        lines.append("")
        lines.append(f"- keyword: `{item.get('keyword', '')}`")
        lines.append(f"- publish_date: `{item.get('publish_date', '')}`")
        lines.append(f"- quality_status: `{item.get('quality_status', '')}`")
        lines.append(f"- ready_now: `{item.get('ready_now', False)}`")
        lines.append(f"- hero_image_selected: `{item.get('hero_image_selected', False)}`")
        if item.get("freshness_status"):
            lines.append(f"- freshness_status: `{item.get('freshness_status', '')}`")
        if item.get("freshness_recommendation"):
            lines.append(f"- freshness_recommendation: {item.get('freshness_recommendation', '')}")
        if item.get("hard_blocking_checks"):
            lines.append(f"- hard_blocking_checks: {', '.join(item.get('hard_blocking_checks', []))}")
        else:
            lines.append("- hard_blocking_checks: none")
        if item.get("advisory_checks"):
            lines.append(f"- advisory_checks: {', '.join(item.get('advisory_checks', []))}")
        if item.get("recovery_mode"):
            lines.append(f"- recovery_mode: `{item.get('recovery_mode', '')}`")
        if item.get("recovery_title"):
            lines.append(f"- recovery_title: {item.get('recovery_title', '')}")
        if item.get("recovery_confirm_command"):
            lines.append(f"- recovery_confirm_command: `{item.get('recovery_confirm_command', '')}`")
        if item.get("recovery_image_search_url"):
            lines.append(
                f"- recovery_image_search: `{item.get('recovery_image_search_query', '')}` / {item.get('recovery_image_search_url', '')}"
            )
        if item.get("recovery_image_apply_helper"):
            lines.append(f"- recovery_image_apply_helper: `{item.get('recovery_image_apply_helper', '')}`")
        if item.get("confirm_command"):
            lines.append(f"- confirm_command: `{item.get('confirm_command', '')}`")
        lines.append(f"- next_action: {item.get('next_action', '')}")
        if item.get("next_command"):
            lines.append(f"- next_command: `{item.get('next_command', '')}`")
        if item.get("followup_commands"):
            lines.append("- followup_commands:")
            for command in item.get("followup_commands", []):
                lines.append(f"  - `{command}`")
        if item.get("helper_preview_command"):
            lines.append(f"- helper_preview_command: `{item.get('helper_preview_command', '')}`")
        if item.get("helper_apply_command"):
            lines.append(f"- helper_apply_command: `{item.get('helper_apply_command', '')}`")
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
