# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-10-16` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - Crypto for Advisors: Wall Street is done waiting on Congress for crypto rules
  - How Brooklyn prosecutors and the FBI took down a massive crypto fraud network targeting Russian speakers
  - Under pressure, Ledger unveils plan to turn its crypto hardware wallet into a smartphone
- recent_evidence:
  - Cointelegraph | 2026-10-15T15:10:44+00:00 | Bitcoin slips under $80K after US PPI gains most in four years
  - CoinDesk RSS | 2026-10-15T11:15:00+00:00 | Bitcoin, copper, stocks, yields all fall; gold rises
  - CoinDesk RSS | 2026-10-15T10:52:11+00:00 | Altcoins lead crypto declines as Asian stocks drop; bitcoin little changed since midnight
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `` / verdict `approve` / quality `needs_fix`
- ready_now: `False` / hero_image_selected: `True`
- intent: 
- why_now: 복수 소스 교차 확인 가능 (5개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Nvidia, AMD, Dell sell-off in global tech rout on AI funding worries
  - TSMC chip capacity is ‘fierce’ battleground for AI customers, amid record quarter
  - Treasuries rally as investors seek shelter from AI turbulence
- recent_evidence:
  - CNBC Top News | 2026-10-15T16:19:09+00:00 | Nvidia, AMD, Dell sell-off in global tech rout on AI funding worries
  - CNBC Top News | 2026-10-15T15:51:23+00:00 | TSMC chip capacity is ‘fierce’ battleground for AI customers, amid record quarter
  - Reuters Markets via Google News RSS | 2026-10-15T14:02:41+00:00 | US chip stocks set to wipe out $2 trillion after latest selloff - Reuters
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`

## 3. 미국 빅테크 주가가 흔들릴 때 확인할 것: 실적, 금리, AI 투자

- keyword `us_big_tech` / publish `2026-10-17` / verdict `approve` / quality `review_before_publish`
- ready_now: `False` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 검색 트렌드 반응 존재, 복수 소스 교차 확인 가능 (3개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능, 실제 급상승 검색어 반영 (tesla autopilot)
- sample_headlines:
  - tesla autopilot
  - Nvidia, AMD, Dell sell-off in global tech rout on AI funding worries
  - TSMC chip capacity is ‘fierce’ battleground for AI customers, amid record quarter
- recent_evidence:
  - MarketWatch Breaking News | 2026-10-15T16:43:00+00:00 | Tesla may finally debut a flying car today, after testing fans’ patience for nearly a decade
  - CNBC Top News | 2026-10-15T16:19:09+00:00 | Nvidia, AMD, Dell sell-off in global tech rout on AI funding worries
  - Google Trends US | 2026-10-15T09:10:00-07:00 | tesla autopilot
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_big_tech`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_big_tech`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_big_tech`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_big_tech --apply`
