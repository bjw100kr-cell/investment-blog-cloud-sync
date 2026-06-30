#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ENV_EXAMPLE = ROOT / ".env.example"
CHECK_REPORT = ROOT / "outputs/latest/setup-check-report.json"
OUTPUT_MD = ROOT / "outputs/latest/github-secrets-checklist.md"

SECRET_KEYS = {
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
}

VARIABLE_KEYS = {
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
}


def parse_env_keys(path: Path) -> list[str]:
    keys = []
    if not path.exists():
        return keys
    for raw_line in path.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _ = line.split("=", 1)
        keys.append(key.strip())
    return keys


def load_check_report(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def main() -> int:
    keys = parse_env_keys(ENV_EXAMPLE)
    report = load_check_report(CHECK_REPORT)
    integrations = {item["name"]: item for item in report.get("integrations", [])}

    lines = []
    lines.append("# GitHub Secrets / Variables 체크리스트")
    lines.append("")
    lines.append("- 위치: `GitHub -> Settings -> Secrets and variables -> Actions`")
    lines.append("- 목적: 로컬 `.env`와 별개로 클라우드 실행용 값을 GitHub에 입력")
    lines.append("")

    lines.append("## Secrets")
    lines.append("")
    for key in keys:
        if key in SECRET_KEYS:
            lines.append(f"- [ ] {key}")
    lines.append("")

    lines.append("## Variables")
    lines.append("")
    for key in keys:
        if key in VARIABLE_KEYS:
            lines.append(f"- [ ] {key}")
    lines.append("")

    lines.append("## 수익화/분석 스택")
    lines.append("")
    lines.append("- [ ] GA4_MEASUREMENT_ID 변수 입력")
    lines.append("- [ ] ADSENSE_PUBLISHER_ID 변수 입력")
    lines.append("- [ ] ADSENSE_SITE_VERIFICATION 변수 입력")
    lines.append("- [ ] NEWSLETTER_SUBSCRIBE_URL 변수 입력")
    lines.append("")

    lines.append("## 통합별 최소 조건")
    lines.append("")
    for name in ["naver_datalab", "search_console", "openai_drafts", "blogger_upload", "wordpress_upload"]:
        item = integrations.get(name, {})
        missing = item.get("missing", [])
        lines.append(f"- {name}: {'ready' if item.get('ready') else 'missing ' + ', '.join(missing)}")
    lines.append("")

    lines.append("## 추천 입력 순서")
    lines.append("")
    lines.append("- [ ] OPENAI_MODEL 변수 입력")
    lines.append("- [ ] OPENAI_API_KEY 시크릿 입력")
    lines.append("- [ ] GOOGLE_CLIENT_ID / GOOGLE_CLIENT_SECRET 입력")
    lines.append("- [ ] GOOGLE_REFRESH_TOKEN 입력")
    lines.append("- [ ] BLOGGER_BLOG_ID 입력")
    lines.append("- [ ] BLOGGER_SYNC_SITE_PAGES / BLOGGER_SITE_PAGES_PUBLISH 변수 입력")
    lines.append(
        "- [ ] BLOGGER_REQUIRE_REVIEW_APPROVAL / BLOGGER_AUTO_PUBLISH_POSTS / "
        "BLOGGER_PUBLISH_ONLY_DUE_POSTS / BLOGGER_MAX_POSTS_PER_RUN 변수 입력"
    )
    lines.append("- [ ] WORDPRESS_SITE_URL / WORDPRESS_USERNAME / WORDPRESS_APPLICATION_PASSWORD 입력")
    lines.append("- [ ] WORDPRESS_AUTO_PUBLISH_POSTS / WORDPRESS_PUBLISH_ONLY_DUE_POSTS / WORDPRESS_MAX_POSTS_PER_RUN 변수 입력")
    lines.append("- [ ] BLOG_BASE_URL 변수 입력 (선택)")
    lines.append("- [ ] GA4_MEASUREMENT_ID 입력")
    lines.append("- [ ] ADSENSE_PUBLISHER_ID / ADSENSE_SITE_VERIFICATION 입력")
    lines.append("- [ ] NEWSLETTER_SUBSCRIBE_URL 입력")
    lines.append("- [ ] SEARCH_CONSOLE_SITE_URL 입력")
    lines.append("- [ ] SEARCH_CONSOLE_CLIENT_ID / SEARCH_CONSOLE_CLIENT_SECRET / SEARCH_CONSOLE_REFRESH_TOKEN 입력")
    lines.append("- [ ] NAVER_CLIENT_ID / NAVER_CLIENT_SECRET 입력")
    lines.append("")

    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
