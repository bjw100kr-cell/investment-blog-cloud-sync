# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-08-14` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - Strategy, Metaplanet unrealized bitcoin losses highlight risk of concentrating on just one token
  - Bitcoin holds steady near $64,000 as monero, hyperliquid outperform
  - Brazil’s largest bitcoin treasury firm plans ETF with 95% allocation to Strategy's STRC
- recent_evidence:
  - CoinDesk RSS | 2026-08-13T11:35:53+00:00 | Strategy, Metaplanet unrealized bitcoin losses highlight risk of concentrating on just one token
  - CoinDesk RSS | 2026-08-13T11:02:43+00:00 | Bitcoin holds steady near $64,000 as monero, hyperliquid outperform
  - CoinDesk RSS | 2026-08-13T09:39:52+00:00 | Brazil’s largest bitcoin treasury firm plans ETF with 95% allocation to Strategy's STRC
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-08-15` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - 'Big Short' investor Steve Eisman sees an Achilles heel in the AI boom
  - Anthropic investors bet on $2tn valuation in record IPO
  - Wall Street giants bet Nvidia’s AI chips will defy the laws of finance
- recent_evidence:
  - Financial Times YouTube | 52K | Silicon shadows: inside the black market for AI chips | FT Film
  - Financial Times World | 2026-08-13T10:14:54+00:00 | FirstFT: Anthropic investors bet on $2tn valuation
  - Financial Times Home | 2026-08-13T04:00:23+00:00 | Anthropic investors bet on $2tn valuation in record IPO
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`

## 3. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-08-16` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - China's WeRide eyes Australia, Southeast Asia among potential new markets after strong Q2 - Reuters
  - Price of niche rare earth jumps on fears of renewed Chinese export controls
  - America Wants to Make Its Own Humanoid Robots. That Won’t Be Easy.
- recent_evidence:
  - Reuters Markets via Google News RSS | 2026-08-13T09:11:43+00:00 | China's WeRide eyes Australia, Southeast Asia among potential new markets after strong Q2 - Reuters
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`
