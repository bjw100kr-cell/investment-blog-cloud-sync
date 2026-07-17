# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-07-18` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - Bitcoin faces fresh headwinds as China’s Kimi beats Claude, GPT in coding benchmark
  - AI frenzy losing steam leaves bitcoin less volatile than South Korean stocks
  - Live markets: Bitcoin returns to $63,000 as Nasdaq trims large early loss
- recent_evidence:
  - Cointelegraph | 2026-07-17T14:37:39+00:00 | Bitcoin price sags under $62.5K as Iran strikes add to US stocks pressure
  - CoinDesk RSS | 2026-07-17T12:45:11+00:00 | Bitcoin faces fresh headwinds as China’s Kimi beats Claude, GPT in coding benchmark
  - CoinDesk RSS | 2026-07-17T11:48:20+00:00 | AI frenzy losing steam leaves bitcoin less volatile than South Korean stocks
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-07-19` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (6개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Bitcoin faces fresh headwinds as China’s Kimi beats Claude, GPT in coding benchmark
  - Apple, Nvidia vie for title of world's most valuable company
  - Apple briefly leapfrogs Nvidia as world’s most valuable company
- recent_evidence:
  - Financial Times YouTube | 34K views | Silicon shadows: inside the black market for AI chips | FT Film
  - Financial Times Home | 2026-07-17T16:18:56+00:00 | US chip stocks head for worst week in more than a year
  - Reuters Markets via Google News RSS | 2026-07-17T14:47:51+00:00 | S&P 500 and Nasdaq slip as chip rout extends; Netflix slides - Reuters
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`

## 3. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-07-20` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Bitcoin faces fresh headwinds as China’s Kimi beats Claude, GPT in coding benchmark
  - Chinese automakers are taking on the UK — and many Brits are embracing it
  - Import prices post surprise gain as costs of goods from China hit highest since 2008
- recent_evidence:
  - CNBC Top News | 2026-07-17T14:13:49+00:00 | Import prices post surprise gain as costs of goods from China hit highest since 2008
  - CoinDesk RSS | 2026-07-17T12:45:11+00:00 | Bitcoin faces fresh headwinds as China’s Kimi beats Claude, GPT in coding benchmark
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`
