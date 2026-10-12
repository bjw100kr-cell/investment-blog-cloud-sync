# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-10-13` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - Tom Lee sees $2 trillion wealth transfer fueling crypto demand as Bitmine buys more ether
  - Bitcoin falls below $83,000 as dollar strength keeps markets on edge
  - South Korea just got its first traditional bank loans backed by bitcoin
- recent_evidence:
  - Cointelegraph | 2026-10-12T16:51:05+00:00 | Bitcoin miners face widening AI financing costs as lenders scrutinize deals
  - Cointelegraph | 2026-10-12T16:30:21+00:00 | Bitcoin drops 2.2% as Ukraine, Iran strikes send oil toward one-month high
  - Cointelegraph | 2026-10-12T14:07:00+00:00 | Ledger implant tests Bitcoin ETFs as safer custodial solutions than hardware wallets
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. 미국 빅테크 주가가 흔들릴 때 확인할 것: 실적, 금리, AI 투자

- keyword `us_big_tech` / publish `2026-10-14` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (5개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능
- sample_headlines:
  - Meta debuts Muse Wonder AI model in latest test of users' willingness to pay
  - Zuckerberg says Meta has reached AI ‘frontier’
  - Musk injects $275mn into Republicans’ fight to retain Congress
- recent_evidence:
  - MarketWatch Breaking News | 2026-10-12T20:40:00+00:00 | Microsoft hits a big milestone that solidifies its revival
  - MarketWatch Breaking News | 2026-10-12T19:43:00+00:00 | Meta is back on the AI leaderboard with its new family of Wonder models
  - CNBC Top News | 2026-10-12T17:34:35+00:00 | Meta debuts Muse Wonder AI model in latest test of users' willingness to pay
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_big_tech`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_big_tech`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_big_tech`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_big_tech --apply`

## 3. FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지

- keyword `fomc` / publish `2026-10-12` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 공식 소스 기반 확인 가능, 복수 소스 교차 확인 가능 (2개), 거시 해설형 글로 전환 가치 높음
- sample_headlines:
  - Federal Reserve issues FOMC statement
  - Federal Reserve Board and Federal Open Market Committee release economic projections from the September 15-16 FOMC meeting
  - Federal Reserve announces the leadership and objectives of its task forces to advance the conduct of monetary policy
- recent_evidence:
  - Federal Reserve Monetary Policy Press | 2026-09-16T18:00:00+00:00 | Federal Reserve issues FOMC statement
  - Federal Reserve Monetary Policy Press | 2026-09-16T18:00:00+00:00 | Federal Reserve Board and Federal Open Market Committee release economic projections from the September 15-16 FOMC meeting
  - Federal Reserve Monetary Policy Press | 2026-07-29T18:00:00+00:00 | Federal Reserve issues FOMC statement
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords fomc`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords fomc`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword fomc`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword fomc --apply`
