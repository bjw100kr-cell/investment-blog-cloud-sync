# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-09-17` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (6개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (risk_off)
- sample_headlines:
  - Crypto longs worth $570 million wiped out as Clarity Act fails
  - XRP sinks 10% as the Clarity Act fails and bitcoin slides toward $76,000
  - Crypto stocks sink after Senate rejects Clarity Act
- recent_evidence:
  - Cointelegraph | 2026-09-16T04:05:39+00:00 | Bitcoin ETFs shed $450M in biggest outflow since June
  - CoinDesk RSS | 2026-09-16T03:37:45+00:00 | XRP sinks 10% as the Clarity Act fails and bitcoin slides toward $76,000
  - Cointelegraph | 2026-09-15T21:23:00+00:00 | BIS paper finds major gap in Bitcoin onchain transfer estimates
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-09-19` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - China's AI leaders keep quiet despite U.S. 'publicity' on tech risks
  - Nvidia CEO Huang attending Trump's state dinner for China's Xi: Source
  - Can the US and China work together on AI risks?
- recent_evidence:
  - CNBC Top News | 2026-09-16T04:01:59+00:00 | China's AI leaders keep quiet despite U.S. 'publicity' on tech risks
  - Financial Times Home | 2026-09-16T01:18:40+00:00 | Can the US and China work together on AI risks?
  - CNBC Top News | 2026-09-15T22:06:16+00:00 | Nvidia CEO Huang attending Trump's state dinner for China's Xi: Source
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`

## 3. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-09-18` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Nvidia's Huang diverges with CEOs of Anthropic, OpenAI on AI safety at Dreamforce
  - Nvidia CEO Huang attending Trump's state dinner for China's Xi: Source
  - Nvidia and Meta bosses reject efforts to co-ordinate AI slowdown
- recent_evidence:
  - Financial Times YouTube | 61K views | Silicon shadows: inside the black market for AI chips | FT Film
  - Financial Times Home | 2026-09-16T01:55:23+00:00 | Nvidia and Meta bosses reject efforts to co-ordinate AI slowdown
  - CNBC Top News | 2026-09-15T22:17:47+00:00 | Nvidia's Huang diverges with CEOs of Anthropic, OpenAI on AI safety at Dreamforce
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`
