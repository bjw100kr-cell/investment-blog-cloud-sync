# Launch Bundle Report

## Automation Snapshot
- primary channel now: `blogger`
- secondary channel later: `wordpress`
- manual-only channels: `naver_blog, tistory`
- ready for first live run: `no`
- repo connected: `no`
- first live status: `needs_preflight_review`
- GitHub launch status: `needs_repo_creation`
- approved upload candidates right now: `1`
- review gate still blocking uploads: `no`

## Integration Status
Ready integrations
- `blogger_upload`

Blocked integrations
- `naver_datalab (NAVER_CLIENT_ID, NAVER_CLIENT_SECRET)`
- `search_console (SEARCH_CONSOLE_SITE_URL)`
- `openai_drafts (OPENAI_API_KEY)`
- `wordpress_upload (WORDPRESS_SITE_URL, WORDPRESS_USERNAME, WORDPRESS_APPLICATION_PASSWORD)`

## Pipeline Parity
- all_core_scripts_present: `yes`
- order_aligned: `yes`
- missing_in_workflow: `none`
- missing_in_pipeline: `none`
- parity report: `outputs/latest/pipeline-workflow-parity.md`

## Today Approval Focus
- top single approval: `bitcoin` -> `비트코인 핵심 흐름 해설`
- top batch approval: `bitcoin`
- user review shortlist:
- `비트코인 핵심 흐름 해설` | keyword `bitcoin` | verdict `approve`
- `중국 변수와 시장 영향 해설` | keyword `china` | verdict `approve`
- `FOMC 이후 시장 해설` | keyword `fomc` | verdict `approve`

## Revenue Path
- `main_post`: `비트코인 핵심 흐름 해설` | `페이지뷰와 체류시간 균형 확보`
- `seo_followup`: `비트코인 핵심 흐름 초보자 가이드: 지금 꼭 알아야 할 핵심 구조` | `초보 검색 유입과 긴 체류시간 확보`
- `next_slot`: `중국 변수와 시장 영향 해설` | `페이지뷰와 체류시간 균형 확보`

## Next Commands After Approval
- `python3 scripts/set_review_approvals.py --keywords bitcoin`
- `python3 scripts/build_platform_publish_plan.py`
- `python3 scripts/upload_blogger_drafts.py`
- `python3 scripts/prepare_first_cloud_run_verification.py --allow-approved-state`

## Current Blockers
- GitHub repo is not connected yet, so cloud automation cannot continue after local preparation.
- Search Console site URL is still missing, so keyword refinement is still using fallback signals.
- OpenAI API key is missing, so paid human-tone draft expansion remains disabled.

## Roadmap
- `phase_1_validate_blogger`: `게시 파이프라인이 실제로 하루 1건씩 안전하게 돌아가는지 확인`
- `phase_2_repeatable_content_loop`: `검색 유입용 메인 글과 후속 SEO 글이 반복 루프로 굴러가는지 확인`
- `phase_3_measurement_stack`: `어떤 글이 실제 체류시간과 재방문을 만드는지 측정`
- `phase_4_retention_stack`: `유입을 재방문으로 바꾸는 장치 추가`

## Refresh Result
- all automation-focused refresh steps completed successfully

## Refreshed Files
- `outputs/latest/automation-scope.md`
- `outputs/latest/current-reference-strategy.md`
- `outputs/latest/reference-strength-benchmark.md`
- `outputs/latest/keyword-capture-strategy.md`
- `outputs/latest/review-packet.md`
- `outputs/latest/approval-dashboard.md`
- `outputs/latest/source-freshness-board.md`
- `outputs/latest/first-approval-path.md`
- `outputs/latest/daily-revenue-focus.md`
- `outputs/latest/traffic-cluster-board.md`
- `outputs/latest/popular-reads-board.md`
- `outputs/latest/retention-cta-board.md`
- `outputs/latest/monetization-roadmap.md`
- `outputs/latest/draft-polish-board.md`
- `outputs/latest/first-publish-operator-run.md`
- `outputs/latest/user-review-shortlist.md`
- `outputs/latest/current-review-focus.html`
- `outputs/latest/user-approval-inbox.html`
- `outputs/latest/user-review-checkpoint.html`
- `outputs/latest/github-minimum-launch-card.md`
- `outputs/latest/automation-progress-board.md`
- `outputs/latest/automation-unblock-card.md`
- `outputs/latest/minimum-unblock-flow.md`
- `outputs/latest/first-blogger-verify-card.md`
- `outputs/latest/first-blogger-verify-flow.md`
- `outputs/latest/review-preview-board.html`
- `outputs/latest/operator-home.html`
- `outputs/latest/platform-publish-plan.md`
- `outputs/latest/cross-platform-publish-pack.md`
- `outputs/latest/pre-publish-quality-gate.md`
- `outputs/latest/first-cloud-run-verification.md`
- `outputs/latest/go-live-dashboard.md`
- `outputs/latest/pipeline-workflow-parity.md`
- `outputs/latest/cloud-launch-preflight.md`
- `outputs/latest/start-here-runbook.md`
- `outputs/latest/today-operator-console.md`
