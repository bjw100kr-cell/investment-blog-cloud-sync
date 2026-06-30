#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

if [[ $# -lt 1 ]]; then
  cat <<'EOF'
Usage:
  bash scripts/bootstrap_github_remote.sh <GITHUB_REPO_URL>
  bash scripts/bootstrap_github_remote.sh <OWNER/REPO>

Example:
  bash scripts/bootstrap_github_remote.sh yourname/investment-blog-cloud-sync
  bash scripts/bootstrap_github_remote.sh git@github.com:yourname/investment-blog-cloud-sync.git
  bash scripts/bootstrap_github_remote.sh https://github.com/yourname/investment-blog-cloud-sync.git
EOF
  exit 1
fi

REMOTE_INPUT="$1"

if [[ "$REMOTE_INPUT" == https://github.com/* ]] || [[ "$REMOTE_INPUT" == git@github.com:* ]]; then
  REMOTE_URL="$REMOTE_INPUT"
elif [[ "$REMOTE_INPUT" == */* ]]; then
  REMOTE_URL="https://github.com/${REMOTE_INPUT}.git"
else
  echo "Unsupported remote input: $REMOTE_INPUT"
  echo "Use either OWNER/REPO or a full GitHub remote URL."
  exit 1
fi

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "This folder is not a git repository."
  exit 1
fi

if ! git rev-parse --verify HEAD >/dev/null 2>&1; then
  echo "No commit found yet. Run:"
  echo "  bash scripts/prepare_initial_commit.sh"
  exit 1
fi

CURRENT_BRANCH="$(git branch --show-current)"
if [[ -z "$CURRENT_BRANCH" ]]; then
  CURRENT_BRANCH="main"
  git checkout -b "$CURRENT_BRANCH"
fi

if [[ "$CURRENT_BRANCH" != "main" ]]; then
  git branch -M main
  CURRENT_BRANCH="main"
fi

AUTH_TOKEN="${GITHUB_TOKEN:-${GH_TOKEN:-${GITHUB_PAT:-}}}"
ORIGIN_URL="${REMOTE_URL}"
REPO_WEB="${REMOTE_URL%.git}"

if [[ -z "${AUTH_TOKEN}" ]]; then
  REPO_ACCESS_TEST="$(python3 - "$REPO_WEB" <<'PY'
import sys, urllib.request, urllib.error
url = sys.argv[1]
try:
    with urllib.request.urlopen(url, timeout=10) as response:
        print(getattr(response, "status", 200))
except Exception as exc:
    if isinstance(exc, urllib.error.HTTPError):
        print(exc.code)
        sys.exit(0)
    print("ERR")
PY
)"
  if [[ "$REPO_ACCESS_TEST" == "ERR" ]]; then
    echo "Remote URL currently not reachable: $REPO_WEB"
    echo "Please create the repository first: https://github.com/new"
    echo "Then run:"
    echo "  bash scripts/bootstrap_github_remote.sh <OWNER/REPO>"
    exit 1
  fi
  if [[ ! "$REPO_ACCESS_TEST" =~ ^[0-9]+$ ]]; then
    echo "Unexpected repo check response: $REPO_ACCESS_TEST"
    exit 1
  fi
  if (( REPO_ACCESS_TEST < 200 || REPO_ACCESS_TEST >= 400 )); then
    echo "Remote URL currently returns 404/unreachable: $REPO_WEB"
    echo "Please create the repository first: https://github.com/new"
    echo "Then run:"
    echo "  bash scripts/bootstrap_github_remote.sh <OWNER/REPO>"
    exit 1
  fi
fi

if git remote get-url origin >/dev/null 2>&1; then
  git remote set-url origin "$REMOTE_URL"
else
  git remote add origin "$REMOTE_URL"
fi

if [[ -n "$AUTH_TOKEN" ]]; then
  echo "Using token-authenticated push for origin."
  if [[ "$AUTH_TOKEN" == "dummy" ]]; then
    echo "Detected non-empty token placeholder (dummy). If this is not a real token, authentication may fail."
  fi
  SAFE_AUTH_REMOTE="https://x-access-token:${AUTH_TOKEN}@${REMOTE_URL#https://}"
  trap 'git remote set-url origin "$ORIGIN_URL"' EXIT
  git remote set-url origin "$SAFE_AUTH_REMOTE"
  git push -u origin "$CURRENT_BRANCH"
  git remote set-url origin "$ORIGIN_URL"
  trap - EXIT
else
  echo "No token env found (GITHUB_TOKEN/GH_TOKEN/GITHUB_PAT)."
  echo "Attempting interactive HTTPS push. If password/credential is required, set one of:"
  echo "  export GITHUB_TOKEN=ghp_..."
  echo "  export GH_TOKEN=ghp_..."
  echo "  export GITHUB_PAT=ghp_..."
  git push -u origin "$CURRENT_BRANCH"
fi

cat <<EOF

Remote bootstrap complete.

- branch: $CURRENT_BRANCH
- origin: $(git remote get-url origin)

Next steps:
1. Open the GitHub repository
2. Go to Settings -> Secrets and variables -> Actions
3. Add the secrets you need from .env.example
4. Run the workflow once from Actions -> Daily Investment Intake
EOF
