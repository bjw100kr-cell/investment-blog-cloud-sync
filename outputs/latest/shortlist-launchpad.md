# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-09-04` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - DOJ says Hamas crypto seizures reached $560,000 as FBI took over fundraising sites
  - Kraken parent Payward delays IPO to second quarter of 2027 at earliest
  - Crypto made new friends in U.S. primaries, but focus now shifts to general election
- recent_evidence:
  - Cointelegraph | 2026-09-02T16:35:56+00:00 | Bitcoin’s apparent demand turns negative as price struggles with $77K
  - CoinDesk RSS | 2026-09-02T12:13:26+00:00 | The bearish 'Bart Simpson' pattern is back as bitcoin and XRP prices pull back
  - Investing.com Crypto News | 2026-09-02 22:10:34 | Bitcoin dips to $77.1k as U.S.-Iran fighting, rate jitters weigh
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. 미국 빅테크 주가가 흔들릴 때 확인할 것: 실적, 금리, AI 투자

- keyword `us_big_tech` / publish `2026-09-05` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (2개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능
- sample_headlines:
  - Microsoft to start disclosing Azure quarterly revenue as company consolidates business units
  - Apple shares are doing something they haven't done in 20 years. Here’s what’s happening
  - HPE follows in Dell’s footsteps as it rides the AI server boom to a big earnings beat
- recent_evidence:
  - MarketWatch Breaking News | 2026-09-03T00:22:00+00:00 | HPE follows in Dell’s footsteps as it rides the AI server boom to a big earnings beat
  - CNBC Top News | 2026-09-02T22:37:13+00:00 | Microsoft to start disclosing Azure quarterly revenue as company consolidates business units
  - CNBC Top News | 2026-09-02T12:10:05+00:00 | Apple shares are doing something they haven't done in 20 years. Here’s what’s happening
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_big_tech`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_big_tech`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_big_tech`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_big_tech --apply`

## 3. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-09-06` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 검색 트렌드 반응 존재, 섹터/세계 흐름 연결 해설 가능, 실제 급상승 검색어 반영 (중국공산당)
- sample_headlines:
  - 중국공산당
- recent_evidence:
  - Google Trends KR | 2026-09-02T19:40:00-07:00 | 중국공산당
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`
