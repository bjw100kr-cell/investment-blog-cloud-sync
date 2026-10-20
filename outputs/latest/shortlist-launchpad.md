# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `2`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-10-21` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - BlackRock seeks to shield bitcoin investors from losses after rival fund weathers 50% crash
  - Kazakhstan court bars Coinbase, five others from unlicensed crypto services in Astana International Financial Centre
  - Equity weakness could damp demand for bitcoin after biggest ETF inflows in a month
- recent_evidence:
  - Cointelegraph | 2026-10-20T16:14:09+00:00 | Bitcoin price spikes to $83.3K as US stocks rise on Q3 earnings, oil falls
  - CoinDesk RSS | 2026-10-20T14:28:39+00:00 | BlackRock seeks to shield bitcoin investors from losses after rival fund weathers 50% crash
  - Cointelegraph | 2026-10-20T13:04:28+00:00 | FINMA approves Switzerland’s first Bitcoin ETF for retail investors
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. 미국 빅테크 주가가 흔들릴 때 확인할 것: 실적, 금리, AI 투자

- keyword `us_big_tech` / publish `2026-10-22` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능
- sample_headlines:
  - Microsoft, Alphabet and Goldman Sachs join objections to OKX-ICE tokenized stock trading
  - Alphabet, Microsoft add objections to OKX-ICE proposed tokenized stock platform
  - Investors in Anticipation Over Musk’s Next Big SpaceX Deal
- recent_evidence:
  - Cointelegraph | 2026-10-20T16:23:17+00:00 | Alphabet, Microsoft add objections to OKX-ICE proposed tokenized stock platform
  - CoinDesk RSS | 2026-10-20T12:40:17+00:00 | Microsoft, Alphabet and Goldman Sachs join objections to OKX-ICE tokenized stock trading
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_big_tech`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_big_tech`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_big_tech`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_big_tech --apply`
