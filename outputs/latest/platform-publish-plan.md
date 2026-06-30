# Platform Publish Plan

- automation_policy: `automation-first`
- primary_channel: `blogger`
- secondary_channel: `wordpress`
- user confirmation policy: `upload blocked until you confirm the draft`
- user_confirmed_all: `False`
- user_confirmed_keywords: `["bitcoin"]`
- user_confirmed_ready_count: `0`
- quality_ready_count: `8`
- freshness policy: `stale source evidence is excluded from upload candidates until refreshed`

## blogger

- ready: `True`
- ready_item_count: `0`
- command: `python3 scripts/upload_blogger_drafts.py`
- first_item: 없음

- 사용자 최종 확인을 마친 업로드 후보가 아직 없습니다.

## wordpress

- ready: `False`
- ready_item_count: `0`
- command: `python3 scripts/upload_wordpress_drafts.py`
- first_item: 없음

- 사용자 최종 확인을 마친 업로드 후보가 아직 없습니다.
