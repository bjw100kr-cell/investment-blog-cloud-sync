# Approval Evidence Sheet

사용자가 초안을 최종 확인하기 전에, 왜 이 글이 오늘 올라올 가치가 있는지 근거를 빠르게 보는 시트입니다.
- 원칙: 초안 내용과 함께 근거 소스, 검색 수요, 시의성을 같이 보고 최종 확인합니다.
- generated_at: `2026-10-05T20:30:40.159133+00:00`
- item_count: `3`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword: `bitcoin`
- publish_date: `2026-10-06`
- priority_score: `126.0`
- ready_now: `True` / quality_status `pass`
- reason: 복수 소스 교차 확인 가능 (5개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (mixed)
- format: `crypto_analysis`
- demand_signal_score: `7200`
- fallback_source: `source_snapshot_rank`
- source_count: `5`
- score_breakdown: search `30` / timeliness `21` / monetization `15`
- source_names: CNBC Top News, CoinDesk RSS, Cointelegraph, Investing.com Crypto News, Reuters Markets via Google News RSS
- sample_headlines:
  - Crypto's campaign arm, Fairshake, sets lists of U.S. House favorites it'll spend on
  - U.S. CFTC joins SEC in proposing crypto regulations, though spot-market gap lingers
  - Stripe to expand stablecoin cards to over 100 countries by the end of the year
  - SEC approves a 3x fix for bitcoin and ether traders who miss the wild swings
  - Treasury crackdown exposes crypto's role in $2 million Hamas fundraising network
- recent_evidence:
  - Cointelegraph | 2026-10-05T16:53:08+00:00 | Treasury yields at 5% threaten extending Bitcoin’s best quarter since 2017 | https://cointelegraph.com/markets/bitcoin-q3-rally-treasury-yields-fed-rate-outlook?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
  - Cointelegraph | 2026-10-05T15:09:57+00:00 | Bitcoin price fails to break higher after best weekly close in eight months | https://cointelegraph.com/markets/bitcoin-price-fails-to-break-higher-after-best-weekly-close-in-eight-months?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
  - Cointelegraph | 2026-10-05T13:47:17+00:00 | Metaplanet reveals net income strategy to fuel Bitcoin accumulation | https://cointelegraph.com/news/metaplanet-net-income-strategy-bitcoin-accumulation?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
  - CoinDesk RSS | 2026-10-05T11:14:35+00:00 | SEC approves a 3x fix for bitcoin and ether traders who miss the wild swings | https://www.coindesk.com/daybook-us/2026/10/05/sec-approves-a-3x-fix-for-bitcoin-and-ether-traders-who-miss-the-wild-swings
  - CoinDesk RSS | 2026-10-05T10:58:03+00:00 | Metaplanet added 1,000 bitcoin net in the third quarter bringing holdings to 44,000 BTC | https://www.coindesk.com/business/2026/10/05/metaplanet-adds-1-000-bitcoin-after-sale-and-repurchase-launches-income-strategy

## 2. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword: `china`
- publish_date: `2026-10-08`
- priority_score: `95.0`
- ready_now: `True` / quality_status `pass`
- reason: 검색 트렌드 반응 존재, 복수 소스 교차 확인 가능 (2개), 섹터/세계 흐름 연결 해설 가능, 실제 급상승 검색어 반영 (중국인)
- format: `macro_explainer`
- demand_signal_score: `300`
- fallback_source: `trend_match`
- source_count: `2`
- score_breakdown: search `20` / timeliness `7` / monetization `15`
- trend_queries: 중국인
- trend_regions: KR
- source_names: Google Trends KR, 무역킹 Trade King YouTube
- sample_headlines:
  - 중국인
  - 2. Nigeria, Linked to the US-China Hegemony (Sunday School: Nigeria)
  - 2. Trump actually lost? Who says so? (US-China Summit)
  - 1. The main topic of the US-China summit was SI (US-China summit)
- recent_evidence:
  - 무역킹 Trade King YouTube | 47K | 2. Trump actually lost? Who says so? (US-China Summit) | https://www.youtube.com/watch?v=2TzvRL6bbAg
  - 무역킹 Trade King YouTube | 22K | 2. Nigeria, Linked to the US-China Hegemony (Sunday School: Nigeria) | https://www.youtube.com/watch?v=QjSdk47w6xI
  - 무역킹 Trade King YouTube | 18K | 1. The main topic of the US-China summit was SI (US-China summit) | https://www.youtube.com/watch?v=ulXxUSqKdKQ
  - Google Trends KR | 2026-10-05T12:20:00-07:00 | 중국인 | https://trends.google.com/trending/rss?geo=KR

## 3. 미국 빅테크 주가가 흔들릴 때 확인할 것: 실적, 금리, AI 투자

- keyword: `us_big_tech`
- publish_date: `2026-10-07`
- priority_score: `101.0`
- ready_now: `False` / quality_status `review_before_publish`
- reason: 복수 소스 교차 확인 가능 (3개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능
- format: `sector_analysis`
- demand_signal_score: `2100`
- fallback_source: `source_snapshot_rank`
- source_count: `3`
- score_breakdown: search `14` / timeliness `15` / monetization `15`
- source_names: CNBC Top News, CoinDesk RSS, MarketWatch Breaking News
- sample_headlines:
  - More than 60 U.S. stocks including Nvidia and Tesla are headed onchain. Here’s how it works
  - Satya Nadella reinvented Microsoft once. Can he do it again in the AI era?
  - Microsoft’s blazing stock comeback isn’t even close to being over, analyst says
- recent_evidence:
  - CNBC Top News | 2026-10-05T17:40:13+00:00 | Satya Nadella reinvented Microsoft once. Can he do it again in the AI era? | https://www.cnbc.com/2026/10/05/satya-nadella-reinvented-microsoft-once-can-he-do-it-in-the-ai-era.html
  - CoinDesk RSS | 2026-10-05T17:18:14+00:00 | More than 60 U.S. stocks including Nvidia and Tesla are headed onchain. Here’s how it works | https://www.coindesk.com/markets/2026/10/05/more-than-60-u-s-stocks-including-nvidia-and-tesla-are-headed-onchain-here-s-how-it-works
  - MarketWatch Breaking News | 2026-10-05T17:02:00+00:00 | Microsoft’s blazing stock comeback isn’t even close to being over, analyst says | https://www.marketwatch.com/story/microsofts-blazing-stock-comeback-isnt-even-close-to-being-over-analyst-says-265f7b6d?mod=mw_rss_topstories
  - Cointelegraph | 2026-10-05T13:47:17+00:00 | Metaplanet reveals net income strategy to fuel Bitcoin accumulation | https://cointelegraph.com/news/metaplanet-net-income-strategy-bitcoin-accumulation?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
  - CoinDesk RSS | 2026-10-05T10:58:03+00:00 | Metaplanet added 1,000 bitcoin net in the third quarter bringing holdings to 44,000 BTC | https://www.coindesk.com/business/2026/10/05/metaplanet-adds-1-000-bitcoin-after-sale-and-repurchase-launches-income-strategy
