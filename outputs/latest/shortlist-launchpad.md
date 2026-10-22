# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-10-23` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (risk_off)
- sample_headlines:
  - Crypto for Advisors: Stablecoins are ready for prime time
  - Crypto custody specialist Fireblocks denies it's in talks to be acquired by Visa
  - Crypto is making a splash in U.S. elections — but chiefly in jabs about industry influence
- recent_evidence:
  - Cointelegraph | 2026-10-22T16:50:51+00:00 | Bitcoin hashrate hits seven-month high as AI shift fails to ease mining competition
  - Cointelegraph | 2026-10-22T16:20:35+00:00 | Bitcoin circles $81.5K ETF cost basis as Trump Iran comments send stocks lower
  - Cointelegraph | 2026-10-22T13:42:34+00:00 | CryptoQuant CEO calls rising Bitcoin hashrate ‘indirect bullish signal’ from institutions
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. 미국 빅테크 주가가 흔들릴 때 확인할 것: 실적, 금리, AI 투자

- keyword `us_big_tech` / publish `2026-10-24` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (6개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능
- sample_headlines:
  - Meta stock sinks 6% as AI spend pushes free cash flow negative
  - Musk's clash with Ukraine accelerates demand for Starlink alternatives. Few exist
  - Meta sell-off drags US tech stocks lower as AI spending fears flare up
- recent_evidence:
  - MarketWatch Breaking News | 2026-10-22T16:48:00+00:00 | Zuckerberg’s California tax move is a win for Meta — and for him
  - CNBC Top News | 2026-10-22T15:45:57+00:00 | Meta stock sinks 6% as AI spend pushes free cash flow negative
  - Financial Times Home | 2026-10-22T14:58:27+00:00 | Meta sell-off drags US tech stocks lower as AI spending fears flare up
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_big_tech`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_big_tech`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_big_tech`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_big_tech --apply`

## 3. 유가 상승이 물가와 증시에 번지는 경로: 투자자가 볼 3가지

- keyword `oil` / publish `2026-10-22` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (5개), 거시 해설형 글로 전환 가치 높음
- sample_headlines:
  - Under-the-radar stocks to play the next leg of the energy trade with oil prices jumping again
  - Bitcoin drops back below $82k as AI selldown, rising oil batter risk
  - Nasdaq leads Wall Street lower on AI spending jitters; oil prices rebound - Reuters
- recent_evidence:
  - CNBC Top News | 2026-10-22T15:16:05+00:00 | Under-the-radar stocks to play the next leg of the energy trade with oil prices jumping again
  - Reuters Markets via Google News RSS | 2026-10-22T14:20:56+00:00 | Nasdaq leads Wall Street lower on AI spending jitters; oil prices rebound - Reuters
  - NYT Business | 2026-10-22T13:43:13+00:00 | Stocks Fall and Oil Rises as Investors Retreat from Mounting Risks
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords oil`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords oil`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword oil`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword oil --apply`
