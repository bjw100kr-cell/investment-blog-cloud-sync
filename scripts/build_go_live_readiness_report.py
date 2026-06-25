#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SETUP_JSON = ROOT / "outputs/latest/setup-check-report.json"
PUBLISH_QUEUE_JSON = ROOT / "outputs/latest/publish-queue.json"
SITE_PAGE_PLAN_JSON = ROOT / "outputs/latest/site-page-publish-plan.json"
MONETIZATION_JSON = ROOT / "outputs/latest/monetization-readiness-report.json"
OUTPUT_JSON = ROOT / "outputs/latest/go-live-readiness-report.json"
OUTPUT_MD = ROOT / "outputs/latest/go-live-readiness-report.md"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def integration_lookup(setup: dict) -> dict:
    return {item.get("name"): item for item in setup.get("integrations", [])}


def filled_env_keys(setup: dict) -> set[str]:
    filled = setup.get("env_keys_filled")
    if isinstance(filled, list):
        return set(filled)
    return set(setup.get("env_keys_present", []))


def build_report() -> dict:
    setup = load_json(SETUP_JSON)
    queue = load_json(PUBLISH_QUEUE_JSON)
    site_plan = load_json(SITE_PAGE_PLAN_JSON)
    monetization = load_json(MONETIZATION_JSON)

    integrations = integration_lookup(setup)
    env_filled = filled_env_keys(setup)
    site_items = site_plan.get("items", [])
    required_site_items = [item for item in site_items if item.get("visibility") == "public_required"]
    ready_site_items = [item for item in required_site_items if Path(item.get("html_path", "")).exists()]
    queue_items = queue.get("items", [])
    ready_posts = [item for item in queue_items if item.get("ready_to_upload")]

    required_credentials = []
    for key in ["OPENAI_API_KEY", "BLOGGER_BLOG_ID", "GOOGLE_CLIENT_ID", "GOOGLE_CLIENT_SECRET", "GOOGLE_REFRESH_TOKEN"]:
        if key not in env_filled:
            required_credentials.append(key)

    optional_growth_keys = []
    for key in [
        "SEARCH_CONSOLE_SITE_URL",
        "SEARCH_CONSOLE_CLIENT_ID",
        "SEARCH_CONSOLE_CLIENT_SECRET",
        "SEARCH_CONSOLE_REFRESH_TOKEN",
        "GA4_MEASUREMENT_ID",
        "ADSENSE_PUBLISHER_ID",
        "ADSENSE_SITE_VERIFICATION",
        "NEWSLETTER_SUBSCRIBE_URL",
    ]:
        if key not in env_filled:
            optional_growth_keys.append(key)

    # OpenAI is optional for the first publish run because local fallback draft generation
    # can still produce publish-ready posts when OPENAI_API_KEY is missing.
    draft_engine_ready = integrations.get("openai_drafts", {}).get("ready", False) or bool(ready_posts)

    live_prerequisites = {
        "site_pages_html_ready": len(ready_site_items) == len(required_site_items) and bool(required_site_items),
        "blog_posts_ready": bool(ready_posts),
        "blogger_connection_ready": integrations.get("blogger_upload", {}).get("ready", False),
        "draft_engine_ready": draft_engine_ready,
        "git_remote_ready": setup.get("git", {}).get("origin") not in {"", "(not configured)"},
    }

    ready_for_first_live_run = all(
        [
            live_prerequisites["site_pages_html_ready"],
            live_prerequisites["blog_posts_ready"],
            live_prerequisites["blogger_connection_ready"],
            live_prerequisites["draft_engine_ready"],
        ]
    )

    return {
        "ready_for_first_live_run": ready_for_first_live_run,
        "live_prerequisites": live_prerequisites,
        "site_pages": {
            "required_count": len(required_site_items),
            "ready_count": len(ready_site_items),
            "top_sequence": [item.get("slug") for item in required_site_items[:5]],
        },
        "posts": {
            "ready_count": len(ready_posts),
            "top_keywords": [item.get("keyword") for item in ready_posts[:3]],
        },
        "required_credentials": required_credentials,
        "optional_growth_keys": optional_growth_keys,
        "monetization_score": monetization.get("readiness_score", 0),
        "next_steps": [
            "Blogger와 Google OAuth 값을 연결합니다.",
            "신뢰 페이지를 먼저 Blogger Pages로 동기화합니다.",
            "publish queue 상위 글을 Blogger draft로 업로드합니다.",
            "GitHub 원격 저장소와 Actions Secrets/Variables를 연결합니다.",
        ],
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# Go Live Readiness Report")
    lines.append("")
    lines.append(f"- first live run ready: `{report.get('ready_for_first_live_run', False)}`")
    lines.append(f"- monetization score: `{report.get('monetization_score', 0)}`")
    lines.append("")
    lines.append("## Live Prerequisites")
    lines.append("")
    for key, value in report.get("live_prerequisites", {}).items():
        lines.append(f"- `{key}`: {value}")
    lines.append("")
    lines.append("## Site Pages")
    lines.append("")
    lines.append(
        f"- required ready: `{report.get('site_pages', {}).get('ready_count', 0)}` / `{report.get('site_pages', {}).get('required_count', 0)}`"
    )
    for slug in report.get("site_pages", {}).get("top_sequence", []):
        lines.append(f"- first publish target: `{slug}`")
    lines.append("")
    lines.append("## Posts")
    lines.append("")
    lines.append(f"- ready posts: `{report.get('posts', {}).get('ready_count', 0)}`")
    for keyword in report.get("posts", {}).get("top_keywords", []):
        lines.append(f"- first draft upload target: `{keyword}`")
    lines.append("")
    lines.append("## Required Credentials")
    lines.append("")
    for key in report.get("required_credentials", []):
        lines.append(f"- `{key}`")
    lines.append("")
    lines.append("## Optional Growth Keys")
    lines.append("")
    for key in report.get("optional_growth_keys", []):
        lines.append(f"- `{key}`")
    lines.append("")
    lines.append("## Next Steps")
    lines.append("")
    for step in report.get("next_steps", []):
        lines.append(f"- {step}")
    lines.append("")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def main() -> int:
    report = build_report()
    OUTPUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    write_markdown(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
