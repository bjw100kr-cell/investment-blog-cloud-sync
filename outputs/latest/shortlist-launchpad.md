# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-07-20` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - Bitcoin's biggest advocate, Michael Saylor, says new plan to clean up the blockchain is 'a bad idea'
  - Tether's USDT hits 2-year countdown threatening its position on U.S. crypto platforms
  - Kraken says simpler options can unlock crypto's next derivatives market
- recent_evidence:
  - CoinDesk RSS | 2026-07-19T15:19:21+00:00 | Bitcoin's biggest advocate, Michael Saylor, says new plan to clean up the blockchain is 'a bad idea'
  - CoinDesk RSS | 2026-07-19T10:00:00+00:00 | Bitcoin’s quantum problem gets a recovery tool, but not for Satoshi’s 1.1 million coins
  - Cointelegraph | 2026-07-19T09:16:42+00:00 | Electronic Transactions Association CEO Expecting More Partnerships with Bitcoin Startups
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-07-21` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Chip stock pullback sparks worries about AI rally strength, leveraged trades - Reuters
  - Wall St ends lower for the day and week as chip selloff broadens - Reuters
  - World stocks fall in semiconductor rout; oil rises on Middle East escalation - Reuters
- recent_evidence:
  - Financial Times YouTube | 38K views | Silicon shadows: inside the black market for AI chips | FT Film
  - Reuters Markets via Google News RSS | 2026-07-17T22:51:35+00:00 | World stocks fall in semiconductor rout; oil rises on Middle East escalation - Reuters
  - Reuters Markets via Google News RSS | 2026-07-17T22:31:24+00:00 | Wall St ends lower for the day and week as chip selloff broadens - Reuters
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`

## 3. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-07-22` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (2개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - China's Jingye Steel urges UK to compensate its investment losses - Reuters
  - China’s Jingye demands payout over British Steel nationalisation
- recent_evidence:
  - Financial Times World | 2026-07-19T10:50:00+00:00 | China’s Jingye demands payout over British Steel nationalisation
  - Reuters Markets via Google News RSS | 2026-07-19T04:22:00+00:00 | China's Jingye Steel urges UK to compensate its investment losses - Reuters
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`
