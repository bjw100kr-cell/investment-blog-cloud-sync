# Approval Evidence Sheet

사용자가 초안을 최종 확인하기 전에, 왜 이 글이 오늘 올라올 가치가 있는지 근거를 빠르게 보는 시트입니다.
- 원칙: 초안 내용과 함께 근거 소스, 검색 수요, 시의성을 같이 보고 최종 확인합니다.
- generated_at: `2026-09-10T16:16:52.959192+00:00`
- item_count: `3`

## 1. FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지

- keyword: `fomc`
- publish_date: `2026-09-10`
- priority_score: `134.0`
- ready_now: `True` / quality_status `pass`
- reason: 공식 소스 기반 확인 가능, 복수 소스 교차 확인 가능 (2개), 거시 해설형 글로 전환 가치 높음
- format: `macro_explainer`
- demand_signal_score: `3500`
- fallback_source: `source_snapshot_rank`
- source_count: `2`
- score_breakdown: search `23` / timeliness `25` / monetization `15`
- source_names: CNBC Top News, Federal Reserve Monetary Policy Press
- sample_headlines:
  - Federal Reserve issues FOMC statement
  - Federal Reserve announces the leadership and objectives of its task forces to advance the conduct of monetary policy
  - Federal Reserve Board and Federal Open Market Committee release economic projections from the June 16-17 FOMC meeting
  - The likelihood of a Fed interest rate hike next week just got a lot higher
- recent_evidence:
  - Federal Reserve Monetary Policy Press | 2026-07-29T18:00:00+00:00 | Federal Reserve issues FOMC statement | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260729a.htm
  - Federal Reserve Monetary Policy Press | 2026-06-17T18:00:00+00:00 | Federal Reserve issues FOMC statement | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617a.htm
  - Federal Reserve Monetary Policy Press | 2026-06-17T18:00:00+00:00 | Federal Reserve Board and Federal Open Market Committee release economic projections from the June 16-17 FOMC meeting | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617b.htm
  - Federal Reserve Monetary Policy Press | 2026-08-19T18:00:00+00:00 | Minutes of the Federal Open Market Committee, July 28–29, 2026 | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260819a.htm
  - Federal Reserve Monetary Policy Press | 2026-07-09T19:00:00+00:00 | Federal Reserve announces the leadership and objectives of its task forces to advance the conduct of monetary policy | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260709a.htm

## 2. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword: `bitcoin`
- publish_date: `2026-09-11`
- priority_score: `121.0`
- ready_now: `True` / quality_status `pass`
- reason: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (risk_off)
- format: `crypto_analysis`
- demand_signal_score: `4000`
- fallback_source: `source_snapshot_rank`
- source_count: `3`
- score_breakdown: search `26` / timeliness `18` / monetization `15`
- source_names: CoinDesk RSS, Cointelegraph, Investing.com Crypto News
- sample_headlines:
  - Bitcoin Bancorp snaps up thousands of defunct Bitcoin Depot ATMs for $620,000
  - Crypto for Advisors: Hyperliquid and the future of finance
  - Threatened with arrest online? Recognizing a law enforcement impersonation scam
  - Crypto researchers cut Bitcoin and Ethereum quantum attack estimate by 50%
  - Bitcoin falls on US PPI overshoot as 30-year bond yield hits new 19-year high
- recent_evidence:
  - CoinDesk RSS | 2026-09-10T15:14:49+00:00 | Bitcoin Bancorp snaps up thousands of defunct Bitcoin Depot ATMs for $620,000 | https://www.coindesk.com/business/2026/09/10/a-quarter-of-bankrupt-bitcoin-depot-s-atms-snapped-up-for-less-than-usd1-million
  - Cointelegraph | 2026-09-10T14:52:15+00:00 | Bitcoin falls on US PPI overshoot as 30-year bond yield hits new 19-year high | https://cointelegraph.com/markets/bitcoin-falls-on-us-ppi-overshoot-as-30-year-bond-yield-hits-new-19-year-high?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
  - CoinDesk RSS | 2026-09-10T13:00:00+00:00 | Crypto researchers cut Bitcoin and Ethereum quantum attack estimate by 50% | https://www.coindesk.com/tech/2026/09/10/crypto-researchers-cut-bitcoin-and-ethereum-quantum-attack-estimate-by-50
  - Investing.com Crypto News | 2026-09-10 13:46:49 | Bitcoin drops to $77.1k on Iran jitters, higher yields | https://www.investing.com/news/cryptocurrency-news/bitcoin-down-to-783k-on-iran-jitters-higher-yields-4894954
  - Investing.com Crypto News | 2026-09-10 07:53:38 | Coinbase CEO calls the bottom in Bitcoin | https://www.investing.com/news/cryptocurrency-news/coinbase-ceo-calls-the-bottom-in-bitcoin-4895075

## 3. 미국 빅테크 주가가 흔들릴 때 확인할 것: 실적, 금리, AI 투자

- keyword: `us_big_tech`
- publish_date: `2026-09-12`
- priority_score: `96.0`
- ready_now: `False` / quality_status `review_before_publish`
- reason: 복수 소스 교차 확인 가능 (4개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능
- format: `sector_analysis`
- demand_signal_score: `0`
- fallback_source: `mapped_candidate`
- source_count: `4`
- score_breakdown: search `15` / timeliness `17` / monetization `15`
- source_names: CNBC Top News, CoinDesk RSS, Investing.com Crypto News, MarketWatch Breaking News
- sample_headlines:
  - Polymarket names former Amazon finance chief Warren Jenson as its first CFO
  - Apple makes biggest change to iPhone release cadence in 7 years in Ternus' first showcase as CEO
  - BTCC Exchange Launches $1M "Trade to Win" Competition Ahead of TOKEN2049, with Tesla Cybertruck as Top Prize
  - Meta is winning over Wall Street with its new Muse AI agent
- recent_evidence:
  - CoinDesk RSS | 2026-09-10T16:10:03+00:00 | Polymarket names former Amazon finance chief Warren Jenson as its first CFO | https://www.coindesk.com/markets/2026/09/10/polymarket-names-former-amazon-finance-chief-warren-jenson-as-its-first-cfo
  - MarketWatch Breaking News | 2026-09-10T15:23:00+00:00 | Meta is winning over Wall Street with its new Muse AI agent | https://www.marketwatch.com/story/meta-is-winning-over-wall-street-with-its-new-muse-ai-agent-0700ca87?mod=mw_rss_topstories
  - CNBC Top News | 2026-09-10T14:45:52+00:00 | Apple makes biggest change to iPhone release cadence in 7 years in Ternus' first showcase as CEO | https://www.cnbc.com/2026/09/10/apple-makes-biggest-change-to-iphone-release-cadence-in-7-years.html
  - Google Trends US | 2026-09-10T08:30:00-07:00 | wolverine metacritic | https://trends.google.com/trending/rss?geo=US
  - Investing.com Crypto News | 2026-09-10 14:30:36 | BTCC Exchange Launches $1M "Trade to Win" Competition Ahead of TOKEN2049, with Tesla Cybertruck as Top Prize | https://www.investing.com/news/cryptocurrency-news/btcc-exchange-launches-1m-trade-to-win-competition-ahead-of-token2049-with-tesla-cybertruck-as-top-prize-4896310
