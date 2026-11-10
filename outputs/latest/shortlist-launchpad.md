# Shortlist Launchpad

shortlist 2개 글만 빠르게 검토하고 바로 다음 실행까지 이어가기 위한 시작 화면입니다.
- 원칙: 먼저 글을 읽고, 그 다음 confirm command 또는 helper apply command를 실행합니다.
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword `bitcoin` / publish `2026-11-11` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- sample_headlines:
  - Bitcoin miner MARA sold 13,597 BTC for $1.1 billion in six weeks, plans to sell more
  - Bitcoin faces U.S. CPI test as analysts warn inflation relief may not be enough
  - A Bitcoin block just neared a 2015 transaction record, but paid only $180 in fees
- recent_evidence:
  - CoinDesk RSS | 2026-11-10T05:18:31+00:00 | Bitcoin miner MARA sold 13,597 BTC for $1.1 billion in six weeks, plans to sell more
  - CoinDesk RSS | 2026-11-10T03:22:26+00:00 | Bitcoin faces U.S. CPI test as analysts warn inflation relief may not be enough
  - Cointelegraph | 2026-11-10T00:42:39+00:00 | HIVE, MARA mine more Bitcoin but earn less as crypto prices fall
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword `ai_semiconductors` / publish `2026-11-12` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (7개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - Google’s AI chip push adds more pressure on Nvidia
  - Jensen Huang affair puts Nvidia's future at risk, with no clear successor to the renowned CEO
  - TSMC's October sales jump as global chip boom rolls on
- recent_evidence:
  - CNBC Top News | 2026-11-10T05:42:42+00:00 | TSMC's October sales jump as global chip boom rolls on
  - Financial Times World | 2026-11-10T05:31:40+00:00 | FirstFT: FBI is ‘looking into’ Nvidia’s Huang, Trump says
  - Reuters Markets via Google News RSS | 2026-11-10T05:31:00+00:00 | Morning Bid: Anthropic IPO: Please try again - Reuters
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`

## 3. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword `china` / publish `2026-11-13` / verdict `approve` / quality `pass`
- ready_now: `True` / hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- why_now: 복수 소스 교차 확인 가능 (4개), 섹터/세계 흐름 연결 해설 가능
- sample_headlines:
  - China’s monthly imports grow at fastest pace in five years as surplus crosses $1 trillion in 2026
  - The short seller who saw signs of Nvidia’s China scandal months ago claims Megaspeed isn’t the only company helping China access chips
  - China’s trade surplus exceeds $1tn for first 10 months of year
- recent_evidence:
  - CNBC Top News | 2026-11-10T05:03:55+00:00 | China’s monthly imports grow at fastest pace in five years as surplus crosses $1 trillion in 2026
  - Financial Times World | 2026-11-10T05:03:06+00:00 | China’s trade surplus exceeds $1tn for first 10 months of year
  - NYT Business | 2026-11-10T04:00:06+00:00 | China’s Trade Surplus Passes $1 Trillion at Record Pace
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china --apply`
