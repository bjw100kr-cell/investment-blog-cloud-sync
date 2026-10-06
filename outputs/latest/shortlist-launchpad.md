# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-10-07` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - Peter Thiel-backed Founders Fund leads a $5 million token buy in crypto collateral protocol Anvil
  - Crypto is expanding the boundaries of what can be priced
  - OKX draws investment from StanChart, Circle, Ripple as it pushes beyond crypto exchange roots
- recent_evidence:
  - Cointelegraph | 2026-10-06T17:19:58+00:00 | Bitcoin grinds toward $87K as US equities hit new record highs
  - CoinDesk RSS | 2026-10-06T11:30:00+00:00 | The VIX of bonds is rising but bitcoin and stocks aren't hearing it yet
  - CoinDesk RSS | 2026-10-06T10:35:49+00:00 | Live updates: Bitcoin remains locked in range as stocks notch another new record high
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. 미국 증시 지수 흐름: 나스닥, 금리, 빅테크 실적을 같이 봐야 하는 이유

- keyword `us_index_flow` / publish `2026-10-08` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (5개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능
- sample_headlines:
  - Bitcoin grinds toward $87K as US equities hit new record highs
  - Former German spy chief arrested for treason
  - S&P 500 hits record high as AI stocks shrug off bond market slump
- recent_evidence:
  - Financial Times Home | 2026-10-06T16:59:33+00:00 | S&P 500 hits record high as AI stocks shrug off bond market slump
  - NYT Business | 2026-10-06T16:46:42+00:00 | How Trump’s Tariff War With Canada Ensnared the Can-Am Spyder
  - Reuters Markets via Google News RSS | 2026-10-06T16:02:59+00:00 | S&P 500, Nasdaq hit record highs as Treasury yields stall, oil slips - Reuters
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_index_flow`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_index_flow`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_index_flow`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_index_flow --apply`

## 3. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-10-09` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - 4. Why the Outcome of the Talks Differs (U.S.-China Summit)
  - 3. They may have smiled to each other, but China’s true intentions... (US-China Summit)
  - 2. Nigeria, Linked to the US-China Hegemony (Sunday School: Nigeria)
- recent_evidence:
  - 무역킹 Trade King YouTube | 8h ago | 4. Why the Outcome of the Talks Differs (U.S.-China Summit)
  - 무역킹 Trade King YouTube | 27K | 3. They may have smiled to each other, but China’s true intentions... (US-China Summit)
  - 무역킹 Trade King YouTube | 24K | 2. Nigeria, Linked to the US-China Hegemony (Sunday School: Nigeria)
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`
