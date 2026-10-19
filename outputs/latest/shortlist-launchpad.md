# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-10-20` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - U.S. CFTC rebuffs CME legal stance in consequential fight over perpetual futures
  - Zerohash rolls out a new tool to move crypto without copying wallet addresses
  - Strategy's price chart is about to flash a major bullish signal weeks after bitcoin did
- recent_evidence:
  - Cointelegraph | 2026-10-19T16:30:18+00:00 | Strive buys $335M in Bitcoin, boosting holdings to 36,818 BTC
  - Cointelegraph | 2026-10-19T16:05:57+00:00 | Bitcoin is rejected at $83K as US bond yields reverse higher with equities
  - Cointelegraph | 2026-10-19T12:30:00+00:00 | Strategy buys $22M in Bitcoin, repurchases $193M in STRC
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. 미국 증시 지수 흐름: 나스닥, 금리, 빅테크 실적을 같이 봐야 하는 이유

- keyword `us_index_flow` / publish `2026-10-21` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능
- sample_headlines:
  - Live updates: Bitcoin holds near $82,000 as Nasdaq rebounds more than 1%
  - Bitcoin extends bounce above $82,000 as stocks rebound, DeFi tokens lead altcoin gains
  - Nasdaq climbs over 1% as AI-linked stocks recover ahead of key earnings - Reuters
- recent_evidence:
  - Financial Times World | 2026-10-19T18:15:49+00:00 | US stocks recover after AI sell-off
  - Reuters Markets via Google News RSS | 2026-10-19T16:17:44+00:00 | Nasdaq climbs over 1% as AI-linked stocks recover ahead of key earnings - Reuters
  - CoinDesk RSS | 2026-10-19T11:05:54+00:00 | Live updates: Bitcoin holds near $82,000 as Nasdaq rebounds more than 1%
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_index_flow`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_index_flow`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_index_flow`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_index_flow --apply`

## 3. 미국채 금리 상승이 나스닥과 코인에 부담이 되는 이유

- keyword `treasury_yields` / publish `2026-10-19` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (5개), 거시 해설형 글로 전환 가치 높음
- sample_headlines:
  - Live updates: Bitcoin holds near $82,000 as Nasdaq rebounds more than 1%
  - Strive buys $335M in Bitcoin, boosting holdings to 36,818 BTC
  - Bitcoin is rejected at $83K as US bond yields reverse higher with equities
- recent_evidence:
  - Financial Times Home | 2026-10-19T18:31:54+00:00 | French bond sell-off intensifies after violent protests
  - Cointelegraph | 2026-10-19T16:05:57+00:00 | Bitcoin is rejected at $83K as US bond yields reverse higher with equities
  - CNBC Top News | 2026-10-19T12:59:13+00:00 | French unrest compounds debt crisis fears. Paris-listed stocks, bonds and the euro fall
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords treasury_yields`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords treasury_yields`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword treasury_yields`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword treasury_yields --apply`
