# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 핵심 흐름 해설

- keyword `bitcoin` / publish `2026-07-01` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성
- sample_headlines:
  - SEC giving novel ETFs a rethink as it opens comment period on overhauling U.S. rules
  - Jefferies warns of crypto market volatility as Clarity Act faces Senate test
  - Financial companies join forces for US dollar stablecoin, keeping reserve earnings
- recent_evidence:
  - Cointelegraph | 2026-06-30T18:17:56+00:00 | Bitcoin price risks drop below $58K as US dollar hits 40-year high against yen
  - Cointelegraph | 2026-06-30T17:44:31+00:00 | AI’s power crunch turns Bitcoin miners’ grid access into an asset
  - Investing.com Crypto News | 2026-06-30 19:07:57 | Bitcoin holds $58,131 support after 2.9% drop: Live levels
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. 미국 증시 지수 흐름 해설

- keyword `us_index_flow` / publish `2026-07-02` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (5개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능
- sample_headlines:
  - Nasdaq brings proprietary market data onchain through Pyth
  - US stocks chalk up biggest quarterly gain in six years
  - S&P 500, Nasdaq post best quarter since 2020 despite Iran war - Reuters
- recent_evidence:
  - Financial Times Home | 2026-06-30T20:08:52+00:00 | US stocks chalk up biggest quarterly gain in six years
  - Reuters Markets via Google News RSS | 2026-06-30T20:01:16+00:00 | S&P 500, Nasdaq post best quarter since 2020 despite Iran war - Reuters
  - Cointelegraph | 2026-06-30T18:46:29+00:00 | Nasdaq brings proprietary market data onchain through Pyth
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_index_flow`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_index_flow`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_index_flow`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_index_flow --apply`

## 3. 중국 변수와 시장 영향 해설

- keyword `china` / publish `2026-07-03` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (2개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Nike earnings, revenue top estimates even as China sales drop 12%
  - 1. The Grand Design to Pressure China
- recent_evidence:
  - 무역킹 Trade King YouTube | 87K views | 1. The Grand Design to Pressure China
  - CNBC Top News | 2026-06-30T20:27:01+00:00 | Nike earnings, revenue top estimates even as China sales drop 12%
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`
