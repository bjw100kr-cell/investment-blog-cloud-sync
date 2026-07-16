# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지

- keyword `fomc` / publish `2026-07-16` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 공식 소스 기반 확인 가능, 복수 소스 교차 확인 가능 (2개), 거시 해설형 글로 전환 가치 높음
- sample_headlines:
  - Federal Reserve announces the leadership and objectives of its task forces to advance the conduct of monetary policy
  - Federal Reserve issues FOMC statement
  - Federal Reserve Board and Federal Open Market Committee release economic projections from the June 16-17 FOMC meeting
- recent_evidence:
  - Federal Reserve Monetary Policy Press | 2026-06-17T18:00:00+00:00 | Federal Reserve issues FOMC statement
  - Federal Reserve Monetary Policy Press | 2026-06-17T18:00:00+00:00 | Federal Reserve Board and Federal Open Market Committee release economic projections from the June 16-17 FOMC meeting
  - Federal Reserve Monetary Policy Press | 2026-04-29T18:00:00+00:00 | Federal Reserve issues FOMC statement
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords fomc`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords fomc`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword fomc`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword fomc --apply`

## 2. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-07-17` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (extreme_fear)
- sample_headlines:
  - Live updates: ZachXBT calls hardware wallets complete garbage; BTC steady after Korea rate hike
  - U.S. Senate unanimously opposes clemency for FTX founder Sam Bankman-Fried
  - A bitcoin wallet dormant since the 2017 peak just moved $383 million
- recent_evidence:
  - CoinDesk RSS | 2026-07-16T05:12:26+00:00 | A bitcoin wallet dormant since the 2017 peak just moved $383 million
  - CoinDesk RSS | 2026-07-16T04:56:15+00:00 | Ether outruns bitcoin as ETF money returns, almost all of from BlackRock's fund
  - CoinDesk RSS | 2026-07-16T04:09:10+00:00 | Two groups of bitcoin investors sell on the rise as U.S. inflation lifts prices to nearly $65,000
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 3. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-07-18` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 검색 트렌드 반응 존재, 복수 소스 교차 확인 가능 (4개), 섹터/세계 흐름 연결 해설 가능, 실제 급상승 검색어 반영 (tsmc stock)
- sample_headlines:
  - tsmc stock
  - TSMC second-quarter profit jumps over 77%, beating estimates, on high-end chip boom
  - SK Hynix shares plunge over 11% as Asia sees tech rout, tracking U.S. chip losses
- recent_evidence:
  - Financial Times YouTube | 30K views | Silicon shadows: inside the black market for AI chips | FT Film
  - CNBC Top News | 2026-07-16T07:02:36+00:00 | SK Hynix shares plunge over 11% as Asia sees tech rout, tracking U.S. chip losses
  - CNBC Top News | 2026-07-16T05:52:58+00:00 | TSMC second-quarter profit jumps over 77%, beating estimates, on high-end chip boom
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`
