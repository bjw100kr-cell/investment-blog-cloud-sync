# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-08-28` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 검색 트렌드 반응 존재, 복수 소스 교차 확인 가능 (5개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed), 실제 급상승 검색어 반영 (fidelity bitcoin etf)
- sample_headlines:
  - fidelity bitcoin etf
  - Bitcoin researchers propose quantum fix that would not crowd out transactions
  - Bitcoin below $79,000, XRP leads losses as traders start betting on a Fed hike
- recent_evidence:
  - CoinDesk RSS | 2026-08-27T07:15:57+00:00 | Bitcoin researchers propose quantum fix that would not crowd out transactions
  - Cointelegraph | 2026-08-27T07:01:19+00:00 | Bitcoin ETF inflows slow to $232M as BTC holds under $80K
  - CoinDesk RSS | 2026-08-27T04:35:18+00:00 | Bitcoin below $79,000, XRP leads losses as traders start betting on a Fed hike
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-08-29` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (7개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Nvidia shares rise after earnings top estimates, guides to $108 billion in revenue next quarter
  - Nvidia jumps 7% in after blockbuster earnings boost AI confidence
  - Nvidia agrees to buy Hugging Face for $12.9 billion, report says
- recent_evidence:
  - Financial Times YouTube | 55K views | Silicon shadows: inside the black market for AI chips | FT Film
  - CNBC Top News | 2026-08-27T08:28:05+00:00 | Nvidia jumps 7% in after blockbuster earnings boost AI confidence
  - CNBC Top News | 2026-08-27T07:29:46+00:00 | Nvidia agrees to buy Hugging Face for $12.9 billion, report says
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`

## 3. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-08-30` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - OPEC+ loses oil market sway in Iran war as China gains influence - Reuters
  - It's Not About China(?): U.S.-Iran Economic Sanctions Edition
  - Up to 1,300 people missing after Nepal flood disaster
- recent_evidence:
  - Reuters Markets via Google News RSS | 2026-08-27T07:14:25+00:00 | OPEC+ loses oil market sway in Iran war as China gains influence - Reuters
  - 무역킹 Trade King YouTube | 14K views | It's Not About China(?): U.S.-Iran Economic Sanctions Edition
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`
