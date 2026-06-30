# GitHub Launch Plan

- status: `needs_gh_cli`
- repo_connected: `True`
- repo_accessible: `True`
- repo_slug: `bjw100kr-cell/investment-blog-cloud-sync`
- current_branch: `main`
- gh_installed: `False`
- has_commit: `True`

## Sync Ready Keys

- `BLOGGER_BLOG_ID`
- `GOOGLE_CLIENT_ID`
- `GOOGLE_CLIENT_SECRET`
- `GOOGLE_REFRESH_TOKEN`

## Optional Sync Keys
- `OPENAI_API_KEY`

## Step Sequence

1. 초기 커밋 생성 [done]
   - bash scripts/prepare_initial_commit.sh
   - .env 는 .gitignore에 포함되어 커밋 대상에서 제외됩니다.
2. GitHub 저장소 생성 [done]
   - https://github.com/new 에서 새 public repository 생성
   - 추천 이름: investment-blog-cloud-sync
3. 원격 저장소 연결 [done]
   - 현재 브랜치: main
   - bash scripts/bootstrap_github_repo.py <OWNER/REPO> (토큰 있으면 생성+연결+푸시 한 번에)
   - 토큰이 없으면: https://github.com/new 에서 생성 후 `bash scripts/bootstrap_github_remote.sh <OWNER/REPO>`
4. GitHub CLI 로그인 (선택) [pending]
   - gh auth login
   - gh 설치 여부: no
   - gh가 없으면 GitHub 웹 UI에서 Secrets and variables를 수동 입력해도 됩니다.
5. Actions Secrets/Variables 입력 [pending]
   - 웹 UI 수동 입력: github-web-launch-checklist.md
   - 현재 로컬에서 즉시 동기화 가능한 핵심 키 수: 4
   - WordPress를 쓸 경우 WORDPRESS_SITE_URL / WORDPRESS_USERNAME / WORDPRESS_APPLICATION_PASSWORD도 함께 동기화
6. Actions 첫 실행 [pending]
   - GitHub -> Actions -> Daily Investment Intake -> Run workflow
   - 첫 실행은 Blogger/WordPress 모두 안전모드 max_posts_per_run=1 유지

## Recommended Commands

- `bash scripts/prepare_initial_commit.sh`
- `bash scripts/bootstrap_github_repo.py OWNER/REPO`
   (토큰이 없으면 기존 방식: `bash scripts/bootstrap_github_remote.sh <OWNER/REPO>` + 웹 브라우저에서 repo 생성)
- `gh auth login` (선택)
- `bash outputs/latest/github-actions-sync.sh OWNER/REPO` (gh 사용 시)

## Cloud Notes

- GitHub Actions 워크플로우는 Blogger와 WordPress 업로드를 모두 지원합니다.
- 승인된 글만 실제 업로드되므로 review approval 파일이 비어 있으면 클라우드에서도 업로드는 건너뜁니다.
- 웹 UI로 진행할 때는 `/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/github-web-launch-checklist.md`를 같이 보면 됩니다.
- 첫 실행 후 검증은 `/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/first-cloud-run-verification.md` 기준으로 확인하면 됩니다.

