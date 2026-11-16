# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-11-17` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (extreme_fear)
- sample_headlines:
  - Former Robinhood engineer pleads guilty to insider trading scheme on Hyperliquid
  - Bitcoin risks falling below $60,000 as Nvidia earnings threaten to deepen crypto sell-off
  - Lighter suspends all withdrawals after $10.4 million crypto exploit
- recent_evidence:
  - 무역킹 Trade King YouTube | 무역킹 Trade King | Dumping Bitcoin for AI? Why Mining Companies Sold Off $8 Billion Worth and What It Means for Your...
  - CoinDesk RSS | 2026-11-16T20:35:21+00:00 | Bitcoin risks falling below $60,000 as Nvidia earnings threaten to deepen crypto sell-off
  - Cointelegraph | 2026-11-16T18:07:49+00:00 | Nvidia turmoil tests Bitcoin miners’ AI funding plans
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-11-18` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (6개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Bitcoin risks falling below $60,000 as Nvidia earnings threaten to deepen crypto sell-off
  - Nvidia turmoil tests Bitcoin miners’ AI funding plans
  - Bitcoin price fails to hold $65K as US stocks drop further on AI nerves
- recent_evidence:
  - 무역킹 Trade King YouTube | 33K | 2. After Mamdani, is AOC next..? The DSA taking over the US Democratic Party (US DSA)
  - MarketWatch Breaking News | 2026-11-16T21:17:00+00:00 | Micron, AMD and other AI stocks fall as the chip sector’s selloff intensifies
  - MarketWatch Breaking News | 2026-11-16T21:05:00+00:00 | Nvidia investors will be clamoring for these answers during a historic earnings call
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`

## 3. FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지

- keyword `fomc` / publish `2026-11-16` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 공식 소스 기반 확인 가능, 복수 소스 교차 확인 가능 (3개), 거시 해설형 글로 전환 가치 높음
- sample_headlines:
  - Federal Reserve announces revised tentative schedule of Federal Open Market Committee meetings in 2027
  - Federal Reserve issues FOMC statement
  - Federal Reserve Board and Federal Open Market Committee release economic projections from the September 15-16 FOMC meeting
- recent_evidence:
  - Federal Reserve Monetary Policy Press | 2026-10-28T18:00:00+00:00 | Federal Reserve issues FOMC statement
  - Federal Reserve Monetary Policy Press | 2026-09-16T18:00:00+00:00 | Federal Reserve issues FOMC statement
  - Federal Reserve Monetary Policy Press | 2026-09-16T18:00:00+00:00 | Federal Reserve Board and Federal Open Market Committee release economic projections from the September 15-16 FOMC meeting
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords fomc`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords fomc`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword fomc`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword fomc --apply`
