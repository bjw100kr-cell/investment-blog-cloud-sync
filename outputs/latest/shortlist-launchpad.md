# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-07-16` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (extreme_fear)
- sample_headlines:
  - Crypto Long & Short: To ETH or not to ETH — is SOL the better diversifier?
  - President Trump expected to meet with senators to work on ethics concerns in crypto bill
  - BlackRock's crypto assets fall 39% despite $15 billion of net inflows
- recent_evidence:
  - Cointelegraph | 2026-07-15T14:45:28+00:00 | Bitcoin hits $65.5K as more surprise US inflation data sparks three-week BTC price high
  - Investing.com Crypto News | 2026-07-15 14:16:37 | Bitcoin climbs to $65k as PPI wholesale inflation falls; Iran tensions limit gains
  - Investing.com Crypto News | 2026-07-15 07:04:50 | Bitcoin breaks above resistance near $65K: Live levels
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-07-17` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Wall St edges higher with earnings in focus; chip stocks retreat - Reuters
  - ASML capacity upgrade soothes AI chip bottleneck fears - Reuters
  - Copper is shadowing the AI hyperscaler stocks — but wait for a dip before buying
- recent_evidence:
  - Financial Times YouTube | 28K views | Silicon shadows: inside the black market for AI chips | FT Film
  - Reuters Markets via Google News RSS | 2026-07-15T16:22:42+00:00 | Wall St edges higher with earnings in focus; chip stocks retreat - Reuters
  - NYT Business | 2026-07-15T07:29:52+00:00 | China’s Chip Champion to Raise Billions in Race for A.I. Control
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`

## 3. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-07-18` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - VIEW China's second-quarter economic growth misses market forecast - Reuters
  - The Taiwan Strait Was China's Achilles' Heel
  - China’s Chip Champion to Raise Billions in Race for A.I. Control
- recent_evidence:
  - 무역킹 Trade King YouTube | 54K views | The Taiwan Strait Was China's Achilles' Heel
  - NYT Business | 2026-07-15T07:29:52+00:00 | China’s Chip Champion to Raise Billions in Race for A.I. Control
  - Reuters Markets via Google News RSS | 2026-07-15T02:24:00+00:00 | VIEW China's second-quarter economic growth misses market forecast - Reuters
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`
