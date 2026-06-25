#!/usr/bin/env python3
import argparse
import json
import os
import subprocess
import time
import webbrowser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ENV_PATH = ROOT / ".env"
OUTPUT_JSON = ROOT / "outputs/latest/login-launch-checklist.json"
OUTPUT_MD = ROOT / "outputs/latest/login-launch-checklist.md"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Prepare or open the required login/setup pages for the blog automation stack.")
    parser.add_argument("--open", action="store_true", help="Open the prepared URLs in the default browser.")
    parser.add_argument("--delay", type=float, default=0.5, help="Delay in seconds between browser tabs when --open is used.")
    parser.add_argument("--limit", type=int, default=8, help="Maximum number of pages to open when --open is used.")
    return parser.parse_args()


def load_env(path: Path) -> dict[str, str]:
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


def git_origin() -> str:
    try:
        result = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
    except Exception:
        return ""
    return result.stdout.strip()


def github_repo_url(origin: str) -> str:
    if not origin:
        return ""
    if origin.startswith("git@github.com:"):
        repo = origin.replace("git@github.com:", "", 1).removesuffix(".git")
        return f"https://github.com/{repo}"
    if origin.startswith("https://github.com/"):
        return origin.removesuffix(".git")
    return ""


def make_pages(env_values: dict[str, str], repo_url: str) -> list[dict]:
    blog_id = env_values.get("BLOGGER_BLOG_ID", "")
    pages = [
        {
            "id": "google_cloud_home",
            "label": "Google Cloud Console",
            "url": "https://console.cloud.google.com/",
            "reason": "OAuth client, API activation, consent screen setup",
            "required_when": ["blogger_upload", "search_console"],
        },
        {
            "id": "google_oauth_consent",
            "label": "Google OAuth consent screen",
            "url": "https://console.cloud.google.com/apis/credentials/consent",
            "reason": "App name, email, and consent screen publishing",
            "required_when": ["blogger_upload", "search_console"],
        },
        {
            "id": "google_credentials",
            "label": "Google OAuth client credentials",
            "url": "https://console.cloud.google.com/apis/credentials",
            "reason": "Create or copy GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET",
            "required_when": ["blogger_upload", "search_console"],
        },
        {
            "id": "google_blogger_api",
            "label": "Blogger API activation page",
            "url": "https://console.cloud.google.com/apis/library/blogger.googleapis.com",
            "reason": "Enable Blogger API",
            "required_when": ["blogger_upload"],
        },
        {
            "id": "google_search_console_api",
            "label": "Search Console API activation page",
            "url": "https://console.cloud.google.com/apis/library/searchconsole.googleapis.com",
            "reason": "Enable Search Console API",
            "required_when": ["search_console"],
        },
        {
            "id": "blogger_dashboard",
            "label": "Blogger dashboard",
            "url": f"https://www.blogger.com/blog/posts/{blog_id}" if blog_id else "https://www.blogger.com/",
            "reason": "Check blog access and confirm BLOGGER_BLOG_ID target",
            "required_when": ["blogger_upload"],
        },
        {
            "id": "search_console_home",
            "label": "Google Search Console",
            "url": "https://search.google.com/search-console",
            "reason": "Verify property access and confirm SEARCH_CONSOLE_SITE_URL",
            "required_when": ["search_console"],
        },
        {
            "id": "openai_api_keys",
            "label": "OpenAI API keys",
            "url": "https://platform.openai.com/api-keys",
            "reason": "Create or paste OPENAI_API_KEY for real draft generation",
            "required_when": ["openai_drafts"],
        },
        {
            "id": "github_repo",
            "label": "GitHub repository or new repo",
            "url": repo_url or "https://github.com/new",
            "reason": "Connect the repo before enabling cloud automation",
            "required_when": ["github_actions"],
        },
        {
            "id": "github_actions_secrets",
            "label": "GitHub Actions secrets",
            "url": f"{repo_url}/settings/secrets/actions" if repo_url else "https://github.com/settings/tokens",
            "reason": "Add Actions secrets and variables for cloud runs",
            "required_when": ["github_actions"],
        },
    ]
    return pages


