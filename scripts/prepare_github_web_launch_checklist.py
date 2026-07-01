#!/usr/bin/env python3
import json
from pathlib import Path
import urllib.error
import urllib.request


ROOT = Path(__file__).resolve().parents[1]
SETUP_JSON = ROOT / "outputs/latest/setup-check-report.json"
GITHUB_LAUNCH_PLAN_JSON = ROOT / "outputs/latest/github-launch-plan.json"
OUTPUT_JSON = ROOT / "outputs/latest/github-web-launch-checklist.json"
OUTPUT_MD = ROOT / "outputs/latest/github-web-launch-checklist.md"
VALUES_CARD_MD = ROOT / "outputs/latest/first-run-values-card.md"
ENV_PATH = ROOT / ".env"

FIRST_RUN_SECRETS = [
    ("BLOGGER_BLOG_ID", "Blogger 업로드 대상 블로그 ID"),
    ("GOOGLE_CLIENT_ID", "Google OAuth client id"),
    ("GOOGLE_CLIENT_SECRET", "Google OAuth client secret"),
    ("GOOGLE_REFRESH_TOKEN", "Blogger 업로드용 refresh token"),
]

DEFAULT_FIRST_RUN_VARIABLES = [
    ("OPENAI_MODEL", "gpt-4o-mini", "초안 생성 모델. 현재 기본값 유지 가능"),
    ("BLOGGER_SYNC_SITE_PAGES", "false", "필요 시 신뢰 페이지까지 동기화"),
    ("BLOGGER_SITE_PAGES_PUBLISH", "false", "첫 실행에서는 페이지도 공개하지 않음"),
    ("BLOGGER_INCLUDE_OPTIONAL_SITE_PAGES", "false", "필수 페이지부터 시작"),
    ("BLOGGER_REQUIRE_REVIEW_APPROVAL", "false", "자동 모드면 승인 단계 생략"),
    ("BLOGGER_AUTO_PUBLISH_POSTS", "true", "드래프트 업로드 후 즉시 공개"),
    ("BLOGGER_PUBLISH_ONLY_DUE_POSTS", "false", "발행일 제한 없이 동작"),
    ("BLOGGER_MAX_POSTS_PER_RUN", "3", "품질 게이트 통과 글을 실행당 최대 3건 처리"),
]

WORDPRESS_LATER_SECRETS = [
    ("WORDPRESS_SITE_URL", "WordPress 사이트 주소"),
    ("WORDPRESS_USERNAME", "WordPress 로그인 계정"),
    ("WORDPRESS_APPLICATION_PASSWORD", "WordPress Application Password"),
]

WORDPRESS_LATER_VARIABLES = [
    ("WORDPRESS_AUTO_PUBLISH_POSTS", "false", "초기에는 draft만 생성"),
    ("WORDPRESS_PUBLISH_ONLY_DUE_POSTS", "true", "기한 도래 글만 대상으로 제한"),
    ("WORDPRESS_MAX_POSTS_PER_RUN", "1", "첫 실행은 1건만 업로드"),
]


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def filled_keys(setup: dict) -> set[str]:
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


def repo_links(repo_slug: str) -> dict:
    if not repo_slug:
        return {
            "repo_home": "https://github.com/new",
            "actions_secrets": "https://github.com/new",
            "actions_runs": "https://github.com/new",
        }
    base = f"https://github.com/{repo_slug}"
    return {
        "repo_home": base,
        "actions_secrets": f"{base}/settings/secrets/actions",
        "actions_runs": f"{base}/actions/workflows/daily-investment-intake.yml",
    }


def repo_accessible(repo_slug: str) -> bool:
    if not repo_slug:
        return False
    url = f"https://github.com/{repo_slug}"
    try:
        request = urllib.request.Request(url, method="HEAD")
        with urllib.request.urlopen(request, timeout=8) as response:
            return 200 <= response.status < 400
    except urllib.error.HTTPError as exc:
        return exc.code in {200, 302, 307, 308}
    except Exception:
        return False


