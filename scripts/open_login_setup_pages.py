#!/usr/bin/env python3
import argparse
import json
import os
import subprocess
import urllib.error
import urllib.request
import time
import webbrowser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ENV_PATH = ROOT / ".env"
OUTPUT_JSON = ROOT / "outputs/latest/login-launch-checklist.json"
OUTPUT_MD = ROOT / "outputs/latest/login-launch-checklist.md"
VISITOR_PROOF_BOARD_JSON = ROOT / "outputs/latest/visitor-proof-board.json"


def normalize_github_origin(origin: str) -> str:
    if not origin:
        return ""
    origin = origin.strip()
    if origin.startswith("https://") and "@github.com/" in origin:
        origin = "https://" + origin.split("@", 1)[1]
    return origin


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Prepare or open the required login/setup pages for the blog automation stack.")
    parser.add_argument("--open", action="store_true", help="Open only the minimum required URLs in the default browser.")
    parser.add_argument("--open-all", action="store_true", help="Open all prepared URLs in the default browser.")
    parser.add_argument("--open-next", action="store_true", help="Open only the single next recommended page for the minimum go-live path.")
    parser.add_argument("--print-next", action="store_true", help="Print the recommended next page without opening a browser.")
    parser.add_argument("--include-wordpress", action="store_true", help="Include optional WordPress setup pages too.")
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


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text())
    except Exception:
        return {}


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


def github_repo_accessible(repo_url: str) -> bool:
    if not repo_url:
        return False
    try:
        request = urllib.request.Request(f"{repo_url}", method="HEAD")
        with urllib.request.urlopen(request, timeout=8) as response:
            return 200 <= response.status < 400
    except urllib.error.HTTPError as exc:
        # Private repos without auth can appear as 404. Treat both as unreachable.
        return exc.code in {200, 302, 307, 308}
    except Exception:
        return False


def github_repo_url(origin: str) -> str:
    if not origin:
        return ""
    origin = normalize_github_origin(origin)
    if origin.startswith("git@github.com:"):
        repo = origin.replace("git@github.com:", "", 1).removesuffix(".git")
        return f"https://github.com/{repo}"
    if origin.startswith("https://github.com/"):
        return origin.removesuffix(".git")
    return ""


def make_pages(env_values: dict[str, str], repo_url: str) -> list[dict]:
    blog_id = env_values.get("BLOGGER_BLOG_ID", "")
    wordpress_site = env_values.get("WORDPRESS_SITE_URL", "").rstrip("/")
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
            "id": "wordpress_dashboard",
            "label": "WordPress dashboard",
            "url": f"{wordpress_site}/wp-admin/" if wordpress_site else "https://wordpress.com/",
            "reason": "Check site access and confirm WORDPRESS_SITE_URL target",
            "required_when": ["wordpress_upload"],
        },
        {
            "id": "wordpress_profile",
            "label": "WordPress profile / application passwords",
            "url": f"{wordpress_site}/wp-admin/profile.php" if wordpress_site else "https://wordpress.com/log-in",
            "reason": "Create or verify WORDPRESS_APPLICATION_PASSWORD",
            "required_when": ["wordpress_upload"],
        },
        {
            "id": "wordpress_login",
            "label": "WordPress login",
            "url": f"{wordpress_site}/wp-login.php" if wordpress_site else "https://wordpress.com/log-in",
            "reason": "Sign in before creating application passwords",
            "required_when": ["wordpress_upload"],
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
        "wordpress_upload": ["WORDPRESS_SITE_URL", "WORDPRESS_USERNAME", "WORDPRESS_APPLICATION_PASSWORD"],
        "search_console": ["SEARCH_CONSOLE_SITE_URL", "SEARCH_CONSOLE_CLIENT_ID", "SEARCH_CONSOLE_CLIENT_SECRET", "SEARCH_CONSOLE_REFRESH_TOKEN"],
        "openai_drafts": ["OPENAI_API_KEY"] if include_openai else [],
        "github_actions": [],
    }
    missing: dict[str, list[str]] = {}
    for group, keys in groups.items():
        missing[group] = [key for key in keys if not env_values.get(key)]
    return missing


def select_pages(
    pages: list[dict],
    missing_groups: dict[str, list[str]],
    repo_url: str,
    include_wordpress: bool,
) -> list[dict]:
    selected = []
    for page in pages:
        if page["id"] == "github_actions_secrets" and not repo_url:
            continue
        if not include_wordpress and "wordpress_upload" in page["required_when"]:
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


