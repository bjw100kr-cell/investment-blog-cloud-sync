# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-11-10` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (risk_off)
- sample_headlines:
  - Binance's bitcoin mining pool finds just one block in a week as shutdown nears
  - Bitcoin drops, then pops as Nvidia cheating scandal and failed Iran talks trigger volatility
  - What the election results mean for crypto: State of Crypto
- recent_evidence:
  - CoinDesk RSS | 2026-11-09T04:54:39+00:00 | Binance's bitcoin mining pool finds just one block in a week as shutdown nears
  - CoinDesk RSS | 2026-11-09T03:21:49+00:00 | Bitcoin drops, then pops as Nvidia cheating scandal and failed Iran talks trigger volatility
  - CoinDesk RSS | 2026-11-08T12:55:59+00:00 | These Finland homes get free heat from bitcoin miners (as long as BTC stays above $70,000)
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-11-12` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 검색 트렌드 반응 존재, 복수 소스 교차 확인 가능 (4개), 섹터/세계 흐름 연결 해설 가능, 실제 급상승 검색어 반영 (중국)
- sample_headlines:
  - 중국
  - China wholesale inflation hits highest in more than four years as consumer measure slows
  - Democrat triumph offers China ‘window to catch up’ on AI
- recent_evidence:
  - Financial Times Home | 2026-11-09T05:09:46+00:00 | China’s producer prices hit four-year high
  - Financial Times Home | 2026-11-09T05:00:48+00:00 | Democrat triumph offers China ‘window to catch up’ on AI
  - Financial Times World | 2026-11-09T05:00:34+00:00 | UK faces China expertise crunch after exodus of senior diplomats
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`

## 3. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-11-11` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (6개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Bitcoin drops, then pops as Nvidia cheating scandal and failed Iran talks trigger volatility
  - Nvidia investigates CEO Jensen Huang's relationship with alleged Chinese spy
  - Nvidia’s Huang admits to affair after allegations of relationship with Chinese spy
- recent_evidence:
  - Financial Times World | 2026-11-09T05:31:35+00:00 | FirstFT: Nvidia CEO admits to affair after allegations of relationship with Chinese spy
  - CoinDesk RSS | 2026-11-09T03:21:49+00:00 | Bitcoin drops, then pops as Nvidia cheating scandal and failed Iran talks trigger volatility
  - Reuters Markets via Google News RSS | 2026-11-09T03:00:00+00:00 | Nvidia falls about 3% in after-hours and perpetual futures trade - Reuters
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`
