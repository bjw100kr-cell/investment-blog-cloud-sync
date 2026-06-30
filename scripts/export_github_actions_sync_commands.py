#!/usr/bin/env python3
import json
import subprocess
from pathlib import Path
from urllib import error, request


ROOT = Path(__file__).resolve().parents[1]
ENV_EXAMPLE = ROOT / ".env.example"
ENV_PATH = ROOT / ".env"
OUTPUT_SH = ROOT / "outputs/latest/github-actions-sync.sh"
OUTPUT_MD = ROOT / "outputs/latest/github-actions-sync.md"

SECRET_KEYS = [
    "NAVER_CLIENT_ID",
    "NAVER_CLIENT_SECRET",
    "SEARCH_CONSOLE_SITE_URL",
    "SEARCH_CONSOLE_CLIENT_ID",
    "SEARCH_CONSOLE_CLIENT_SECRET",
    "SEARCH_CONSOLE_REFRESH_TOKEN",
    "OPENAI_API_KEY",
    "BLOGGER_BLOG_ID",
    "GOOGLE_CLIENT_ID",
    "GOOGLE_CLIENT_SECRET",
    "GOOGLE_REFRESH_TOKEN",
    "GOOGLE_ACCESS_TOKEN",
    "SEARCH_CONSOLE_ACCESS_TOKEN",
    "WORDPRESS_SITE_URL",
    "WORDPRESS_USERNAME",
    "WORDPRESS_APPLICATION_PASSWORD",
]

VARIABLE_KEYS = [
    "SEARCH_CONSOLE_LAG_DAYS",
    "SEARCH_CONSOLE_WINDOW_DAYS",
    "OPENAI_MODEL",
    "BLOG_BASE_URL",
    "BLOGGER_SYNC_SITE_PAGES",
    "BLOGGER_SITE_PAGES_PUBLISH",
    "BLOGGER_INCLUDE_OPTIONAL_SITE_PAGES",
    "BLOGGER_REQUIRE_REVIEW_APPROVAL",
    "BLOGGER_AUTO_PUBLISH_POSTS",
    "BLOGGER_PUBLISH_ONLY_DUE_POSTS",
    "BLOGGER_MAX_POSTS_PER_RUN",
    "WORDPRESS_AUTO_PUBLISH_POSTS",
    "WORDPRESS_PUBLISH_ONLY_DUE_POSTS",
    "WORDPRESS_MAX_POSTS_PER_RUN",
    "GA4_MEASUREMENT_ID",
    "ADSENSE_PUBLISHER_ID",
    "ADSENSE_SITE_VERIFICATION",
    "NEWSLETTER_SUBSCRIBE_URL",
]


def normalize_github_origin(origin: str) -> str:
    if not origin:
        return ""
    origin = origin.strip()
    if origin.startswith("https://") and "@github.com/" in origin:
        origin = "https://" + origin.split("@", 1)[1]
    return origin


def parse_env(path: Path) -> dict[str, str]:
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


def parse_expected_keys(path: Path) -> list[str]:
    return list(parse_env(path).keys())


