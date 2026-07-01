# Platform Publish Plan

- automation_policy: `automation-first`
- primary_channel: `blogger`
- secondary_channel: `wordpress`
- user confirmation policy: `automatic publishing mode; quality and freshness gates still apply`
- user_confirmed_all: `False`
- user_confirmed_keywords: `["bitcoin"]`
- user_confirmed_ready_count: `6`
- quality_ready_count: `6`
- freshness policy: `stale source evidence is excluded from upload candidates until refreshed`

## blogger

- ready: `True`
- ready_item_count: `6`
- command: `python3 scripts/upload_blogger_drafts.py`
- first_item: `비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트`
- first_keyword: `bitcoin`

- `bitcoin`: 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트 / main_post / score 129.0 / quality=True / freshness=`fresh` / user_confirmed=True
- `us_index_flow`: 미국 증시 지수 흐름: 나스닥, 금리, 빅테크 실적을 같이 봐야 하는 이유 / main_post / score 120.0 / quality=True / freshness=`fresh` / user_confirmed=True
- `china`: 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유 / main_post / score 103.0 / quality=True / freshness=`` / user_confirmed=True
- `seo_china_13`: 중국 변수와 시장 영향 관련 대표 종목 한눈에 보기 / seo_followup / score 102.5 / quality=True / freshness=`` / user_confirmed=True
- `seo_china_14`: 중국 변수와 시장 영향 공급망 정리: 누가 수혜를 보나 / seo_followup / score 99.5 / quality=True / freshness=`` / user_confirmed=True

## wordpress

- ready: `False`
- ready_item_count: `6`
- command: `python3 scripts/upload_wordpress_drafts.py`
- first_item: `비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트`
- first_keyword: `bitcoin`

- `bitcoin`: 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트 / main_post / score 129.0 / quality=True / freshness=`fresh` / user_confirmed=True
- `us_index_flow`: 미국 증시 지수 흐름: 나스닥, 금리, 빅테크 실적을 같이 봐야 하는 이유 / main_post / score 120.0 / quality=True / freshness=`fresh` / user_confirmed=True
- `china`: 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유 / main_post / score 103.0 / quality=True / freshness=`` / user_confirmed=True
- `seo_china_13`: 중국 변수와 시장 영향 관련 대표 종목 한눈에 보기 / seo_followup / score 102.5 / quality=True / freshness=`` / user_confirmed=True
- `seo_china_14`: 중국 변수와 시장 영향 공급망 정리: 누가 수혜를 보나 / seo_followup / score 99.5 / quality=True / freshness=`` / user_confirmed=True
