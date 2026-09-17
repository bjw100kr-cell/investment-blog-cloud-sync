# Approval Evidence Sheet

사용자가 초안을 최종 확인하기 전에, 왜 이 글이 오늘 올라올 가치가 있는지 근거를 빠르게 보는 시트입니다.
- 원칙: 초안 내용과 함께 근거 소스, 검색 수요, 시의성을 같이 보고 최종 확인합니다.
- generated_at: `2026-09-17T16:48:14.075347+00:00`
- item_count: `3`

## 1. FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지

- keyword: `fomc`
- publish_date: `2026-09-17`
- priority_score: `140.0`
- ready_now: `True` / quality_status `pass`
- reason: 공식 소스 기반 확인 가능, 복수 소스 교차 확인 가능 (7개), 거시 해설형 글로 전환 가치 높음
- format: `macro_explainer`
- demand_signal_score: `6000`
- fallback_source: `source_snapshot_rank`
- source_count: `7`
- score_breakdown: search `29` / timeliness `25` / monetization `15`
- source_names: CNBC Top News, Cointelegraph, Federal Reserve Monetary Policy Press, Financial Times World, Investing.com Crypto News, NYT Business, Reuters Markets via Google News RSS
- sample_headlines:
  - Federal Reserve issues FOMC statement
  - Federal Reserve Board and Federal Open Market Committee release economic projections from the September 15-16 FOMC meeting
  - Federal Reserve announces the leadership and objectives of its task forces to advance the conduct of monetary policy
  - Bitcoin coils near $76.5K as US stocks rebound from Fed rate hike
- recent_evidence:
  - Federal Reserve Monetary Policy Press | 2026-09-16T18:00:00+00:00 | Federal Reserve issues FOMC statement | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm
  - Federal Reserve Monetary Policy Press | 2026-09-16T18:00:00+00:00 | Federal Reserve Board and Federal Open Market Committee release economic projections from the September 15-16 FOMC meeting | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916b.htm
  - Federal Reserve Monetary Policy Press | 2026-07-29T18:00:00+00:00 | Federal Reserve issues FOMC statement | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260729a.htm
  - Federal Reserve Monetary Policy Press | 2026-08-19T18:00:00+00:00 | Minutes of the Federal Open Market Committee, July 28–29, 2026 | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260819a.htm
  - Federal Reserve Monetary Policy Press | 2026-07-09T19:00:00+00:00 | Federal Reserve announces the leadership and objectives of its task forces to advance the conduct of monetary policy | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260709a.htm

## 2. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword: `bitcoin`
- publish_date: `2026-09-18`
- priority_score: `124.0`
- ready_now: `True` / quality_status `pass`
- reason: 복수 소스 교차 확인 가능 (4개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- format: `crypto_analysis`
- demand_signal_score: `5800`
- fallback_source: `source_snapshot_rank`
- source_count: `4`
- score_breakdown: search `29` / timeliness `20` / monetization `15`
- source_names: CNBC Top News, CoinDesk RSS, Cointelegraph, Investing.com Crypto News
- sample_headlines:
  - UK signals end of 'light-touch' era with multi-agency raid on peer-to-peer crypto hubs
  - U.S. SEC begins prepping for around-the-clock trading that crypto treats as the norm
  - Crypto for Advisors: Beyond bitcoin and ether
  - Clarity Act failure may hamper U.S. crypto as industry seeks legal clarity elsewhere
  - Bitcoin coils near $76.5K as US stocks rebound from Fed rate hike
- recent_evidence:
  - Cointelegraph | 2026-09-17T16:22:23+00:00 | Bitcoin coils near $76.5K as US stocks rebound from Fed rate hike | https://cointelegraph.com/markets/bitcoin-coils-near-765k-as-us-stocks-rebound-from-fed-rate-hike?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
  - CoinDesk RSS | 2026-09-17T14:57:11+00:00 | Crypto for Advisors: Beyond bitcoin and ether | https://www.coindesk.com/coindesk-indices/2026/09/17/crypto-for-advisors-beyond-bitcoin-and-ether
  - Cointelegraph | 2026-09-17T13:30:00+00:00 | Bitcoin treasury firms can outperform BTC... but is the risk worth taking? | https://cointelegraph.com/magazine/bitcoin-treasuries-can-outperform-btc-but-is-it-a-risk-worth-taking?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
  - Investing.com Crypto News | 2026-09-17 13:57:03 | Bitcoin steady at $76.5k as markets digest Fed rate hike, M.East tensions | https://www.investing.com/news/cryptocurrency-news/bitcoin-steady-as-markets-digest-fed-rate-hike-meast-tensions-4904892
  - Investing.com Crypto News | 2026-09-17 07:11:34 | Bitcoin consolidates above $75K support: Live levels | https://www.investing.com/news/cryptocurrency-news/bitcoin-trapped-in-76k81k-rectangle-live-breakout-levels-93CH-4898873

## 3. 미국 증시 지수 흐름: 나스닥, 금리, 빅테크 실적을 같이 봐야 하는 이유

- keyword: `us_index_flow`
- publish_date: `2026-09-19`
- priority_score: `126.0`
- ready_now: `False` / quality_status `review_before_publish`
- reason: 검색 트렌드 반응 존재, 복수 소스 교차 확인 가능 (4개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능, 실제 급상승 검색어 반영 (dow jones stock market)
- format: `sector_analysis`
- demand_signal_score: `5200`
- fallback_source: `trend_match`
- source_count: `4`
- score_breakdown: search `30` / timeliness `20` / monetization `15`
- trend_queries: dow jones stock market
- trend_regions: US
- source_names: CoinDesk RSS, Cointelegraph, Financial Times Home, Google Trends US
- sample_headlines:
  - dow jones stock market
  - Ratings giant S&P Global acquires OpenZeppelin in tokenized finance risk push
  - Zcash miner Fortitude names former Hut 8 chief Jaime Leverton CEO ahead of Nasdaq deal
  - Bitcoin coils near $76.5K as US stocks rebound from Fed rate hike
  - S&P Global to acquire blockchain security platform OpenZeppelin
- recent_evidence:
  - Cointelegraph | 2026-09-17T16:22:23+00:00 | Bitcoin coils near $76.5K as US stocks rebound from Fed rate hike | https://cointelegraph.com/markets/bitcoin-coils-near-765k-as-us-stocks-rebound-from-fed-rate-hike?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
  - CoinDesk RSS | 2026-09-17T13:15:21+00:00 | Ratings giant S&P Global acquires OpenZeppelin in tokenized finance risk push | https://www.coindesk.com/business/2026/09/17/ratings-giant-s-and-p-global-acquires-openzeppelin-in-tokenized-finance-risk-push
  - Cointelegraph | 2026-09-17T12:56:23+00:00 | S&P Global to acquire blockchain security platform OpenZeppelin | https://cointelegraph.com/news/sp-global-openzeppelin-acquisition-blockchain-security?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
  - CoinDesk RSS | 2026-09-17T12:00:00+00:00 | Zcash miner Fortitude names former Hut 8 chief Jaime Leverton CEO ahead of Nasdaq deal | https://www.coindesk.com/business/2026/09/17/zcash-miner-fortitude-names-former-hut-8-chief-jaime-leverton-ceo-ahead-of-nasdaq-deal
  - Financial Times Home | 2026-09-17T11:59:41+00:00 | Turkish authorities rush to stem fallout from stock market scandal | https://www.ft.com/content/ef54585a-4d2f-4538-b185-9bff75ef2f5e?syn-25a6b1a6=1
