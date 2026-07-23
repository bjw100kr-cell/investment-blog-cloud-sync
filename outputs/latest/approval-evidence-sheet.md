# Approval Evidence Sheet

사용자가 초안을 최종 확인하기 전에, 왜 이 글이 오늘 올라올 가치가 있는지 근거를 빠르게 보는 시트입니다.
- 원칙: 초안 내용과 함께 근거 소스, 검색 수요, 시의성을 같이 보고 최종 확인합니다.
- generated_at: `2026-07-23T17:04:07.646784+00:00`
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword: `bitcoin`
- publish_date: `2026-07-24`
- priority_score: `122.0`
- ready_now: `True` / quality_status `pass`
- reason: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- format: `crypto_analysis`
- demand_signal_score: `6000`
- fallback_source: `source_snapshot_rank`
- source_count: `3`
- score_breakdown: search `29` / timeliness `18` / monetization `15`
- source_names: CoinDesk RSS, Cointelegraph, Investing.com Crypto News
- sample_headlines:
  - Crypto for Advisors: It’s time for tokenization to get to work
  - Goldman Sachs CEO backs Clarity Act despite banking industry's concerns over stablecoin rules
  - BlackRock, Coinbase, Strategy in a new group pledging $15 million to prepare Bitcoin for quantum threats
  - Goldman Sachs CEO backs ‘not perfect’ CLARITY Act as vote expected soon
  - Here’s why the CLARITY Act’s ethics deal may be so hard to reach
- recent_evidence:
  - Cointelegraph | 2026-07-23T16:26:43+00:00 | Ethereum nears market bottom against Bitcoin, though key signals remain unconfirmed: CryptoQuant | https://cointelegraph.com/news/ethereum-nears-market-bottom-against-bitcoin-key-signals-remain-unconfirmed-cryptoquant?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
  - Cointelegraph | 2026-07-23T13:03:18+00:00 | Strategy-led group pledges $15M to quantum-proof Bitcoin network | https://cointelegraph.com/news/strategy-consortium-15m-quantum-proof-bitcoin?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
  - CoinDesk RSS | 2026-07-23T12:54:27+00:00 | BlackRock, Coinbase, Strategy in a new group pledging $15 million to prepare Bitcoin for quantum threats | https://www.coindesk.com/business/2026/07/23/blackrock-coinbase-strategy-in-group-pledging-usd15-million-to-prepare-bitcoin-for-quantum-threats
  - Investing.com Crypto News | 2026-07-23 13:49:54 | Bitcoin muted at $65k with Clarity Act progress in focus | https://www.investing.com/news/cryptocurrency-news/bitcoin-steady-at-65k-with-clarity-act-progress-in-focus-4807647
  - Investing.com Crypto News | 2026-07-23 07:06:34 | Bitcoin coils near $65,700 in tight range: Hourly levels | https://www.investing.com/news/cryptocurrency-news/bitcoin-trapped-in-64k-range-doji-at-resistance-live-levels-93CH-4800901

## 2. 미국 빅테크 주가가 흔들릴 때 확인할 것: 실적, 금리, AI 투자

- keyword: `us_big_tech`
- publish_date: `2026-07-25`
- priority_score: `116.0`
- ready_now: `False` / quality_status `review_before_publish`
- reason: 검색 트렌드 반응 존재, 복수 소스 교차 확인 가능 (3개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능, 실제 급상승 검색어 반영 (tesla stock)
- format: `sector_analysis`
- demand_signal_score: `1200`
- fallback_source: `trend_match`
- source_count: `3`
- score_breakdown: search `28` / timeliness `18` / monetization `15`
- trend_queries: tesla stock
- trend_regions: KR
- source_names: CNBC Top News, Google Trends KR, NYT Business
- sample_headlines:
  - tesla stock
  - Amazon and Microsoft pivot cloud gaming strategies to target different players
  - Tesla falls 13%, Alphabet sinks 7% as AI spending concerns spook investors
  - Ford Will Use Apple Maps in New Self-Driving System
- recent_evidence:
  - Google Trends KR | 2026-07-23T07:00:00-07:00 | tesla stock | https://trends.google.com/trending/rss?geo=KR
  - CNBC Top News | 2026-07-23T16:12:17+00:00 | Amazon and Microsoft pivot cloud gaming strategies to target different players | https://www.cnbc.com/2026/07/23/amazon-microsoft-cloud-gaming.html
  - CNBC Top News | 2026-07-23T15:57:35+00:00 | Tesla falls 13%, Alphabet sinks 7% as AI spending concerns spook investors | https://www.cnbc.com/2026/07/23/tesla-tsla-alphabet-googl-stock-today.html
  - NYT Business | 2026-07-23T14:28:40+00:00 | Ford Will Use Apple Maps in New Self-Driving System | https://www.nytimes.com/2026/07/23/business/ford-apple-software-self-driving.html

## 3. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword: `china`
- publish_date: `2026-07-26`
- priority_score: `80.0`
- ready_now: `False` / quality_status `review_before_publish`
- reason: 복수 소스 교차 확인 가능 (2개), 섹터/세계 흐름 연결 해설 가능
- format: `macro_explainer`
- demand_signal_score: `0`
- fallback_source: `mapped_candidate`
- source_count: `2`
- score_breakdown: search `8` / timeliness `10` / monetization `13`
- source_names: Financial Times Home, NYT Business
- sample_headlines:
  - Why the US is losing Chinese AI stars
  - China Rewrites the ‘Soft Power’ Playbook for the A.I. Age
- recent_evidence:
  - NYT Business | 2026-07-23T15:37:01+00:00 | China Rewrites the ‘Soft Power’ Playbook for the A.I. Age | https://www.nytimes.com/2026/07/23/business/china-ai-soft-power.html
