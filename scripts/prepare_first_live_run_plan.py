#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SETUP_JSON = ROOT / "outputs/latest/setup-check-report.json"
GO_LIVE_JSON = ROOT / "outputs/latest/go-live-readiness-report.json"
PUBLISH_INVENTORY_JSON = ROOT / "outputs/latest/publish-inventory.json"
SOURCE_FRESHNESS_JSON = ROOT / "outputs/latest/source-freshness-board.json"
BLOGGER_UPLOAD_JSON = ROOT / "outputs/latest/blogger-upload-report.json"
WORDPRESS_UPLOAD_JSON = ROOT / "outputs/latest/wordpress-upload-report.json"
PLATFORM_PUBLISH_PLAN_JSON = ROOT / "outputs/latest/platform-publish-plan.json"
OUTPUT_JSON = ROOT / "outputs/latest/first-live-run-plan.json"
OUTPUT_MD = ROOT / "outputs/latest/first-live-run-plan.md"
ENV_PATH = ROOT / ".env"

DEFAULT_SAFE_MODE_ENV = {
    "BLOGGER_SYNC_SITE_PAGES": "false",
    "BLOGGER_SITE_PAGES_PUBLISH": "false",
    "BLOGGER_AUTO_PUBLISH_POSTS": "false",
    "BLOGGER_PUBLISH_ONLY_DUE_POSTS": "true",
    "BLOGGER_MAX_POSTS_PER_RUN": "1",
    "WORDPRESS_AUTO_PUBLISH_POSTS": "false",
    "WORDPRESS_PUBLISH_ONLY_DUE_POSTS": "true",
    "WORDPRESS_MAX_POSTS_PER_RUN": "1",
}
BLOGGER_REQUIRED_CREDENTIALS = ["BLOGGER_BLOG_ID", "GOOGLE_CLIENT_ID", "GOOGLE_CLIENT_SECRET", "GOOGLE_REFRESH_TOKEN"]
WORDPRESS_REQUIRED_CREDENTIALS = ["WORDPRESS_SITE_URL", "WORDPRESS_USERNAME", "WORDPRESS_APPLICATION_PASSWORD"]
OPTIONAL_CREDENTIALS = ["OPENAI_API_KEY"]


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def env_lookup(setup: dict) -> set[str]:
    return set(setup.get("env_keys_filled", []))


