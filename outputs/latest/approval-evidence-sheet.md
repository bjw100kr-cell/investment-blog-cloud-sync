# Approval Evidence Sheet

사용자가 초안을 최종 확인하기 전에, 왜 이 글이 오늘 올라올 가치가 있는지 근거를 빠르게 보는 시트입니다.
- 원칙: 초안 내용과 함께 근거 소스, 검색 수요, 시의성을 같이 보고 최종 확인합니다.
- generated_at: `2026-11-21T06:37:51.990819+00:00`
- item_count: `3`

## 1. FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지

- keyword: `fomc`
- publish_date: `2026-11-21`
- priority_score: `135.0`
- ready_now: `True` / quality_status `pass`
- reason: 공식 소스 기반 확인 가능, 복수 소스 교차 확인 가능 (2개), 거시 해설형 글로 전환 가치 높음
- format: `macro_explainer`
- demand_signal_score: `3600`
- fallback_source: `source_snapshot_rank`
- source_count: `2`
- score_breakdown: search `24` / timeliness `25` / monetization `15`
- source_names: CoinDesk RSS, Federal Reserve Monetary Policy Press
- sample_headlines:
  - Federal Reserve announces revised tentative schedule of Federal Open Market Committee meetings in 2027
  - Federal Reserve issues FOMC statement
  - Federal Reserve Board and Federal Open Market Committee release economic projections from the September 15-16 FOMC meeting
  - Bitcoin plunges below $59,000 as rush to cash puts new bear market lows back in play
- recent_evidence:
  - Federal Reserve Monetary Policy Press | 2026-10-28T18:00:00+00:00 | Federal Reserve issues FOMC statement | https://www.federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm
  - Federal Reserve Monetary Policy Press | 2026-09-16T18:00:00+00:00 | Federal Reserve issues FOMC statement | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm
  - Federal Reserve Monetary Policy Press | 2026-09-16T18:00:00+00:00 | Federal Reserve Board and Federal Open Market Committee release economic projections from the September 15-16 FOMC meeting | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916b.htm
  - Federal Reserve Monetary Policy Press | 2026-11-18T19:00:00+00:00 | Minutes of the Federal Open Market Committee, October 27-28, 2026 | https://www.federalreserve.gov/newsevents/pressreleases/monetary20261118a.htm
  - Federal Reserve Monetary Policy Press | 2026-11-12T17:45:00+00:00 | Federal Reserve announces revised tentative schedule of Federal Open Market Committee meetings in 2027 | https://www.federalreserve.gov/newsevents/pressreleases/monetary20261112a.htm