def load_setup_report(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def repo_slug_from_origin(origin: str) -> str:
    if not origin:
        return ""
    origin = normalize_github_origin(origin)
    if origin.startswith("git@github.com:"):
        return origin.replace("git@github.com:", "", 1).removesuffix(".git")
    if origin.startswith("https://github.com/"):
        return origin.replace("https://github.com/", "", 1).removesuffix(".git")
    return ""


def get_repo_origin_from_git() -> str:
    try:
        completed = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            check=True,
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
    except Exception:
        return ""
    return completed.stdout.strip()


def is_github_repo_accessible(repo_slug: str) -> bool:
    if not repo_slug:
        return False
    url = f"https://github.com/{repo_slug}"
    try:
        response = request.urlopen(url, timeout=8)
        return 200 <= response.status < 400
    except error.HTTPError as exc:
        return exc.code in {200, 302, 307, 308}
    except Exception:
        return False


def shell_quote_list(items: list[str]) -> str:
    return " ".join(f'"{item}"' for item in items)


def build_script(repo_slug: str) -> str:
    repo_default = repo_slug or "OWNER/REPO"
    return f"""#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

if ! command -v gh >/dev/null 2>&1; then
  echo "GitHub CLI (gh)가 설치되어 있지 않습니다."
  echo "https://cli.github.com/ 에서 설치 후 다시 실행하세요."
  exit 1
fi

if [[ ! -f ".env" ]]; then
  echo ".env 파일이 없습니다."
  exit 1
fi

REPO_SLUG="${{1:-{repo_default}}}"
SECRET_KEYS=({shell_quote_list(SECRET_KEYS)})
VARIABLE_KEYS=({shell_quote_list(VARIABLE_KEYS)})

set -a
source .env
set +a

echo "Sync target repo: $REPO_SLUG"
echo

for key in "${{SECRET_KEYS[@]}}"; do
  value="${{!key:-}}"
  if [[ -z "$value" ]]; then
    echo "skip secret: $key (empty)"
    continue
  fi
  gh secret set "$key" --repo "$REPO_SLUG" --body "$value"
  echo "set secret: $key"
done

for key in "${{VARIABLE_KEYS[@]}}"; do
  value="${{!key:-}}"
  if [[ -z "$value" ]]; then
    echo "skip variable: $key (empty)"
    continue
  fi
  gh variable set "$key" --repo "$REPO_SLUG" --body "$value"
  echo "set variable: $key"
done

echo
echo "GitHub Actions secrets/variables sync complete."
echo "Next: GitHub Actions -> Daily Investment Intake -> Run workflow"
"""


def main() -> int:
    env_values = parse_env(ENV_PATH)
    expected_keys = parse_expected_keys(ENV_EXAMPLE)
    origin = get_repo_origin_from_git()
    repo_slug = repo_slug_from_origin(origin if origin != "(not configured)" else "")
    repo_connected = bool(repo_slug) and is_github_repo_accessible(repo_slug)

    OUTPUT_SH.write_text(build_script(repo_slug))
    OUTPUT_SH.chmod(0o755)

    lines = []
    lines.append("# GitHub Actions Sync Guide")
    lines.append("")
    lines.append(f"- script: `{OUTPUT_SH}`")
    lines.append(f"- repo_connected: `{repo_connected}`")
    if repo_slug and not repo_connected:
        lines.append("- repo_connected_note: `원격 URL은 있으나 GitHub에서 404/접근 불가 상태입니다.`")
    lines.append(f"- repo_slug: `{repo_slug or 'OWNER/REPO 필요'}`")
    lines.append("")
    lines.append("## What It Does")
    lines.append("")
    lines.append("- `.env`에서 비어 있지 않은 값을 읽습니다.")
    lines.append("- GitHub Actions `Secrets`와 `Variables`를 `gh` CLI로 한 번에 올립니다.")
    lines.append("- 이미 비어 있는 키는 자동으로 건너뜁니다.")
    lines.append("")
    lines.append("## Usage")
    lines.append("")
    if repo_slug:
        lines.append(f"```bash\nbash outputs/latest/github-actions-sync.sh {repo_slug}\n```")
    else:
        lines.append("```bash\nbash outputs/latest/github-actions-sync.sh OWNER/REPO\n```")
    lines.append("")
    synced_local_keys = []
    local_only_keys = []
    for key in expected_keys:
        value = env_values.get(key, "")
        if not value:
            continue
        if key in SECRET_KEYS or key in VARIABLE_KEYS:
            synced_local_keys.append(key)
        else:
            local_only_keys.append(key)

    lines.append("## Keys With Local Values That Will Sync")
    lines.append("")
    for key in synced_local_keys:
        category = "secret" if key in SECRET_KEYS else "variable"
        lines.append(f"- `{key}` ({category})")
    if not synced_local_keys:
        lines.append("- 현재 GitHub로 동기화할 로컬 값이 없습니다.")
    lines.append("")
    lines.append("## Local Only Keys")
    lines.append("")
    for key in local_only_keys:
        lines.append(f"- `{key}`")
    if not local_only_keys:
        lines.append("- 없음")
    lines.append("")
    lines.append("## Before Running")
    lines.append("")
    lines.append("- `gh auth login` 이 완료되어 있어야 합니다.")
    lines.append("- GitHub 저장소가 먼저 생성되어 있어야 합니다.")
    lines.append("- `.env` 안의 값이 최신인지 확인합니다.")
    lines.append("")
    OUTPUT_MD.write_text("\n".join(lines))
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
