# Source Freshness Board

사용자에게 초안을 보여주기 전에, 근거 소스가 지금 시점에도 충분히 신선한지 확인하는 보드입니다.
- generated_at: `2026-10-10T17:16:11.029499+00:00`
- snapshot_generated_at: `2026-10-10T17:16:06.103599+00:00`
- snapshot_age_days: `0.0`
- snapshot_status: `fresh`
- counts: fresh `2` / aging `1` / stale `0` / unknown `0`

## 1. FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지

- keyword: `fomc`
- freshness_status: `aging`
- newest_evidence_age_days: `3.0`
- newest_evidence_iso: `2026-10-07T18:00:00+00:00`
- quality_status: `pass` / ready_now `True`
- summary: 아직 쓸 수는 있지만 뉴스 속도는 조금 늦었습니다. 대표 근거: Federal Reserve issues FOMC statement
- recommendation: 초안은 유지하되 발행 직전에 가격, 수치, headline을 한 번 더 갱신하는 편이 안전합니다.
- recovery_mode: `refresh_before_publish`
- recovery_summary: 발행 직전 전체 파이프라인을 다시 돌려 headline과 숫자를 최신 상태로 갱신하는 편이 안전합니다.
- recovery_command: `bash scripts/run_pipeline.sh`
- evidence: Federal Reserve Monetary Policy Press / 2026-09-16T18:00:00+00:00 / Federal Reserve issues FOMC statement
- evidence: Federal Reserve Monetary Policy Press / 2026-09-16T18:00:00+00:00 / Federal Reserve Board and Federal Open Market Committee release economic projections from the September 15-16 FOMC meeting
- evidence: Federal Reserve Monetary Policy Press / 2026-07-29T18:00:00+00:00 / Federal Reserve issues FOMC statement

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword: `ai_semiconductors`
- freshness_status: `fresh`
- newest_evidence_age_days: `0.2`
- newest_evidence_iso: `2026-10-10T12:30:00+00:00`
- quality_status: `review_before_publish` / ready_now `False`
- summary: 최신 근거가 살아 있어 데일리 해설로 다루기 좋은 상태입니다. 대표 근거: Why Nvidia’s stock is dodging the AI credit scare that is crushing Broadcom and Oracle
- recommendation: 신선도는 괜찮습니다. 이미지나 품질 게이트만 보완하면 됩니다.
- recovery_mode: `publish_direct`
- recovery_summary: 현재 신선도가 살아 있어 데일리 해설형으로 바로 검토를 이어가도 됩니다.
- evidence: MarketWatch Breaking News / 2026-10-10T12:30:00+00:00 / Why Nvidia’s stock is dodging the AI credit scare that is crushing Broadcom and Oracle
- evidence: CNBC Top News / 2026-10-10T11:00:01+00:00 / Nvidia GPUs are everywhere. Here are the ways companies are accessing them

## 3. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword: `bitcoin`
- freshness_status: `fresh`
- newest_evidence_age_days: `0.1`
- newest_evidence_iso: `2026-10-10T15:08:04+00:00`
- quality_status: `pass` / ready_now `True`
- summary: 최신 근거가 살아 있어 데일리 해설로 다루기 좋은 상태입니다. 대표 근거: One year after 10/10 flash crash, bitcoin and ether liquidity have rebuilt, but altcoins still face risks
- recommendation: 사용자 검토만 통과하면 바로 게시 후보로 유지해도 됩니다.
- recovery_mode: `publish_direct`
- recovery_summary: 현재 신선도가 살아 있어 데일리 해설형으로 바로 검토를 이어가도 됩니다.
- evidence: CoinDesk RSS / 2026-10-10T12:00:00+00:00 / One year after 10/10 flash crash, bitcoin and ether liquidity have rebuilt, but altcoins still face risks
- evidence: CoinDesk RSS / 2026-10-10T11:00:00+00:00 / Bitcoin's $19 billion wake-up call: One-year after flash crash, has crypto learned anything?
- evidence: Cointelegraph / 2026-10-10T07:10:43+00:00 / Sam Altman-backed Bitcoin life insurer, Meanwhile, raises more funds
