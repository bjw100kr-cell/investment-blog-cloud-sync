# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-11-19` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (extreme_fear)
- sample_headlines:
  - Bitcoin's 12% slide through key support looks scary, but history says give it 3 months.
  - Coinbase CEO says AI agents will account for '99.9%' of transactions within a decade
  - Here’s what happened in crypto today
- recent_evidence:
  - 무역킹 Trade King YouTube | 무역킹 Trade King | Dumping Bitcoin for AI? Why Mining Companies Sold Off $8 Billion Worth and What It Means for Your...
  - CoinDesk RSS | 2026-11-18T04:34:21+00:00 | Bitcoin's 12% slide through key support looks scary, but history says give it 3 months.
  - Investing.com Crypto News | 2026-11-17 22:39:07 | Bitcoin slips to $64.7k amid ht to risk sentiment; Strategy buys more coins
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-11-20` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (9개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Nvidia shares rise on earnings beat, raised outlook despite leadership uncertainty
  - Nvidia board rejects Huang comeback despite record $116B quarter
  - Trump’s accounts traded up to $97.5 million in Nvidia as Huang gained White House access
- recent_evidence:
  - Financial Times World | 2026-11-18T05:31:23+00:00 | FirstFT: Nvidia insists Jensen Huang will not return as CEO
  - Financial Times World | 2026-11-18T05:00:26+00:00 | Nvidia’s big business in Singapore
  - Financial Times Home | 2026-11-18T05:00:26+00:00 | Anthropic IPO set to deliver windfall to handful of smaller VC firms
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`

## 3. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-11-21` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - China’s Xi calls for removing trade and investment barriers ahead of his meeting with Trump and Putin
  - Three things to watch as Trump, Xi and Putin meet in China
  - Putin pushes ‘Eurasian’ order ahead of meeting with Xi and Trump
- recent_evidence:
  - CNBC Top News | 2026-11-18T06:04:39+00:00 | Three things to watch as Trump, Xi and Putin meet in China
  - CNBC Top News | 2026-11-18T03:30:51+00:00 | China’s Xi calls for removing trade and investment barriers ahead of his meeting with Trump and Putin
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`
