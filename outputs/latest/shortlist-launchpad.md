# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 유가 상승이 물가와 증시에 번지는 경로: 투자자가 볼 3가지

- keyword `oil` / publish `2026-07-04` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 거시 해설형 글로 전환 가치 높음
- sample_headlines:
  - Oman walks a diplomatic tightrope over Strait of Hormuz fees, creating a ‘blind spot’ for markets
  - Oil prices little changed as US-Iran peace efforts hold - Reuters
  - Can Kazakhstan’s oil boom survive Putin’s War? | FT Film
- recent_evidence:
  - Financial Times YouTube | 90K views | Can Kazakhstan’s oil boom survive Putin’s War? | FT Film
  - Reuters Markets via Google News RSS | 2026-07-03T02:05:00+00:00 | Oil prices little changed as US-Iran peace efforts hold - Reuters
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords oil`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords oil`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword oil`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword oil --apply`

## 2. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-07-05` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (extreme_fear)
- sample_headlines:
  - Bitcoin’s next parabolic run may need $1 trillion in fresh capital
  - This sanctioned Russian stablecoin claims it processes billions, but blockchain analysts disagree
  - Trump says there is ‘nothing wrong’ with family’s crypto windfall
- recent_evidence:
  - Cointelegraph | 2026-07-04T08:31:02+00:00 | Tim Draper denies moving Bitcoin, reiterates $250,000 BTC prediction
  - CoinDesk RSS | 2026-07-04T06:48:42+00:00 | Bitcoin’s next parabolic run may need $1 trillion in fresh capital
  - Cointelegraph | 2026-07-04T05:05:19+00:00 | Bitcoin profit and loss ratio falls to 43-month low
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 3. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-07-06` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Memory and semiconductor stocks lose momentum, bitcoin rebounds in sign of changing investor focus
  - Trading Day: Chips are down, and so are payrolls - Reuters
  - Dow jumps to record closing high after soft US jobs data, Nasdaq down with chip shares - Reuters
- recent_evidence:
  - MarketWatch Breaking News | 2026-07-03T18:52:00+00:00 | Nvidia is betting on a trillion-dollar robotics boom. Here is the hidden way to trade it.
  - CoinDesk RSS | 2026-07-03T10:41:52+00:00 | Memory and semiconductor stocks lose momentum, bitcoin rebounds in sign of changing investor focus
  - Reuters Markets via Google News RSS | 2026-07-02T23:11:39+00:00 | Dow jumps to record closing high after soft US jobs data, Nasdaq down with chip shares - Reuters
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`
