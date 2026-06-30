# User Approval Inbox

사용자가 글을 읽고 승인 여부만 빠르게 답할 수 있게 만든 확인 전용 인박스입니다.
- 안전 원칙: 제가 먼저 이 화면으로 초안을 보여드리고, 사용자 최종 확인 전에는 실제 업로드가 계속 차단됩니다.
- current review focus: `/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/current-review-focus.html`
- shortlist launchpad: `/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/shortlist-launchpad.html`
- approval briefing board: `/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/approval-briefing-board.html`

## 어떻게 답하면 되는가

- `bitcoin` 글 먼저 진행
- `bitcoin` 먼저 검토, 이미지 보완 후 업로드 준비
- `FOMC 메인 말고 SEO 후속 글로 전환`
- 둘 다 보류, 제목 톤만 조금 더 부드럽게 수정

## 답변을 승인 파일로 바꾸는 헬퍼

- `python3 /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/scripts/apply_user_approval_reply.py --reply "bitcoin 글 먼저 진행"`
- `python3 /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/scripts/apply_user_approval_reply.py --reply "bitcoin 먼저 검토, 이미지 보완 후 업로드 준비"`
- `python3 /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/scripts/apply_user_approval_reply.py --reply "bitcoin 글 먼저 진행" --apply`

## 답변에서 다음 실행 흐름까지 이어보기

- `python3 /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/scripts/run_user_approval_reply_flow.py --reply "bitcoin 글 먼저 진행"`
- `python3 /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/scripts/run_user_approval_reply_flow.py --reply "bitcoin 글 먼저 진행" --apply`

## 업로드 없이 안전하게 리허설하기

- `python3 /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/scripts/rehearse_user_approval_reply.py --reply "bitcoin 글 먼저 진행"`
- `python3 /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/scripts/rehearse_user_approval_reply.py --reply "FOMC 메인 말고 SEO 후속 글로 전환"`

## 1. 비트코인 핵심 흐름 해설

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
- excerpt: 한 줄 요약: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성 관점에서, 지금 투자자가 먼저 봐야 할 포인트를 한 번에 정리합니다.
- excerpt: 2026년 6월 30일 기준 시장이 특히 예민하게 반응하는 주제 중 하나가 바로 비트코인 핵심 흐름 해설입니다.
- excerpt: 비트코인이 오르거나 내릴 때 가장 먼저 보이는 건 가격입니다. 그런데 투자자 입장에서 더 중요한 건 왜 그런 움직임이 나왔는지, 그 배경이 하루짜리 잡음인지 구조적인 변화인지를 구분하는 일입니다.
- preview: 한 줄 요약: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성 관점에서, 지금 투자자가 먼저 봐야 할 포인트를 한 번에 정리합니다.
- preview: 2026년 6월 30일 기준 시장이 특히 예민하게 반응하는 주제 중 하나가 바로 비트코인 핵심 흐름 해설입니다. 비트코인이 오르거나 내릴 때 가장 먼저 보이는 건 가격입니다. 그런데 투자자 입장에서 더 중요한 건 왜 그런 움직임이 나왔는지, 그 배경이 하루짜리 잡음인지 구조적인 변화인지를 구분하는 일입니다. 쉽게 말해 이 이슈는 멀어 보여도 코인 전문 매체 기사까지 같이 보면 자산군 간 파급 경로가 보입니다. 개인 투자자 입장에서는 지금 결론을 단정하기보다, 무엇이 먼저 반응했는지와 무엇이 아직 가격에 덜 반영됐는지를 나눠 보는 것입니다. 여기서 먼저 봐야 할 건 `Jefferies warns of crypto market volatility as Clarity Act faces Senate test` 같은 제목 자체보다, 그 발표가 자금 흐름에 어떤 해석을 붙였는지입니다.
- evidence: Cointelegraph / 2026-06-30T12:44:21+00:00 / Swan's Cory Klippsten sees record Bitcoin holder supply revealing early bottom
- evidence: CoinDesk RSS / 2026-06-30T11:55:34+00:00 / Bitcoin’s quiet $59,000-$60,000 range is starting to look dangerous
- confirm_command: `python3 /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- next_command: `python3 /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- recovery_mode: `publish_direct`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin`
- hero_image_apply_helper: `python3 /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword bitcoin --slot hero --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- draft_path: `/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/drafts/02-bitcoin.md`
- html_path: `/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/publish-ready/02-비트코인-핵심-흐름-해설.html`

## 2. 미국 증시 지수 흐름 해설

- keyword: `us_index_flow`
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
- excerpt: 한 줄 요약: 복수 소스 교차 확인 가능 (2개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능 관점에서, 지금 투자자가 먼저 봐야 할 포인트를 한 번에 정리합니다.
- excerpt: 2026년 6월 30일 기준 시장이 특히 예민하게 반응하는 주제 중 하나가 바로 미국 증시 지수 흐름 해설입니다.
- excerpt: 반도체나 AI 이야기는 늘 뜨겁지만, 모든 종목이 같은 이유로 움직이는 건 아닙니다. 생각보다 중요한 포인트는 뉴스 제목보다 돈이 어디로 몰리고 있는지, 그리고 그 흐름이 실적으로 이어질 수 있는지입니다.
- preview: 한 줄 요약: 복수 소스 교차 확인 가능 (2개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능 관점에서, 지금 투자자가 먼저 봐야 할 포인트를 한 번에 정리합니다.
- preview: 2026년 6월 30일 기준 시장이 특히 예민하게 반응하는 주제 중 하나가 바로 미국 증시 지수 흐름 해설입니다. 반도체나 AI 이야기는 늘 뜨겁지만, 모든 종목이 같은 이유로 움직이는 건 아닙니다. 생각보다 중요한 포인트는 뉴스 제목보다 돈이 어디로 몰리고 있는지, 그리고 그 흐름이 실적으로 이어질 수 있는지입니다. 쉽게 말해 이 이슈는 멀어 보여도 해외 주요 매체 보도, 코인 전문 매체 기사까지 같이 보면 자산군 간 파급 경로가 보입니다. 개인 투자자 입장에서는 지금 결론을 단정하기보다, 무엇이 먼저 반응했는지와 무엇이 아직 가격에 덜 반영됐는지를 나눠 보는 것입니다. 여기서 먼저 봐야 할 건 `Nasdaq expands distribution of its market data into blockchain infrastructure` 같은 제목 자체보다, 그 발표가 자금 흐름에 어떤 해석을 붙였는지입니다.
- evidence: CoinDesk RSS / 2026-06-30T13:00:00+00:00 / Nasdaq expands distribution of its market data into blockchain infrastructure
- evidence: Reuters Markets via Google News RSS / 2026-06-30T10:25:32+00:00 / AI spending, earnings hopes, Fed outlook set to sway US stocks in second half - Reuters
- confirm_command: `python3 /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_index_flow`
- next_command: `python3 /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords us_index_flow`
- recovery_mode: `publish_direct`
- helper_preview_command: `python3 scripts/run_shortlist_keyword_flow.py --keyword us_index_flow`
- hero_image_apply_helper: `python3 /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword us_index_flow --slot hero --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- draft_path: `/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/drafts/03-us-index-flow.md`
- html_path: `/Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync/outputs/latest/publish-ready/03-미국-증시-지수-흐름-해설.html`
