# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-08-05` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (extreme_fear)
- sample_headlines:
  - U.S. FBI intelligence agent arrested in connection with theft of $1 million in crypto
  - Trump-linked American Bitcoin president Matt Prusak departs for Giga Energy
  - U.S.-Japan intervention revives yen carry trade fears for bitcoin
- recent_evidence:
  - CoinDesk RSS | 2026-08-03T15:24:45+00:00 | Trump-linked American Bitcoin president Matt Prusak departs for Giga Energy
  - CoinDesk RSS | 2026-08-03T14:46:08+00:00 | U.S.-Japan intervention revives yen carry trade fears for bitcoin
  - CoinDesk RSS | 2026-08-03T12:17:10+00:00 | Strategy sold another $105 million of bitcoin last week, repurchased $81.2 million of STRC
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지

- keyword `fomc` / publish `2026-08-04` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 공식 소스 기반 확인 가능, 복수 소스 교차 확인 가능 (2개), 거시 해설형 글로 전환 가치 높음
- sample_headlines:
  - Federal Reserve issues FOMC statement
  - Federal Reserve announces the leadership and objectives of its task forces to advance the conduct of monetary policy
  - Federal Reserve Board and Federal Open Market Committee release economic projections from the June 16-17 FOMC meeting
- recent_evidence:
  - Federal Reserve Monetary Policy Press | 2026-07-29T18:00:00+00:00 | Federal Reserve issues FOMC statement
  - Federal Reserve Monetary Policy Press | 2026-06-17T18:00:00+00:00 | Federal Reserve issues FOMC statement
  - Federal Reserve Monetary Policy Press | 2026-06-17T18:00:00+00:00 | Federal Reserve Board and Federal Open Market Committee release economic projections from the June 16-17 FOMC meeting
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords fomc`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords fomc`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword fomc`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword fomc --apply`

## 3. AI 성장주를 볼 때 놓치기 쉬운 리스크: 매출 성장과 금리 부담

- keyword `ai_growth_stocks` / publish `2026-08-06` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (5개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능
- sample_headlines:
  - Palantir soars 12% on blowout quarter, with U.S. commercial revenue soaring nearly 150%
  - Palantir forecasts greater demand from US groups for its AI software
  - Palantir’s stock climbs after earnings, as AI drives turbocharged growth
- recent_evidence:
  - Financial Times Home | 2026-08-03T23:35:43+00:00 | Palantir forecasts greater demand from US groups for its AI software
  - CNBC Top News | 2026-08-03T22:47:54+00:00 | Palantir soars 12% on blowout quarter, with U.S. commercial revenue soaring nearly 150%
  - MarketWatch Breaking News | 2026-08-03T21:59:00+00:00 | Palantir’s stock climbs after earnings, as AI drives turbocharged growth
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_growth_stocks`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_growth_stocks`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_growth_stocks`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_growth_stocks --apply`
