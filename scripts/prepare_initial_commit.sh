#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "This folder is not a git repository."
  exit 1
fi

if [[ -f ".env" ]]; then
  git check-ignore -q .env || {
    echo ".env is not ignored yet. Refusing to proceed to avoid committing secrets."
    echo "Add .env to .gitignore first, then rerun."
    exit 1
  }
fi

git add .

if [[ -f ".env" ]]; then
  git reset -- .env >/dev/null 2>&1 || true
fi

if git diff --cached --quiet; then
  echo "No staged changes. Nothing to commit."
  exit 0
fi

git commit -m "chore: initialize investment blog cloud sync"

cat <<'EOF'

Initial commit created.

Next steps:
1. Create a GitHub repository, preferably named investment-blog-cloud-sync
2. Connect and push in one step:
   bash scripts/bootstrap_github_remote.sh <OWNER/REPO>
3. Check local readiness:
   python3 scripts/check_setup.py
4. Add GitHub Actions secrets and run the workflow once

EOF