def build_steps(env_values: dict[str, str], repo_url: str, include_wordpress: bool) -> list[str]:
    steps = []
    blogger_ready = (
        env_values.get("BLOGGER_BLOG_ID")
        and env_values.get("GOOGLE_CLIENT_ID")
        and env_values.get("GOOGLE_CLIENT_SECRET")
        and env_values.get("GOOGLE_REFRESH_TOKEN")
    )

    if not repo_url:
        steps.append("GitHub에서 public repo를 먼저 만들고 이 프로젝트와 연결합니다.")
        steps.append("repo 연결 뒤 GitHub Actions Secrets/Variables에 Blogger 필수값을 옮깁니다.")

    if not blogger_ready:
        steps.extend(
            [
                "Google Cloud Console에서 Blogger API를 켭니다.",
                "OAuth 동의 화면과 OAuth Client를 만든 뒤 GOOGLE_CLIENT_ID / GOOGLE_CLIENT_SECRET을 확보합니다.",
                "로컬에서 get_google_refresh_token.py를 실행해 GOOGLE_REFRESH_TOKEN을 발급합니다.",
                "Blogger 대시보드에서 대상 블로그가 맞는지 확인합니다.",
            ]
        )

    if repo_url and blogger_ready:
        steps.append("Blogger 필수값은 준비되어 있으니 GitHub Actions Secrets/Variables만 반영하면 됩니다.")

    wordpress_ready = (
        env_values.get("WORDPRESS_SITE_URL")
        and env_values.get("WORDPRESS_USERNAME")
        and env_values.get("WORDPRESS_APPLICATION_PASSWORD")
    )
    proof = load_json(VISITOR_PROOF_BOARD_JSON)
    if proof.get("proof_status") == "measurement_missing":
        steps.append("현재 200명/일 목표의 1순위 병목은 Search Console 속성 검증입니다. Search Console에서 URL-prefix 속성을 추가/검증하세요.")
    elif not env_values.get("SEARCH_CONSOLE_SITE_URL"):
        steps.append("Search Console은 첫 가동 뒤 붙여도 됩니다. 지금은 SEARCH_CONSOLE_SITE_URL 없이도 시작 가능합니다.")
    if include_wordpress and not wordpress_ready:
        steps.extend(
            [
                "WordPress 관리자 화면에 로그인해서 대상 사이트 주소가 맞는지 확인합니다.",
                "WordPress 프로필 화면에서 Application Password를 새로 발급합니다.",
                "WORDPRESS_SITE_URL, WORDPRESS_USERNAME, WORDPRESS_APPLICATION_PASSWORD를 `.env`에 입력합니다.",
            ]
        )
    elif not include_wordpress and not wordpress_ready:
        steps.append("WordPress는 지금 열지 않고 Blogger 자동화 검증이 끝난 뒤 두 번째 채널로 붙입니다.")
    if not env_values.get("OPENAI_API_KEY"):
        steps.append("OpenAI 키도 후순위입니다. 나중에 넣으면 사람 같은 초안 품질을 더 끌어올릴 수 있습니다.")
    return steps


def find_page(pages: list[dict], page_id: str) -> dict:
    return next((page for page in pages if page.get("id") == page_id), {})


def page_subset(pages: list[dict], page_ids: list[str]) -> list[dict]:
    lookup = {page.get("id"): page for page in pages}
    return [lookup[page_id] for page_id in page_ids if page_id in lookup]


def choose_next_page(
    env_values: dict[str, str],
    repo_url: str,
    missing_groups: dict[str, list[str]],
    selected_pages: list[dict],
) -> dict:
    auto_channel_ready = not missing_groups.get("blogger_upload") or not missing_groups.get("wordpress_upload")
    proof = load_json(VISITOR_PROOF_BOARD_JSON)

    if not repo_url:
        page = find_page(selected_pages, "github_repo")
        if page:
            return page

    if auto_channel_ready and proof.get("proof_status") == "measurement_missing":
        page = find_page(selected_pages, "search_console_home")
        if page:
            return page

    if auto_channel_ready:
        actions_page = find_page(selected_pages, "github_actions_secrets")
        if actions_page:
            return actions_page

    if not auto_channel_ready:
        if missing_groups.get("blogger_upload"):
            for page_id in ["google_credentials", "google_blogger_api", "blogger_dashboard"]:
                page = find_page(selected_pages, page_id)
                if page:
                    return page
        if missing_groups.get("wordpress_upload"):
            for page_id in ["wordpress_login", "wordpress_dashboard", "wordpress_profile"]:
                page = find_page(selected_pages, page_id)
                if page:
                    return page

    if missing_groups.get("search_console"):
        for page_id in ["search_console_home", "google_search_console_api"]:
            page = find_page(selected_pages, page_id)
            if page:
                return page

    if missing_groups.get("wordpress_upload"):
        for page_id in ["wordpress_login", "wordpress_dashboard", "wordpress_profile"]:
            page = find_page(selected_pages, page_id)
            if page:
                return page

    return selected_pages[0] if selected_pages else {}


