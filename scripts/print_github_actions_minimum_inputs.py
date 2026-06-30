#!/usr/bin/env python3
import argparse
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENV_PATH = ROOT / ".env"
OUTPUT_PATH = ROOT / "outputs/latest/login-launch-checklist.md"

REQUIRED_SECRETS = [
    "BLOGGER_BLOG_ID",
    "GOOGLE_CLIENT_ID",
    "GOOGLE_CLIENT_SECRET",
    "GOOGLE_REFRESH_TOKEN",
]

REQUIRED_VARIABLES = [
    "OPENAI_MODEL",
    "BLOGGER_SYNC_SITE_PAGES",
    "BLOGGER_SITE_PAGES_PUBLISH",
    "BLOGGER_INCLUDE_OPTIONAL_SITE_PAGES",
    "BLOGGER_REQUIRE_REVIEW_APPROVAL",
    "BLOGGER_AUTO_PUBLISH_POSTS",
    "BLOGGER_PUBLISH_ONLY_DUE_POSTS",
    "BLOGGER_MAX_POSTS_PER_RUN",
]


def parse_env(path: Path) -> dict[str, str]:
    values = {}
    if not path.exists():
        return values
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip().strip("\"'")
    return values


def repo_url() -> str:
    try:
        result = subprocess.run(["git", "remote", "get-url", "origin"], cwd=ROOT, check=True, capture_output=True, text=True)
        origin = result.stdout.strip()
    except Exception:
        return ""
    if origin.startswith("git@github.com:"):
        return "https://github.com/" + origin.replace("git@github.com:", "").removesuffix(".git")
    if origin.startswith("https://github.com/"):
        return origin.removesuffix(".git")
    return ""


def main() -> int:
    args = argparse.ArgumentParser()
    args.add_argument("--mask", action="store_true", help="Mask secret values for safer logs")
    ns = args.parse_args()

    values = parse_env(ENV_PATH)
    url = repo_url()
    actions_url = f"{url}/settings/secrets/actions" if url else "https://github.com/settings/secrets/actions"

    print("# GitHub Minimum Inputs")
    print(f"next_url={actions_url}")
    print("## Secrets")
    for key in REQUIRED_SECRETS:
        value = values.get(key, "")
        if not value:
            print(f"{key}=<MISSING>")
        elif ns.mask:
            masked = value[:6] + "..." + value[-4:]
            print(f"{key}={masked}")
        else:
            print(f"{key}={value}")

    print("## Variables")
    for key in REQUIRED_VARIABLES:
        value = values.get(key, "")
        print(f"{key}={value}")

    print("## Copy secrets block")
    print("```")
    for key in REQUIRED_SECRETS:
        value = values.get(key, "")
        if value:
            print(f"{key}={value}")
    print("```")

    print("## Copy variables block")
    print("```")
    for key in REQUIRED_VARIABLES:
        value = values.get(key, "")
        if value:
            print(f"{key}={value}")
    print("```")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
