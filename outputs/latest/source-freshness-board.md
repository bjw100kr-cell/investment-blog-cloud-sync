# Source Freshness Board

사용자에게 초안을 보여주기 전에, 근거 소스가 지금 시점에도 충분히 신선한지 확인하는 보드입니다.
- generated_at: `2026-08-04T03:16:38.549788+00:00`
- snapshot_generated_at: `2026-08-04T03:16:33.953696+00:00`
- snapshot_age_days: `0.0`
- snapshot_status: `fresh`
- counts: fresh `2` / aging `0` / stale `1` / unknown `0`

## 1. FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지

- keyword: `fomc`
- freshness_status: `stale`
- newest_evidence_age_days: `5.4`
- newest_evidence_iso: `2026-07-29T18:00:00+00:00`
- quality_status: `pass` / ready_now `True`
- summary: 핵심 근거가 이미 오래돼 그대로 올리기에는 위험합니다. 마지막 대표 근거: Federal Reserve issues FOMC statement
- recommendation: 지금 상태로는 데일리 뉴스형 게시보다 refresh 후 재작성 또는 evergreen 해설형 전환이 더 안전합니다.
- recovery_mode: `full_refresh_needed`
- recovery_summary: 현재 fresh 근거가 없어서 먼저 전체 파이프라인을 다시 돌려 새 소스가 들어오는지 확인해야 합니다.
- recovery_command: `bash scripts/run_pipeline.sh`
- evidence: Federal Reserve Monetary Policy Press / 2026-07-29T18:00:00+00:00 / Federal Reserve issues FOMC statement
- evidence: Federal Reserve Monetary Policy Press / 2026-06-17T18:00:00+00:00 / Federal Reserve issues FOMC statement
- evidence: Federal Reserve Monetary Policy Press / 2026-06-17T18:00:00+00:00 / Federal Reserve Board and Federal Open Market Committee release economic projections from the June 16-17 FOMC meeting

## 2. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword: `bitcoin`
- freshness_status: `fresh`
- newest_evidence_age_days: `0.2`
- newest_evidence_iso: `2026-08-03T21:34:56+00:00`
- quality_status: `pass` / ready_now `True`
- summary: 최신 근거가 살아 있어 데일리 해설로 다루기 좋은 상태입니다. 대표 근거: Trump-linked American Bitcoin president Matt Prusak departs for Giga Energy
- recommendation: 사용자 검토만 통과하면 바로 게시 후보로 유지해도 됩니다.
- recovery_mode: `publish_direct`
- recovery_summary: 현재 신선도가 살아 있어 데일리 해설형으로 바로 검토를 이어가도 됩니다.
- evidence: CoinDesk RSS / 2026-08-03T15:24:45+00:00 / Trump-linked American Bitcoin president Matt Prusak departs for Giga Energy
- evidence: CoinDesk RSS / 2026-08-03T14:46:08+00:00 / U.S.-Japan intervention revives yen carry trade fears for bitcoin
- evidence: CoinDesk RSS / 2026-08-03T12:17:10+00:00 / Strategy sold another $105 million of bitcoin last week, repurchased $81.2 million of STRC

## 3. AI 성장주를 볼 때 놓치기 쉬운 리스크: 매출 성장과 금리 부담

- keyword: `ai_growth_stocks`
- freshness_status: `fresh`
- newest_evidence_age_days: `0.2`
- newest_evidence_iso: `2026-08-03T23:35:43+00:00`
- quality_status: `review_before_publish` / ready_now `False`
- summary: 최신 근거가 살아 있어 데일리 해설로 다루기 좋은 상태입니다. 대표 근거: Palantir forecasts greater demand from US groups for its AI software
- recommendation: 신선도는 괜찮습니다. 이미지나 품질 게이트만 보완하면 됩니다.
- recovery_mode: `publish_direct`
- recovery_summary: 현재 신선도가 살아 있어 데일리 해설형으로 바로 검토를 이어가도 됩니다.
- evidence: Financial Times Home / 2026-08-03T23:35:43+00:00 / Palantir forecasts greater demand from US groups for its AI software
- evidence: CNBC Top News / 2026-08-03T22:47:54+00:00 / Palantir soars 12% on blowout quarter, with U.S. commercial revenue soaring nearly 150%
- evidence: MarketWatch Breaking News / 2026-08-03T21:59:00+00:00 / Palantir’s stock climbs after earnings, as AI drives turbocharged growth