def build_report() -> dict:
    setup = load_json(SETUP_JSON)
    launch = load_json(GITHUB_LAUNCH_PLAN_JSON)
    env_values = parse_env(ENV_PATH)
    env_filled = filled_keys(setup)
    repo_slug = launch.get("repo_slug", "")
    raw_repo_slug = repo_slug
    accessible = bool(repo_accessible(repo_slug if repo_slug != "OWNER/REPO 필요" else ""))
    links = repo_links(repo_slug if repo_slug != "OWNER/REPO 필요" else "")

    def env_value(key: str, fallback: str) -> str:
        if key == "BLOGGER_MAX_POSTS_PER_RUN":
            return fallback
        return env_values.get(key, fallback).strip() or fallback

    first_run_secret_rows = [
        {
            "key": key,
            "description": description,
            "filled_locally": key in env_filled,
        }
        for key, description in FIRST_RUN_SECRETS
    ]
    first_run_variable_rows = [
        {
            "key": key,
            "recommended_value": env_value(key, value),
            "description": description,
            "filled_locally": key in env_filled,
        }
        for key, value, description in DEFAULT_FIRST_RUN_VARIABLES
    ]
    wordpress_secret_rows = [
        {
            "key": key,
            "description": description,
            "filled_locally": key in env_filled,
        }
        for key, description in WORDPRESS_LATER_SECRETS
    ]
    wordpress_variable_rows = [
        {
            "key": key,
            "recommended_value": value,
            "description": description,
            "filled_locally": key in env_filled,
        }
        for key, value, description in WORDPRESS_LATER_VARIABLES
    ]

    return {
        "repo_connected": launch.get("repo_connected", False),
        "repo_slug": repo_slug,
        "repo_accessible": accessible,
        "raw_repo_slug": raw_repo_slug,
        "gh_installed": launch.get("gh_installed", False),
        "links": links,
        "repo_access_note": "repo_connected_before_actions_ready" if accessible else "repo_not_created_or_private_yet",
        "minimum_path_summary": {
            "required_secrets_count": len(first_run_secret_rows),
            "required_variables_count": len(first_run_variable_rows),
            "wordpress_required_now": False,
            "openai_required_now": False,
            "first_goal": "GitHub Actions에서 Blogger 자동 업로드/공개가 정상적으로 동작하는지 확인",
        },
        "ui_path": {
            "repo_creation": "GitHub > New repository",
            "actions_settings": "Repo > Settings > Secrets and variables > Actions",
            "workflow_run": "Repo > Actions > Daily Investment Intake > Run workflow",
        },
        "first_run_secrets": first_run_secret_rows,
        "first_run_variables": first_run_variable_rows,
        "wordpress_later_secrets": wordpress_secret_rows,
        "wordpress_later_variables": wordpress_variable_rows,
        "copy_block": [f"{row['key']}={row['recommended_value']}" for row in first_run_variable_rows],
        "secrets_copy_keys": [row["key"] for row in first_run_secret_rows],
        "next_steps": [
            "GitHub에서 새 public repo를 만듭니다.",
            "로컬에서 `bash scripts/bootstrap_github_remote.sh <OWNER/REPO>` 를 실행합니다.",
            "GitHub 웹 UI에서 Actions Secrets 4개와 Variables를 먼저 입력합니다.",
            "Actions에서 Daily Investment Intake를 수동 실행합니다.",
            "Blogger 업로드 결과에서 processed_count, published, skipped 이유를 확인합니다.",
        ],
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# GitHub Web Launch Checklist")
    lines.append("")
    lines.append(f"- repo_connected: `{report.get('repo_connected', False)}`")
    lines.append(f"- repo_accessible: `{report.get('repo_accessible', False)}`")
    lines.append(f"- repo_slug: `{report.get('repo_slug', '') or 'OWNER/REPO 필요'}`")
    if report.get("repo_slug"):
        lines.append(f"- repo_accessible: `{report.get('repo_accessible', False)}`")
        if not report.get("repo_accessible", False):
            lines.append(
                "- repo_note: 현재는 저장소 URL만 알고 있고, 아직 접근 가능한 저장소가 아니므로 Settings/Actions 링크는 생성한 뒤 한 번 더 열어주세요."
            )
    lines.append(f"- gh_installed: `{report.get('gh_installed', False)}`")
    lines.append(f"- repo_create_link: {report.get('links', {}).get('repo_home', '')}")
    lines.append(f"- actions_secrets_link: {report.get('links', {}).get('actions_secrets', '')}")
    lines.append(f"- actions_run_link: {report.get('links', {}).get('actions_runs', '')}")
    lines.append("")
    lines.append("## Minimum Go-Live Path")
    lines.append("")
    lines.append(
        f"- 지금 필요한 Secrets 수: `{report.get('minimum_path_summary', {}).get('required_secrets_count', 0)}`"
    )
    lines.append(
        f"- 지금 필요한 Variables 수: `{report.get('minimum_path_summary', {}).get('required_variables_count', 0)}`"
    )
    lines.append(
        f"- WordPress 지금 필수 여부: `{report.get('minimum_path_summary', {}).get('wordpress_required_now', False)}`"
    )
    lines.append(
        f"- OpenAI 지금 필수 여부: `{report.get('minimum_path_summary', {}).get('openai_required_now', False)}`"
    )
    lines.append(f"- 첫 목표: {report.get('minimum_path_summary', {}).get('first_goal', '')}")
    lines.append("")
    lines.append("## UI Path")
    lines.append("")
    lines.append(f"- repo_creation: `{report.get('ui_path', {}).get('repo_creation', '')}`")
    lines.append(f"- actions_settings: `{report.get('ui_path', {}).get('actions_settings', '')}`")
    lines.append(f"- workflow_run: `{report.get('ui_path', {}).get('workflow_run', '')}`")
    lines.append("")
    lines.append("## First Run Secrets")
    lines.append("")
    for row in report.get("first_run_secrets", []):
        lines.append(f"- `{row['key']}`: {row['description']} / local_filled={row['filled_locally']}")
    lines.append("")
    lines.append("## Secrets Copy Checklist")
    lines.append("")
    lines.append("```text")
    for item in report.get("secrets_copy_keys", []):
        lines.append(item)
    lines.append("```")
    lines.append("")
    lines.append("## First Run Variables")
    lines.append("")
    for row in report.get("first_run_variables", []):
        lines.append(
            f"- `{row['key']}={row['recommended_value']}`: {row['description']} / local_filled={row['filled_locally']}"
        )
    lines.append("")
    lines.append("## WordPress Later")
    lines.append("")
    for row in report.get("wordpress_later_secrets", []):
        lines.append(f"- secret `{row['key']}`: {row['description']} / local_filled={row['filled_locally']}")
    for row in report.get("wordpress_later_variables", []):
        lines.append(
            f"- variable `{row['key']}={row['recommended_value']}`: {row['description']} / local_filled={row['filled_locally']}"
        )
    lines.append("")
    lines.append("## Variables Copy Block")
    lines.append("")
    lines.append("```text")
    for item in report.get("copy_block", []):
        lines.append(item)
    lines.append("```")
    lines.append("")
    lines.append("## Next Steps")
    lines.append("")
    for index, step in enumerate(report.get("next_steps", []), start=1):
        lines.append(f"{index}. {step}")
    lines.append("")
    lines.append("## Fastest Reference")
    lines.append("")
    lines.append(f"- 더 짧은 값 카드: `{VALUES_CARD_MD}`")
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
