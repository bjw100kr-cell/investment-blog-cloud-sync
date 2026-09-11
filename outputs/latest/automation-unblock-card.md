# Automation Unblock Card

지금 자동화를 더 앞으로 밀기 위해 사용자 쪽에서 필요한 건 사실 2개입니다.

- main_candidate: `fomc` / FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지

## 지금 할 2개

- `1. fomc 승인`
  - why: 이 1건만 승인되면 Blogger draft loop 실검증으로 바로 넘어갈 수 있습니다.
  - command: python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords fomc
- `2. GitHub repo 연결`
  - why: 이 단계가 끝나야 컴퓨터가 꺼져 있어도 무료 클라우드 자동화가 돌아갑니다.
  - repo_create_link: https://github.com/bjw100kr-cell/investment-blog-cloud-sync
  - web_checklist_md: /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/github-web-launch-checklist.md

## 나중에 해도 되는 것

- `WordPress 연결` / status `blocked`
  - why: Blogger 루프 검증 뒤 붙여도 늦지 않습니다.
- `Search Console / GA4 / AdSense` / status `later`
  - why: 수익화 측정 고도화 단계이며 지금 당장 첫 자동화 검증의 선행조건은 아닙니다.

## Shortcut Flow

- preview: `python3 scripts/run_minimum_unblock_flow.py`
- preview_with_repo: `python3 scripts/run_minimum_unblock_flow.py --repo OWNER/REPO`
- apply_with_repo: `python3 scripts/run_minimum_unblock_flow.py --repo OWNER/REPO --apply`

## References

- `automation_progress_board_md`: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/automation-progress-board.md`
- `first_approval_path_md`: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/first-approval-path.md`
- `github_minimum_launch_card_md`: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/github-minimum-launch-card.md`
- `minimum_unblock_flow_md`: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/minimum-unblock-flow.md`
