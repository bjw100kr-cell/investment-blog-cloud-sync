# First Publish Operator Run

사용자 최종 확인부터 Blogger 업로드 검증까지 이어지는 운영 실행 카드입니다.
사용자 확인 전에는 실제 업로드를 실행하면 안 됩니다.

- apply_mode: `False`
- approval_mode: `auto_single`
- current_user_confirmed_keywords: `["bitcoin"]`
- target_user_confirmed_keywords: `["bitcoin"]`

## Planned Commands

- `python3 scripts/set_review_approvals.py --keywords bitcoin`
- `python3 scripts/build_platform_publish_plan.py`
- `python3 scripts/upload_blogger_drafts.py`
- `python3 scripts/prepare_first_cloud_run_verification.py --allow-approved-state`

## How To Execute

- preview only: `python3 scripts/first_publish_operator_run.py`
- apply single recommendation: `python3 scripts/first_publish_operator_run.py --apply`
- apply batch recommendation: `python3 scripts/first_publish_operator_run.py --apply --approval auto_batch`
- apply manual keywords: `python3 scripts/first_publish_operator_run.py --apply --keywords bitcoin`
- shortest helper: `python3 scripts/run_minimum_unblock_flow.py --repo OWNER/REPO --apply`
