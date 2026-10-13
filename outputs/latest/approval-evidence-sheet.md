# Approval Evidence Sheet

사용자가 초안을 최종 확인하기 전에, 왜 이 글이 오늘 올라올 가치가 있는지 근거를 빠르게 보는 시트입니다.
- 원칙: 초안 내용과 함께 근거 소스, 검색 수요, 시의성을 같이 보고 최종 확인합니다.
- generated_at: `2026-10-13T06:24:18.718113+00:00`
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword: `bitcoin`
- publish_date: `2026-10-14`
- priority_score: `121.0`
- ready_now: `True` / quality_status `pass`
- reason: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- format: `crypto_analysis`
- demand_signal_score: `5200`
- fallback_source: `source_snapshot_rank`
- source_count: `3`
- score_breakdown: search `28` / timeliness `18` / monetization `15`
- source_names: CoinDesk RSS, Cointelegraph, Investing.com Crypto News
- sample_headlines:
  - Bitcoin whale that sat through the March 2020 crash moves $378 million
  - Tokenized SanDisk bets saw more liquidations than XRP as Asia’s chip rout wipes out $800 million
  - Bitcoin rebounds above $83,000 as it decouples from tumbling Korean stocks and Nasdaq futures
  - Tom Lee sees $2 trillion wealth transfer fueling crypto demand as Bitmine buys more ether
  - Here’s what happened in crypto today
- recent_evidence:
  - CoinDesk RSS | 2026-10-13T05:45:10+00:00 | Bitcoin whale that sat through the March 2020 crash moves $378 million | https://www.coindesk.com/markets/2026/10/13/bitcoin-whale-that-sat-through-the-march-2020-crash-moves-usd378-million
  - CoinDesk RSS | 2026-10-13T04:18:20+00:00 | Bitcoin rebounds above $83,000 as it decouples from tumbling Korean stocks and Nasdaq futures | https://www.coindesk.com/markets/2026/10/13/bitcoin-rebounds-above-usd83-000-as-it-decouples-from-tumbling-korean-stocks-and-nasdaq-futures
  - Investing.com Crypto News | 2026-10-12 22:04:19 | Bitcoin slips to $82.6k as rise in oil prices weigh on risk sentiment | https://www.investing.com/news/cryptocurrency-news/bitcoin-recovers-to-near-84k-as-falling-oil-prices-offer-some-support-4943235
  - Investing.com Crypto News | 2026-10-12 19:18:23 | Bitcoin clings to $81,479 support under heavy resistance: Live levels | https://www.investing.com/news/cryptocurrency-news/bitcoin-wedged-at-84175-between-key-support-and-resistance-live-93CH-4943299
  - Investing.com Crypto News | 2026-10-11 19:02:17 | Bitcoin trapped in $81K-$84K range: Breakout watch live | https://www.investing.com/news/cryptocurrency-news/bitcoin-tests-87363-resistance-with-fading-momentum-live-levels-93CH-4931135

## 2. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword: `china`
- publish_date: `2026-10-16`
- priority_score: `90.0`
- ready_now: `True` / quality_status `pass`
- reason: 복수 소스 교차 확인 가능 (3개), 섹터/세계 흐름 연결 해설 가능
- format: `macro_explainer`
- demand_signal_score: `0`
- fallback_source: `mapped_candidate`
- source_count: `3`
- score_breakdown: search `13` / timeliness `12` / monetization `14`
- source_names: CNBC Top News, Financial Times World, 무역킹 Trade King YouTube
- sample_headlines:
  - Visa gets Beijing's green light for bank card business after 40 years of working with China
  - So, what was the outcome of the US-China summit? (Recap)
  - China gets spiky on currencies
- recent_evidence:
  - CNBC Top News | 2026-10-13T06:20:55+00:00 | Visa gets Beijing's green light for bank card business after 40 years of working with China | https://www.cnbc.com/2026/10/13/visa-china-green-light-bank-card-business-.html
  - Financial Times World | 2026-10-13T05:30:09+00:00 | China gets spiky on currencies | https://www.ft.com/content/27be530d-2faf-43ce-874f-0e6e0802bee2?syn-25a6b1a6=1
  - 무역킹 Trade King YouTube | 10K | So, what was the outcome of the US-China summit? (Recap) | https://www.youtube.com/watch?v=vmt7f1eesDE

## 3. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword: `ai_semiconductors`
- publish_date: `2026-10-15`
- priority_score: `125.0`
- ready_now: `False` / quality_status `review_before_publish`
- reason: 검색 트렌드 반응 존재, 복수 소스 교차 확인 가능 (7개), 섹터/세계 흐름 연결 해설 가능, 실제 급상승 검색어 반영 (반도체)
- format: `sector_analysis`
- demand_signal_score: `5200`
- fallback_source: `trend_match`
- source_count: `7`
- score_breakdown: search `30` / timeliness `21` / monetization `15`
- trend_queries: 반도체
- trend_regions: KR
- source_names: CNBC Top News, CoinDesk RSS, Cointelegraph, Financial Times Home, Financial Times World, Google Trends KR, MarketWatch Breaking News
- sample_headlines:
  - 반도체
  - Tokenized SanDisk bets saw more liquidations than XRP as Asia’s chip rout wipes out $800 million
  - Bitcoin rebounds above $83,000 as it decouples from tumbling Korean stocks and Nasdaq futures
  - Meta claims new Muse Wonder AI models rival OpenAI, Anthropic
  - SK Hynix, SoftBank shares plunge as tech stocks in Asia track Wall Street chip sell-off
- recent_evidence:
  - Google Trends KR | 2026-10-12T22:10:00-07:00 | 반도체 | https://trends.google.com/trending/rss?geo=KR
  - Financial Times Home | 2026-10-13T05:44:06+00:00 | Chip stocks slide in wake of ‘casino’ comment by Broadcom boss | https://www.ft.com/content/e16f0422-cf75-4cc9-962d-4605e421dc63?syn-25a6b1a6=1
  - CoinDesk RSS | 2026-10-13T05:27:17+00:00 | Tokenized SanDisk bets saw more liquidations than XRP as Asia’s chip rout wipes out $800 million | https://www.coindesk.com/markets/2026/10/13/tokenized-sandisk-bets-saw-more-liquidations-than-xrp-as-asia-s-chip-rout-wipes-out-usd800-million
  - CNBC Top News | 2026-10-13T02:49:17+00:00 | SK Hynix, SoftBank shares plunge as tech stocks in Asia track Wall Street chip sell-off | https://www.cnbc.com/2026/10/13/sk-hynix-softbank-samsung-electronics-shares-tech-stocks-fall.html
  - Cointelegraph | 2026-10-13T01:54:31+00:00 | Meta claims new Muse Wonder AI models rival OpenAI, Anthropic | https://cointelegraph.com/news/meta-launches-muse-wonder-ai-models-challenging-top-rivals?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
