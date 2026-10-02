# Approval Evidence Sheet

사용자가 초안을 최종 확인하기 전에, 왜 이 글이 오늘 올라올 가치가 있는지 근거를 빠르게 보는 시트입니다.
- 원칙: 초안 내용과 함께 근거 소스, 검색 수요, 시의성을 같이 보고 최종 확인합니다.
- generated_at: `2026-10-02T05:06:31.388349+00:00`
- item_count: `3`

## 1. FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지

- keyword: `fomc`
- publish_date: `2026-10-02`
- priority_score: `137.0`
- ready_now: `True` / quality_status `pass`
- reason: 공식 소스 기반 확인 가능, 복수 소스 교차 확인 가능 (3개), 거시 해설형 글로 전환 가치 높음
- format: `macro_explainer`
- demand_signal_score: `4100`
- fallback_source: `source_snapshot_rank`
- source_count: `3`
- score_breakdown: search `26` / timeliness `25` / monetization `15`
- source_names: CNBC Top News, Federal Reserve Monetary Policy Press, Reuters Markets via Google News RSS
- sample_headlines:
  - Federal Reserve issues FOMC statement
  - Federal Reserve Board and Federal Open Market Committee release economic projections from the September 15-16 FOMC meeting
  - Federal Reserve announces the leadership and objectives of its task forces to advance the conduct of monetary policy
  - Trump could target three Fed governors. Removing them may be harder than it looks
- recent_evidence:
  - Federal Reserve Monetary Policy Press | 2026-09-16T18:00:00+00:00 | Federal Reserve issues FOMC statement | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm
  - Federal Reserve Monetary Policy Press | 2026-09-16T18:00:00+00:00 | Federal Reserve Board and Federal Open Market Committee release economic projections from the September 15-16 FOMC meeting | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916b.htm
  - Federal Reserve Monetary Policy Press | 2026-07-29T18:00:00+00:00 | Federal Reserve issues FOMC statement | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260729a.htm
  - Federal Reserve Monetary Policy Press | 2026-08-19T18:00:00+00:00 | Minutes of the Federal Open Market Committee, July 28–29, 2026 | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260819a.htm
  - Federal Reserve Monetary Policy Press | 2026-07-09T19:00:00+00:00 | Federal Reserve announces the leadership and objectives of its task forces to advance the conduct of monetary policy | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260709a.htm

## 2. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword: `bitcoin`
- publish_date: `2026-10-03`
- priority_score: `126.0`
- ready_now: `True` / quality_status `pass`
- reason: 복수 소스 교차 확인 가능 (4개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- format: `crypto_analysis`
- demand_signal_score: `6300`
- fallback_source: `source_snapshot_rank`
- source_count: `4`
- score_breakdown: search `29` / timeliness `20` / monetization `15`
- source_names: CNBC Top News, CoinDesk RSS, Cointelegraph, Investing.com Crypto News
- sample_headlines:
  - SEC proposes new crypto custody rules for investment advisers and funds
  - Crypto for Advisors: The CLARITY Act failed, but the rules came anyway
  - NEAR Intents hit by $3.8 million exploit as crypto's rough year of hacks continues
  - Live updates: Bitcoin posts tentative gains as rates drop ahead of Friday's jobs report
  - Illinois agrees to six-month delay of crypto tax as industry continues court battle
- recent_evidence:
  - Cointelegraph | 2026-10-02T04:18:43+00:00 | Core Lightning warns attackers are targeting unpatched Bitcoin nodes | https://cointelegraph.com/news/core-lightning-urges-upgrade-amid-reports-attackers-targeting-unpatched-nodes?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
  - CoinDesk RSS | 2026-10-01T11:59:17+00:00 | Live updates: Bitcoin posts tentative gains as rates drop ahead of Friday's jobs report | https://www.coindesk.com/tech/2026/10/01/live-updates-bitcoin-flat-near-usd84-000-after-best-quarter-since-2024
  - CoinDesk RSS | 2026-10-01T11:30:38+00:00 | Crypto lost $1.26 billion in hacks while bitcoin bulls enjoyed a monster quarter | https://www.coindesk.com/daybook-us/2026/10/01/crypto-lost-usd1-26-billion-in-hacks-while-bitcoin-bulls-enjoyed-a-monster-quarter
  - Investing.com Crypto News | 2026-10-01 21:51:19 | Bitcoin reverses course, inches up to kick off Q4 as U.S. Treasury bonds rally | https://www.investing.com/news/cryptocurrency-news/bitcoin-rises-to-84k-after-bumper-q3-gains-stubborn-yields-weigh-4926370
  - Investing.com Crypto News | 2026-10-01 19:18:44 | Bitcoin hits MFI 100 overbought at $84,789: Live levels | https://www.investing.com/news/cryptocurrency-news/bitcoin-slips-to-83119-bears-eye-81194-live-levels-93CH-4919475

## 3. 미국 증시 지수 흐름: 나스닥, 금리, 빅테크 실적을 같이 봐야 하는 이유

- keyword: `us_index_flow`
- publish_date: `2026-10-04`
- priority_score: `100.0`
- ready_now: `False` / quality_status `review_before_publish`
- reason: 복수 소스 교차 확인 가능 (3개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능
- format: `sector_analysis`
- demand_signal_score: `0`
- fallback_source: `mapped_candidate`
- source_count: `3`
- score_breakdown: search `15` / timeliness `18` / monetization `15`
- source_names: Cointelegraph, MarketWatch Breaking News, NYT Business
- sample_headlines:
  - China warns foreign spies about crypto, Singapore dominates Asia: Asia Express
  - Evernorth clears shareholder vote ahead of Nasdaq debut with 473M XRP treasury
  - Here’s who’s joining the S&P 500 in the index’s latest shakeup
  - The stock market is anything but normal right now — and these charts show it
  - U.S. Bond Yields Hit Highest Level Since 2002
- recent_evidence:
  - MarketWatch Breaking News | 2026-10-02T00:14:00+00:00 | Here’s who’s joining the S&P 500 in the index’s latest shakeup | https://www.marketwatch.com/story/heres-whos-joining-the-s-p-500-in-the-indexs-latest-shakeup-07280a15?mod=mw_rss_topstories
  - Cointelegraph | 2026-10-01T21:07:45+00:00 | Evernorth clears shareholder vote ahead of Nasdaq debut with 473M XRP treasury | https://cointelegraph.com/news/evernorth-clears-shareholder-vote-ahead-nasdaq-debut-473m-xrp-treasury?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
  - MarketWatch Breaking News | 2026-10-01T21:01:00+00:00 | The stock market is anything but normal right now — and these charts show it | https://www.marketwatch.com/story/the-stock-market-is-anything-but-normal-right-now-and-these-charts-show-it-91ea187d?mod=mw_rss_topstories
