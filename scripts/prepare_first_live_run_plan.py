#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SETUP_JSON = ROOT / "outputs/latest/setup-check-report.json"
GO_LIVE_JSON = ROOT / "outputs/latest/go-live-readiness-report.json"
PUBLISH_INVENTORY_JSON = ROOT / "outputs/latest/publish-inventory.json"
BLOGGER_UPLOAD_JSON = ROOT / "outputs/latest/blogger-upload-report.json"
OUTPUT_JSON = ROOT / "outputs/latest/first-live-run-plan.json"
OUTPUT_MD = ROOT / "outputs/latest/first-live-run-plan.md"

SAFE_MODE_ENV = {
    "BLOGGER_SYNC_SITE_PAGES": "true",
    "BLOGGER_SITE_PAGES_PUBLISH": "false",
    "BLOGGER_AUTO_PUBLISH_POSTS": "false",
    "BLOGGER_PUBLISH_ONLY_DUE_POSTS": "true",
    "BLOGGER_MAX_POSTS_PER_RUN": "1",
}
LIVE_REQUIRED_CREDENTIALS = ["BLOGGER_BLOG_ID", "GOOGLE_CLIENT_ID", "GOOGLE_CLIENT_SECRET", "GOOGLE_REFRESH_TOKEN"]
OPTIONAL_CREDENTIALS = ["OPENAI_API_KEY"]


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def env_lookup(setup: dict) -> set[str]:
    return set(setup.get("env_keys_filled", []))


def build_status(setup: dict, go_live: dict) -> str:
    env_keys = env_lookup(setup)
    required = [key for key in LIVE_REQUIRED_CREDENTIALS]
    missing = [key for key in required if key not in env_keys]
    if missing:
        return "awaiting_credentials"
    if not go_live.get("ready_for_first_live_run", False):
        return "needs_preflight_review"
    return "ready_for_draft_test"


def build_plan() -> dict:
    setup = load_json(SETUP_JSON)
    go_live = load_json(GO_LIVE_JSON)
    inventory = load_json(PUBLISH_INVENTORY_JSON)
    blogger_report = load_json(BLOGGER_UPLOAD_JSON)
    env_keys = env_lookup(setup)
    required = [key for key in LIVE_REQUIRED_CREDENTIALS]
    missing = [key for key in required if key not in env_keys]
    optional_missing = [key for key in OPTIONAL_CREDENTIALS if key not in env_keys]

    ready_items = [item for item in inventory.get("items", []) if item.get("ready_to_upload")]
    first_post = ready_items[0] if ready_items else {}
    followups = ready_items[1:4]
    dry_run_summary = blogger_report.get("summary", {})
    dry_run_items = blogger_report.get("items", [])
    first_dry_run = dry_run_items[0] if dry_run_items else {}

    steps = [
        {
            "phase": "credentials",
            "title": "필수 계정 연결",
            "done": not missing,
            "details": (
                missing
                if missing
                else [
                    "필수 자격값이 모두 채워졌습니다.",
                    "참고: `OPENAI_API_KEY`는 없더라도 템플릿 fallback 초안으로 테스트 업로드가 가능합니다.",
                ]
            ),
        },
        {
            "phase": "safe_mode",
            "title": "안전모드 유지",
            "done": True,
            "details": [f"{key}={value}" for key, value in SAFE_MODE_ENV.items()],
        },
        {
            "phase": "first_upload",
            "title": "첫 테스트 업로드",
            "done": False,
            "details": [
                f"대상 글: {first_post.get('title', '없음')}",
                f"업로드 유형: {first_post.get('inventory_type', 'n/a')}",
                "권장 액션: Blogger 초안으로 1개만 업로드 후 화면 검수",
            ],
        },
        {
            "phase": "review",
            "title": "Blogger 화면 검수",
            "done": False,
            "details": [
                "제목/본문/라벨/내부링크가 정상인지 확인",
                "고정 페이지가 draft 상태로 잘 들어가는지 확인",
                "문제 없으면 다음날부터 max_posts_per_run을 2~3으로 점진 확대",
            ],
        },
    ]

    return {
        "status": build_status(setup, go_live),
        "required_credentials_missing": missing,
        "optional_credentials_missing": optional_missing,
        "safe_mode_env": SAFE_MODE_ENV,
        "dry_run_summary": {
            "reason": blogger_report.get("reason", ""),
            "manifest_candidate_count": dry_run_summary.get("manifest_candidate_count", 0),
            "processed_count": dry_run_summary.get("processed_count", 0),
            "max_posts_per_run": dry_run_summary.get("max_posts_per_run", SAFE_MODE_ENV["BLOGGER_MAX_POSTS_PER_RUN"]),
            "first_item_reason": first_dry_run.get("reason", ""),
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
        for key in missing:
            lines.append(f"- `{key}`")
    else:
        lines.append("- 모든 필수 자격값이 준비되었습니다.")
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
    lines.append(f"- reason: `{plan.get('dry_run_summary', {}).get('reason', '')}`")
    lines.append(f"- first_item_reason: `{plan.get('dry_run_summary', {}).get('first_item_reason', '')}`")
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
    lines.append("- `python3 scripts/upload_blogger_drafts.py`")
    lines.append("- 실행 전 Blogger/Google OAuth 값이 `.env`에 들어가 있어야 합니다.")
    OUTPUT_MD.write_text("\n".join(lines) + "\n")


def main() -> int:
    plan = build_plan()
    OUTPUT_JSON.write_text(json.dumps(plan, ensure_ascii=False, indent=2))
    write_markdown(plan)
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
