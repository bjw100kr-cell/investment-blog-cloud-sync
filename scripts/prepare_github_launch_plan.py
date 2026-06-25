#!/usr/bin/env python3
import json
import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SETUP_JSON = ROOT / "outputs/latest/setup-check-report.json"
SYNC_GUIDE_JSON_SOURCE = ROOT / "outputs/latest/github-actions-sync.md"
OUTPUT_JSON = ROOT / "outputs/latest/github-launch-plan.json"
OUTPUT_MD = ROOT / "outputs/latest/github-launch-plan.md"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


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


def repo_slug_from_origin(origin: str) -> str:
    if not origin or origin == "(not configured)":
        return ""
    if origin.startswith("git@github.com:"):
        return origin.replace("git@github.com:", "", 1).removesuffix(".git")
    if origin.startswith("https://github.com/"):
        return origin.replace("https://github.com/", "", 1).removesuffix(".git")
    return ""


def build_plan() -> dict:
    setup = load_json(SETUP_JSON)
    origin = ((setup.get("git") or {}).get("origin") or "").strip()
    repo_slug = repo_slug_from_origin(origin)
    gh_installed = shutil.which("gh") is not None
    current_branch = git_value(["branch", "--show-current"]) or "main"
    has_commit = bool(git_value(["rev-parse", "--verify", "HEAD"]))
    env_filled = set(setup.get("env_keys_filled", []))
    sync_ready_keys = [
        key
        for key in [
            "BLOGGER_BLOG_ID",
            "GOOGLE_CLIENT_ID",
            "GOOGLE_CLIENT_SECRET",
            "GOOGLE_REFRESH_TOKEN",
        ]
        if key in env_filled
    ]
    sync_optional_keys = ["OPENAI_API_KEY"] if "OPENAI_API_KEY" in env_filled else []

    if not has_commit:
        status = "needs_initial_commit"
    elif not repo_slug:
        status = "needs_repo_creation"
    elif not gh_installed:
        status = "needs_gh_cli"
    else:
        status = "ready_for_actions_sync"

    steps = [
        {
            "title": "초기 커밋 생성",
            "done": has_commit,
            "details": [
                "bash scripts/prepare_initial_commit.sh",
                ".env 는 .gitignore에 포함되어 커밋 대상에서 제외됩니다.",
            ],
        },
        {
            "title": "GitHub 저장소 생성",
            "done": bool(repo_slug),
            "details": [
                "https://github.com/new 에서 새 public repository 생성",
                "추천 이름: investment-blog-cloud-sync",
            ],
        },
        {
            "title": "원격 저장소 연결",
            "done": bool(repo_slug),
            "details": [
                f"현재 브랜치: {current_branch}",
                "bash scripts/bootstrap_github_remote.sh <YOUR_GITHUB_REPO_URL>",
            ],
        },
        {
            "title": "GitHub CLI 로그인",
            "done": False,
            "details": [
                "gh auth login",
                f"gh 설치 여부: {'yes' if gh_installed else 'no'}",
                "gh가 없으면 GitHub 웹 UI에서 Secrets and variables를 수동 입력해도 됩니다.",
            ],
        },
        {
            "title": "Actions Secrets/Variables 동기화",
            "done": False,
            "details": [
                "bash outputs/latest/github-actions-sync.sh OWNER/REPO",
                f"현재 로컬에서 즉시 동기화 가능한 핵심 키 수: {len(sync_ready_keys)}",
            ],
        },
        {
            "title": "Actions 첫 실행",
            "done": False,
            "details": [
                "GitHub -> Actions -> Daily Investment Intake -> Run workflow",
                "첫 실행은 안전모드 max_posts_per_run=1 유지",
            ],
        },
    ]

    return {
        "status": status,
        "repo_connected": bool(repo_slug),
        "repo_slug": repo_slug,
        "current_branch": current_branch,
        "has_commit": has_commit,
        "gh_installed": gh_installed,
        "sync_ready_keys": sync_ready_keys,
        "sync_optional_keys": sync_optional_keys,
        "sync_guide_path": str(SYNC_GUIDE_JSON_SOURCE),
        "steps": steps,
    }


def write_markdown(plan: dict) -> None:
    lines = []
    lines.append("# GitHub Launch Plan")
    lines.append("")
    lines.append(f"- status: `{plan.get('status', 'unknown')}`")
    lines.append(f"- repo_connected: `{plan.get('repo_connected', False)}`")
    lines.append(f"- repo_slug: `{plan.get('repo_slug', '') or 'OWNER/REPO 필요'}`")
    lines.append(f"- current_branch: `{plan.get('current_branch', 'main')}`")
    lines.append(f"- gh_installed: `{plan.get('gh_installed', False)}`")
    lines.append(f"- has_commit: `{plan.get('has_commit', False)}`")
    lines.append("")
    lines.append("## Sync Ready Keys")
    lines.append("")
    sync_ready_keys = plan.get("sync_ready_keys", [])
    sync_optional_keys = plan.get("sync_optional_keys", [])
    if sync_ready_keys:
        for key in sync_ready_keys:
            lines.append(f"- `{key}`")
    else:
        lines.append("- 아직 GitHub로 넘길 핵심 키가 채워지지 않았습니다.")
    lines.append("")
    lines.append("## Optional Sync Keys")
    if sync_optional_keys:
        for key in sync_optional_keys:
            lines.append(f"- `{key}`")
    else:
        lines.append("- `OPENAI_API_KEY`")
    lines.append("")
    lines.append("## Step Sequence")
    lines.append("")
    for index, step in enumerate(plan.get("steps", []), start=1):
        state = "done" if step.get("done") else "pending"
        lines.append(f"{index}. {step.get('title')} [{state}]")
        for detail in step.get("details", []):
            lines.append(f"   - {detail}")
    lines.append("")
    lines.append("## Recommended Commands")
    lines.append("")
    lines.append("- `bash scripts/prepare_initial_commit.sh`")
    lines.append("- `bash scripts/bootstrap_github_remote.sh <YOUR_GITHUB_REPO_URL>`")
    lines.append("- `gh auth login`")
    lines.append("- `bash outputs/latest/github-actions-sync.sh OWNER/REPO`")
    lines.append("")
    OUTPUT_MD.write_text("\n".join(lines) + "\n")


def main() -> int:
    plan = build_plan()
    OUTPUT_JSON.write_text(json.dumps(plan, ensure_ascii=False, indent=2))
    write_markdown(plan)
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
