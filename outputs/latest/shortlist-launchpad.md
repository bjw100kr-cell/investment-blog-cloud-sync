# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-10-06` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (5개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - Crypto's campaign arm, Fairshake, sets lists of U.S. House favorites it'll spend on
  - U.S. CFTC joins SEC in proposing crypto regulations, though spot-market gap lingers
  - Stripe to expand stablecoin cards to over 100 countries by the end of the year
- recent_evidence:
  - Cointelegraph | 2026-10-05T16:53:08+00:00 | Treasury yields at 5% threaten extending Bitcoin’s best quarter since 2017
  - Cointelegraph | 2026-10-05T15:09:57+00:00 | Bitcoin price fails to break higher after best weekly close in eight months
  - Cointelegraph | 2026-10-05T13:47:17+00:00 | Metaplanet reveals net income strategy to fuel Bitcoin accumulation
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-10-08` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 검색 트렌드 반응 존재, 복수 소스 교차 확인 가능 (2개), 섹터/세계 흐름 연결 해설 가능, 실제 급상승 검색어 반영 (중국인)
- sample_headlines:
  - 중국인
  - 2. Nigeria, Linked to the US-China Hegemony (Sunday School: Nigeria)
  - 2. Trump actually lost? Who says so? (US-China Summit)
- recent_evidence:
  - 무역킹 Trade King YouTube | 47K | 2. Trump actually lost? Who says so? (US-China Summit)
  - 무역킹 Trade King YouTube | 22K | 2. Nigeria, Linked to the US-China Hegemony (Sunday School: Nigeria)
  - 무역킹 Trade King YouTube | 18K | 1. The main topic of the US-China summit was SI (US-China summit)
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`

## 3. 미국 빅테크 주가가 흔들릴 때 확인할 것: 실적, 금리, AI 투자

- keyword `us_big_tech` / publish `2026-10-07` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능
- sample_headlines:
  - More than 60 U.S. stocks including Nvidia and Tesla are headed onchain. Here’s how it works
  - Satya Nadella reinvented Microsoft once. Can he do it again in the AI era?
  - Microsoft’s blazing stock comeback isn’t even close to being over, analyst says
- recent_evidence:
  - CNBC Top News | 2026-10-05T17:40:13+00:00 | Satya Nadella reinvented Microsoft once. Can he do it again in the AI era?
  - CoinDesk RSS | 2026-10-05T17:18:14+00:00 | More than 60 U.S. stocks including Nvidia and Tesla are headed onchain. Here’s how it works
  - MarketWatch Breaking News | 2026-10-05T17:02:00+00:00 | Microsoft’s blazing stock comeback isn’t even close to being over, analyst says
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_big_tech`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_big_tech`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_big_tech`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_big_tech --apply`
