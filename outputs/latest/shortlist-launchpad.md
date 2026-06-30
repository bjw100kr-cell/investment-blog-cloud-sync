# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-07-01` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (5개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (extreme_fear)
- sample_headlines:
  - Phantom doubles down on perpetual futures with hire of Hyperliquid market builders
  - SEC giving novel ETFs a rethink as it opens comment period on overhauling U.S. rules
  - Jefferies warns of crypto market volatility as Clarity Act faces Senate test
- recent_evidence:
  - MarketWatch Breaking News | 2026-06-30T21:57:00+00:00 | Bitcoin ETFs were supposed to make selloffs less painful. That theory is being put to the test.
  - Cointelegraph | 2026-06-30T21:49:08+00:00 | Bitcoin just $5K away from ‘best investment opportunity’ of bear market
  - Cointelegraph | 2026-06-30T18:17:56+00:00 | Bitcoin price risks drop below $58K as US dollar hits 40-year high against yen
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. 미국 증시 지수 흐름: 나스닥, 금리, 빅테크 실적을 같이 봐야 하는 이유

- keyword `us_index_flow` / publish `2026-07-02` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (5개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능
- sample_headlines:
  - Nasdaq brings proprietary market data onchain through Pyth
  - US stocks chalk up biggest quarterly gain in six years
  - S&P 500, Nasdaq register best quarter since 2020 despite Iran war - Reuters
- recent_evidence:
  - MarketWatch Breaking News | 2026-06-30T21:13:00+00:00 | The 20 best-performing stocks in the S&P 500 for the first half of 2026
  - MarketWatch Breaking News | 2026-06-30T21:04:00+00:00 | 20 stocks in the S&P 500 that plunged the most in 2026’s first half
  - Reuters Markets via Google News RSS | 2026-06-30T20:55:04+00:00 | S&P 500, Nasdaq register best quarter since 2020 despite Iran war - Reuters
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_index_flow`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_index_flow`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_index_flow`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_index_flow --apply`

## 3. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-07-03` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (5개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Nike results top estimates even as China sales drop 12%; retailer expects $986 million tariff refund
  - World Bank to phase out China lending
  - 1. The Grand Design to Pressure China
- recent_evidence:
  - 무역킹 Trade King YouTube | 87K views | 1. The Grand Design to Pressure China
  - CNBC Top News | 2026-06-30T21:20:06+00:00 | Nike results top estimates even as China sales drop 12%; retailer expects $986 million tariff refund
  - Financial Times Home | 2026-06-30T20:47:12+00:00 | World Bank to phase out China lending
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`
