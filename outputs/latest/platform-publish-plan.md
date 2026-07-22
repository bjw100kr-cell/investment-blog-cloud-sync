# Platform Publish Plan

- automation_policy: `automation-first`
- primary_channel: `blogger`
- secondary_channel: `wordpress`
- user confirmation policy: `upload blocked until you confirm the draft`
- user_confirmed_all: `False`
- user_confirmed_keywords: `["bitcoin"]`
- user_confirmed_ready_count: `1`
- quality_ready_count: `6`
- freshness policy: `stale source evidence is excluded from upload candidates until refreshed`

## blogger

- ready: `True`
- ready_item_count: `1`
- command: `python3 scripts/upload_blogger_drafts.py`
- first_item: `비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트`
- first_keyword: `bitcoin`

- `bitcoin`: 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트 / main_post / score 123.0 / quality=True / freshness=`fresh` / user_confirmed=True

## wordpress

- ready: `False`
- ready_item_count: `1`
- command: `python3 scripts/upload_wordpress_drafts.py`
- first_item: `비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트`
- first_keyword: `bitcoin`

- `bitcoin`: 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트 / main_post / score 123.0 / quality=True / freshness=`fresh` / user_confirmed=True
