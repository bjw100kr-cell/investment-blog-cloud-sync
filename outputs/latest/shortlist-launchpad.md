# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-11-29` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (extreme_fear)
- sample_headlines:
  - Bitcoin 'death cross' is coming. Here's what happened after previous 13.
  - Bitcoin on course to end seven-week losing streak while trailing stock rebound
  - Live updates: Bitcoin's Thanksgiving gains prove fleeting
- recent_evidence:
  - Investing.com Crypto News | 2026-11-28 05:56:50 | Bitcoin price falls below $60,000 as whales buy dip, ETF outflows mount
  - Cointelegraph | 2026-11-27T19:23:00+00:00 | Bitcoin whales pile into BTC despite shrinking profit cushion
  - Cointelegraph | 2026-11-27T16:48:51+00:00 | Bitcoin price drops below $59K as Anthropic joins tech stock rebound
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. 미국 증시 지수 흐름: 나스닥, 금리, 빅테크 실적을 같이 봐야 하는 이유

- keyword `us_index_flow` / publish `2026-11-30` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능
- sample_headlines:
  - What was Coinbase worth while Nasdaq was closed?
  - The S&P 500 is in a correction. Bear markets and recessions don't always follow
  - Africa’s richest man is taking his mega-refinery public in a blockbuster IPO
- recent_evidence:
  - NYT Business | 2026-11-27T22:16:28+00:00 | How to Live Calmly, Despite Stock Market Whiplash
  - Cointelegraph | 2026-11-27T14:40:54+00:00 | What was Coinbase worth while Nasdaq was closed?
  - CNBC Top News | 2026-11-27T13:21:56+00:00 | The S&P 500 is in a correction. Bear markets and recessions don't always follow
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_index_flow`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_index_flow`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_index_flow`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_index_flow --apply`

## 3. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-12-01` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - China sets March 2027 rollout for blockchain identity regulations
  - PODCAST: China boost lifts tech - Reuters
  - China stocks surge most in two years as Beijing vows stronger market support - Reuters
- recent_evidence:
  - 무역킹 Trade King YouTube | 41K | Taiwan Election Interference: Is China Aiming for Division?
  - 무역킹 Trade King YouTube | 21h ago | Island Nation Ditches China Security Pact for Australia
  - Cointelegraph | 2026-11-27T17:37:23+00:00 | China sets March 2027 rollout for blockchain identity regulations
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`
