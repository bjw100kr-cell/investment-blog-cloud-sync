# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-10-17` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - Quantum Alliance forms amid warnings 6.4 million bitcoin face future quantum threat
  - Altcoins outpace bitcoin as celestia jumps 16%, Warsh silent on interest-rate plans
  - Scammer gets scammed in Ledger spy-chip exploit, loses almost $5 million in bitcoin
- recent_evidence:
  - Cointelegraph | 2026-10-16T15:45:43+00:00 | Bitcoin price steadies around $82K after Fed’s Warsh avoids rate-hike hints
  - CoinDesk RSS | 2026-10-16T10:52:26+00:00 | Quantum Alliance forms amid warnings 6.4 million bitcoin face future quantum threat
  - CoinDesk RSS | 2026-10-16T10:41:03+00:00 | Altcoins outpace bitcoin as celestia jumps 16%, Warsh silent on interest-rate plans
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. 미국 빅테크 주가가 흔들릴 때 확인할 것: 실적, 금리, AI 투자

- keyword `us_big_tech` / publish `2026-10-18` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능
- sample_headlines:
  - Tokenized Tesla surges as Elon Musk unveils SpaceX-powered flying Roadster prototype
  - Tesla unveils long-delayed Roadster developed with SpaceX, fueling merger speculation
  - Is Apple’s foldable iPhone Duo worth $2,000? See how it stacks up against other foldable phones.
- recent_evidence:
  - CNBC Top News | 2026-10-16T15:52:41+00:00 | Tesla unveils long-delayed Roadster developed with SpaceX, fueling merger speculation
  - Financial Times World | 2026-10-16T15:21:03+00:00 | Apple set for UK legal fight over iPhone tap-to-pay rules
  - MarketWatch Breaking News | 2026-10-16T14:40:00+00:00 | Is Apple’s foldable iPhone Duo worth $2,000? See how it stacks up against other foldable phones.
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_big_tech`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_big_tech`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_big_tech`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_big_tech --apply`

## 3. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-10-19` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (2개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - U.S. raises Mastercard, Citigroup China market access in bilateral Bangkok talks, official says
  - After Welcoming China’s Electric Vehicles, This Country Is Paying the Price
- recent_evidence:
  - CNBC Top News | 2026-10-16T16:11:09+00:00 | U.S. raises Mastercard, Citigroup China market access in bilateral Bangkok talks, official says
  - NYT Business | 2026-10-16T11:20:58+00:00 | After Welcoming China’s Electric Vehicles, This Country Is Paying the Price
  - Reuters Markets via Google News RSS | 2026-10-16T08:19:55+00:00 | EXCLUSIVE: PetroChina set for record trading profit as war upends market, sources say - Reuters
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`
