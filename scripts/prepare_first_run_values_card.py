#!/usr/bin/env python3
import json
from pathlib import Path
from typing import Dict


ROOT = Path(__file__).resolve().parents[1]
ENV_PATH = ROOT / ".env"
OUTPUT_JSON = ROOT / "outputs/latest/first-run-values-card.json"
OUTPUT_MD = ROOT / "outputs/latest/first-run-values-card.md"


def parse_env(path: Path) -> Dict[str, str]:
    values: Dict[str, str] = {}
    if not path.exists():
        return values

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip().strip("'").strip('"')
    return values


def build_report() -> dict:
    env_values = parse_env(ENV_PATH)

    def env_value(key: str, fallback: str) -> str:
        return env_values.get(key, fallback).strip() or fallback

    first_run_variables = [
        {"key": "OPENAI_MODEL", "value": env_value("OPENAI_MODEL", "gpt-4o-mini")},
        {"key": "BLOGGER_SYNC_SITE_PAGES", "value": env_value("BLOGGER_SYNC_SITE_PAGES", "false")},
        {"key": "BLOGGER_SITE_PAGES_PUBLISH", "value": env_value("BLOGGER_SITE_PAGES_PUBLISH", "false")},
        {"key": "BLOGGER_INCLUDE_OPTIONAL_SITE_PAGES", "value": env_value("BLOGGER_INCLUDE_OPTIONAL_SITE_PAGES", "false")},
        {"key": "BLOGGER_REQUIRE_REVIEW_APPROVAL", "value": env_value("BLOGGER_REQUIRE_REVIEW_APPROVAL", "false")},
        {"key": "BLOGGER_AUTO_PUBLISH_POSTS", "value": env_value("BLOGGER_AUTO_PUBLISH_POSTS", "false")},
        {"key": "BLOGGER_PUBLISH_ONLY_DUE_POSTS", "value": env_value("BLOGGER_PUBLISH_ONLY_DUE_POSTS", "false")},
        {"key": "BLOGGER_MAX_POSTS_PER_RUN", "value": env_value("BLOGGER_MAX_POSTS_PER_RUN", "3")},
    ]

    return {
        "title": "First Run Values Card",
        "where": [
            "GitHub repo > Settings > Secrets and variables > Actions",
            "Secrets 탭에서 아래 4개 추가",
            "Variables 탭에서 아래 항목 추가",
        ],
        "secrets": [
            "BLOGGER_BLOG_ID",
            "GOOGLE_CLIENT_ID",
            "GOOGLE_CLIENT_SECRET",
            "GOOGLE_REFRESH_TOKEN",
        ],
        "variables": first_run_variables,
        "later": [
            "WORDPRESS_SITE_URL",
            "WORDPRESS_USERNAME",
            "WORDPRESS_APPLICATION_PASSWORD",
            "SEARCH_CONSOLE_SITE_URL",
            "OPENAI_API_KEY",
        ],
        "copy_block": [f"{item['key']}={item['value']}" for item in first_run_variables],
        "next_action": "GitHub repo 생성 후 OWNER/REPO 형태로 bootstrap_github_remote.sh 실행",
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# First Run Values Card")
    lines.append("")
    lines.append("## 어디에 넣나")
    lines.append("")
    for index, item in enumerate(report.get("where", []), start=1):
        lines.append(f"{index}. {item}")
    lines.append("")
    lines.append("## Secrets 4개")
    lines.append("")
    for index, key in enumerate(report.get("secrets", []), start=1):
        lines.append(f"{index}. `{key}`")
    lines.append("")
    lines.append("## Variables")
    lines.append("")
    for index, item in enumerate(report.get("variables", []), start=1):
        lines.append(f"{index}. `{item.get('key')}={item.get('value')}`")
    lines.append("")
    lines.append("## 나중에 붙일 것")
    lines.append("")
    for item in report.get("later", []):
        lines.append(f"- `{item}`")
    lines.append("")
    lines.append("## Variables 복붙용")
    lines.append("")
    lines.append("```text")
    for item in report.get("copy_block", []):
        lines.append(item)
    lines.append("```")
    lines.append("")
    lines.append("## Next")
    lines.append("")
    lines.append(f"- {report.get('next_action', '')}")
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
