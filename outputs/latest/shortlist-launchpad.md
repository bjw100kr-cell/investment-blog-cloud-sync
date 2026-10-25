# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-10-26` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - Strategy, Strive face balancing act between bitcoin buying and preferred stock dividends
  - Crypto under weekend pressure, bitcoin slides below $80,000 on U.S. Middle East evacuations
  - Bitcoin’s wealthy holders turning to loans and yield as investment habits mature: Xapo CEO
- recent_evidence:
  - CoinDesk RSS | 2026-10-24T16:00:00+00:00 | Strategy, Strive face balancing act between bitcoin buying and preferred stock dividends
  - CoinDesk RSS | 2026-10-24T15:11:24+00:00 | Crypto under weekend pressure, bitcoin slides below $80,000 on U.S. Middle East evacuations
  - CoinDesk RSS | 2026-10-24T14:00:00+00:00 | Bitcoin’s wealthy holders turning to loans and yield as investment habits mature: Xapo CEO
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-10-28` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - China targets 2030 for its national blockchain network buildout
  - GLP-1 boom in China, India, Brazil could create $22 bln market by 2035, J.P. Morgan says - Reuters
  - North Korea’s Kim crosses new China border bridge to reaffirm ties
- recent_evidence:
  - Financial Times World | 2026-10-24T15:44:19+00:00 | North Korea’s Kim crosses new China border bridge to reaffirm ties
  - Cointelegraph | 2026-10-23T13:21:07+00:00 | China targets 2030 for its national blockchain network buildout
  - Reuters Markets via Google News RSS | 2026-10-23T10:02:25+00:00 | GLP-1 boom in China, India, Brazil could create $22 bln market by 2035, J.P. Morgan says - Reuters
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`

## 3. 미국 증시 지수 흐름: 나스닥, 금리, 빅테크 실적을 같이 봐야 하는 이유

- keyword `us_index_flow` / publish `2026-10-27` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능
- sample_headlines:
  - Nasdaq CEO flags 'modest softening' in IPO market as macro uncertainty hits debuts - Reuters
- recent_evidence:
  - Reuters Markets via Google News RSS | 2026-10-22T16:02:09+00:00 | Nasdaq CEO flags 'modest softening' in IPO market as macro uncertainty hits debuts - Reuters
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_index_flow`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_index_flow`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_index_flow`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_index_flow --apply`
