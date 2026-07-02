# Current Review Focus

지금 사용자에게 먼저 보여줄 글만 다시 줄인 검토 카드입니다.
- 발행 안전 원칙: 제가 먼저 이 화면으로 초안을 보여드리고, 사용자 최종 확인 전에는 실제 업로드가 계속 차단됩니다.
- 지금 1순위로 읽을 글: `FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지` / keyword `fomc`
- shortlist: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/user-review-shortlist.md`
- full draft review sheet: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/full-draft-review-sheet.md`
- approval briefing board: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/approval-briefing-board.html`
- shortlist launchpad: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/shortlist-launchpad.html`
- source freshness board: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/source-freshness-board.html`

## 1. FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지

- keyword: `fomc`
- ready_now: `True`
- quality_status: `pass`
- hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- CTA focus: 환율·금리·미국증시 evergreen 글로 연결
- final retention CTA: FOMC 흐름이 여기서 끝이 아닙니다. 아래 체크포인트 글과 초보자 가이드까지 같이 보면 다음 일정에서 뭘 봐야 할지 훨씬 선명해집니다.
- later revisit CTA: 거시 이벤트를 놓치지 않으려면 다음 체크포인트 글까지 같이 보고, 이후에는 텔레그램/구독 채널로 이어 받아보세요.
- demand_signal_score: `4600`
- freshness: `stale` / newest evidence age `15.0` days
- freshness_summary: 핵심 근거가 이미 오래돼 그대로 올리기에는 위험합니다. 마지막 대표 근거: Federal Reserve issues FOMC statement
- freshness_recommendation: 지금 상태로는 데일리 뉴스형 게시보다 refresh 후 재작성 또는 evergreen 해설형 전환이 더 안전합니다.
- sources: CoinDesk RSS, Cointelegraph, Federal Reserve Monetary Policy Press
- advisory_checks: canonical_url_present, newsletter_ready, ga4_ready
- next_action: 사용자 최종 확인 후 Blogger draft 업로드
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords fomc`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword fomc`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword fomc --apply`
- excerpt: 한 줄 요약: `달러 인덱스`, `미국채 2년물/10년물 금리`, `나스닥과 비트코인 동시 반응` 세 지표를 같이 봐야 이 이슈가 단기 뉴스인지 실제 흐름인지 구분할 수 있습니다.
- excerpt: - FOMC는 금리 결정 한 줄보다 달러, 미국채 금리, 위험자산 심리를 동시에 바꾸는 이벤트입니다.
- excerpt: - 시장은 발표 결과보다 성명서 문구, 점도표, 기자회견 톤이 다음 금리 경로를 어떻게 바꾸는지에 더 민감하게 반응합니다.
- excerpt: - 개인 투자자는 발표 직후 방향을 단정하기보다 달러 인덱스, 미국채 2년물/10년물, 나스닥과 비트코인 반응을 같이 확인하는 편이 안전합니다.
- preview: 한 줄 요약: `달러 인덱스`, `미국채 2년물/10년물 금리`, `나스닥과 비트코인 동시 반응` 세 지표를 같이 봐야 이 이슈가 단기 뉴스인지 실제 흐름인지 구분할 수 있습니다.
- preview: - FOMC는 금리 결정 한 줄보다 달러, 미국채 금리, 위험자산 심리를 동시에 바꾸는 이벤트입니다. - 시장은 발표 결과보다 성명서 문구, 점도표, 기자회견 톤이 다음 금리 경로를 어떻게 바꾸는지에 더 민감하게 반응합니다. - 개인 투자자는 발표 직후 방향을 단정하기보다 달러 인덱스, 미국채 2년물/10년물, 나스닥과 비트코인 반응을 같이 확인하는 편이 안전합니다.
- evidence: Federal Reserve Monetary Policy Press / 2026-06-17T18:00:00+00:00 / Federal Reserve issues FOMC statement
- evidence: Federal Reserve Monetary Policy Press / 2026-06-17T18:00:00+00:00 / Federal Reserve Board and Federal Open Market Committee release economic projections from the June 16-17 FOMC meeting
- evidence: Federal Reserve Monetary Policy Press / 2026-04-29T18:00:00+00:00 / Federal Reserve issues FOMC statement
- hero_image_search: `central bank meeting finance city skyline` / https://unsplash.com/s/photos/central+bank+meeting+finance+city+skyline
- hero_image_apply_helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword fomc --slot hero --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- draft_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/drafts/01-fomc.md`
- html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/publish-ready/01-fomc-이후-시장-해설.html`

