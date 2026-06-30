#!/usr/bin/env python3
import json
import os
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ENV_PATH = ROOT / ".env"
ENV_EXAMPLE_PATH = ROOT / ".env.example"
OUTPUT_DIR = ROOT / "outputs/latest"
REPORT_PATH = ROOT / "outputs/latest/setup-check-report.json"
PUBLISH_READY_REPORT = ROOT / "outputs/latest/publish-ready-report.json"
SITE_PAGE_PLAN_REPORT = ROOT / "outputs/latest/site-page-publish-plan.json"
GO_LIVE_REPORT = ROOT / "outputs/latest/go-live-readiness-report.json"

INTEGRATIONS = {
    "naver_datalab": ["NAVER_CLIENT_ID", "NAVER_CLIENT_SECRET"],
    "search_console": [
        "SEARCH_CONSOLE_SITE_URL",
        "SEARCH_CONSOLE_CLIENT_ID",
        "SEARCH_CONSOLE_CLIENT_SECRET",
        "SEARCH_CONSOLE_REFRESH_TOKEN",
    ],
    "openai_drafts": ["OPENAI_API_KEY"],
    "blogger_upload": [
        "BLOGGER_BLOG_ID",
        "GOOGLE_CLIENT_ID",
        "GOOGLE_CLIENT_SECRET",
        "GOOGLE_REFRESH_TOKEN",
    ],
    "wordpress_upload": [
        "WORDPRESS_SITE_URL",
        "WORDPRESS_USERNAME",
        "WORDPRESS_APPLICATION_PASSWORD",
    ],
}


