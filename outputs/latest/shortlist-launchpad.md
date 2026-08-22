# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-08-23` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (risk_on)
- sample_headlines:
  - Bitcoin and Ether bears get decimated amid 'squeeze-led' rally and Musk's X wants to pay creators in stablecoins: Crypto week in 5 stories
  - Zcash jumps 48% to over $800 as Grayscale spot ETF push adds to ‘next bitcoin’ buzz
  - How a Treasury buyback tweak helped bitcoin surge 25% to nearly $80,000 in days
- recent_evidence:
  - CoinDesk RSS | 2026-08-22T12:00:00+00:00 | Bitcoin and Ether bears get decimated amid 'squeeze-led' rally and Musk's X wants to pay creators in stablecoins: Crypto week in 5 stories
  - CoinDesk RSS | 2026-08-22T05:37:43+00:00 | Zcash jumps 48% to over $800 as Grayscale spot ETF push adds to ‘next bitcoin’ buzz
  - CoinDesk RSS | 2026-08-22T05:05:13+00:00 | How a Treasury buyback tweak helped bitcoin surge 25% to nearly $80,000 in days
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-08-24` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (2개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Wall St Week Ahead Nvidia earnings, Jackson Hole to test pillars of stock rally - Reuters
  - Silicon shadows: inside the black market for AI chips | FT Film
- recent_evidence:
  - Financial Times YouTube | 54K views | Silicon shadows: inside the black market for AI chips | FT Film
  - Reuters Markets via Google News RSS | 2026-08-21T10:15:25+00:00 | Wall St Week Ahead Nvidia earnings, Jackson Hole to test pillars of stock rally - Reuters
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`

## 3. 미국채 금리 상승이 나스닥과 코인에 부담이 되는 이유

- keyword `treasury_yields` / publish `2026-08-26` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: FOMC가 무엇인지와 금리·주식·코인에 왜 중요한지 알고 싶어 하는 초중급 투자자
- why_now: 복수 소스 교차 확인 가능 (7개), 거시 해설형 글로 전환 가치 높음
- sample_headlines:
  - Bitcoin and Ether bears get decimated amid 'squeeze-led' rally and Musk's X wants to pay creators in stablecoins: Crypto week in 5 stories
  - How a Treasury buyback tweak helped bitcoin surge 25% to nearly $80,000 in days
  - Bitcoin rally sends crypto stocks soaring as miners, treasury companies jump
- recent_evidence:
  - CoinDesk RSS | 2026-08-22T05:05:13+00:00 | How a Treasury buyback tweak helped bitcoin surge 25% to nearly $80,000 in days
  - Financial Times Home | 2026-08-22T04:00:38+00:00 | Bossing the bond market around never works
  - Investing.com Crypto News | 2026-08-22 10:01:31 | Bitcoin holds above $77,000 after Treasury-fuelled short squeeze
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords treasury_yields`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords treasury_yields`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword treasury_yields`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword treasury_yields --apply`