## 2. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword: `bitcoin`
- ready_now: `True`
- quality_status: `pass`
- hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- CTA focus: ETF·규제·초보 가이드 글로 연결
- final retention CTA: 비트코인은 가격만 보면 놓치는 게 많습니다. 아래 ETF·규제 정리와 초보자 가이드까지 같이 보면 구조가 훨씬 빨리 잡힙니다.
- later revisit CTA: 코인 해설을 짧게 계속 받고 싶다면 텔레그램형 재방문 동선과 연결합니다.
- demand_signal_score: `5200`
- freshness: `fresh` / newest evidence age `0.0` days
- freshness_summary: 최신 근거가 살아 있어 데일리 해설로 다루기 좋은 상태입니다. 대표 근거: Bitcoin price taps new July high above $62K on weak US jobs data
- freshness_recommendation: 사용자 검토만 통과하면 바로 게시 후보로 유지해도 됩니다.
- sources: CoinDesk RSS, Cointelegraph, Investing.com Crypto News
- advisory_checks: canonical_url_present, newsletter_ready, ga4_ready
- next_action: 사용자 최종 확인 후 Blogger draft 업로드
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply`
- excerpt: 한 줄 요약: `현물 ETF 순유입/순유출`, `달러 인덱스와 미국채 금리`, `이더리움과 알트코인 확산 여부` 세 지표를 같이 봐야 이 이슈가 단기 뉴스인지 실제 흐름인지 구분할 수 있습니다.
- excerpt: - 비트코인 흐름은 가격 캔들만 보면 늦습니다. ETF 자금과 달러 흐름, 규제 뉴스가 먼저 분위기를 바꾸는 경우가 많습니다.
- excerpt: - 강한 상승처럼 보여도 실제 자금 유입이 약하거나 달러가 강하면 흐름이 쉽게 끊길 수 있습니다.
- excerpt: - 개인 투자자는 비트코인 단독 상승인지, 이더리움·알트코인·나스닥까지 같이 움직이는지를 함께 확인해야 합니다.
- preview: 한 줄 요약: `현물 ETF 순유입/순유출`, `달러 인덱스와 미국채 금리`, `이더리움과 알트코인 확산 여부` 세 지표를 같이 봐야 이 이슈가 단기 뉴스인지 실제 흐름인지 구분할 수 있습니다.
- preview: - 비트코인 흐름은 가격 캔들만 보면 늦습니다. ETF 자금과 달러 흐름, 규제 뉴스가 먼저 분위기를 바꾸는 경우가 많습니다. - 강한 상승처럼 보여도 실제 자금 유입이 약하거나 달러가 강하면 흐름이 쉽게 끊길 수 있습니다. - 개인 투자자는 비트코인 단독 상승인지, 이더리움·알트코인·나스닥까지 같이 움직이는지를 함께 확인해야 합니다.
- evidence: Cointelegraph / 2026-07-02T17:41:26+00:00 / Bitcoin price taps new July high above $62K on weak US jobs data
- evidence: CoinDesk RSS / 2026-07-02T14:44:55+00:00 / SBI Crypto to shut down mining pool that holds roughly 2% of Bitcoin's hashrate
- evidence: CoinDesk RSS / 2026-07-02T13:11:22+00:00 / JPMorgan says Strategy's bitcoin sales policy adds 'two-way risk' to crypto markets
- hero_image_search: `bitcoin blockchain abstract blue finance` / https://www.pexels.com/search/bitcoin+blockchain+abstract+blue+finance/
- hero_image_apply_helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword bitcoin --slot hero --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- draft_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/drafts/02-bitcoin.md`
- html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/publish-ready/02-비트코인-핵심-흐름-해설.html`