def select_minimum_path_pages(
    pages: list[dict],
    env_values: dict[str, str],
    repo_url: str,
    missing_groups: dict[str, list[str]],
    include_wordpress: bool,
) -> list[dict]:
    blogger_ready = not missing_groups.get("blogger_upload")

    if not repo_url:
        return page_subset(pages, ["github_repo"])

    if not blogger_ready:
        return page_subset(pages, ["google_credentials", "google_blogger_api", "blogger_dashboard"])

    minimum_pages = page_subset(pages, ["github_actions_secrets"])

    if include_wordpress and missing_groups.get("wordpress_upload"):
        minimum_pages.extend(page_subset(pages, ["wordpress_login", "wordpress_profile"]))

    return minimum_pages


def write_outputs(payload: dict) -> None:
    OUTPUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2))

    lines = []
    lines.append("# Login Launch Checklist")
    lines.append("")
    lines.append(f"- repo_connected: `{payload['repo_connected']}`")
    if payload.get("repo_url"):
        lines.append(f"- repo_url: `{payload['repo_url']}`")
    lines.append(f"- repo_accessible: `{payload.get('repo_accessible', False)}`")
    lines.append(f"- blogger_ready: `{payload['blogger_ready']}`")
    lines.append(f"- wordpress_ready: `{payload['wordpress_ready']}`")
    lines.append(f"- search_console_ready: `{payload['search_console_ready']}`")
    lines.append(f"- openai_ready: `{payload['openai_ready']}`")
    lines.append(f"- openai_optional: `True`")
    lines.append(f"- openai_note: `현재는 OpenAI 키가 없더라도 무료 템플릿/기반 워크플로는 동작합니다.`")
    if payload.get("next_page"):
        lines.append(f"- next_page: [{payload['next_page']['label']}]({payload['next_page']['url']})")
    lines.append("")
    lines.append("## Minimum Go-Live Path")
    lines.append("")
    for page in payload.get("minimum_pages", []):
        lines.append(f"- [{page['label']}]({page['url']}): {page['reason']}")
    if not payload.get("minimum_pages"):
        lines.append("- minimum path page 없음")
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
    repo_accessible = github_repo_accessible(repo_url)
    effective_repo_url = repo_url if repo_accessible else ""
    missing_groups = detect_missing_groups(env_values)
    pages = make_pages(env_values, effective_repo_url)
    selected_pages = select_pages(pages, missing_groups, effective_repo_url, args.include_wordpress)
    minimum_pages = select_minimum_path_pages(pages, env_values, effective_repo_url, missing_groups, args.include_wordpress)
    steps = build_steps(env_values, effective_repo_url, args.include_wordpress)
    next_page = choose_next_page(env_values, effective_repo_url, missing_groups, selected_pages)

    payload = {
        "repo_connected": bool(effective_repo_url),
        "repo_url": repo_url,
        "repo_accessible": repo_accessible,
        "blogger_ready": not missing_groups["blogger_upload"],
        "wordpress_ready": not missing_groups["wordpress_upload"],
        "search_console_ready": not missing_groups["search_console"],
        "openai_ready": bool(env_values.get("OPENAI_API_KEY")),
        "include_wordpress": args.include_wordpress,
        "missing_groups": missing_groups,
        "minimum_pages": minimum_pages,
        "pages": selected_pages,
        "next_page": next_page,
        "steps": steps,
    }
    write_outputs(payload)

    print(OUTPUT_MD)
    if (args.open_next or args.print_next) and next_page:
        print(f"next_url={next_page['url']}")
        print(f"next_label={next_page.get('label', '')}")
    if args.open_next and next_page and not args.print_next:
        webbrowser.open(next_page["url"])
    elif args.open_all:
        for page in selected_pages[: args.limit]:
            webbrowser.open(page["url"])
            time.sleep(max(args.delay, 0))
    elif args.open:
        for page in minimum_pages[: max(args.limit, 1)]:
            webbrowser.open(page["url"])
            time.sleep(max(args.delay, 0))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
