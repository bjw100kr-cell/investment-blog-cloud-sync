# User Approval Inbox

사용자가 글을 읽고 승인 여부만 빠르게 답할 수 있게 만든 확인 전용 인박스입니다.
- 안전 원칙: 제가 먼저 이 화면으로 초안을 보여드리고, 사용자 최종 확인 전에는 실제 업로드가 계속 차단됩니다.
- current review focus: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/current-review-focus.html`
- shortlist launchpad: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/shortlist-launchpad.html`
- approval briefing board: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/approval-briefing-board.html`

## 어떻게 답하면 되는가

- `fomc` 글 먼저 진행
- `bitcoin` 먼저 검토, 이미지 보완 후 업로드 준비
- `FOMC 메인 말고 SEO 후속 글로 전환`
- 둘 다 보류, 제목 톤만 조금 더 부드럽게 수정

## 답변을 승인 파일로 바꾸는 헬퍼

- `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/apply_user_approval_reply.py --reply "fomc 글 먼저 진행"`
- `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/apply_user_approval_reply.py --reply "bitcoin 먼저 검토, 이미지 보완 후 업로드 준비"`
- `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/apply_user_approval_reply.py --reply "fomc 글 먼저 진행" --apply`

## 답변에서 다음 실행 흐름까지 이어보기

- `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/run_user_approval_reply_flow.py --reply "fomc 글 먼저 진행"`
- `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/run_user_approval_reply_flow.py --reply "fomc 글 먼저 진행" --apply`

## 업로드 없이 안전하게 리허설하기

- `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/rehearse_user_approval_reply.py --reply "fomc 글 먼저 진행"`
- `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/rehearse_user_approval_reply.py --reply "FOMC 메인 말고 SEO 후속 글로 전환"`

## 1. FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지

- keyword: `fomc`
- ready_now: `True`
- quality_status: `pass`
- decision_note: 이 글은 내용만 괜찮으면 바로 승인 후보입니다.
- freshness_status: `stale`
- freshness_recommendation: 지금 상태로는 데일리 뉴스형 게시보다 refresh 후 재작성 또는 evergreen 해설형 전환이 더 안전합니다.
- next_action: 사용자 최종 확인 후 Blogger draft 업로드
- reader_intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- CTA focus: 환율·금리·미국증시 evergreen 글로 연결
- final retention CTA: FOMC 흐름이 여기서 끝이 아닙니다. 아래 체크포인트 글과 초보자 가이드까지 같이 보면 다음 일정에서 뭘 봐야 할지 훨씬 선명해집니다.
- later revisit CTA: 거시 이벤트를 놓치지 않으려면 다음 체크포인트 글까지 같이 보고, 이후에는 텔레그램/구독 채널로 이어 받아보세요.
- excerpt: 한 줄 요약: `달러 인덱스`, `미국채 2년물/10년물 금리`, `나스닥과 비트코인 동시 반응` 세 지표를 같이 봐야 이 이슈가 단기 뉴스인지 실제 흐름인지 구분할 수 있습니다.
- excerpt: - FOMC는 금리 결정 한 줄보다 달러, 미국채 금리, 위험자산 심리를 동시에 바꾸는 이벤트입니다.
- excerpt: - 시장은 발표 결과보다 성명서 문구, 점도표, 기자회견 톤이 다음 금리 경로를 어떻게 바꾸는지에 더 민감하게 반응합니다.
- preview: 한 줄 요약: `달러 인덱스`, `미국채 2년물/10년물 금리`, `나스닥과 비트코인 동시 반응` 세 지표를 같이 봐야 이 이슈가 단기 뉴스인지 실제 흐름인지 구분할 수 있습니다.
- preview: - FOMC는 금리 결정 한 줄보다 달러, 미국채 금리, 위험자산 심리를 동시에 바꾸는 이벤트입니다. - 시장은 발표 결과보다 성명서 문구, 점도표, 기자회견 톤이 다음 금리 경로를 어떻게 바꾸는지에 더 민감하게 반응합니다. - 개인 투자자는 발표 직후 방향을 단정하기보다 달러 인덱스, 미국채 2년물/10년물, 나스닥과 비트코인 반응을 같이 확인하는 편이 안전합니다.
- evidence: Federal Reserve Monetary Policy Press / 2026-06-17T18:00:00+00:00 / Federal Reserve issues FOMC statement
- evidence: Federal Reserve Monetary Policy Press / 2026-06-17T18:00:00+00:00 / Federal Reserve Board and Federal Open Market Committee release economic projections from the June 16-17 FOMC meeting
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords fomc`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords fomc`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword fomc`
- hero_image_apply_helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword fomc --slot hero --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- draft_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/drafts/01-fomc.md`
- html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/publish-ready/01-fomc-이후-시장-해설.html`

## 2. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword: `bitcoin`
- ready_now: `True`
- quality_status: `pass`
- decision_note: 이 글은 내용만 괜찮으면 바로 승인 후보입니다.
- freshness_status: `fresh`
- freshness_recommendation: 사용자 검토만 통과하면 바로 게시 후보로 유지해도 됩니다.
- next_action: 사용자 최종 확인 후 Blogger draft 업로드
- reader_intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- CTA focus: ETF·규제·초보 가이드 글로 연결
- final retention CTA: 비트코인은 가격만 보면 놓치는 게 많습니다. 아래 ETF·규제 정리와 초보자 가이드까지 같이 보면 구조가 훨씬 빨리 잡힙니다.
- later revisit CTA: 코인 해설을 짧게 계속 받고 싶다면 텔레그램형 재방문 동선과 연결합니다.
- excerpt: 한 줄 요약: `현물 ETF 순유입/순유출`, `달러 인덱스와 미국채 금리`, `이더리움과 알트코인 확산 여부` 세 지표를 같이 봐야 이 이슈가 단기 뉴스인지 실제 흐름인지 구분할 수 있습니다.
- excerpt: - 비트코인 흐름은 가격 캔들만 보면 늦습니다. ETF 자금과 달러 흐름, 규제 뉴스가 먼저 분위기를 바꾸는 경우가 많습니다.
- excerpt: - 강한 상승처럼 보여도 실제 자금 유입이 약하거나 달러가 강하면 흐름이 쉽게 끊길 수 있습니다.
- preview: 한 줄 요약: `현물 ETF 순유입/순유출`, `달러 인덱스와 미국채 금리`, `이더리움과 알트코인 확산 여부` 세 지표를 같이 봐야 이 이슈가 단기 뉴스인지 실제 흐름인지 구분할 수 있습니다.
- preview: - 비트코인 흐름은 가격 캔들만 보면 늦습니다. ETF 자금과 달러 흐름, 규제 뉴스가 먼저 분위기를 바꾸는 경우가 많습니다. - 강한 상승처럼 보여도 실제 자금 유입이 약하거나 달러가 강하면 흐름이 쉽게 끊길 수 있습니다. - 개인 투자자는 비트코인 단독 상승인지, 이더리움·알트코인·나스닥까지 같이 움직이는지를 함께 확인해야 합니다.
- evidence: Cointelegraph / 2026-07-01T18:59:27+00:00 / Bitcoin bear market ‘dead’ after first TD9 reversal signal since July 2022 fires
- evidence: CNBC Top News / 2026-07-01T17:10:22+00:00 / Bitcoin's summer swoon creates unique trade in Strategy
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- recovery_mode: `publish_direct`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- hero_image_apply_helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword bitcoin --slot hero --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- draft_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/drafts/02-bitcoin.md`
- html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/publish-ready/02-비트코인-핵심-흐름-해설.html`
