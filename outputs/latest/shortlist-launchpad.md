# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-10-04` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - Crypto job postings triple to over 1,200 in September, but applications fall
  - Crypto's Sisyphean struggle
  - Bank group sues U.S. regulator over granting crypto trust charters
- recent_evidence:
  - MarketWatch Breaking News | 2026-10-03T15:30:00+00:00 | ‘I’m never selling’: I’m 47 and buy bitcoin with every dollar I earn. Am I crazy?
  - Investing.com Crypto News | 2026-10-03 07:02:06 | Bitcoin consolidates $83K-$87K flag: Live levels
  - Investing.com Crypto News | 2026-10-03 02:15:26 | Bitcoin holds below $85,000 as SEC custody proposal boosts institutional outlook
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-10-06` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - China, America and the new Great Game
  - China launches anti-dumping probe into European chemical exports
  - 2. Trump actually lost? Who says so? (US-China Summit)
- recent_evidence:
  - 무역킹 Trade King YouTube | 35K | 2. Trump actually lost? Who says so? (US-China Summit)
  - Financial Times Home | 2026-10-03T10:16:42+00:00 | China launches anti-dumping probe into European chemical exports
  - Financial Times Home | 2026-10-03T04:00:30+00:00 | China, America and the new Great Game
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`

## 3. 미국 증시 지수 흐름: 나스닥, 금리, 빅테크 실적을 같이 봐야 하는 이유

- keyword `us_index_flow` / publish `2026-10-05` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능
- sample_headlines:
  - Payments firm OpenPayd targets year-end Nasdaq listing to fund U.S. expansion and acquisitions
- recent_evidence:
  - CoinDesk RSS | 2026-10-03T16:00:00+00:00 | Payments firm OpenPayd targets year-end Nasdaq listing to fund U.S. expansion and acquisitions
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_index_flow`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_index_flow`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_index_flow`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_index_flow --apply`
