# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-09-24` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (risk_off)
- sample_headlines:
  - Inside the FBI’s little-known annual crypto crime gathering
  - Crypto Long & Short: Inside the chain settling $150 billion of stablecoins a week
  - Bitcoin's $16 billion quarterly options settlement arrives with a 'call-heavy' book
- recent_evidence:
  - Cointelegraph | 2026-09-23T14:52:11+00:00 | Bitcoin long liquidations hit $280M as BTC price dips under $84K
  - CoinDesk RSS | 2026-09-23T13:02:43+00:00 | Bitcoin's $16 billion quarterly options settlement arrives with a 'call-heavy' book
  - CoinDesk RSS | 2026-09-23T11:29:30+00:00 | Live updates: Bitcoin slips as higher rates and dollar pressure markets
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. 미국 증시 지수 흐름: 나스닥, 금리, 빅테크 실적을 같이 봐야 하는 이유

- keyword `us_index_flow` / publish `2026-09-25` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능
- sample_headlines:
  - The S&P 500 has a 'breadth' problem. Crypto doesn’t.
  - NYSE, Blockchain.com in tie-up to bring tokenized US stocks to crypto users
  - US stocks fall as 10-year Treasury yield hits highest since 2007 - Reuters
- recent_evidence:
  - Cointelegraph | 2026-09-23T15:56:20+00:00 | NYSE, Blockchain.com in tie-up to bring tokenized US stocks to crypto users
  - CoinDesk RSS | 2026-09-23T11:28:50+00:00 | The S&P 500 has a 'breadth' problem. Crypto doesn’t.
  - Reuters Markets via Google News RSS | 2026-09-23T01:51:00+00:00 | US stocks fall as 10-year Treasury yield hits highest since 2007 - Reuters
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_index_flow`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_index_flow`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_index_flow`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_index_flow --apply`

## 3. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-09-26` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Trump faces Xi as strains with allies complicate U.S. pressure on China
  - Trump’s diesel ban would hurt America and help China
  - Wall St falls as oil ticks up, yields rise ahead of US-China summit - Reuters
- recent_evidence:
  - CNBC Top News | 2026-09-23T16:22:49+00:00 | Trump faces Xi as strains with allies complicate U.S. pressure on China
  - Financial Times Home | 2026-09-23T15:37:23+00:00 | Trump’s diesel ban would hurt America and help China
  - Reuters Markets via Google News RSS | 2026-09-23T14:23:34+00:00 | Wall St falls as oil ticks up, yields rise ahead of US-China summit - Reuters
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`
