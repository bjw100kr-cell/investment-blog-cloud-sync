# Approval Evidence Sheet

사용자가 초안을 최종 확인하기 전에, 왜 이 글이 오늘 올라올 가치가 있는지 근거를 빠르게 보는 시트입니다.
- 원칙: 초안 내용과 함께 근거 소스, 검색 수요, 시의성을 같이 보고 최종 확인합니다.
- generated_at: `2026-08-06T14:29:36.452541+00:00`
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword: `bitcoin`
- publish_date: `2026-08-07`
- priority_score: `124.0`
- ready_now: `True` / quality_status `pass`
- reason: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (extreme_fear)
- format: `crypto_analysis`
- demand_signal_score: `6300`
- fallback_source: `source_snapshot_rank`
- source_count: `3`
- score_breakdown: search `29` / timeliness `18` / monetization `15`
- source_names: CoinDesk RSS, Cointelegraph, Investing.com Crypto News
- sample_headlines:
  - JPMorgan says Hyperliquid ETF inflows have stalled as competition mounts
  - Bitcoin’s low volatility doesn’t necessarily mean low risk
  - Free Markets and Innovation, Sort Of
  - Why Sandisk and Western Digital crashed 10% and what it means for bitcoin
  - Bitcoin, ether benefit as traders seek safety of largest tokens
- recent_evidence:
  - Cointelegraph | 2026-08-06T11:48:37+00:00 | Bitcoin treasury trade ‘breaking’ and fund holdings drop 10%: Analysis | https://cointelegraph.com/markets/bitcoin-treasury-trade-breaking-and-fund-holdings-drop-10-analysis?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
  - CoinDesk RSS | 2026-08-06T11:37:03+00:00 | Bitcoin’s low volatility doesn’t necessarily mean low risk | https://www.coindesk.com/daybook-us/2026/08/06/bitcoin-s-low-volatility-doesn-t-necessarily-mean-low-risk
  - CoinDesk RSS | 2026-08-06T11:14:47+00:00 | Why Sandisk and Western Digital crashed 10% and what it means for bitcoin | https://www.coindesk.com/markets/2026/08/06/why-sandisk-and-western-digital-crashed-10-and-what-it-means-for-bitcoin
  - CoinDesk RSS | 2026-08-06T10:43:07+00:00 | Bitcoin, ether benefit as traders seek safety of largest tokens | https://www.coindesk.com/markets/2026/08/06/bitcoin-ether-benefit-as-traders-seek-safety-of-largest-tokens
  - Investing.com Crypto News | 2026-08-06 13:38:28 | Bitcoin muted at $64k as investors await Hormuz deal developments | https://www.investing.com/news/cryptocurrency-news/bitcoin-nears-65k-amid-hormuz-hopes-improving-etf-flows-4840150

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword: `ai_semiconductors`
- publish_date: `2026-08-08`
- priority_score: `91.0`
- ready_now: `True` / quality_status `pass`
- reason: 복수 소스 교차 확인 가능 (3개), 섹터/세계 흐름 연결 해설 가능
- format: `sector_analysis`
- demand_signal_score: `0`
- fallback_source: `mapped_candidate`
- source_count: `3`
- score_breakdown: search `12` / timeliness `12` / monetization `15`
- source_names: Financial Times Home, Financial Times YouTube, Reuters Markets via Google News RSS
- sample_headlines:
  - The deal that saved Intel
  - S&P 500 flat as chip, software weakness offsets broader gains - Reuters
  - Silicon shadows: inside the black market for AI chips | FT Film
- recent_evidence:
  - Financial Times YouTube | 50K views | Silicon shadows: inside the black market for AI chips | FT Film | https://www.youtube.com/watch?v=kFcWmQevQo8
  - Reuters Markets via Google News RSS | 2026-08-06T14:09:17+00:00 | S&P 500 flat as chip, software weakness offsets broader gains - Reuters | https://news.google.com/rss/articles/CBMiuwFBVV95cUxOa2poa2tBUFVOZFo0R0Q4T2lKVF9aWk5CWGd1Y1A0aXlTOFE1c1JBNlF3bk9qLVlnSUFmMTZoT05MVExKZk9oQzVhUmg4SnBLZ29vLUFDMU1Qb1lOZmd5ZVZHRGVuaTJHWWJyUjFRV19pU3U4NmItdkd0d2JaNWVUSmJZcFBSVEtPVDQyd1RySlA0Q2VCT3RZSzlsSUFPY2FsLUtNMWlubFpQbkZiVmt6TjBZdmRZeXlPMFBZ?oc=5

## 3. 관세와 무역 갈등이 증시에 미치는 영향: 환율과 공급망까지 보기

- keyword: `tariffs_trade`
- publish_date: `2026-08-09`
- priority_score: `84.0`
- ready_now: `False` / quality_status `review_before_publish`
- reason: 검색 트렌드 반응 존재, 섹터/세계 흐름 연결 해설 가능, 실제 급상승 검색어 반영 (무역)
- format: `macro_explainer`
- demand_signal_score: `400`
- fallback_source: `trend_match`
- source_count: `1`
- score_breakdown: search `11` / timeliness `5` / monetization `15`
- trend_queries: 무역
- trend_regions: KR
- source_names: Google Trends KR
- sample_headlines:
  - 무역
- recent_evidence:
  - Google Trends KR | 2026-08-06T05:10:00-07:00 | 무역 | https://trends.google.com/trending/rss?geo=KR
