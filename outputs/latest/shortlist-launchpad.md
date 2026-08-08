# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 미국채 금리 상승이 나스닥과 코인에 부담이 되는 이유

- keyword `treasury_yields` / publish `2026-08-08` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (2개), 거시 해설형 글로 전환 가치 높음
- sample_headlines:
  - Trump Media pulls back from crypto, scraps Crypto.com's CRO token treasury deal
  - U.S. widens Iran crypto crackdown with sanctions on two exchanges
  - Donald Trump’s media company to terminate Crypto.com deal
- recent_evidence:
  - CoinDesk RSS | 2026-08-07T21:13:21+00:00 | Trump Media pulls back from crypto, scraps Crypto.com's CRO token treasury deal
  - Cointelegraph | 2026-08-07T20:02:20+00:00 | US Treasury’s OFAC sanctions 2 Iran-linked crypto exchanges
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords treasury_yields`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords treasury_yields`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword treasury_yields`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword treasury_yields --apply`

## 2. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-08-09` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (5개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - Why trillion-dollar asset manager T. Rowe Price put memecoins in its crypto ETF
  - U.S. Senate opens first stage of crypto Clarity Act voting to give bill a chance next month
  - Another Bitcoin infrastructure exploit hits, this time draining Lightning payment servers
- recent_evidence:
  - CoinDesk RSS | 2026-08-08T07:46:04+00:00 | Another Bitcoin infrastructure exploit hits, this time draining Lightning payment servers
  - CoinDesk RSS | 2026-08-08T02:30:00+00:00 | Bitcoin holders risk losing real BTC if they sell coins from BIP-110 fork, says developer
  - Investing.com Crypto News | 2026-08-08 08:51:16 | Bitcoin rises toward $65,000 as fresh security risks hit infrastructure
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 3. 미국 증시 지수 흐름: 나스닥, 금리, 빅테크 실적을 같이 봐야 하는 이유

- keyword `us_index_flow` / publish `2026-08-10` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능
- sample_headlines:
  - A record-breaking week for options powers S&P 500 surge; volatility gauge is near 2026 low
  - Moonshot shake-up seeks to win Beijing nod for stock market debut
  - S&P closes at record high as soft jobs report eases rate-hike concerns - Reuters
- recent_evidence:
  - CNBC Top News | 2026-08-08T11:49:22+00:00 | A record-breaking week for options powers S&P 500 surge; volatility gauge is near 2026 low
  - Financial Times Home | 2026-08-07T23:00:07+00:00 | Moonshot shake-up seeks to win Beijing nod for stock market debut
  - Reuters Markets via Google News RSS | 2026-08-07T10:02:00+00:00 | Wall St Week Ahead: Inflation data to test record-setting US stocks, Fed rate views - Reuters
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_index_flow`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_index_flow`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_index_flow`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_index_flow --apply`
