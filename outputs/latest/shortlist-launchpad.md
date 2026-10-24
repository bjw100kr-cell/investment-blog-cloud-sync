# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 유가 상승이 물가와 증시에 번지는 경로: 투자자가 볼 3가지

- keyword `oil` / publish `2026-10-24` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (5개), 거시 해설형 글로 전환 가치 높음
- sample_headlines:
  - Robinhood sees surge in bitcoin, gold prediction markets as traders move beyond sports
  - Live updates: Bitcoin holds above $81,000 as oil prices hit six-month high
  - Bitcoin seeks support above $81K as Brent crude oil hits highest level since March
- recent_evidence:
  - CNBC Top News | 2026-10-24T01:57:24+00:00 | Turmoil hits AI buildout as neoclouds face pressure, credit risks mount and Solidigm pulls IPO
  - CNBC Top News | 2026-10-23T22:49:42+00:00 | Moody's holds steady on France's credit rating as country grapples with turmoil and higher yields
  - NYT Business | 2026-10-23T20:03:29+00:00 | Global Oil Price Hits $116 a Barrel, Highest Since April
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords oil`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords oil`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword oil`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword oil --apply`

## 2. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-10-25` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - Robinhood sees surge in bitcoin, gold prediction markets as traders move beyond sports
  - Bitcoin Core changes security rules as AI makes finding code bugs dangerously easy
  - Bitcoin's price is as jumpy as Nvidia's and eight times more turbulent than the euro
- recent_evidence:
  - Cointelegraph | 2026-10-23T15:39:17+00:00 | Bitcoin seeks support above $81K as Brent crude oil hits highest level since March
  - CoinDesk RSS | 2026-10-23T13:58:56+00:00 | Robinhood sees surge in bitcoin, gold prediction markets as traders move beyond sports
  - CoinDesk RSS | 2026-10-23T12:03:53+00:00 | Bitcoin Core changes security rules as AI makes finding code bugs dangerously easy
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 3. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-10-26` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Bitcoin's price is as jumpy as Nvidia's and eight times more turbulent than the euro
  - Will Anthropic pull off a November IPO? Time is running out to file key paperwork.
  - Investors piled a record sum into a leveraged semiconductor ETF last week. Things didn’t work out.
- recent_evidence:
  - MarketWatch Breaking News | 2026-10-23T22:00:00+00:00 | Will Anthropic pull off a November IPO? Time is running out to file key paperwork.
  - MarketWatch Breaking News | 2026-10-23T21:46:00+00:00 | Investors piled a record sum into a leveraged semiconductor ETF last week. Things didn’t work out.
  - NYT Business | 2026-10-23T15:59:45+00:00 | U.S. Government Takes a Cut of Chip Business in Japan-Funded Deal
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`
