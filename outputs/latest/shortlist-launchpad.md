# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-08-27` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (risk_off)
- sample_headlines:
  - Zerohash back for second effort at OCC trust bank charter
  - LayerZero unveils trading infrastructure for crypto and tokenized markets, ZRO surges
  - Bitwise turns Coinbase's tokenized stocks into automated AI, robotics and tech portfolios
- recent_evidence:
  - Cointelegraph | 2026-08-25T18:13:11+00:00 | Bitcoin enters ‘initial phase’ of new bull market, but $83K remains key: CryptoQuant
  - Cointelegraph | 2026-08-25T16:47:40+00:00 | Strategy’s $66B Bitcoin machine hinges on capital markets, not BTC price: Report
  - Cointelegraph | 2026-08-25T15:15:35+00:00 | Bitcoin slips from $80K as gold cools with falling US bond yields
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-08-28` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 검색 트렌드 반응 존재, 복수 소스 교차 확인 가능 (4개), 섹터/세계 흐름 연결 해설 가능, 실제 급상승 검색어 반영 (엔비디아 실적)
- sample_headlines:
  - 엔비디아 실적
  - Wall Street ends higher as tech rebounds before Nvidia results - Reuters
  - Nvidia shares set for $280 billion price swing after earnings, options show - Reuters
- recent_evidence:
  - Google Trends KR | 2026-08-25T16:00:00-07:00 | 엔비디아 실적
  - Financial Times YouTube | 55K views | Silicon shadows: inside the black market for AI chips | FT Film
  - Reuters Markets via Google News RSS | 2026-08-25T23:14:21+00:00 | Wall Street ends higher as tech rebounds before Nvidia results - Reuters
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`

## 3. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-08-29` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - South Korea challenges China on Arctic trade route
  - It's Not About China(?): U.S.-Iran Economic Sanctions Edition
  - FirstFT: China warns US it could retaliate over Iran sanctions
- recent_evidence:
  - Financial Times Home | 2026-08-26T01:24:46+00:00 | South Korea challenges China on Arctic trade route
  - Financial Times World | 2026-08-25T21:48:15+00:00 | FirstFT: China warns US it could retaliate over Iran sanctions
  - NYT Business | 2026-08-25T14:59:39+00:00 | China Pushes Back After Trump Tightens the Screws on Iran
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`
