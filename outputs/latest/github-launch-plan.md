# GitHub Launch Plan

- status: `needs_initial_commit`
- repo_connected: `False`
- repo_slug: `OWNER/REPO 필요`
- current_branch: `main`
- gh_installed: `False`
- has_commit: `False`

## Sync Ready Keys

- `BLOGGER_BLOG_ID`

## Optional Sync Keys
- `OPENAI_API_KEY`

## Step Sequence

1. 초기 커밋 생성 [pending]
   - bash scripts/prepare_initial_commit.sh
   - .env 는 .gitignore에 포함되어 커밋 대상에서 제외됩니다.
2. GitHub 저장소 생성 [pending]
   - https://github.com/new 에서 새 public repository 생성
   - 추천 이름: investment-blog-cloud-sync
3. 원격 저장소 연결 [pending]
   - 현재 브랜치: main
   - bash scripts/bootstrap_github_remote.sh <YOUR_GITHUB_REPO_URL>
4. GitHub CLI 로그인 [pending]
   - gh auth login
   - gh 설치 여부: no
   - gh가 없으면 GitHub 웹 UI에서 Secrets and variables를 수동 입력해도 됩니다.
5. Actions Secrets/Variables 동기화 [pending]
   - bash outputs/latest/github-actions-sync.sh OWNER/REPO
   - 현재 로컬에서 즉시 동기화 가능한 핵심 키 수: 1
6. Actions 첫 실행 [pending]
   - GitHub -> Actions -> Daily Investment Intake -> Run workflow
   - 첫 실행은 안전모드 max_posts_per_run=1 유지

## Recommended Commands

- `bash scripts/prepare_initial_commit.sh`
- `bash scripts/bootstrap_github_remote.sh <YOUR_GITHUB_REPO_URL>`
- `gh auth login`
- `bash outputs/latest/github-actions-sync.sh OWNER/REPO`

