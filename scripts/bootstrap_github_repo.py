#!/usr/bin/env python3
"""Bootstrap a GitHub repository with minimal token-based flow and then call the existing push script."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
from pathlib import Path
from typing import Optional
from urllib import error, request


ROOT = Path(__file__).resolve().parents[1]
BOOTSTRAP_SCRIPT = ROOT / "scripts" / "bootstrap_github_remote.sh"


def parse_repo_spec(spec: str) -> tuple[str, str]:
    repo = spec.strip()
    if "/" in repo and not repo.startswith("git@") and repo.startswith("https://"):
        parts = repo.replace("https://github.com/", "").replace(".git", "").split("/")
        if len(parts) == 2:
            return parts[0], parts[1]

    if "/" in repo and ":" in repo and repo.startswith("git@github.com:"):
        repo = repo.split(":", 1)[1]
    if repo.endswith(".git"):
        repo = repo[: -len(".git")]

    if "/" not in repo:
        raise ValueError("repo argument must be OWNER/REPO, git@github.com:OWNER/REPO.git, or full https URL")

    owner, repo_name = repo.split("/", 1)
    if not owner or not repo_name:
        raise ValueError("OWNER/REPO could not be parsed")
    return owner, repo_name


def get_token() -> Optional[str]:
    for key in ("GITHUB_TOKEN", "GH_TOKEN", "GITHUB_PAT"):
        value = os.getenv(key, "").strip()
        if value:
            return value
    return None


def github_request(method: str, url: str, token: str, payload: Optional[dict] = None) -> tuple[int, dict]:
    body = None
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "User-Agent": "investment-blog-bootstrap",
    }
    if payload is not None:
        body = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"

    req = request.Request(url=url, data=body, method=method.upper(), headers=headers)
    try:
        with request.urlopen(req, timeout=15) as resp:
            status = getattr(resp, "status", 200)
            text = resp.read().decode("utf-8")
            data = json.loads(text) if text else {}
            return status, data
    except error.HTTPError as exc:
        text = exc.read().decode("utf-8") if exc.fp else "{}"
        try:
            data = json.loads(text or "{}")
        except Exception:
            data = {"raw": text}
        return exc.code, data


def get_authenticated_user(token: str) -> str:
    status, data = github_request("GET", "https://api.github.com/user", token)
    if status != 200:
        raise RuntimeError(f"Cannot verify GitHub user: status={status}, data={data}")
    login = str(data.get("login", "")).strip()
    if not login:
        raise RuntimeError("Authenticated user login is missing from API response")
    return login


def ensure_repo(owner: str, repo: str, token: str) -> tuple[bool, str]:
    owner = owner.lower()
    status, data = github_request("GET", f"https://api.github.com/repos/{owner}/{repo}", token)
    if status == 200:
        return True, f"Repo already exists: https://github.com/{owner}/{repo}"

    if status not in {404}:
        return False, f"Cannot check existing repo: {status} {data}"

    payload = {
        "name": repo,
        "private": False,
        "auto_init": False,
    }
    try:
        current_user = get_authenticated_user(token)
    except Exception as exc:
        return False, f"Auth check failed: {exc}"

    if owner.lower() == current_user.lower():
        create_url = "https://api.github.com/user/repos"
    else:
        create_url = f"https://api.github.com/orgs/{owner}/repos"
    create_status, create_data = github_request("POST", create_url, token, payload)
    if create_status == 201:
        return True, f"Repo created: https://github.com/{owner}/{repo}"

    if create_status == 422 and isinstance(create_data, dict) and "already exists" in str(create_data).lower():
        return True, f"Repo exists or is reserved: https://github.com/{owner}/{repo}"

    return False, f"Repo create failed: status={create_status}, response={create_data}"


def run_bootstrap(owner: str, repo: str, token: str) -> int:
    env = os.environ.copy()
    env["GITHUB_TOKEN"] = token
    cmd = ["bash", str(BOOTSTRAP_SCRIPT), f"{owner}/{repo}"]
    completed = subprocess.run(cmd, cwd=ROOT, env=env, capture_output=True, text=True)
    if completed.stdout:
        print(completed.stdout)
    if completed.stderr:
        print(completed.stderr)
    return completed.returncode


def main() -> int:
    parser = argparse.ArgumentParser(description="Create GitHub repo (if possible) and bind origin via bootstrap_github_remote.sh.")
    parser.add_argument("owner_repo", help="OWNER/REPO, git@github.com:OWNER/REPO.git, or https URL")
    parser.add_argument("--skip-push", action="store_true", help="Create/check repo only; skip bootstrap remote/push")
    args = parser.parse_args()

    try:
        owner, repo = parse_repo_spec(args.owner_repo)
    except ValueError as exc:
        print(f"invalid repo spec: {exc}")
        return 2

    token = get_token()
    if not token:
        print("No GitHub token env found (GITHUB_TOKEN / GH_TOKEN / GITHUB_PAT).")
        print("Use one of these after creating the repo in browser:")
        print("- export GITHUB_TOKEN=ghp_...")
        print("- OR set GH_TOKEN / GITHUB_PAT")
        print("- then run: bash scripts/bootstrap_github_remote.sh {owner}/{repo}".format(owner=owner, repo=repo))
        print("- create repo shortcut: https://github.com/new")
        return 1

    ok, message = ensure_repo(owner, repo, token)
    print(message)
    if not ok:
        return 2

    if args.skip_push:
        print(f"Repo check/create finished for https://github.com/{owner}/{repo}. Bootstrap push was skipped by flag.")
        return 0

    print("Running push bootstrap...")
    return run_bootstrap(owner, repo, token)


if __name__ == "__main__":
    raise SystemExit(main())
