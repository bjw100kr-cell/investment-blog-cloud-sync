# Go Live Dashboard

- ready_for_first_live_run: `True`
- monetization_score: `50.0`
- repo_connected: `True`
- login_pages_count: `7`
- oauth_client_candidate_count: `0`
- publish_queue_ready_count: `4`
- publish_inventory_ready_count: `13`
- auto_channel_ready_count: `1`
- automation_policy: `automation-first`
- active_channel_now: `blogger`
- expand_channel_later: `wordpress`
- first_live_run_status: `ready_for_draft_test`
- github_launch_status: `needs_gh_cli`

## Minimum Cloud Blocker

- repo_connected: `True`
- required_secrets_count: `4`
- required_variables_count: `7`
- wordpress_required_now: `False`
- openai_required_now: `False`
- github minimum launch card: `/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/github-minimum-launch-card.md`
- user review checkpoint: `/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/user-review-checkpoint.html`
- cloud launch preflight: `/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/cloud-launch-preflight.md`
- pipeline_workflow_parity: `/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/pipeline-workflow-parity.md`
- parity_all_core_scripts_present: `True`
- parity_order_aligned: `True`

## Missing Before First Live Run

- 필수 자격값은 모두 채워졌습니다.

## Growth Gaps

- `SEARCH_CONSOLE_SITE_URL`
- `GA4_MEASUREMENT_ID`
- `ADSENSE_PUBLISHER_ID`
- `ADSENSE_SITE_VERIFICATION`
- `NEWSLETTER_SUBSCRIBE_URL`

## First Content Targets

- `fomc`
- `bitcoin`
- `us_index_flow`

## Automated Channels

- 현재 기본 운영 경로는 Blogger 단일 자동화입니다.
- WordPress는 Blogger 검증 후 두 번째 자동 채널로만 확장합니다.
- `blogger`: ready=True / approved_ready_items=1 / command `python3 scripts/upload_blogger_drafts.py`
- `wordpress`: ready=False / approved_ready_items=1 / command `python3 scripts/upload_wordpress_drafts.py`

## Daily Opportunity Board

- `fomc`: FOMC 이후 시장 해설 / urgency publish_now
- `bitcoin`: 비트코인 핵심 흐름 해설 / urgency prep_today
- `us_index_flow`: 미국 증시 지수 흐름 해설 / urgency watch

## First Page Targets

- `about`
- `disclosure`
- `privacy-policy`
- `editorial-policy`
- `contact`

## Next Commands

- `python3 scripts/export_github_actions_sync_commands.py`
- `bash scripts/run_pipeline.sh`
- `python3 scripts/resume_after_login.py`
- `python3 scripts/prepare_first_live_run_plan.py`
- `python3 scripts/prepare_github_launch_plan.py`

## First Queue Actions

- `fomc`: FOMC 이후 시장 해설 / CTA 환율·금리·미국증시 evergreen 글로 연결
- `bitcoin`: 비트코인 핵심 흐름 해설 / CTA ETF·규제·초보 가이드 글로 연결
- `us_index_flow`: 미국 증시 지수 흐름 해설 / CTA 실적·공급망·대표 종목 글로 연결

## First Approval Path

- 추천 묶음: `가장 먼저 볼 메인 글` / 1건 / command `python3 /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- 단건 추천: `bitcoin` / 비트코인 핵심 흐름 해설 / command `python3 /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`

## Daily Revenue Focus

- `main_post` / `비트코인 핵심 흐름 해설` / revenue `페이지뷰와 체류시간 균형 확보`
- `seo_followup` / `비트코인 핵심 흐름 초보자 가이드: 지금 꼭 알아야 할 핵심 구조` / revenue `초보 검색 유입과 긴 체류시간 확보`
- `next_slot` / `미국 증시 지수 흐름 해설` / revenue `페이지뷰와 체류시간 균형 확보`

## Monetization Roadmap

- `phase_1_validate_blogger` / gate `GitHub repo 연결 전후 첫 Blogger draft 검증`
- `phase_2_repeatable_content_loop` / gate `첫 draft 검증 성공 후 3~7일 운영`
- `phase_3_measurement_stack` / gate `반복 발행 루프 확인 후`

## First Publish Operator Run

- approval_mode: `auto_single`
- `python3 scripts/set_review_approvals.py --keywords bitcoin`
- `python3 scripts/build_platform_publish_plan.py`
- `python3 scripts/upload_blogger_drafts.py`
- `python3 scripts/prepare_first_cloud_run_verification.py --allow-approved-state`

## User Review Shortlist

- `비트코인 핵심 흐름 해설` / keyword `bitcoin` / verdict `approve`
- `미국 증시 지수 흐름 해설` / keyword `us_index_flow` / verdict `approve`
- `중국 변수와 시장 영향 해설` / keyword `china` / verdict `approve`

## Today Operator Console

- ready `True` / repo_connected `True` / github `needs_gh_cli`

## Next SEO Follow-ups

- `fomc` -> FOMC 이후 시장이 주식과 코인에 미치는 영향 / score 139.5
- `fomc` -> FOMC 이후 시장에서 다음으로 봐야 할 체크포인트 5가지 / score 136.5
- `fomc` -> FOMC 이후 시장 초보자 가이드: 용어부터 시장 반응까지 / score 133.5