def parse_env(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    if not path.exists():
        return values
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip().strip("'").strip('"')
    return values


def load_freshness_map() -> dict[str, str]:
    if not SOURCE_FRESHNESS_JSON.exists():
        return {}
    payload = load_json(SOURCE_FRESHNESS_JSON)
    return {
        item.get("keyword"): item.get("freshness_status", "unknown")
        for item in payload.get("items", [])
    }


def build_status(setup: dict, go_live: dict) -> str:
    env_keys = env_lookup(setup)
    blogger_ready = all(key in env_keys for key in BLOGGER_REQUIRED_CREDENTIALS)
    wordpress_ready = all(key in env_keys for key in WORDPRESS_REQUIRED_CREDENTIALS)
    if not blogger_ready and not wordpress_ready:
        return "awaiting_credentials"
    if not go_live.get("ready_for_first_live_run", False):
        return "needs_preflight_review"
    return "ready_for_draft_test"


def build_plan() -> dict:
    setup = load_json(SETUP_JSON)
    go_live = load_json(GO_LIVE_JSON)
    inventory = load_json(PUBLISH_INVENTORY_JSON)
    freshness_map = load_freshness_map()
    platform_plan = load_json(PLATFORM_PUBLISH_PLAN_JSON)
    blogger_report = load_json(BLOGGER_UPLOAD_JSON)
    wordpress_report = load_json(WORDPRESS_UPLOAD_JSON)
    env_keys = env_lookup(setup)
    blogger_missing = [key for key in BLOGGER_REQUIRED_CREDENTIALS if key not in env_keys]
    wordpress_missing = [key for key in WORDPRESS_REQUIRED_CREDENTIALS if key not in env_keys]
    missing = [] if (not blogger_missing or not wordpress_missing) else sorted(set(blogger_missing + wordpress_missing))
    optional_missing = [key for key in OPTIONAL_CREDENTIALS if key not in env_keys]
    env_values = parse_env(ENV_PATH)
    safe_mode_env = {
        key: env_values.get(key, default)
        for key, default in DEFAULT_SAFE_MODE_ENV.items()
    }

    ready_items = [item for item in inventory.get("items", []) if item.get("ready_to_upload")]
    followups = []
    first_post = {}

    # Keep first live candidate aligned with the real upload plan, so UI commands and runbooks are consistent.
    channels = platform_plan.get("channels", [])
    primary_channel = "none"
    blogger_ready = not blogger_missing
    wordpress_ready = not wordpress_missing
    if blogger_ready:
        primary_channel = "blogger"
    elif wordpress_ready:
        primary_channel = "wordpress"

    for channel in channels:
        if channel.get("name") == primary_channel and channel.get("ready") and channel.get("first_item"):
            first_post = channel.get("first_item", {})
            if channel.get("items"):
                followups = [item for item in channel.get("items", [])[1:4] if item.get("ready_to_upload", False)]
            break

    if not first_post and primary_channel == "blogger" and channels:
        # Fallback to platform plan ordering even when the first channel has no explicit first_item.
        all_candidates = []
        for channel in channels:
            if not channel.get("ready"):
                continue
            all_candidates.extend(channel.get("items", []))
        if all_candidates:
            def _freshness_value(item: dict) -> tuple[int, int]:
                status = freshness_map.get(item.get("keyword"), item.get("freshness_status", "unknown"))
                # prefer fresh > aging > unknown > stale so stale content does not lead.
                rank = {"fresh": 0, "aging": 1, "unknown": 2, "stale": 3}.get(status, 2)
                return rank, -int(item.get("priority_score", 0))

            ranked_candidates = sorted(all_candidates, key=_freshness_value)
            # preserve fallback path for edge cases where all candidates are stale
            first_post = ranked_candidates[0]
            followups = [item for item in ranked_candidates[1:4] if item.get("ready_to_upload", False)]
    if not first_post and ready_items:
        def _freshness_value_from_inventory(item: dict) -> tuple[int, int]:
            status = freshness_map.get(item.get("keyword"), item.get("freshness_status", "unknown"))
            rank = {"fresh": 0, "aging": 1, "unknown": 2, "stale": 3}.get(status, 2)
            return rank, -int(item.get("priority_score", 0))

        ranked_ready = sorted(ready_items, key=_freshness_value_from_inventory)
        first_post = ranked_ready[0]
        followups = [item for item in ranked_ready[1:4] if item.get("ready_to_upload", False)]
    dry_run_summary = blogger_report.get("summary", {})
    dry_run_items = blogger_report.get("items", [])
    first_dry_run = dry_run_items[0] if dry_run_items else {}
    wordpress_dry_run_summary = wordpress_report.get("summary", {})
    wordpress_dry_run_items = wordpress_report.get("items", [])
    wordpress_first_dry_run = wordpress_dry_run_items[0] if wordpress_dry_run_items else {}
    steps = [
        {
            "phase": "credentials",
            "title": "자동 채널 1개 이상 연결",
            "done": blogger_ready or wordpress_ready,
            "details": (
                [
                    f"Blogger missing: {', '.join(blogger_missing) if blogger_missing else 'none'}",
                    f"WordPress missing: {', '.join(wordpress_missing) if wordpress_missing else 'none'}",
                ]
                if not (blogger_ready or wordpress_ready)
                else [
                    f"자동 채널 준비 상태: blogger={blogger_ready}, wordpress={wordpress_ready}",
                    "참고: `OPENAI_API_KEY`는 없더라도 템플릿 fallback 초안으로 테스트 업로드가 가능합니다.",
                ]
            ),
        },
        {
            "phase": "safe_mode",
            "title": "안전모드 유지",
            "done": True,
            "details": [f"{key}={value}" for key, value in safe_mode_env.items()],
        },
        {
            "phase": "first_upload",
            "title": "첫 테스트 업로드",
            "done": False,
            "details": [
                f"대상 글: {first_post.get('title', '없음')}",
                f"업로드 유형: {first_post.get('inventory_type', 'n/a')}",
                f"권장 채널: {primary_channel}",
                "권장 액션: Blogger에서 초안 1개만 업로드 후 화면 검수",
            ],
        },
        {
            "phase": "review",
            "title": "발행 화면 검수",
            "done": False,
            "details": [
                "제목/본문/라벨/내부링크가 정상인지 확인",
                "Blogger를 쓰는 경우 고정 페이지가 draft 상태로 잘 들어가는지 확인",
                "문제 없으면 다음날부터 max_posts_per_run을 2~3으로 점진 확대",
            ],
        },
    ]

    return {
        "status": build_status(setup, go_live),
        "required_credentials_missing": missing,
        "channel_missing": {
            "blogger": blogger_missing,
            "wordpress": wordpress_missing,
        },
        "primary_channel": primary_channel,
        "optional_credentials_missing": optional_missing,
            "safe_mode_env": safe_mode_env,
        "dry_run_summary": {
            "reason": blogger_report.get("reason", ""),
            "manifest_candidate_count": dry_run_summary.get("manifest_candidate_count", 0),
            "processed_count": dry_run_summary.get("processed_count", 0),
            "max_posts_per_run": dry_run_summary.get("max_posts_per_run", safe_mode_env["BLOGGER_MAX_POSTS_PER_RUN"]),
            "first_item_reason": first_dry_run.get("reason", ""),
        },
        "wordpress_dry_run_summary": {
            "reason": wordpress_report.get("reason", ""),
            "manifest_candidate_count": wordpress_dry_run_summary.get("manifest_candidate_count", 0),
            "processed_count": wordpress_dry_run_summary.get("processed_count", 0),
            "max_posts_per_run": wordpress_dry_run_summary.get(
                "max_posts_per_run", safe_mode_env["WORDPRESS_MAX_POSTS_PER_RUN"]
            ),
            "first_item_reason": wordpress_first_dry_run.get("reason", ""),
        },
        "first_post_candidate": first_post,
        "next_post_candidates": followups,
        "steps": steps,
    }


def write_markdown(plan: dict) -> None:
    lines = []
    lines.append("# First Live Run Plan")
    lines.append("")
    lines.append(f"- status: `{plan.get('status', 'unknown')}`")
    lines.append(f"- missing_credentials_count: `{len(plan.get('required_credentials_missing', []))}`")
    lines.append(f"- manifest_candidate_count: `{plan.get('dry_run_summary', {}).get('manifest_candidate_count', 0)}`")
    lines.append(f"- max_posts_per_run: `{plan.get('dry_run_summary', {}).get('max_posts_per_run', 0)}`")
    lines.append("")
    lines.append("## Missing Credentials")
    lines.append("")
    missing = plan.get("required_credentials_missing", [])
    if missing:
        lines.append(f"- primary_channel_recommended: `{plan.get('primary_channel', 'none')}`")
        for channel, keys in (plan.get("channel_missing") or {}).items():
            lines.append(f"- `{channel}` missing: {', '.join(keys) if keys else 'none'}")
    else:
        lines.append("- 자동 채널 최소 1개 이상 준비되었습니다.")
    missing_optional = plan.get("optional_credentials_missing", [])
    if missing_optional:
        lines.append("")
        lines.append("## Optional Credentials")
        for key in missing_optional:
            lines.append(f"- `{key}` (문구 품질 향상)")
    lines.append("")
    lines.append("## Safe Mode Env")
    lines.append("")
    for key, value in plan.get("safe_mode_env", {}).items():
        lines.append(f"- `{key}={value}`")
    lines.append("")
    lines.append("## First Upload Candidate")
    lines.append("")
    first_post = plan.get("first_post_candidate", {})
    if first_post:
        lines.append(f"- title: `{first_post.get('title', '')}`")
        lines.append(f"- inventory_type: `{first_post.get('inventory_type', '')}`")
        lines.append(f"- publish_date: `{first_post.get('publish_date', '')}`")
        lines.append(f"- priority_score: `{first_post.get('priority_score', '')}`")
        lines.append(f"- cta_focus: {first_post.get('cta_focus', '')}")
    else:
        lines.append("- 아직 업로드 가능한 글이 없습니다.")
    lines.append("")
    lines.append("## Next Candidates")
    lines.append("")
    next_candidates = plan.get("next_post_candidates", [])
    if next_candidates:
        for item in next_candidates:
            lines.append(
                f"- `{item.get('title', '')}` / {item.get('inventory_type', '')} / score {item.get('priority_score', '')}"
            )
    else:
        lines.append("- 다음 후보가 아직 없습니다.")
    lines.append("")
    lines.append("## Dry Run Snapshot")
    lines.append("")
    lines.append(f"- blogger_reason: `{plan.get('dry_run_summary', {}).get('reason', '')}`")
    lines.append(f"- blogger_first_item_reason: `{plan.get('dry_run_summary', {}).get('first_item_reason', '')}`")
    lines.append(f"- wordpress_reason: `{plan.get('wordpress_dry_run_summary', {}).get('reason', '')}`")
    lines.append(f"- wordpress_first_item_reason: `{plan.get('wordpress_dry_run_summary', {}).get('first_item_reason', '')}`")
    lines.append("")
    lines.append("## Step Sequence")
    lines.append("")
    for index, step in enumerate(plan.get("steps", []), start=1):
        state = "done" if step.get("done") else "pending"
        lines.append(f"{index}. {step.get('title')} [{state}]")
        for detail in step.get("details", []):
            lines.append(f"   - {detail}")
    lines.append("")
    lines.append("## Recommended Command")
    lines.append("")
    if plan.get("primary_channel") == "blogger":
        lines.append("- `python3 scripts/upload_blogger_drafts.py`")
        lines.append("- 실행 전 Blogger/Google OAuth 값이 `.env`에 들어가 있어야 합니다.")
    elif plan.get("primary_channel") == "wordpress":
        lines.append("- `python3 scripts/upload_wordpress_drafts.py`")
        lines.append("- 실행 전 WordPress 사이트/계정/Application Password가 `.env`에 들어가 있어야 합니다.")
    else:
        lines.append("- Blogger 또는 WordPress 중 하나의 자격값을 먼저 채운 뒤 다시 생성하세요.")
    OUTPUT_MD.write_text("\n".join(lines) + "\n")


def main() -> int:
    plan = build_plan()
    OUTPUT_JSON.write_text(json.dumps(plan, ensure_ascii=False, indent=2))
    write_markdown(plan)
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
