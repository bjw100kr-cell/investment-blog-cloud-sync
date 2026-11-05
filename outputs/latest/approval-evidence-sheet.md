# Approval Evidence Sheet

사용자가 초안을 최종 확인하기 전에, 왜 이 글이 오늘 올라올 가치가 있는지 근거를 빠르게 보는 시트입니다.
- 원칙: 초안 내용과 함께 근거 소스, 검색 수요, 시의성을 같이 보고 최종 확인합니다.
- generated_at: `2026-11-05T06:04:22.477505+00:00`
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword: `bitcoin`
- publish_date: `2026-11-06`
- priority_score: `124.0`
- ready_now: `True` / quality_status `pass`
- reason: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (risk_on)
- format: `crypto_analysis`
- demand_signal_score: `5900`
- fallback_source: `source_snapshot_rank`
- source_count: `3`
- score_breakdown: search `29` / timeliness `18` / monetization `15`
- source_names: CoinDesk RSS, Cointelegraph, Investing.com Crypto News
- sample_headlines:
  - Bitcoin holds above $80,000 as Zcash jumps 12% in post-election crypto rebound
  - Trump Media moves $342 million in bitcoin to Crypto.com, blockchain data show
  - Tokenization and stablecoins may weather Democrats' sweep as broader crypto rules face uncertainty
  - Crypto's Washington hopes fade, but Grayscale and BlackRock see growth ahead
  - Crypto's powerhouse super PAC suffers costly setback as Democrats sweep Congress
- recent_evidence:
  - CoinDesk RSS | 2026-11-05T05:13:45+00:00 | Bitcoin holds above $80,000 as Zcash jumps 12% in post-election crypto rebound | https://www.coindesk.com/markets/2026/11/05/bitcoin-holds-above-usd80-000-as-zcash-jumps-12-in-post-election-crypto-rebound
  - CoinDesk RSS | 2026-11-05T04:11:33+00:00 | Trump Media moves $342 million in bitcoin to Crypto.com, blockchain data show | https://www.coindesk.com/markets/2026/11/05/trump-media-moves-usd434-million-in-bitcoin-to-crypto-com-blockchain-data-show
  - Cointelegraph | 2026-11-04T23:20:17+00:00 | Mercado Bitcoin says phased reopening to begin Monday, will cover losses | https://cointelegraph.com/news/mercado-bitcoin-phased-reopening-to-begin-monday-pledges-to-cover-losses?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
  - Cointelegraph | 2026-11-04T21:30:00+00:00 | How Aussie Bitcoiners can avoid 2027’s shock CGT hike | https://cointelegraph.com/magazine/how-aussie-bitcoiners-can-avoid-2027s-shock-cgt-increase-part-1?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
  - Investing.com Crypto News | 2026-11-04 22:42:49 | Bitcoin tops $80k as Democrats sweep midterm elections, boosting risk sentiment | https://www.investing.com/news/cryptocurrency-news/bitcoin-recovers-to-near-78k-as-democrats-sweep-midterm-elections-4997542

## 2. 미국 증시 지수 흐름: 나스닥, 금리, 빅테크 실적을 같이 봐야 하는 이유

- keyword: `us_index_flow`
- publish_date: `2026-11-07`
- priority_score: `86.0`
- ready_now: `True` / quality_status `pass`
- reason: 복수 소스 교차 확인 가능 (2개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능
- format: `sector_analysis`
- demand_signal_score: `0`
- fallback_source: `mapped_candidate`
- source_count: `2`
- score_breakdown: search `8` / timeliness `10` / monetization `15`
- source_names: CNBC Top News, MarketWatch Breaking News
- sample_headlines:
  - What was really behind Wednesday's monster rally? Trump quickly making peace
  - This year’s worst-performing S&P 500 stock is finally seeing some major relief
- recent_evidence:
  - MarketWatch Breaking News | 2026-11-05T01:05:00+00:00 | This year’s worst-performing S&P 500 stock is finally seeing some major relief | https://www.marketwatch.com/story/this-years-worst-performing-s-p-500-stock-is-finally-seeing-some-major-relief-fff3fa85?mod=mw_rss_topstories

## 3. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword: `china`
- publish_date: `2026-11-08`
- priority_score: `69.0`
- ready_now: `False` / quality_status `review_before_publish`
- reason: 섹터/세계 흐름 연결 해설 가능
- format: `macro_explainer`
- demand_signal_score: `0`
- fallback_source: `mapped_candidate`
- source_count: `1`
- score_breakdown: search `4` / timeliness `5` / monetization `12`
- source_names: CNBC Top News
- sample_headlines:
  - Russia, China may be more aggressive if they feel Trump is on 'his way out': Brookings
- recent_evidence:
  - CNBC Top News | 2026-11-05T05:58:33+00:00 | Russia, China may be more aggressive if they feel Trump is on 'his way out': Brookings | https://www.cnbc.com/2026/11/05/trump-russia-china-summit-apec-midterms.html
