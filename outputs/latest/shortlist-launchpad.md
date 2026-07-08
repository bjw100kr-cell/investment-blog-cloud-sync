# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-07-09` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 검색 트렌드 반응 존재, 복수 소스 교차 확인 가능 (4개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (extreme_fear), 실제 급상승 검색어 반영 (bitcoin)
- sample_headlines:
  - bitcoin
  - Live markets: Bitcoin drops as yen, Iran ceasefire collapse
  - Bitcoin under pressure as Trump says Iran ceasefire is over
- recent_evidence:
  - Cointelegraph | 2026-07-08T05:48:42+00:00 | StarkWare CEO suggests 4% annual Bitcoin inflation to replace 21M cap
  - CoinDesk RSS | 2026-07-08T05:29:16+00:00 | Live markets: Bitcoin drops as yen, Iran ceasefire collapse
  - CoinDesk RSS | 2026-07-08T04:30:24+00:00 | Bitcoin under pressure as Trump says Iran ceasefire is over
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. 미국 증시 지수 흐름: 나스닥, 금리, 빅테크 실적을 같이 봐야 하는 이유

- keyword `us_index_flow` / publish `2026-07-10` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 검색 트렌드 반응 존재, 복수 소스 교차 확인 가능 (3개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능, 실제 급상승 검색어 반영 (stock market today)
- sample_headlines:
  - stock market today
  - South Korea to closely watch risks around stock market volatility - Reuters
  - Nasdaq sinks as AI worries hit chipmakers - Reuters
- recent_evidence:
  - MarketWatch Breaking News | 2026-07-08T08:53:00+00:00 | It was the world’s hottest stock market. Now South Korea’s stock market has entered bear-market territory
  - Reuters Markets via Google News RSS | 2026-07-08T01:21:40+00:00 | South Korea to closely watch risks around stock market volatility - Reuters
  - Google Trends US | 2026-07-08T00:50:00-07:00 | stock market today
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_index_flow`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_index_flow`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_index_flow`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_index_flow --apply`

## 3. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-07-11` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (2개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - China warns about AI risks with Anthropic's Claude Code
  - Lawmakers probe growing use of Chinese AI models in U.S. companies
  - Alibaba just had its best day in 10 months. Is it time for China techs to catch up?
- recent_evidence:
  - MarketWatch Breaking News | 2026-07-08T08:57:00+00:00 | Alibaba just had its best day in 10 months. Is it time for China techs to catch up?
  - CNBC Top News | 2026-07-08T08:14:28+00:00 | China warns about AI risks with Anthropic's Claude Code
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`
