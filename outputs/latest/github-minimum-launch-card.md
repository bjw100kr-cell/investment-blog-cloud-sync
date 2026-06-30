# GitHub Minimum Launch Card

무료 클라우드 자동화를 붙일 때 지금 바로 따라가면 되는 최소 실행 카드입니다.

- repo_connected: `True`
- github_status: `needs_gh_cli`
- repo_slug: `bjw100kr-cell/investment-blog-cloud-sync`
- 지금 필요한 Secrets 수: `4`
- 지금 필요한 Variables 수: `8`
- WordPress 지금 필수 여부: `False`
- OpenAI 지금 필수 여부: `False`
- 첫 목표: GitHub Actions에서 Blogger 자동 업로드/공개가 정상적으로 동작하는지 확인

## Links

- repo_create_link: https://github.com/bjw100kr-cell/investment-blog-cloud-sync
- actions_secrets_link: https://github.com/bjw100kr-cell/investment-blog-cloud-sync/settings/secrets/actions
- workflow_run_link: https://github.com/bjw100kr-cell/investment-blog-cloud-sync/actions/workflows/daily-investment-intake.yml

## Steps

1. GitHub에서 새 public repo를 만듭니다.
2. 로컬에서 `bash scripts/bootstrap_github_remote.sh <OWNER/REPO>` 를 실행합니다.
3. GitHub 웹 UI에서 Secrets 4개와 Variables 7개만 먼저 입력합니다.
4. Actions에서 `Daily Investment Intake`를 수동 실행합니다.
5. Blogger draft가 1건만 안전모드로 생성됐는지 확인합니다.

## Reference

- web checklist: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/github-web-launch-checklist.md`
- values card: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/first-run-values-card.md`
