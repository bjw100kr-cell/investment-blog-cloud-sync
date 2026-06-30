# First Blogger Verify Flow

사용자 확인 뒤 로컬 Blogger draft 검증까지 바로 이어지는 최소 실행 흐름입니다.

- apply_mode: `False`
- main_candidate: `bitcoin` / 비트코인 핵심 흐름 해설

## Command Chain

- `python3 /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- `python3 scripts/build_platform_publish_plan.py`
- `python3 scripts/upload_blogger_drafts.py`

## How To Use

- preview: `python3 scripts/run_first_blogger_verify_flow.py`
- apply: `python3 scripts/run_first_blogger_verify_flow.py --apply`
- apply_skip_approval: `python3 scripts/run_first_blogger_verify_flow.py --apply --skip-approval`
- apply_with_safety_check: `python3 scripts/run_first_blogger_verify_flow.py --apply --run-safety-check`