## 2. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword: `bitcoin`
- publish_date: `2026-11-22`
- priority_score: `128.0`
- ready_now: `True` / quality_status `pass`
- reason: 복수 소스 교차 확인 가능 (4개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (extreme_fear)
- format: `crypto_analysis`
- demand_signal_score: `5900`
- fallback_source: `source_snapshot_rank`
- source_count: `4`
- score_breakdown: search `29` / timeliness `20` / monetization `15`
- source_names: CoinDesk RSS, Cointelegraph, Investing.com Crypto News, Reuters Markets via Google News RSS
- sample_headlines:
  - Bitcoin nodes could be stalled by repeating one ID 50,000 times. AI found the bug
  - XRP falls 10% as long bets unwind and ETF assets slip below $1 billion
  - Bitcoin tanks below $57,000 for the first time in two years, and its not alone
  - Bitcoin plunges below $59,000 as rush to cash puts new bear market lows back in play
  - Hong Kong moves to extend crypto licensing rules to brokers, advisers and custodians
- recent_evidence:
  - CoinDesk RSS | 2026-11-21T06:16:42+00:00 | Bitcoin nodes could be stalled by repeating one ID 50,000 times. AI found the bug | https://www.coindesk.com/markets/2026/11/21/bitcoin-nodes-could-be-stalled-by-repeating-one-id-50-000-times-ai-found-the-bug
  - CoinDesk RSS | 2026-11-21T04:10:07+00:00 | Bitcoin tanks below $57,000 for the first time in two years, and its not alone | https://www.coindesk.com/markets/2026/11/21/bitcoin-tanks-below-usd57-000-for-the-first-time-in-two-years-and-its-not-alone
  - Reuters Markets via Google News RSS | 2026-11-21T04:10:00+00:00 | Bitcoin falls to its lowest in two years - Reuters | https://news.google.com/rss/articles/CBMid0FVX3lxTE1NUk9lTzRodUF5M1QyMkpkS3ViSDhVQ2hHZlV1ZUowRnBQeF9Za3l0WkRFb1BUNzVoS1NxcFFERDAydTVnLVpIMG9hcmRUV3hyb1F1RURKeGF3WV9iNlJScVlrYk95VmRJWWxjcE5GLUR4NUgtYWVj?oc=5
  - Investing.com Crypto News | 2026-11-21 06:02:03 | Bitcoin Falls 10% In Rout | https://www.investing.com/news/cryptocurrency-news/bitcoin-falls-10-in-rout-5043212
  - Investing.com Crypto News | 2026-11-21 05:46:26 | Bitcoin crashes below $56,000 as liquidity squeeze deepens crypto selloff | https://www.investing.com/news/cryptocurrency-news/bitcoin-crashes-below-56000-as-liquidity-squeeze-deepens-crypto-selloff-5043199

## 3. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword: `ai_semiconductors`
- publish_date: ``
- priority_score: `120.0`
- ready_now: `False` / quality_status `needs_fix`
- reason: 복수 소스 교차 확인 가능 (7개), 섹터/세계 흐름 연결 해설 가능
- format: `sector_analysis`
- demand_signal_score: `6100`
- fallback_source: `source_snapshot_rank`
- source_count: `7`
- score_breakdown: search `29` / timeliness `21` / monetization `15`
- source_names: CNBC Top News, Cointelegraph, Financial Times Home, Financial Times World, MarketWatch Breaking News, NYT Business, Reuters Markets via Google News RSS
- sample_headlines:
  - Bitcoin falls below $60K for first time since July amid broader market selloff
  - Bitcoin price drops to $60K as Anthropic drops to $87 in tech sell-off
  - Nvidia stock plunges 14%, wraps up longest weekly losing streak since 2008 financial crisis
  - A massive bearish trade just happened in the chip stocks
  - The bull market has a new problem. The 'smart money' is selling
- recent_evidence:
  - NYT Business | 2026-11-21T05:13:03+00:00 | Alice Huang, Accused of Spying on Nvidia’s CEO, Is Linked to Firms With Ties to China’s Military | https://www.nytimes.com/2026/11/20/us/politics/nvidia-alice-huang-chips-china.html
  - Financial Times World | 2026-11-21T05:00:36+00:00 | The chip war’s next battleground | https://www.ft.com/content/cd4ecaf3-0ded-4830-94a8-4d9c24098c07?syn-25a6b1a6=1
  - NYT Business | 2026-11-21T01:06:52+00:00 | Nvidia Said to Face S.E.C. Probe Into Its Accounting Practices | https://www.nytimes.com/2026/11/20/business/nvidia-sec-accounting.html
  - CNBC Top News | 2026-11-20T22:59:33+00:00 | Nvidia stock plunges 14%, wraps up longest weekly losing streak since 2008 financial crisis | https://www.cnbc.com/2026/11/20/nvidias-7-week-losing-streak-is-longest-since-2008-financial-crisis.html
  - MarketWatch Breaking News | 2026-11-20T22:44:00+00:00 | Chip stocks see $2.3 trillion weekly wipeout as panic grips the AI trade | https://www.marketwatch.com/story/chip-stocks-see-2-3-trillion-weekly-wipeout-as-panic-grips-the-ai-trade-371f2f03?mod=mw_rss_topstories