def parse_env_file(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    if not path.exists():
        return values

    for raw_line in path.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip().strip("'").strip('"')
    return values


def git_value(args: list[str]) -> str:
    try:
        completed = subprocess.run(
            ["git", *args],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
    except Exception:
        return ""
    return completed.stdout.strip()


def mask(value: str) -> str:
    if not value:
        return ""
    if len(value) <= 6:
        return "*" * len(value)
    return f"{value[:3]}***{value[-2:]}"


def integration_status(env_values: dict[str, str]) -> list[dict]:
    items = []
    for name, required_keys in INTEGRATIONS.items():
        if name == "search_console":
            site_ready = bool(
                env_values.get("SEARCH_CONSOLE_SITE_URL")
                or env_values.get("BLOG_BASE_URL")
                or env_values.get("BLOGGER_PUBLIC_URL")
            )
            client_ready = bool(env_values.get("SEARCH_CONSOLE_CLIENT_ID") or env_values.get("GOOGLE_CLIENT_ID"))
            secret_ready = bool(env_values.get("SEARCH_CONSOLE_CLIENT_SECRET") or env_values.get("GOOGLE_CLIENT_SECRET"))
            refresh_ready = bool(env_values.get("SEARCH_CONSOLE_REFRESH_TOKEN") or env_values.get("GOOGLE_REFRESH_TOKEN"))
            missing = []
            if not site_ready:
                missing.append("SEARCH_CONSOLE_SITE_URL or BLOG_BASE_URL")
            if not client_ready:
                missing.append("SEARCH_CONSOLE_CLIENT_ID or GOOGLE_CLIENT_ID")
            if not secret_ready:
                missing.append("SEARCH_CONSOLE_CLIENT_SECRET or GOOGLE_CLIENT_SECRET")
            if not refresh_ready:
                missing.append("SEARCH_CONSOLE_REFRESH_TOKEN or GOOGLE_REFRESH_TOKEN")
            items.append(
                {
                    "name": name,
                    "ready": not missing,
                    "missing": missing,
                }
            )
            continue
        missing = [key for key in required_keys if not env_values.get(key)]
        items.append(
            {
                "name": name,
                "ready": not missing,
                "missing": missing,
            }
        )
    return items


def env_display_value(key: str, env_values: dict[str, str], example_values: dict[str, str]) -> str:
    current = env_values.get(key, "")
    if current:
        return f"set ({mask(current)})"

    default = example_values.get(key, "")
    if default:
        return f"default ({default})"

    return "missing"


def main() -> int:
    env_values = parse_env_file(ENV_PATH)
    env_example_values = parse_env_file(ENV_EXAMPLE_PATH)

    branch = git_value(["branch", "--show-current"])
    origin = git_value(["remote", "get-url", "origin"])
    head_commit = git_value(["rev-parse", "--verify", "HEAD"])
    latest_files = sorted(str(path.relative_to(ROOT)) for path in OUTPUT_DIR.glob("*") if path.is_file())
    publish_ready = {}
    if PUBLISH_READY_REPORT.exists():
        publish_ready = json.loads(PUBLISH_READY_REPORT.read_text())
    publish_ready_items = publish_ready.get("items", [])
    site_page_plan = {}
    if SITE_PAGE_PLAN_REPORT.exists():
        site_page_plan = json.loads(SITE_PAGE_PLAN_REPORT.read_text())
    site_page_items = site_page_plan.get("items", [])
    public_required_site_pages = [item for item in site_page_items if item.get("visibility") == "public_required"]

    report = {
        "project_root": str(ROOT),
        "env_file_exists": ENV_PATH.exists(),
        "env_keys_present": sorted(env_values.keys()),
        "env_keys_filled": sorted([key for key, value in env_values.items() if value]),
        "env_keys_empty": sorted([key for key, value in env_values.items() if not value]),
        "env_keys_expected": sorted(env_example_values.keys()),
        "git": {
            "branch": branch or "(none)",
            "origin": origin or "(not configured)",
            "has_commit": bool(head_commit),
        },
        "integrations": integration_status(env_values),
        "outputs_latest_exists": OUTPUT_DIR.exists(),
        "outputs_latest_files": latest_files,
        "publish_ready": {
            "report_exists": PUBLISH_READY_REPORT.exists(),
            "item_count": len(publish_ready_items),
            "ready_count": sum(1 for item in publish_ready_items if item.get("ready")),
        },
        "site_pages": {
            "report_exists": SITE_PAGE_PLAN_REPORT.exists(),
            "item_count": len(site_page_items),
            "public_required_count": len(public_required_site_pages),
            "rendered_required_count": sum(
                1 for item in public_required_site_pages if Path(item.get("html_path", "")).exists()
            ),
        },
        "go_live": {
            "report_exists": GO_LIVE_REPORT.exists(),
        },
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2))

    print("Investment Blog Cloud Sync setup check")
    print()
    print(f"- project: {ROOT}")
    print(f"- .env present: {'yes' if ENV_PATH.exists() else 'no'}")
    print(f"- git branch: {report['git']['branch']}")
    print(f"- git origin: {report['git']['origin']}")
    print(f"- outputs/latest present: {'yes' if OUTPUT_DIR.exists() else 'no'}")
    print()
    print("Local .env values")
    for key in sorted(env_example_values.keys()):
        print(f"- {key}: {env_display_value(key, env_values, env_example_values)}")
    print()
    print("Integration readiness")
    for item in report["integrations"]:
        if item["ready"]:
            print(f"- {item['name']}: ready")
        else:
            print(f"- {item['name']}: missing {', '.join(item['missing'])}")
    print()
    print("Publish-ready status")
    print(f"- report exists: {'yes' if report['publish_ready']['report_exists'] else 'no'}")
    print(f"- items: {report['publish_ready']['item_count']}")
    print(f"- ready html items: {report['publish_ready']['ready_count']}")
    print()
    print("Site-page status")
    print(f"- plan exists: {'yes' if report['site_pages']['report_exists'] else 'no'}")
    print(f"- items: {report['site_pages']['item_count']}")
    print(
        f"- required rendered pages: {report['site_pages']['rendered_required_count']} / {report['site_pages']['public_required_count']}"
    )
    print()
    print("Go-live report")
    print(f"- report exists: {'yes' if report['go_live']['report_exists'] else 'no'}")
    print()
    print("GitHub Actions notes")
    print("- Local .env values do not automatically sync to GitHub Secrets.")
    print("- Add the same keys manually in GitHub -> Settings -> Secrets and variables -> Actions.")
    print("- Public repositories are usually the safest free option for this lightweight schedule.")
    print("- Automation-first 운영 기준에서 현재 1차 채널은 Blogger, WordPress는 나중 확장입니다.")
    print()
    print(f"JSON report written to: {REPORT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
