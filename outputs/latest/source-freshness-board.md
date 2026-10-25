# Source Freshness Board

사용자에게 초안을 보여주기 전에, 근거 소스가 지금 시점에도 충분히 신선한지 확인하는 보드입니다.
- generated_at: `2026-10-25T04:09:54.831426+00:00`
- snapshot_generated_at: `2026-10-25T04:09:50.443475+00:00`
- snapshot_age_days: `0.0`
- snapshot_status: `fresh`
- counts: fresh `2` / aging `1` / stale `0` / unknown `0`

## 1. 미국 증시 지수 흐름: 나스닥, 금리, 빅테크 실적을 같이 봐야 하는 이유

- keyword: `us_index_flow`
- freshness_status: `aging`
- newest_evidence_age_days: `2.5`
- newest_evidence_iso: `2026-10-22T16:02:09+00:00`
- quality_status: `pass` / ready_now `True`
- summary: 아직 쓸 수는 있지만 뉴스 속도는 조금 늦었습니다. 대표 근거: Nasdaq CEO flags 'modest softening' in IPO market as macro uncertainty hits debuts - Reuters
- recommendation: 초안은 유지하되 발행 직전에 가격, 수치, headline을 한 번 더 갱신하는 편이 안전합니다.
- recovery_mode: `refresh_before_publish`
- recovery_summary: 발행 직전 전체 파이프라인을 다시 돌려 headline과 숫자를 최신 상태로 갱신하는 편이 안전합니다.
- recovery_command: `bash scripts/run_pipeline.sh`
- evidence: Reuters Markets via Google News RSS / 2026-10-22T16:02:09+00:00 / Nasdaq CEO flags 'modest softening' in IPO market as macro uncertainty hits debuts - Reuters

## 2. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword: `bitcoin`
- freshness_status: `fresh`
- newest_evidence_age_days: `0.5`
- newest_evidence_iso: `2026-10-24T16:00:00+00:00`
- quality_status: `pass` / ready_now `True`
- summary: 최신 근거가 살아 있어 데일리 해설로 다루기 좋은 상태입니다. 대표 근거: Strategy, Strive face balancing act between bitcoin buying and preferred stock dividends
- recommendation: 사용자 검토만 통과하면 바로 게시 후보로 유지해도 됩니다.
- recovery_mode: `publish_direct`
- recovery_summary: 현재 신선도가 살아 있어 데일리 해설형으로 바로 검토를 이어가도 됩니다.
- evidence: CoinDesk RSS / 2026-10-24T16:00:00+00:00 / Strategy, Strive face balancing act between bitcoin buying and preferred stock dividends
- evidence: CoinDesk RSS / 2026-10-24T15:11:24+00:00 / Crypto under weekend pressure, bitcoin slides below $80,000 on U.S. Middle East evacuations
- evidence: CoinDesk RSS / 2026-10-24T14:00:00+00:00 / Bitcoin’s wealthy holders turning to loans and yield as investment habits mature: Xapo CEO

## 3. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword: `china`
- freshness_status: `fresh`
- newest_evidence_age_days: `0.5`
- newest_evidence_iso: `2026-10-24T15:44:19+00:00`
- quality_status: `pass` / ready_now `True`
- summary: 최신 근거가 살아 있어 데일리 해설로 다루기 좋은 상태입니다. 대표 근거: North Korea’s Kim crosses new China border bridge to reaffirm ties
- recommendation: 사용자 검토만 통과하면 바로 게시 후보로 유지해도 됩니다.
- recovery_mode: `publish_direct`
- recovery_summary: 현재 신선도가 살아 있어 데일리 해설형으로 바로 검토를 이어가도 됩니다.
- evidence: Financial Times World / 2026-10-24T15:44:19+00:00 / North Korea’s Kim crosses new China border bridge to reaffirm ties
- evidence: Cointelegraph / 2026-10-23T13:21:07+00:00 / China targets 2030 for its national blockchain network buildout
- evidence: Reuters Markets via Google News RSS / 2026-10-23T10:02:25+00:00 / GLP-1 boom in China, India, Brazil could create $22 bln market by 2035, J.P. Morgan says - Reuters
