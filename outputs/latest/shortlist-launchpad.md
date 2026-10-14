# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-10-15` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - Bitcoin climbs toward $84,000 after Fed’s Williams sees no rate hikes in 2027
  - Largest Philippines crypto exchange, Coins.ph, said to face central bank regulatory action
  - Strive raising $500 million to buy additional bitcoin with new preferred share class
- recent_evidence:
  - CoinDesk RSS | 2026-10-14T03:50:54+00:00 | Bitcoin climbs toward $84,000 after Fed’s Williams sees no rate hikes in 2027
  - CoinDesk RSS | 2026-10-13T23:23:05+00:00 | Strive raising $500 million to buy additional bitcoin with new preferred share class
  - Cointelegraph | 2026-10-13T15:57:55+00:00 | Strive reports $208M in warrant exercises as Bitcoin holdings jump 11%
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-10-16` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Crypto exchange MNX takes on OKX, Bitget offering pre-IPO futures for AI giants
  - Asia shares edge up as chip selloff eases; US CPI awaited - Reuters
  - PODCAST: Cashing in chips - Reuters
- recent_evidence:
  - Reuters Markets via Google News RSS | 2026-10-14T01:53:00+00:00 | Asia shares edge up as chip selloff eases; US CPI awaited - Reuters
  - Reuters Markets via Google News RSS | 2026-10-13T23:25:08+00:00 | Nasdaq ends down as chipmakers fall and bank earnings roll in - Reuters
  - MarketWatch Breaking News | 2026-10-13T21:02:00+00:00 | Chip stocks suffer worst stretch in 16 months as AI fatigue grips the market
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`

## 3. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-10-17` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - China's producer prices rise at fastest pace since June 2022, beating expectations
  - Bank of America fined $1.2bn over money laundering failures
  - China’s exports surge 36% as AI-related shipments boom
- recent_evidence:
  - NYT Business | 2026-10-14T04:00:29+00:00 | China’s Exports Soar, Putting Its Trade Surplus on Track for a Record
  - Financial Times Home | 2026-10-14T03:56:03+00:00 | China’s exports surge 36% as AI-related shipments boom
  - CNBC Top News | 2026-10-14T03:14:48+00:00 | China's producer prices rise at fastest pace since June 2022, beating expectations
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`
