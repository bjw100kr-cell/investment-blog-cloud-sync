# Source Freshness Board

사용자에게 초안을 보여주기 전에, 근거 소스가 지금 시점에도 충분히 신선한지 확인하는 보드입니다.
- generated_at: `2026-11-11T19:29:44.356957+00:00`
- snapshot_generated_at: `2026-11-11T19:29:40.594391+00:00`
- snapshot_age_days: `0.0`
- snapshot_status: `fresh`
- counts: fresh `2` / aging `0` / stale `1` / unknown `0`

## 1. FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지

- keyword: `fomc`
- freshness_status: `stale`
- newest_evidence_age_days: `14.1`
- newest_evidence_iso: `2026-10-28T18:00:00+00:00`
- quality_status: `pass` / ready_now `True`
- summary: 핵심 근거가 이미 오래돼 그대로 올리기에는 위험합니다. 마지막 대표 근거: Federal Reserve issues FOMC statement
- recommendation: 지금 상태로는 데일리 뉴스형 게시보다 refresh 후 재작성 또는 evergreen 해설형 전환이 더 안전합니다.
- recovery_mode: `full_refresh_needed`
- recovery_summary: 현재 fresh 근거가 없어서 먼저 전체 파이프라인을 다시 돌려 새 소스가 들어오는지 확인해야 합니다.
- recovery_command: `bash scripts/run_pipeline.sh`
- evidence: Federal Reserve Monetary Policy Press / 2026-10-28T18:00:00+00:00 / Federal Reserve issues FOMC statement
- evidence: Federal Reserve Monetary Policy Press / 2026-09-16T18:00:00+00:00 / Federal Reserve issues FOMC statement
- evidence: Federal Reserve Monetary Policy Press / 2026-09-16T18:00:00+00:00 / Federal Reserve Board and Federal Open Market Committee release economic projections from the September 15-16 FOMC meeting

## 2. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword: `bitcoin`
- freshness_status: `fresh`
- newest_evidence_age_days: `0.1`
- newest_evidence_iso: `2026-11-11T16:26:00+00:00`
- quality_status: `pass` / ready_now `True`
- summary: 최신 근거가 살아 있어 데일리 해설로 다루기 좋은 상태입니다. 대표 근거: Bitcoin hovers near $74K as stocks rise despite US bond yield rebound
- recommendation: 사용자 검토만 통과하면 바로 게시 후보로 유지해도 됩니다.
- recovery_mode: `publish_direct`
- recovery_summary: 현재 신선도가 살아 있어 데일리 해설형으로 바로 검토를 이어가도 됩니다.
- evidence: Cointelegraph / 2026-11-11T16:26:00+00:00 / Bitcoin hovers near $74K as stocks rise despite US bond yield rebound
- evidence: Cointelegraph / 2026-11-11T13:26:18+00:00 / Bitcoin Covenants Part 5: MATT and OP_CHECKCONTRACTVERIFY — How Bitcoin could carry state across transactions
- evidence: CoinDesk RSS / 2026-11-11T12:21:24+00:00 / Live news: Bitcoin remains under pressure as CoreWeave, Nvidia lead AI rebound

## 3. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword: `ai_semiconductors`
- freshness_status: `fresh`
- newest_evidence_age_days: `0.0`
- newest_evidence_iso: `2026-11-11T19:17:19+00:00`
- quality_status: `pass` / ready_now `True`
- summary: 최신 근거가 살아 있어 데일리 해설로 다루기 좋은 상태입니다. 대표 근거: Analysis: Is Nvidia too big to fail? Its AI financing web raises the stakes
- recommendation: 사용자 검토만 통과하면 바로 게시 후보로 유지해도 됩니다.
- recovery_mode: `publish_direct`
- recovery_summary: 현재 신선도가 살아 있어 데일리 해설형으로 바로 검토를 이어가도 됩니다.
- evidence: CNBC Top News / 2026-11-11T19:17:19+00:00 / Analysis: Is Nvidia too big to fail? Its AI financing web raises the stakes
- evidence: MarketWatch Breaking News / 2026-11-11T18:48:00+00:00 / Nvidia is spending more than ever on Washington lobbying. It may not stop Congress from limiting China chip sales now.
- evidence: Cointelegraph / 2026-11-11T18:30:43+00:00 / OKXICE moves ahead with tokenized stocks as blue chips push back
