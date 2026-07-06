# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-07-07` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (extreme_fear)
- sample_headlines:
  - Bitmine added another $74 million in ether as Tom Lee bets on Clarity Act boost
  - Michael Saylor's Strategy dramatically ups pace of bitcoin sales, raising $216 million
  - Russia's largest bank plans crypto wallet launch as Moscow clears market path
- recent_evidence:
  - Cointelegraph | 2026-07-06T12:59:04+00:00 | Strategy sells 3,588 Bitcoin for $216M to fund dividends, keeps $2.55B reserve intact
  - CoinDesk RSS | 2026-07-06T12:16:28+00:00 | Michael Saylor's Strategy dramatically ups pace of bitcoin sales, raising $216 million
  - CoinDesk RSS | 2026-07-06T11:15:00+00:00 | U.S. inflation outlook underpins bitcoin bulls after best week since March
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-07-08` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - TeraWulf shares soar after Anthropic leases data center in Kentucky
  - Why OpenAI and Anthropic may struggle to float
  - Morning Bid: Samsung to serve chip taster for earnings feast - Reuters
- recent_evidence:
  - CNBC Top News | 2026-07-06T12:54:48+00:00 | TeraWulf shares soar after Anthropic leases data center in Kentucky
  - MarketWatch Breaking News | 2026-07-06T12:02:00+00:00 | AI hyperscalers are poised for a big comeback rally as chip gains cool, says Morgan Stanley
  - Reuters Markets via Google News RSS | 2026-07-06T04:32:00+00:00 | Morning Bid: Samsung to serve chip taster for earnings feast - Reuters
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`

## 3. 관세와 무역 갈등이 증시에 미치는 영향: 환율과 공급망까지 보기

- keyword `tariffs_trade` / publish `2026-07-09` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - The Chinese Company That Could Start a Trade War With Europe
- recent_evidence:
  - NYT Business | 2026-07-06T09:00:42+00:00 | The Chinese Company That Could Start a Trade War With Europe
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords tariffs_trade`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords tariffs_trade`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword tariffs_trade`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword tariffs_trade --apply`
