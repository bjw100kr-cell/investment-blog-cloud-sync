# Source Freshness Board

사용자에게 초안을 보여주기 전에, 근거 소스가 지금 시점에도 충분히 신선한지 확인하는 보드입니다.
- generated_at: `2026-06-30T21:54:06.672611+00:00`
- snapshot_generated_at: `2026-06-30T21:54:01.988871+00:00`
- snapshot_age_days: `0.0`
- snapshot_status: `fresh`
- counts: fresh `2` / aging `0` / stale `1` / unknown `0`

## 1. FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지

- keyword: `fomc`
- freshness_status: `stale`
- newest_evidence_age_days: `13.2`
- newest_evidence_iso: `2026-06-17T18:00:00+00:00`
- quality_status: `pass` / ready_now `True`
- summary: 핵심 근거가 이미 오래돼 그대로 올리기에는 위험합니다. 마지막 대표 근거: Federal Reserve issues FOMC statement
- recommendation: 지금 상태로는 데일리 뉴스형 게시보다 refresh 후 재작성 또는 evergreen 해설형 전환이 더 안전합니다.
- recovery_mode: `evergreen_salvage`
- recovery_summary: 뉴스형 본문 대신 evergreen 후속 글로 전환하는 편이 더 안전하고 검색형 수익화에도 유리합니다.
- recovery_title: FOMC 이후 시장이 주식과 코인에 미치는 영향
- recovery_confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords seo_fomc_1`
- recovery_image_search: `central bank meeting finance city skyline` / https://unsplash.com/s/photos/central+bank+meeting+finance+city+skyline
- recovery_image_apply_helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword seo_fomc_1 --slot hero --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- evidence: Federal Reserve Monetary Policy Press / 2026-06-17T18:00:00+00:00 / Federal Reserve issues FOMC statement
- evidence: Federal Reserve Monetary Policy Press / 2026-06-17T18:00:00+00:00 / Federal Reserve Board and Federal Open Market Committee release economic projections from the June 16-17 FOMC meeting
- evidence: Federal Reserve Monetary Policy Press / 2026-04-29T18:00:00+00:00 / Federal Reserve issues FOMC statement

## 2. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword: `bitcoin`
- freshness_status: `fresh`
- newest_evidence_age_days: `0.1`
- newest_evidence_iso: `2026-06-30T19:07:57+00:00`
- quality_status: `pass` / ready_now `True`
- summary: 최신 근거가 살아 있어 데일리 해설로 다루기 좋은 상태입니다. 대표 근거: Bitcoin price risks drop below $58K as US dollar hits 40-year high against yen
- recommendation: 사용자 검토만 통과하면 바로 게시 후보로 유지해도 됩니다.
- recovery_mode: `publish_direct`
- recovery_summary: 현재 신선도가 살아 있어 데일리 해설형으로 바로 검토를 이어가도 됩니다.
- evidence: Cointelegraph / 2026-06-30T18:17:56+00:00 / Bitcoin price risks drop below $58K as US dollar hits 40-year high against yen
- evidence: Cointelegraph / 2026-06-30T17:44:31+00:00 / AI’s power crunch turns Bitcoin miners’ grid access into an asset
- evidence: Investing.com Crypto News / 2026-06-30 19:07:57 / Bitcoin holds $58,131 support after 2.9% drop: Live levels

## 3. 미국 증시 지수 흐름 해설: 나스닥, 금리, 빅테크 실적을 같이 봐야 하는 이유

- keyword: `us_index_flow`
- freshness_status: `fresh`
- newest_evidence_age_days: `0.0`
- newest_evidence_iso: `2026-06-30T21:13:00+00:00`
- quality_status: `pass` / ready_now `True`
- summary: 최신 근거가 살아 있어 데일리 해설로 다루기 좋은 상태입니다. 대표 근거: The 20 best-performing stocks in the S&P 500 for the first half of 2026
- recommendation: 사용자 검토만 통과하면 바로 게시 후보로 유지해도 됩니다.
- recovery_mode: `publish_direct`
- recovery_summary: 현재 신선도가 살아 있어 데일리 해설형으로 바로 검토를 이어가도 됩니다.
- evidence: MarketWatch Breaking News / 2026-06-30T21:13:00+00:00 / The 20 best-performing stocks in the S&P 500 for the first half of 2026
- evidence: MarketWatch Breaking News / 2026-06-30T21:04:00+00:00 / 20 stocks in the S&P 500 that plunged the most in 2026’s first half
- evidence: Reuters Markets via Google News RSS / 2026-06-30T20:55:04+00:00 / S&P 500, Nasdaq register best quarter since 2020 despite Iran war - Reuters
