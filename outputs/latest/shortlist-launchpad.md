# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-08-18` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - No change in bitcoin holdings as Strategy boosted dollar reserve, bought back more STRC last week
  - Israel’s largest crypto broker Bits of Gold hit by data breach affecting 200,000 customers
  - Bitcoin options remain expensive despite summer calm. Here's why it matters
- recent_evidence:
  - CoinDesk RSS | 2026-08-17T12:19:45+00:00 | No change in bitcoin holdings as Strategy boosted dollar reserve, bought back more STRC last week
  - CoinDesk RSS | 2026-08-17T11:43:02+00:00 | Bitcoin options remain expensive despite summer calm. Here's why it matters
  - Cointelegraph | 2026-08-17T11:38:52+00:00 | BTC price loses 200-week trend line as 2022 repeats: Five things to know in Bitcoin this week
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-08-20` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - The next China shock will come from open-source AI
  - China surprises oil markets again with a return to stockpiling in July - reuters.com
  - China investment slump deepens as economy shows signs of weakness
- recent_evidence:
  - Financial Times World | 2026-08-17T08:51:14+00:00 | China investment slump deepens as economy shows signs of weakness
  - NYT Business | 2026-08-17T04:01:11+00:00 | As China Hunts for Scientific Talent, the US Makes It Easier
  - Financial Times Home | 2026-08-17T01:00:05+00:00 | The next China shock will come from open-source AI
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`

## 3. 미국 증시 지수 흐름: 나스닥, 금리, 빅테크 실적을 같이 봐야 하는 이유

- keyword `us_index_flow` / publish `2026-08-19` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (2개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능
- sample_headlines:
  - Santoli: Earnings bonanza that lifted market to record may not be all that it appears to be
  - S&P 500, Nasdaq futures rise on tech boost - reuters.com
- recent_evidence:
  - Reuters Markets via Google News RSS | 2026-08-17T11:52:24+00:00 | S&P 500, Nasdaq futures rise on tech boost - reuters.com
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_index_flow`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_index_flow`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_index_flow`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_index_flow --apply`
