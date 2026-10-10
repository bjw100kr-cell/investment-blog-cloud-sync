# Source Freshness Board

사용자에게 초안을 보여주기 전에, 근거 소스가 지금 시점에도 충분히 신선한지 확인하는 보드입니다.
- generated_at: `2026-10-10T05:21:54.246183+00:00`
- snapshot_generated_at: `2026-10-10T05:21:48.776743+00:00`
- snapshot_age_days: `0.0`
- snapshot_status: `fresh`
- counts: fresh `1` / aging `1` / stale `0` / unknown `1`

## 1. FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지

- keyword: `fomc`
- freshness_status: `aging`
- newest_evidence_age_days: `2.5`
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

## 2. 미국 증시 지수 흐름: 나스닥, 금리, 빅테크 실적을 같이 봐야 하는 이유

- keyword: `us_index_flow`
- freshness_status: `unknown`
- newest_evidence_age_days: `None`
- newest_evidence_iso: ``
- quality_status: `review_before_publish` / ready_now `False`
- summary: 대표 근거 시각을 읽지 못해 판단이 보류되었습니다.
- recommendation: 최근 근거 시각을 다시 수집해 신선도를 먼저 확인하세요.
- recovery_mode: `manual_check`
- recovery_summary: 최근 근거 시각을 먼저 다시 확인한 뒤 다음 액션을 결정하세요.

## 3. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword: `bitcoin`
- freshness_status: `fresh`
- newest_evidence_age_days: `0.1`
- newest_evidence_iso: `2026-10-10T03:59:57+00:00`
- quality_status: `pass` / ready_now `True`
- summary: 최신 근거가 살아 있어 데일리 해설로 다루기 좋은 상태입니다. 대표 근거: Bitcoin trades above $82,000 as rising oil prices, Fed outlook weigh
- recommendation: 사용자 검토만 통과하면 바로 게시 후보로 유지해도 됩니다.
- recovery_mode: `publish_direct`
- recovery_summary: 현재 신선도가 살아 있어 데일리 해설형으로 바로 검토를 이어가도 됩니다.
- evidence: Investing.com Crypto News / 2026-10-10 03:59:57 / Bitcoin trades above $82,000 as rising oil prices, Fed outlook weigh
- evidence: Investing.com Crypto News / 2026-10-09 20:46:24 / Bitcoin holds ground above $82k, heads for weekly losses amid yield pressure
- evidence: Investing.com Crypto News / 2026-10-09 19:18:52 / Bitcoin clings to $81,121 macro support on 5h chart: Live levels
