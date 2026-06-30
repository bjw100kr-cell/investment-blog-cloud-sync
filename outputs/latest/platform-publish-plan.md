# Platform Publish Plan

- automation_policy: `automation-first`
- primary_channel: `blogger`
- secondary_channel: `wordpress`
- user confirmation policy: `upload blocked until you confirm the draft`
- user_confirmed_all: `False`
- user_confirmed_keywords: `["bitcoin"]`
- user_confirmed_ready_count: `1`
- quality_ready_count: `12`
- freshness policy: `stale source evidence is excluded from upload candidates until refreshed`

## blogger

- ready: `True`
- ready_item_count: `1`
- command: `python3 scripts/upload_blogger_drafts.py`
- first_item: `비트코인 핵심 흐름 해설`
- first_keyword: `bitcoin`

- `bitcoin`: 비트코인 핵심 흐름 해설 / main_post / score 121.0 / quality=True / freshness=`fresh` / user_confirmed=True

## wordpress

- ready: `False`
- ready_item_count: `1`
- command: `python3 scripts/upload_wordpress_drafts.py`
- first_item: `비트코인 핵심 흐름 해설`
- first_keyword: `bitcoin`

- `bitcoin`: 비트코인 핵심 흐름 해설 / main_post / score 121.0 / quality=True / freshness=`fresh` / user_confirmed=True
