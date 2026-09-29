# User Approval Inbox

사용자가 글을 읽고 승인 여부만 빠르게 답할 수 있게 만든 확인 전용 인박스입니다.
- 안전 원칙: 제가 먼저 이 화면으로 초안을 보여드리고, 사용자 최종 확인 전에는 실제 업로드가 계속 차단됩니다.
- current review focus: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/current-review-focus.html`
- shortlist launchpad: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/shortlist-launchpad.html`
- approval briefing board: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/approval-briefing-board.html`

## 어떻게 답하면 되는가

- `treasury_yields` 글 먼저 진행
- `bitcoin` 먼저 검토, 이미지 보완 후 업로드 준비
- `FOMC 메인 말고 SEO 후속 글로 전환`
- 둘 다 보류, 제목 톤만 조금 더 부드럽게 수정

## 답변을 승인 파일로 바꾸는 헬퍼

- `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/apply_user_approval_reply.py --reply "treasury_yields 글 먼저 진행"`
- `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/apply_user_approval_reply.py --reply "bitcoin 먼저 검토, 이미지 보완 후 업로드 준비"`
- `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/apply_user_approval_reply.py --reply "treasury_yields 글 먼저 진행" --apply`

## 답변에서 다음 실행 흐름까지 이어보기

- `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/run_user_approval_reply_flow.py --reply "treasury_yields 글 먼저 진행"`
- `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/run_user_approval_reply_flow.py --reply "treasury_yields 글 먼저 진행" --apply`

## 업로드 없이 안전하게 리허설하기

- `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/rehearse_user_approval_reply.py --reply "treasury_yields 글 먼저 진행"`
- `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/rehearse_user_approval_reply.py --reply "FOMC 메인 말고 SEO 후속 글로 전환"`

## 1. 미국채 금리 상승이 나스닥과 코인에 부담이 되는 이유

- keyword: `treasury_yields`
- ready_now: `False`
- quality_status: `review_before_publish`
- decision_note: 이 글은 내용 확인 후 대표 이미지 보완이 먼저 필요합니다.
- freshness_status: `fresh`
- freshness_recommendation: 신선도는 괜찮습니다. 이미지나 품질 게이트만 보완하면 됩니다.
- next_action: 사용자 최종 확인 후 업로드
- reader_intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- CTA focus: 환율·금리·미국증시 evergreen 글로 연결
- excerpt: 한 줄 요약: `공식 발표 날짜와 핵심 문구`, `달러·금리·주식·코인 중 먼저 반응한 자산`, `거래량과 자금 흐름` 세 지표를 같이 봐야 이 이슈가 단기 뉴스인지 실제 흐름인지 구분할 수 있습니다.
- excerpt: - 미국채 금리 상승이 나스닥과 코인에 부담이 되는 이유은 제목만 보면 단순 뉴스처럼 보이지만, 실제로는 자금 흐름과 투자심리를 같이 건드릴 수 있는 이슈입니다.
- excerpt: - 핵심은 발표 자체보다 시장이 그 발표를 어떤 방향으로 해석했는지입니다.
- preview: 한 줄 요약: `공식 발표 날짜와 핵심 문구`, `달러·금리·주식·코인 중 먼저 반응한 자산`, `거래량과 자금 흐름` 세 지표를 같이 봐야 이 이슈가 단기 뉴스인지 실제 흐름인지 구분할 수 있습니다.
- preview: - 미국채 금리 상승이 나스닥과 코인에 부담이 되는 이유은 제목만 보면 단순 뉴스처럼 보이지만, 실제로는 자금 흐름과 투자심리를 같이 건드릴 수 있는 이슈입니다. - 핵심은 발표 자체보다 시장이 그 발표를 어떤 방향으로 해석했는지입니다. - 개인 투자자는 가격 반응, 관련 자산 확산, 다음 공식 일정을 함께 확인하는 편이 좋습니다.
- evidence: CNBC Top News / 2026-09-29T17:55:39+00:00 / Trump Accounts will auto-enroll children, potentially adding 60 million accounts: Treasury
- evidence: Financial Times Home / 2026-09-29T17:25:41+00:00 / US 30-year Treasury yield hits highest since 2002
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords treasury_yields`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords treasury_yields`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword treasury_yields`
- hero_image_apply_helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword treasury_yields --slot hero --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- draft_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/drafts/01-treasury-yields.md`
- html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/publish-ready/01-미국채-금리-상승이-나스닥과-코인에-부담이-되는-이유.html`

## 2. AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword: `ai_semiconductors`
- ready_now: `True`
- quality_status: `pass`
- decision_note: 이 글은 내용만 괜찮으면 바로 승인 후보입니다.
- freshness_status: `fresh`
- freshness_recommendation: 사용자 검토만 통과하면 바로 게시 후보로 유지해도 됩니다.
- next_action: 사용자 최종 확인 후 Blogger draft 업로드
- reader_intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- CTA focus: 실적·공급망·대표 종목 글로 연결
- final retention CTA: 이 글과 함께 아래 읽을거리까지 보면 `실적·공급망·대표 종목 글로 연결` 흐름이 훨씬 더 잘 이어집니다.
- later revisit CTA: 핵심 흐름을 짧게 계속 받고 싶다면 텔레그램형 재방문 동선과 연결합니다.
- excerpt: 한 줄 요약: `나스닥과 S&P500 상대 강도`, `미국채 10년물 금리`, `엔비디아·마이크로소프트 등 빅테크 실적 가이던스` 세 지표를 같이 봐야 이 이슈가 단기 뉴스인지 실제 흐름인지 구분할 수 있습니다.
- excerpt: - 미국 증시 흐름은 지수 등락률만 보면 부족합니다. 금리와 달러, 빅테크 실적 기대가 같이 움직입니다.
- excerpt: - 나스닥이 강해도 시장 폭이 좁으면 일부 대형주 쏠림일 수 있고, 반대로 섹터 확산이 나오면 추세가 더 단단해질 수 있습니다.
- preview: 한 줄 요약: `나스닥과 S&P500 상대 강도`, `미국채 10년물 금리`, `엔비디아·마이크로소프트 등 빅테크 실적 가이던스` 세 지표를 같이 봐야 이 이슈가 단기 뉴스인지 실제 흐름인지 구분할 수 있습니다.
- preview: - 미국 증시 흐름은 지수 등락률만 보면 부족합니다. 금리와 달러, 빅테크 실적 기대가 같이 움직입니다. - 나스닥이 강해도 시장 폭이 좁으면 일부 대형주 쏠림일 수 있고, 반대로 섹터 확산이 나오면 추세가 더 단단해질 수 있습니다. - 개인 투자자는 지수보다 금리, 반도체·AI 대표주, 실적 가이던스, 거래대금 확산을 함께 보는 편이 좋습니다.
- evidence: NYT Business / 2026-09-29T11:58:36+00:00 / What’s In Anthropic’s I.P.O. Filing
- evidence: Financial Times Home / 2026-09-29T04:04:31+00:00 / Nvidia turns to insurers to spread the risk of AI build-out
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords ai_semiconductors`
- recovery_mode: `publish_direct`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword ai_semiconductors`
- hero_image_apply_helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword ai_semiconductors --slot hero --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- draft_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/drafts/03-ai-semiconductors.md`
- html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/publish-ready/03-ai-반도체-주가를-볼-때-실적보다-먼저-확인할-3가지.html`
