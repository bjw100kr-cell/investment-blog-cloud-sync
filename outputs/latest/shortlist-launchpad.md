# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-11-12` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - Crypto is now teamed up with U.S. government in two legal battles over perps
  - Will stablecoins survive once the banks catch up?
  - Crypto ally Tom Emmer elected House GOP minority whip
- recent_evidence:
  - Cointelegraph | 2026-11-11T01:16:58+00:00 | LNbits rushes emergency patch after reported Bitcoin wallet thefts
  - Investing.com Crypto News | 2026-11-10 22:34:37 | Bitcoin falls over 2%, drops under $74k after hot CPI data, hawkish Waller
  - Investing.com Crypto News | 2026-11-09 23:11:41 | Bitcoin turns slightly higher amid Wall Street rally, slide in oil prices
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-11-13` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (6개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Nvidia's Huang tries to project 'business as usual' in return to office after affair revelation
  - Alibaba announces plans to list T-Head, its Nvidia chip rival
  - Anthropic opens Australian retail IPO offering as AI scrutiny intensifies
- recent_evidence:
  - Financial Times World | 2026-11-11T05:31:36+00:00 | FirstFT: Anthropic bankers prepare to increase IPO valuation to $1.5tn
  - CNBC Top News | 2026-11-11T03:08:17+00:00 | Alibaba announces plans to list T-Head, its Nvidia chip rival
  - NYT Business | 2026-11-11T02:10:37+00:00 | How a Suspected Chinese Spy Gained Access to Nvidia Chips
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`

## 3. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-11-14` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (2개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - U.S., China should ‘harbor no illusions’ as they cooperate, compete on AI, Bessent says
  - Europe’s struggle to compete with China ramps up
- recent_evidence:
  - CNBC Top News | 2026-11-11T05:15:50+00:00 | U.S., China should ‘harbor no illusions’ as they cooperate, compete on AI, Bessent says
  - Financial Times World | 2026-11-11T05:13:03+00:00 | Europe’s struggle to compete with China ramps up
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`
