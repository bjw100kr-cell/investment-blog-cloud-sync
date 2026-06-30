# First Cloud Run Verification

- all_core_checks_passed: `False`

## Core Checks

- `workflow_snapshot_generated`: True
  - success_condition: review-packet.json 이 생성되어 있어야 함
- `approval_dashboard_generated`: True
  - success_condition: approval-dashboard.json 이 생성되어 있어야 함
- `platform_publish_plan_generated`: True
  - success_condition: platform-publish-plan.json 이 생성되어 있어야 함
- `review_approval_state_is_safe`: False
  - success_condition: 첫 클라우드 런 전에는 review-approvals.json 의 사용자 최종 확인 목록이 비어 있어야 함
- `blogger_report_matches_current_approval_file`: True
  - success_condition: blogger-upload-report summary 가 현재 사용자 최종 확인 상태와 일치해야 함
- `blogger_safely_blocked_without_approval`: False
  - success_condition: 사용자 최종 확인 전에는 Blogger 업로드가 awaiting_user_review_approval 로 차단되어야 함
- `wordpress_not_accidentally_publishing`: True
  - success_condition: WordPress 미연결 상태에서는 credentials_missing_dry_run 이거나 업로드 시도가 없어야 함
- `repo_prereq_still_visible`: True
  - success_condition: 성공 게이트에서 GitHub 연결 상태가 계속 드러나야 함

## Quick Read

- review_item_count: `13`
- approval_dashboard_count: `13`
- review_approval_state: `{"user_confirmed_all": false, "user_confirmed_keywords": ["bitcoin"]}`
- channel `blogger`: ready=True / ready_item_count=1
- channel `wordpress`: ready=False / ready_item_count=1
- blogger_summary: `{"processed_count": 3, "auto_publish": true, "publish_due_only": false, "max_posts_per_run": 3, "allow_reupload_same_content": false, "review_required": false, "approval_file_present": true, "user_final_confirmation_required": true, "user_confirmed_all": false, "user_confirmed_keywords": ["bitcoin"], "approved_all": false, "approved_keywords": ["bitcoin"], "quality_gate_blocked": []}`
- wordpress_summary: `{"processed_count": 0, "auto_publish": false, "publish_due_only": true, "max_posts_per_run": 1, "manifest_candidate_count": 13, "review_required": true}`

## Next Manual Checks

- GitHub Actions 실행 로그에서 failed step 이 없는지 확인
- outputs/latest/review-packet.md 가 최신 스냅샷으로 커밋됐는지 확인
- Blogger 초안이 승인 전 업로드되지 않았는지 확인
