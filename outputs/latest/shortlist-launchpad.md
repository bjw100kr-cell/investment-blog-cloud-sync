# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-07-29` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (risk_off)
- sample_headlines:
  - Core Scientific lands AMD AI deal as bitcoin mining operation winds down
  - Binance makes fighting crypto crime more difficult, says new report
  - Apple kept fake bitcoin wallet on App Store after $875,000 theft report, lawsuit alleges
- recent_evidence:
  - CoinDesk RSS | 2026-07-28T12:46:05+00:00 | Core Scientific lands AMD AI deal as bitcoin mining operation winds down
  - CoinDesk RSS | 2026-07-28T11:59:17+00:00 | Apple kept fake bitcoin wallet on App Store after $875,000 theft report, lawsuit alleges
  - CoinDesk RSS | 2026-07-28T11:37:31+00:00 | Bitcoin’s recent stability hasn't been enough to spark a broader altcoin rally
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-07-31` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (2개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Micron’s stock sinks toward worst monthly drop in 11 years as China fears escalate
  - Tech Stocks Tumble on Worries About A.I. Spending and China’s Chip Competition
  - He Served China’s Police State of Xinjiang. He Says It Imprisoned Him, Too.
- recent_evidence:
  - MarketWatch Breaking News | 2026-07-28T14:25:00+00:00 | Micron’s stock sinks toward worst monthly drop in 11 years as China fears escalate
  - NYT Business | 2026-07-28T14:21:14+00:00 | Tech Stocks Tumble on Worries About A.I. Spending and China’s Chip Competition
  - NYT Business | 2026-07-28T04:01:20+00:00 | He Served China’s Police State of Xinjiang. He Says It Imprisoned Him, Too.
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`

## 3. 미국 증시 지수 흐름: 나스닥, 금리, 빅테크 실적을 같이 봐야 하는 이유

- keyword `us_index_flow` / publish `2026-07-30` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 검색 트렌드 반응 존재, 복수 소스 교차 확인 가능 (4개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능, 실제 급상승 검색어 반영 (stock market)
- sample_headlines:
  - stock market
  - US tech stocks enter correction as AI sell-off deepens
  - Nasdaq opens lower as AI worries mount ahead of pivotal earnings - Reuters
- recent_evidence:
  - Reuters Markets via Google News RSS | 2026-07-28T13:33:44+00:00 | Nasdaq opens lower as AI worries mount ahead of pivotal earnings - Reuters
  - Google Trends US | 2026-07-28T07:10:00-07:00 | stock market
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_index_flow`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_index_flow`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_index_flow`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_index_flow --apply`
