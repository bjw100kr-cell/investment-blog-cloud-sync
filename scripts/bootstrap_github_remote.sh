#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

if [[ $# -lt 1 ]]; then
  cat <<'EOF'
Usage:
  bash scripts/bootstrap_github_remote.sh <GITHUB_REPO_URL>

Example:
  bash scripts/bootstrap_github_remote.sh git@github.com:yourname/investment-blog-cloud-sync.git
  bash scripts/bootstrap_github_remote.sh https://github.com/yourname/investment-blog-cloud-sync.git
EOF
  exit 1
fi

REMOTE_URL="$1"

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

if git remote get-url origin >/dev/null 2>&1; then
  git remote set-url origin "$REMOTE_URL"
else
  git remote add origin "$REMOTE_URL"
fi

git push -u origin "$CURRENT_BRANCH"

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
