# Approval Evidence Sheet

사용자가 초안을 최종 확인하기 전에, 왜 이 글이 오늘 올라올 가치가 있는지 근거를 빠르게 보는 시트입니다.
- 원칙: 초안 내용과 함께 근거 소스, 검색 수요, 시의성을 같이 보고 최종 확인합니다.
- generated_at: `2026-07-09T18:30:29.697233+00:00`
- item_count: `3`

## 1. FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지

- keyword: `fomc`
- publish_date: `2026-07-09`
- priority_score: `136.0`
- ready_now: `True` / quality_status `pass`
- reason: 공식 소스 기반 확인 가능, 복수 소스 교차 확인 가능 (3개), 거시 해설형 글로 전환 가치 높음
- format: `macro_explainer`
- demand_signal_score: `3500`
- fallback_source: `source_snapshot_rank`
- source_count: `3`
- score_breakdown: search `25` / timeliness `25` / monetization `15`
- source_names: CNBC Top News, Federal Reserve Monetary Policy Press, NYT Business
- sample_headlines:
  - Federal Reserve issues FOMC statement
  - Federal Reserve Board and Federal Open Market Committee release economic projections from the June 16-17 FOMC meeting
  - Kalshi traders see roughly 50% odds of a rate hike in 2026 as Fed is split on policy
  - Anthropic appoints former Fed Chair Ben Bernanke to its independent trust
- recent_evidence:
  - Federal Reserve Monetary Policy Press | 2026-06-17T18:00:00+00:00 | Federal Reserve issues FOMC statement | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617a.htm
  - Federal Reserve Monetary Policy Press | 2026-06-17T18:00:00+00:00 | Federal Reserve Board and Federal Open Market Committee release economic projections from the June 16-17 FOMC meeting | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617b.htm
  - Federal Reserve Monetary Policy Press | 2026-04-29T18:00:00+00:00 | Federal Reserve issues FOMC statement | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260429a.htm
  - Federal Reserve Monetary Policy Press | 2026-07-08T18:00:00+00:00 | Minutes of the Federal Open Market Committee, June 16-17, 2026 | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260708a.htm
  - Federal Reserve Monetary Policy Press | 2026-05-20T18:00:00+00:00 | Minutes of the Federal Open Market Committee, April 28-29, 2026 | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260520a.htm

## 2. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword: `bitcoin`
- publish_date: `2026-07-10`
- priority_score: `125.0`
- ready_now: `True` / quality_status `pass`
- reason: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (extreme_fear)
- format: `crypto_analysis`
- demand_signal_score: `7300`
- fallback_source: `source_snapshot_rank`
- source_count: `3`
- score_breakdown: search `30` / timeliness `18` / monetization `15`
- source_names: CoinDesk RSS, Cointelegraph, Investing.com Crypto News
- sample_headlines:
  - Billions flowing out of bitcoin ETFs and private credit funds suggest rising market risks
  - AI contracts, not bitcoin, now drive miner valuations, and Cipher and TeraWulf look cheap, says analyst
  - Ethereum's newest nonprofit wants to become Wall Street's guide to crypto
  - Pricing houses in bitcoin exposes dollar's loss of value
  - Bitcoin miners’ AI pivot faces investor scrutiny over insider sales
- recent_evidence:
  - CoinDesk RSS | 2026-07-09T18:13:04+00:00 | Billions flowing out of bitcoin ETFs and private credit funds suggest rising market risks | https://www.coindesk.com/markets/2026/07/09/billions-flowing-out-of-bitcoin-etfs-and-private-credit-funds-suggest-rising-market-risks
  - Cointelegraph | 2026-07-09T17:09:01+00:00 | Bitcoin miners’ AI pivot faces investor scrutiny over insider sales | https://cointelegraph.com/news/bitcoin-miners-ai-pivot-faces-investor-scrutiny-over-insider-sales?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
  - Cointelegraph | 2026-07-09T16:31:10+00:00 | Can Bitcoin hold $62K ahead of Friday’s $1.4 billion options expiry? | https://cointelegraph.com/markets/can-bitcoin-hold-62k-ahead-of-fridays-14-billion-options-expiry?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
  - Cointelegraph | 2026-07-09T15:56:59+00:00 | Bitcoin traders reveal key levels as BTC price passes $63K after Trump Iran 'deal' comments | https://cointelegraph.com/markets/bitcoin-traders-reveal-key-levels-as-btc-price-passes-63k-after-trump-iran-deal-comments?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
  - CoinDesk RSS | 2026-07-09T15:53:42+00:00 | AI contracts, not bitcoin, now drive miner valuations, and Cipher and TeraWulf look cheap, says analyst | https://www.coindesk.com/markets/2026/07/09/cipher-terawulf-among-ai-infrastructure-stocks-trading-below-contract-value-compass-point-argues

## 3. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword: `ai_semiconductors`
- publish_date: ``
- priority_score: `104.0`
- ready_now: `False` / quality_status `needs_fix`
- reason: 복수 소스 교차 확인 가능 (3개), 섹터/세계 흐름 연결 해설 가능
- format: `sector_analysis`
- demand_signal_score: `2300`
- fallback_source: `source_snapshot_rank`
- source_count: `3`
- score_breakdown: search `15` / timeliness `18` / monetization `15`
- source_names: CNBC Top News, MarketWatch Breaking News, Reuters Markets via Google News RSS
- sample_headlines:
  - Meta jumps into AI coding market in effort to chase Anthropic and OpenAI
  - Anthropic appoints former Fed Chair Ben Bernanke to its independent trust
  - Wall St rises as chip rally offsets renewed Iran worries - Reuters
  - Micron’s stock surges on multibillion-dollar U.S. manufacturing push
- recent_evidence:
  - CNBC Top News | 2026-07-09T17:23:40+00:00 | Anthropic appoints former Fed Chair Ben Bernanke to its independent trust | https://www.cnbc.com/2026/07/09/anthropic-fed-chair-bernanke-independent-trust.html
  - Reuters Markets via Google News RSS | 2026-07-09T16:51:29+00:00 | Wall St rises as chip rally offsets renewed Iran worries - Reuters | https://news.google.com/rss/articles/CBMitAFBVV95cUxOWlJrcUhGNjUtY2dOX1RQcWxqNW1KNGtrZU9uYU5KSjZiaDdZM3ozU1BZUjR4WmJyLVJjLW9yYjJGRHdSSEo4T0NNVUQ1T2VHN19keUtvRklORURPYUhtS0hUR2NJWnRIcnd3VFRLdGpDTmcwSnA0WHcxSUJ2RHhrNG1hOWUycm5kUjl6OHhoTjhSNVZXRmFUVnRMclJYMW9FdXRJZ1VLSkFrbmxRWVg5N3Z5c3M?oc=5
  - CNBC Top News | 2026-07-09T14:00:01+00:00 | Meta jumps into AI coding market in effort to chase Anthropic and OpenAI | https://www.cnbc.com/2026/07/09/meta-jumps-into-ai-coding-market-to-chase-anthropic-and-openai.html
