# Approval Evidence Sheet

사용자가 초안을 최종 확인하기 전에, 왜 이 글이 오늘 올라올 가치가 있는지 근거를 빠르게 보는 시트입니다.
- 원칙: 초안 내용과 함께 근거 소스, 검색 수요, 시의성을 같이 보고 최종 확인합니다.
- generated_at: `2026-08-28T22:11:03.752602+00:00`
- item_count: `3`

## 1. FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지

- keyword: `fomc`
- publish_date: `2026-08-28`
- priority_score: `140.0`
- ready_now: `True` / quality_status `pass`
- reason: 공식 소스 기반 확인 가능, 복수 소스 교차 확인 가능 (8개), 거시 해설형 글로 전환 가치 높음
- format: `macro_explainer`
- demand_signal_score: `5700`
- fallback_source: `source_snapshot_rank`
- source_count: `8`
- score_breakdown: search `29` / timeliness `25` / monetization `15`
- source_names: CoinDesk RSS, Cointelegraph, Federal Reserve Monetary Policy Press, Financial Times Home, Financial Times World, MarketWatch Breaking News, NYT Business, Reuters Markets via Google News RSS
- sample_headlines:
  - Federal Reserve issues FOMC statement
  - Federal Reserve announces the leadership and objectives of its task forces to advance the conduct of monetary policy
  - Federal Reserve Board and Federal Open Market Committee release economic projections from the June 16-17 FOMC meeting
  - Fed Chair Kevin Warsh at Jackson Hole: 'We have work to do' on inflation
- recent_evidence:
  - Federal Reserve Monetary Policy Press | 2026-07-29T18:00:00+00:00 | Federal Reserve issues FOMC statement | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260729a.htm
  - Federal Reserve Monetary Policy Press | 2026-06-17T18:00:00+00:00 | Federal Reserve issues FOMC statement | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617a.htm
  - Federal Reserve Monetary Policy Press | 2026-06-17T18:00:00+00:00 | Federal Reserve Board and Federal Open Market Committee release economic projections from the June 16-17 FOMC meeting | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617b.htm
  - Federal Reserve Monetary Policy Press | 2026-08-19T18:00:00+00:00 | Minutes of the Federal Open Market Committee, July 28–29, 2026 | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260819a.htm
  - Federal Reserve Monetary Policy Press | 2026-07-09T19:00:00+00:00 | Federal Reserve announces the leadership and objectives of its task forces to advance the conduct of monetary policy | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260709a.htm

## 2. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword: `bitcoin`
- publish_date: `2026-08-29`
- priority_score: `121.0`
- ready_now: `True` / quality_status `pass`
- reason: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (risk_off)
- format: `crypto_analysis`
- demand_signal_score: `4700`
- fallback_source: `source_snapshot_rank`
- source_count: `3`
- score_breakdown: search `26` / timeliness `18` / monetization `15`
- source_names: CoinDesk RSS, Cointelegraph, Investing.com Crypto News
- sample_headlines:
  - Ethena looks beyond crypto to squeeze yield from booming equity perpetuals
  - Bitcoin is outperforming stocks and correlating with gold just when it matters most
  - Here’s what happened in crypto today
  - Bullish provides USD.AI $100M stablecoin facility for GPU-backed lending
  - Bitcoin dips to $78.4K as Fed’s Warsh downplays softer inflation prints
- recent_evidence:
  - Cointelegraph | 2026-08-28T15:31:25+00:00 | Bitcoin dips to $78.4K as Fed’s Warsh downplays softer inflation prints | https://cointelegraph.com/markets/bitcoin-dips-fed-warsh-dismisses-recent-low-inflation-prints?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
  - Cointelegraph | 2026-08-28T14:53:40+00:00 | Crypto Biz: Bitcoin pumps, Wall Street does the paperwork | https://cointelegraph.com/news/crypto-biz-bitcoin-rally-crypto-stocks-circle-strategy-solana?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
  - CoinDesk RSS | 2026-08-28T11:43:19+00:00 | Bitcoin is outperforming stocks and correlating with gold just when it matters most | https://www.coindesk.com/daybook-us/2026/08/28/bitcoin-is-outperforming-stocks-and-correlating-with-gold-just-when-it-matters-most
  - Investing.com Crypto News | 2026-08-28 21:37:51 | Bitcoin sheds more than 3% on hawkish Warsh, loses steam after debasement rally | https://www.investing.com/news/cryptocurrency-news/bitcoin-steadies-near-80k-with-warsh-speech-in-focus-4880563
  - Investing.com Crypto News | 2026-08-28 19:27:35 | Bitcoin double top 70% formed near $77,742: Live levels | https://www.investing.com/news/cryptocurrency-news/bitcoin-stalls-below-78500-resistance-live-hourly-levels-93CH-4872743

## 3. 미국 빅테크 주가가 흔들릴 때 확인할 것: 실적, 금리, AI 투자

- keyword: `us_big_tech`
- publish_date: `2026-08-30`
- priority_score: `101.0`
- ready_now: `False` / quality_status `review_before_publish`
- reason: 검색 트렌드 반응 존재, 복수 소스 교차 확인 가능 (3개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능, 실제 급상승 검색어 반영 (apple watch ultra 4)
- format: `sector_analysis`
- demand_signal_score: `400`
- fallback_source: `trend_match`
- source_count: `3`
- score_breakdown: search `19` / timeliness `15` / monetization `15`
- trend_queries: apple watch ultra 4
- trend_regions: US
- source_names: CNBC Top News, Google Trends US, MarketWatch Breaking News
- sample_headlines:
  - apple watch ultra 4
  - Apple hikes subscription prices for Apple TV and Apple One in the U.S.
  - Microsoft’s stock seals its longest winning streak of the year as AI software fears fade
- recent_evidence:
  - MarketWatch Breaking News | 2026-08-28T21:34:00+00:00 | Microsoft’s stock seals its longest winning streak of the year as AI software fears fade | https://www.marketwatch.com/story/microsofts-stock-seals-its-longest-winning-streak-of-the-year-as-ai-software-fears-fade-e5669f5b?mod=mw_rss_topstories
  - CNBC Top News | 2026-08-28T19:09:34+00:00 | Apple hikes subscription prices for Apple TV and Apple One in the U.S. | https://www.cnbc.com/2026/08/28/apple-tv-one-price-hike-us.html
  - Google Trends US | 2026-08-28T14:30:00-07:00 | apple watch ultra 4 | https://trends.google.com/trending/rss?geo=US
