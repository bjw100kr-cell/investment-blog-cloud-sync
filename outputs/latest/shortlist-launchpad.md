# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-07-25` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - Senate Dems should accept the victory they won on Trump's crypto limits: White House
  - Institutional crypto trading platform LMAX is exploring sale, IPO
  - Saylor and team overhaul Strategy's bitcoin metrics as bear market persists
- recent_evidence:
  - Cointelegraph | 2026-07-24T14:28:03+00:00 | Bitcoin falls under $64K as surging US bond yields boost Fed rate-hike odds
  - Cointelegraph | 2026-07-24T13:30:00+00:00 | A quantum roadmap would push Bitcoin much higher: Charles Edwards
  - CoinDesk RSS | 2026-07-24T13:15:15+00:00 | Saylor and team overhaul Strategy's bitcoin metrics as bear market persists
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-07-27` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Yang Zhilin, the rock star founder behind China’s Moonshot AI
  - Nvidia and Palantir urge US not to ban ‘open’ AI models after China scare
  - Oil down more than 4% on profit taking, report of China-backed push to end US-Iran fighting - Reuters
- recent_evidence:
  - NYT Business | 2026-07-24T17:02:20+00:00 | China Wields Its Rare Earth Leverage Over Europe With New Export Controls
  - Financial Times Home | 2026-07-24T15:20:23+00:00 | Nvidia and Palantir urge US not to ban ‘open’ AI models after China scare
  - Financial Times Home | 2026-07-24T15:00:02+00:00 | Yang Zhilin, the rock star founder behind China’s Moonshot AI
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`

## 3. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-07-26` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Anthropic's new AI model rivals Fable 5 and is cheaper as businesses fret about costs
  - Nvidia, Microsoft, Meta warn against 'premature restrictions' of open-weight models
  - Nvidia and Palantir urge US not to ban ‘open’ AI models after China scare
- recent_evidence:
  - Financial Times YouTube | 43K views | Silicon shadows: inside the black market for AI chips | FT Film
  - CNBC Top News | 2026-07-24T17:00:01+00:00 | Anthropic's new AI model rivals Fable 5 and is cheaper as businesses fret about costs
  - CNBC Top News | 2026-07-24T15:47:40+00:00 | Nvidia, Microsoft, Meta warn against 'premature restrictions' of open-weight models
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`
