# Shortlist Publish Action Board

shortlist 글 기준으로 지금 남은 blocker와 다음 한 줄 실행만 따로 뽑은 보드입니다.
- blogger_ready: `True`
- user_confirmed_keywords: `["bitcoin"]`
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword: `bitcoin`
- publish_date: `2026-07-09`
- quality_status: `pass`
- ready_now: `True`
- hero_image_selected: `True`
- freshness_status: `fresh`
- freshness_recommendation: 사용자 검토만 통과하면 바로 게시 후보로 유지해도 됩니다.
- hard_blocking_checks: none
- advisory_checks: canonical_url_present, newsletter_ready, ga4_ready
- recovery_mode: `publish_direct`
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_action: 사용자 최종 확인 후 Blogger draft 업로드
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- followup_commands:
  - `python3 scripts/build_platform_publish_plan.py`
  - `python3 scripts/upload_blogger_drafts.py`
  - `python3 scripts/prepare_first_cloud_run_verification.py --allow-approved-state`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. 미국 증시 지수 흐름: 나스닥, 금리, 빅테크 실적을 같이 봐야 하는 이유

- keyword: `us_index_flow`
- publish_date: `2026-07-10`
- quality_status: `pass`
- ready_now: `True`
- hero_image_selected: `True`
- hard_blocking_checks: none
- advisory_checks: canonical_url_present, newsletter_ready, ga4_ready
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_index_flow`
- next_action: 사용자 최종 확인 후 Blogger draft 업로드
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_index_flow`
- followup_commands:
  - `python3 scripts/build_platform_publish_plan.py`
  - `python3 scripts/upload_blogger_drafts.py`
  - `python3 scripts/prepare_first_cloud_run_verification.py --allow-approved-state`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_index_flow`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_index_flow --apply`

## 3. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword: `china`
- publish_date: `2026-07-11`
- quality_status: `pass`
- ready_now: `True`
- hero_image_selected: `True`
- hard_blocking_checks: none
- advisory_checks: canonical_url_present, newsletter_ready, ga4_ready
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_action: 사용자 최종 확인 후 Blogger draft 업로드
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- followup_commands:
  - `python3 scripts/build_platform_publish_plan.py`
  - `python3 scripts/upload_blogger_drafts.py`
  - `python3 scripts/prepare_first_cloud_run_verification.py --allow-approved-state`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`
