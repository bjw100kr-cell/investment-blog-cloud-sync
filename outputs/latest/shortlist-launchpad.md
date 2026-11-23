# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-11-24` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (extreme_fear)
- sample_headlines:
  - Bitcoin sold for $17,000 on Kraken's Canadian dollar market, and the trades stand
  - More on the pending oversight hearings: State of Crypto
  - Bitcoin's quantum security challenge extends to bridges, custodians and millions of coins
- recent_evidence:
  - CoinDesk RSS | 2026-11-23T05:42:22+00:00 | Bitcoin sold for $17,000 on Kraken's Canadian dollar market, and the trades stand
  - Cointelegraph | 2026-11-22T22:47:09+00:00 | Will Bitcoin’s big rebound hold? More tampered Ledgers found: Hodler’s Digest
  - CoinDesk RSS | 2026-11-22T14:00:00+00:00 | Bitcoin's quantum security challenge extends to bridges, custodians and millions of coins
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-11-25` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (8개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - OpenAI, Anthropic and rivals seek AI agent rules to prevent commerce chaos
  - Trump renews call for Nvidia to rehire Jensen Huang as CEO
  - U.S. probes Megaspeed, Alice Huang as new figure emerges in Nvidia chip case
- recent_evidence:
  - CNBC Top News | 2026-11-23T05:08:03+00:00 | U.S. probes Megaspeed, Alice Huang as new figure emerges in Nvidia chip case
  - Cointelegraph | 2026-11-23T03:37:20+00:00 | Trump renews call for Nvidia to rehire Jensen Huang as CEO
  - NYT Business | 2026-11-22T17:55:31+00:00 | Scott Bessent Calls on Nvidia to Provide Answers on Chip Sales to China
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`

## 3. FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지

- keyword `fomc` / publish `2026-11-23` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 공식 소스 기반 확인 가능, 복수 소스 교차 확인 가능 (4개), 거시 해설형 글로 전환 가치 높음
- sample_headlines:
  - Federal Reserve announces revised tentative schedule of Federal Open Market Committee meetings in 2027
  - Federal Reserve issues FOMC statement
  - Federal Reserve Board and Federal Open Market Committee release economic projections from the September 15-16 FOMC meeting
- recent_evidence:
  - Federal Reserve Monetary Policy Press | 2026-10-28T18:00:00+00:00 | Federal Reserve issues FOMC statement
  - Federal Reserve Monetary Policy Press | 2026-09-16T18:00:00+00:00 | Federal Reserve issues FOMC statement
  - Federal Reserve Monetary Policy Press | 2026-09-16T18:00:00+00:00 | Federal Reserve Board and Federal Open Market Committee release economic projections from the September 15-16 FOMC meeting
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords fomc`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords fomc`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword fomc`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword fomc --apply`