def detect_missing_groups(env_values: dict[str, str]) -> dict[str, list[str]]:
    include_openai = os.getenv("INCLUDE_OPENAI_SETUP", "false").lower() in {"1", "true", "yes"}
    groups = {
        "blogger_upload": ["BLOGGER_BLOG_ID", "GOOGLE_CLIENT_ID", "GOOGLE_CLIENT_SECRET", "GOOGLE_REFRESH_TOKEN"],
        "search_console": ["SEARCH_CONSOLE_SITE_URL", "SEARCH_CONSOLE_CLIENT_ID", "SEARCH_CONSOLE_CLIENT_SECRET", "SEARCH_CONSOLE_REFRESH_TOKEN"],
        "openai_drafts": ["OPENAI_API_KEY"] if include_openai else [],
        "github_actions": [],
    }
    missing: dict[str, list[str]] = {}
    for group, keys in groups.items():
        missing[group] = [key for key in keys if not env_values.get(key)]
    return missing


def select_pages(pages: list[dict], missing_groups: dict[str, list[str]], repo_url: str) -> list[dict]:
    selected = []
    for page in pages:
        if page["id"] == "github_actions_secrets" and not repo_url:
            continue
        needed = False
        for group in page["required_when"]:
            if group == "github_actions":
                needed = True
            elif missing_groups.get(group):
                needed = True
        if needed:
            selected.append(page)
    return selected


def build_steps(env_values: dict[str, str], repo_url: str) -> list[str]:
    steps = [
        "Google Cloud Console에서 Blogger API와 Search Console API를 켭니다.",
        "OAuth 동의 화면과 OAuth Client를 만든 뒤 GOOGLE_CLIENT_ID / GOOGLE_CLIENT_SECRET을 확보합니다.",
        "로컬에서 get_google_refresh_token.py를 실행해 GOOGLE_REFRESH_TOKEN을 발급합니다.",
        "Blogger 대시보드에서 대상 블로그가 맞는지 확인합니다.",
        "Search Console에서 사이트 속성 접근 권한과 SEARCH_CONSOLE_SITE_URL을 확인합니다.",
    ]
    if repo_url:
        steps.append("GitHub 저장소의 Actions Secrets/Variables에 같은 값을 입력합니다.")
    else:
        steps.append("GitHub 저장소를 먼저 연결한 뒤 Actions Secrets/Variables에 같은 값을 입력합니다.")
    if not env_values.get("OPENAI_API_KEY"):
        steps.append("OPENAI_API_KEY를 넣어 사람 같은 초안 생성 품질을 높입니다.")
    return steps


def write_outputs(payload: dict) -> None:
    OUTPUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2))

    lines = []
    lines.append("# Login Launch Checklist")
    lines.append("")
    lines.append(f"- repo_connected: `{payload['repo_connected']}`")
    lines.append(f"- blogger_ready: `{payload['blogger_ready']}`")
    lines.append(f"- search_console_ready: `{payload['search_console_ready']}`")
    lines.append(f"- openai_ready: `{payload['openai_ready']}`")
    lines.append("")
    lines.append("## Missing Keys")
    lines.append("")
    for group, keys in payload["missing_groups"].items():
        if keys:
            lines.append(f"- `{group}`: {', '.join(keys)}")
        else:
            lines.append(f"- `{group}`: none")
    lines.append("")
    lines.append("## Open These Pages")
    lines.append("")
    for page in payload["pages"]:
        lines.append(f"- [{page['label']}]({page['url']}): {page['reason']}")
    lines.append("")
    lines.append("## Suggested Order")
    lines.append("")
    for idx, step in enumerate(payload["steps"], start=1):
        lines.append(f"{idx}. {step}")
    lines.append("")
    OUTPUT_MD.write_text("\n".join(lines))


def main() -> int:
    args = parse_args()
    env_values = load_env(ENV_PATH)
    origin = git_origin()
    repo_url = github_repo_url(origin)
    missing_groups = detect_missing_groups(env_values)
    pages = make_pages(env_values, repo_url)
    selected_pages = select_pages(pages, missing_groups, repo_url)
    steps = build_steps(env_values, repo_url)

    payload = {
        "repo_connected": bool(repo_url),
        "repo_url": repo_url,
        "blogger_ready": not missing_groups["blogger_upload"],
        "search_console_ready": not missing_groups["search_console"],
        "openai_ready": not missing_groups["openai_drafts"],
        "missing_groups": missing_groups,
        "pages": selected_pages,
        "steps": steps,
    }
    write_outputs(payload)

    print(OUTPUT_MD)
    if args.open:
        for page in selected_pages[: args.limit]:
            webbrowser.open(page["url"])
            time.sleep(max(args.delay, 0))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
