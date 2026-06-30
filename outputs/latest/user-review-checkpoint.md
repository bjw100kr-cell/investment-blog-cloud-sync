# User Review Checkpoint

블로그 업로드 전에 사용자에게 가장 먼저 보여줄 초안과 확인 상태를 한 장에 묶은 체크포인트입니다.
- guardrail: 게시 전에는 제가 먼저 초안을 보여드리고, 사용자가 확인한 글만 다음 단계로 넘깁니다.
- posting_blocked_until_user_confirmation: `False`
- approved_keywords: `["bitcoin"]`
- approved_ready_count: `1`
- current review focus: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/current-review-focus.html`
- user approval inbox: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/user-approval-inbox.html`
- source freshness board: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/source-freshness-board.html`

## 지금 먼저 보여줄 글

- title: `FOMC 이후 시장 해설`
- keyword: `fomc`
- ready_now: `True`
- quality_status: `pass`
- draft_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/drafts/01-fomc.md`
- html_path: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/publish-ready/01-fomc-이후-시장-해설.html`
- freshness: `stale` / newest evidence age `12.9` days
- freshness_summary: 핵심 근거가 이미 오래돼 그대로 올리기에는 위험합니다. 마지막 대표 근거: Federal Reserve issues FOMC statement
- freshness_recommendation: 지금 상태로는 데일리 뉴스형 게시보다 refresh 후 재작성 또는 evergreen 해설형 전환이 더 안전합니다.
- next_action: 사용자 최종 확인 후 Blogger draft 업로드
- final retention CTA: FOMC 흐름이 여기서 끝이 아닙니다. 아래 체크포인트 글과 초보자 가이드까지 같이 보면 다음 일정에서 뭘 봐야 할지 훨씬 선명해집니다.
- later revisit CTA: 거시 이벤트를 놓치지 않으려면 다음 체크포인트 글까지 같이 보고, 이후에는 텔레그램/구독 채널로 이어 받아보세요.
- reply_example: `fomc` 글 먼저 진행
- confirm_command: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords fomc`
- excerpt: 한 줄 요약: 공식 소스 기반 확인 가능, 복수 소스 교차 확인 가능 (5개), 거시 해설형 글로 전환 가치 높음 관점에서, 지금 투자자가 먼저 봐야 할 포인트를 한 번에 정리합니다.
- excerpt: 2026년 6월 30일 기준 시장이 특히 예민하게 반응하는 주제 중 하나가 바로 FOMC 이후 시장 해설입니다.
- excerpt: 미국 기준금리 이야기는 멀게 느껴질 수 있습니다. 그런데 막상 시장이 흔들릴 때는 이 이슈가 달러, 나스닥, 비트코인까지 한 번에 건드리는 경우가 많습니다. 투자자 입장에서 보면 결국 중요한 건 발표 그 자체보다, 그 발표가 자금 흐름을 어떻게 바꾸느냐입니다.
- preview: 한 줄 요약: 공식 소스 기반 확인 가능, 복수 소스 교차 확인 가능 (5개), 거시 해설형 글로 전환 가치 높음 관점에서, 지금 투자자가 먼저 봐야 할 포인트를 한 번에 정리합니다.
- preview: 2026년 6월 30일 기준 시장이 특히 예민하게 반응하는 주제 중 하나가 바로 FOMC 이후 시장 해설입니다. 미국 기준금리 이야기는 멀게 느껴질 수 있습니다. 그런데 막상 시장이 흔들릴 때는 이 이슈가 달러, 나스닥, 비트코인까지 한 번에 건드리는 경우가 많습니다. 투자자 입장에서 보면 결국 중요한 건 발표 그 자체보다, 그 발표가 자금 흐름을 어떻게 바꾸느냐입니다. 쉽게 말해 이 이슈는 멀어 보여도 공식 발표 자료, 해외 주요 매체 보도까지 같이 보면 자산군 간 파급 경로가 보입니다. 개인 투자자 입장에서는 지금 결론을 단정하기보다, 무엇이 먼저 반응했는지와 무엇이 아직 가격에 덜 반영됐는지를 나눠 보는 것입니다. 여기서 먼저 봐야 할 건 `Federal Reserve issues FOMC statement` 같은 제목 자체보다, 그 발표가 자금 흐름에 어떤 해석을 붙였는지입니다.

## 다음 후보

- `비트코인 핵심 흐름 해설` / keyword `bitcoin` / ready `True` / quality `pass` / freshness `fresh`
  next action: 사용자 최종 확인 후 Blogger draft 업로드
