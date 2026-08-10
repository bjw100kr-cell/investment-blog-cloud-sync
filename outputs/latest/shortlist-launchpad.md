# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-08-11` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - Strategy sells 1,690 bitcoin, raises $653 million from MSTR shares
  - Crypto exchange Coinsbuy loses $8 million in coordinated two-blockchain attack
  - Bitcoin's BIP-110 episode is free-market capitalism in purest form
- recent_evidence:
  - Cointelegraph | 2026-08-10T13:07:42+00:00 | Bitdeer increased Bitcoin mining output by nearly fivefold in Q2
  - CoinDesk RSS | 2026-08-10T12:09:26+00:00 | Strategy sells 1,690 bitcoin, raises $653 million from MSTR shares
  - CoinDesk RSS | 2026-08-10T11:31:29+00:00 | Bitcoin's BIP-110 episode is free-market capitalism in purest form
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-08-13` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - China bypasses shipping chokepoints with ‘Ice Silk Road’ through Arctic
  - Hong Kong’s plan to clear rural villages for a new gateway to China
- recent_evidence:
  - Financial Times Home | 2026-08-10T07:57:31+00:00 | Hong Kong’s plan to clear rural villages for a new gateway to China
  - Financial Times Home | 2026-08-10T04:00:07+00:00 | China bypasses shipping chokepoints with ‘Ice Silk Road’ through Arctic
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`

## 3. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-08-12` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Meta to open source its most powerful AI model as it takes swipe at OpenAI, Anthropic
  - World's biggest chipmaker TSMC's sales surge 45% amid buoyant AI demand
  - House Dems call for AI companies to testify on recent hacks: ‘Clear risk to safety’
- recent_evidence:
  - Financial Times YouTube | 51K views | Silicon shadows: inside the black market for AI chips | FT Film
  - CNBC Top News | 2026-08-10T12:40:36+00:00 | Meta to open source its most powerful AI model as it takes swipe at OpenAI, Anthropic
  - CNBC Top News | 2026-08-10T10:29:27+00:00 | World's biggest chipmaker TSMC's sales surge 45% amid buoyant AI demand
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`
