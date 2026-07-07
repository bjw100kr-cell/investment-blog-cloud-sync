# User Approval Inbox

사용자가 글을 읽고 승인 여부만 빠르게 답할 수 있게 만든 확인 전용 인박스입니다.
- 안전 원칙: 제가 먼저 이 화면으로 초안을 보여드리고, 사용자 최종 확인 전에는 실제 업로드가 계속 차단됩니다.
- current review focus: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/current-review-focus.html`
- shortlist launchpad: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/shortlist-launchpad.html`
- approval briefing board: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/approval-briefing-board.html`

## 어떻게 답하면 되는가

- `bitcoin` 글 먼저 진행
- `bitcoin` 먼저 검토, 이미지 보완 후 업로드 준비
- `FOMC 메인 말고 SEO 후속 글로 전환`
- 둘 다 보류, 제목 톤만 조금 더 부드럽게 수정

## 답변을 승인 파일로 바꾸는 헬퍼

- `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/apply_user_approval_reply.py --reply "bitcoin 글 먼저 진행"`
- `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/apply_user_approval_reply.py --reply "bitcoin 먼저 검토, 이미지 보완 후 업로드 준비"`
- `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/apply_user_approval_reply.py --reply "bitcoin 글 먼저 진행" --apply`

## 답변에서 다음 실행 흐름까지 이어보기

- `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/run_user_approval_reply_flow.py --reply "bitcoin 글 먼저 진행"`
- `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/run_user_approval_reply_flow.py --reply "bitcoin 글 먼저 진행" --apply`

## 업로드 없이 안전하게 리허설하기

- `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/rehearse_user_approval_reply.py --reply "bitcoin 글 먼저 진행"`
- `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/rehearse_user_approval_reply.py --reply "FOMC 메인 말고 SEO 후속 글로 전환"`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

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
- evidence: CoinDesk RSS / 2026-07-07T10:44:09+00:00 / Bitcoin stalls as open interest decline raises questions about rally's staying power
- evidence: Cointelegraph / 2026-07-07T10:14:40+00:00 / Bitcoin can fall below $58K if one of its 'cleanest' metrics copies history: Analysis
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- recovery_mode: `publish_direct`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- hero_image_apply_helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword bitcoin --slot hero --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- draft_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/drafts/02-bitcoin.md`
- html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/publish-ready/02-비트코인-핵심-흐름-해설.html`

## 2. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword: `china`
- ready_now: `False`
- quality_status: `review_before_publish`
- decision_note: 이 글은 내용 확인 후 대표 이미지 보완이 먼저 필요합니다.
- freshness_status: `fresh`
- freshness_recommendation: 신선도는 괜찮습니다. 이미지나 품질 게이트만 보완하면 됩니다.
- next_action: 사용자 최종 확인 후 업로드
- reader_intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- CTA focus: 실적·공급망·대표 종목 글로 연결
- excerpt: 한 줄 요약: `달러/위안 환율`, `중국 부동산·소비 지표`, `구리와 유가` 세 지표를 같이 봐야 이 이슈가 단기 뉴스인지 실제 흐름인지 구분할 수 있습니다.
- excerpt: - 중국 변수는 중국 증시만의 문제가 아니라 원자재, 환율, 한국 수출주, 글로벌 위험심리로 번질 수 있습니다.
- excerpt: - 정책 부양 뉴스가 나와도 실제 소비와 부동산, 위안화 흐름이 따라오는지 확인해야 합니다.
- preview: 한 줄 요약: `달러/위안 환율`, `중국 부동산·소비 지표`, `구리와 유가` 세 지표를 같이 봐야 이 이슈가 단기 뉴스인지 실제 흐름인지 구분할 수 있습니다.
- preview: - 중국 변수는 중국 증시만의 문제가 아니라 원자재, 환율, 한국 수출주, 글로벌 위험심리로 번질 수 있습니다. - 정책 부양 뉴스가 나와도 실제 소비와 부동산, 위안화 흐름이 따라오는지 확인해야 합니다. - 개인 투자자는 중국 관련 ETF나 소재·산업재만 보지 말고 달러/위안, 구리·유가, 한국 수출주 반응을 같이 보는 편이 좋습니다.
- evidence: Reuters Markets via Google News RSS / 2026-07-07T01:10:00+00:00 / China breaks step with global markets, and investors buy in - Reuters
- evidence: Reuters Markets via Google News RSS / 2026-07-06T23:03:00+00:00 / China's booming gig economy masks job market pain, strains welfare system - Reuters
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- next_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords china`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword china`
- hero_image_apply_helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword china --slot hero --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- draft_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/drafts/04-china.md`
- html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/publish-ready/04-중국-변수와-시장-영향-해설.html`
