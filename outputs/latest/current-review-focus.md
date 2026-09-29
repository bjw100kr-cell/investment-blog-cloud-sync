# Current Review Focus

지금 사용자에게 먼저 보여줄 글만 다시 줄인 검토 카드입니다.
- 발행 안전 원칙: 제가 먼저 이 화면으로 초안을 보여드리고, 사용자 최종 확인 전에는 실제 업로드가 계속 차단됩니다.
- 지금 1순위로 읽을 글: `미국채 금리 상승이 나스닥과 코인에 부담이 되는 이유` / keyword `treasury_yields`
- shortlist: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/user-review-shortlist.md`
- full draft review sheet: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/full-draft-review-sheet.md`
- approval briefing board: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/approval-briefing-board.html`
- shortlist launchpad: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/shortlist-launchpad.html`
- source freshness board: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/source-freshness-board.html`

## 1. 미국채 금리 상승이 나스닥과 코인에 부담이 되는 이유

- keyword: `treasury_yields`
- ready_now: `False`
- quality_status: `review_before_publish`
- hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- CTA focus: 환율·금리·미국증시 evergreen 글로 연결
- demand_signal_score: `3600`
- freshness: `fresh` / newest evidence age `0.0` days
- freshness_summary: 최신 근거가 살아 있어 데일리 해설로 다루기 좋은 상태입니다. 대표 근거: Trump Accounts will auto-enroll children, potentially adding 60 million accounts: Treasury
- freshness_recommendation: 신선도는 괜찮습니다. 이미지나 품질 게이트만 보완하면 됩니다.
- sources: CNBC Top News, CoinDesk RSS, Cointelegraph
- advisory_checks: follow_up_posts_present, canonical_url_present, newsletter_ready, ga4_ready
- next_action: 사용자 최종 확인 후 업로드
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords treasury_yields`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword treasury_yields`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword treasury_yields --apply`
- excerpt: 한 줄 요약: `공식 발표 날짜와 핵심 문구`, `달러·금리·주식·코인 중 먼저 반응한 자산`, `거래량과 자금 흐름` 세 지표를 같이 봐야 이 이슈가 단기 뉴스인지 실제 흐름인지 구분할 수 있습니다.
- excerpt: - 미국채 금리 상승이 나스닥과 코인에 부담이 되는 이유은 제목만 보면 단순 뉴스처럼 보이지만, 실제로는 자금 흐름과 투자심리를 같이 건드릴 수 있는 이슈입니다.
- excerpt: - 핵심은 발표 자체보다 시장이 그 발표를 어떤 방향으로 해석했는지입니다.
- excerpt: - 개인 투자자는 가격 반응, 관련 자산 확산, 다음 공식 일정을 함께 확인하는 편이 좋습니다.
- preview: 한 줄 요약: `공식 발표 날짜와 핵심 문구`, `달러·금리·주식·코인 중 먼저 반응한 자산`, `거래량과 자금 흐름` 세 지표를 같이 봐야 이 이슈가 단기 뉴스인지 실제 흐름인지 구분할 수 있습니다.
- preview: - 미국채 금리 상승이 나스닥과 코인에 부담이 되는 이유은 제목만 보면 단순 뉴스처럼 보이지만, 실제로는 자금 흐름과 투자심리를 같이 건드릴 수 있는 이슈입니다. - 핵심은 발표 자체보다 시장이 그 발표를 어떤 방향으로 해석했는지입니다. - 개인 투자자는 가격 반응, 관련 자산 확산, 다음 공식 일정을 함께 확인하는 편이 좋습니다.
- evidence: CNBC Top News / 2026-09-29T17:55:39+00:00 / Trump Accounts will auto-enroll children, potentially adding 60 million accounts: Treasury
- evidence: Financial Times Home / 2026-09-29T17:25:41+00:00 / US 30-year Treasury yield hits highest since 2002
- evidence: MarketWatch Breaking News / 2026-09-29T16:44:00+00:00 / The hidden messages the bond market is sending about the AI boom and the stock market
- hero_image_search: `central bank finance city skyline market data` / https://unsplash.com/s/photos/central+bank+finance+city+skyline+market+data
- hero_image_apply_helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword treasury_yields --slot hero --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- draft_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/drafts/01-treasury-yields.md`
- html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/publish-ready/01-미국채-금리-상승이-나스닥과-코인에-부담이-되는-이유.html`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword: `ai_semiconductors`
- ready_now: `True`
- quality_status: `pass`
- hero_image_selected: `True`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- CTA focus: 실적·공급망·대표 종목 글로 연결
- final retention CTA: 이 글과 함께 아래 읽을거리까지 보면 `실적·공급망·대표 종목 글로 연결` 흐름이 훨씬 더 잘 이어집니다.
- later revisit CTA: 핵심 흐름을 짧게 계속 받고 싶다면 텔레그램형 재방문 동선과 연결합니다.
- demand_signal_score: `0`
- freshness: `fresh` / newest evidence age `0.3` days
- freshness_summary: 최신 근거가 살아 있어 데일리 해설로 다루기 좋은 상태입니다. 대표 근거: What’s In Anthropic’s I.P.O. Filing
- freshness_recommendation: 사용자 검토만 통과하면 바로 게시 후보로 유지해도 됩니다.
- sources: Financial Times Home, NYT Business
- advisory_checks: canonical_url_present, newsletter_ready, ga4_ready
- next_action: 사용자 최종 확인 후 Blogger draft 업로드
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- helper_apply_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors --apply`
- excerpt: 한 줄 요약: `나스닥과 S&P500 상대 강도`, `미국채 10년물 금리`, `엔비디아·마이크로소프트 등 빅테크 실적 가이던스` 세 지표를 같이 봐야 이 이슈가 단기 뉴스인지 실제 흐름인지 구분할 수 있습니다.
- excerpt: - 미국 증시 흐름은 지수 등락률만 보면 부족합니다. 금리와 달러, 빅테크 실적 기대가 같이 움직입니다.
- excerpt: - 나스닥이 강해도 시장 폭이 좁으면 일부 대형주 쏠림일 수 있고, 반대로 섹터 확산이 나오면 추세가 더 단단해질 수 있습니다.
- excerpt: - 개인 투자자는 지수보다 금리, 반도체·AI 대표주, 실적 가이던스, 거래대금 확산을 함께 보는 편이 좋습니다.
- preview: 한 줄 요약: `나스닥과 S&P500 상대 강도`, `미국채 10년물 금리`, `엔비디아·마이크로소프트 등 빅테크 실적 가이던스` 세 지표를 같이 봐야 이 이슈가 단기 뉴스인지 실제 흐름인지 구분할 수 있습니다.
- preview: - 미국 증시 흐름은 지수 등락률만 보면 부족합니다. 금리와 달러, 빅테크 실적 기대가 같이 움직입니다. - 나스닥이 강해도 시장 폭이 좁으면 일부 대형주 쏠림일 수 있고, 반대로 섹터 확산이 나오면 추세가 더 단단해질 수 있습니다. - 개인 투자자는 지수보다 금리, 반도체·AI 대표주, 실적 가이던스, 거래대금 확산을 함께 보는 편이 좋습니다.
- evidence: NYT Business / 2026-09-29T11:58:36+00:00 / What’s In Anthropic’s I.P.O. Filing
- evidence: Financial Times Home / 2026-09-29T04:04:31+00:00 / Nvidia turns to insurers to spread the risk of AI build-out
- evidence: Financial Times Home / 2026-09-29T02:28:18+00:00 / Anthropic warns of ‘existential risks to humanity’ in IPO prospectus
- hero_image_search: `semiconductor chip blue abstract` / https://unsplash.com/s/photos/semiconductor+chip+blue+abstract
- hero_image_apply_helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword ai_semiconductors --slot hero --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- draft_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/drafts/03-ai-semiconductors.md`
- html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/publish-ready/03-ai-반도체-주가를-볼-때-실적보다-먼저-확인할-3가지.html`
