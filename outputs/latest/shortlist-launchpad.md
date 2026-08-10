# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지

- keyword `fomc` / publish `2026-08-10` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 공식 소스 기반 확인 가능, 복수 소스 교차 확인 가능 (3개), 거시 해설형 글로 전환 가치 높음
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

## 2. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-08-11` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - Is Clarity's delay a blessing in disguise?: State of Crypto
  - Bitcoin investors pour $853 million into spot ETFs. BlackRock’s IBIT claims the bulk
  - Crypto is going through a massive dot-com style shakeout as over 100 projects fold in 2026
- recent_evidence:
  - CoinDesk RSS | 2026-08-09T14:19:35+00:00 | Bitcoin investors pour $853 million into spot ETFs. BlackRock’s IBIT claims the bulk
  - Cointelegraph | 2026-08-09T11:00:53+00:00 | BIP-110 Bitcoin branch stalls after two blocks as gap widens
  - CoinDesk RSS | 2026-08-09T05:08:20+00:00 | Controversial Bitcoin fork BIP-110 mines two blocks, then stops
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 3. 미국 증시 지수 흐름: 나스닥, 금리, 빅테크 실적을 같이 봐야 하는 이유

- keyword `us_index_flow` / publish `2026-08-12` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능
- sample_headlines:
  - For retirees, staying in the stock market is critical. How much exposure is the make-or-break question
  - Wall St Week Ahead Inflation data to test record-setting US stocks, Fed rate views - Reuters
  - S&P closes at record high as soft jobs report eases rate-hike concerns - Reuters
- recent_evidence:
  - MarketWatch Breaking News | 2026-08-09T19:11:00+00:00 | The number of stocks beating the S&P 500 is the highest in 4 years. Why that number should rise.
  - MarketWatch Breaking News | 2026-08-09T14:00:00+00:00 | S&P 500 sales growth is at a nearly 5-year high. Here’s what’s behind the surge.
  - CNBC Top News | 2026-08-08T13:00:01+00:00 | For retirees, staying in the stock market is critical. How much exposure is the make-or-break question
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_index_flow`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_index_flow`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_index_flow`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_index_flow --apply`
