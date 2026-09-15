# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-09-16` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (6개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - U.S. House panel shares crypto tax bill ahead of hearing later this week
  - Bitcoin slips to $77,800 as Senate Clarity Act vote nears and oil prices climb
  - Even if Clarity fails, Wall Street’s crypto push is unlikely to stop
- recent_evidence:
  - CoinDesk RSS | 2026-09-15T03:23:28+00:00 | Bitcoin slips to $77,800 as Senate Clarity Act vote nears and oil prices climb
  - Cointelegraph | 2026-09-14T18:56:28+00:00 | Bitcoin tops $79K, oil falls as Trump says Iran war could end
  - Cointelegraph | 2026-09-14T17:50:12+00:00 | Strive adds 469 Bitcoin to reach 25,000 BTC treasury
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-09-17` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Kraken brings DeFi yield to tokenized stocks and ETFs
  - The murky AI milestone that has some of the industry’s leading voices increasingly on edge
  - CrowdStrike and Palo Alto Networks lead software stocks to a never-before-seen feat
- recent_evidence:
  - Financial Times YouTube | 61K views | Silicon shadows: inside the black market for AI chips | FT Film
  - MarketWatch Breaking News | 2026-09-14T21:11:00+00:00 | Chip stocks were a safe AI play. Now they’ve turned into the market’s pain trade.
  - Reuters Markets via Google News RSS | 2026-09-14T09:16:00+00:00 | Wall Street ends down, calls for AI slowdown pummel chipmakers - Reuters
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`

## 3. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-09-18` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Trump goes scorched earth on AI warnings, raging about data center opposition and regulation
  - China's August retail sales miss forecast while investment slump deepens, piling pressure on Beijing
  - China tightens control of overseas travel in sweeping new law
- recent_evidence:
  - CNBC Top News | 2026-09-15T04:06:17+00:00 | China's August retail sales miss forecast while investment slump deepens, piling pressure on Beijing
  - Financial Times Home | 2026-09-15T02:26:44+00:00 | China’s economy shows signs of weakness as investment slumps
  - Financial Times Home | 2026-09-15T00:28:53+00:00 | China tightens control of overseas travel in sweeping new law
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`
