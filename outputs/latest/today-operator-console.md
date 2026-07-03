# Today Operator Console

오늘 운영자가 바로 보면 되는 핵심만 모은 한 장짜리 콘솔입니다.

- ready_for_first_live_run: `True`
- repo_connected: `True`
- first_live_run_status: `ready_for_draft_test`
- github_launch_status: `needs_gh_cli`

## 1. 먼저 읽을 글

- shortlist: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/user-review-shortlist.md`
- reference strength benchmark: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/reference-strength-benchmark.md`
- user review checkpoint: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/user-review-checkpoint.html`
- current review focus: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/current-review-focus.html`
- user approval inbox: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/user-approval-inbox.html`
- source freshness board: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/source-freshness-board.md`
- github minimum launch card: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/github-minimum-launch-card.md`
- pipeline workflow parity: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/pipeline-workflow-parity.md`
- cloud launch preflight: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/cloud-launch-preflight.md`
- automation progress board: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/automation-progress-board.md`
- automation unblock card: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/automation-unblock-card.md`
- minimum unblock flow: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/minimum-unblock-flow.md`
- first blogger verify card: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/first-blogger-verify-card.md`
- click title sync report: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/click-title-sync-report.md`
- title experiment board: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/title-experiment-board.md`
- review packet: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/review-packet.md`
- full draft review sheet: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/full-draft-review-sheet.md`
- draft polish board: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/draft-polish-board.md`
- daily traffic goal: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/daily-traffic-goal.md`
- traffic cluster board: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/traffic-cluster-board.md`
- traffic amplification plan: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/traffic-amplification-plan.md`
- daily 200 visitor action board: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/daily-200-visitor-action-board.md`
- visitor proof board: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/visitor-proof-board.md`
- search console setup card: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/search-console-setup-card.md`
- indexing priority pack: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/indexing-priority-pack.md`
- internal link application report: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/internal-link-application-report.md`
- popular reads application report: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/popular-reads-application-report.md`
- reader share application report: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/reader-share-application-report.md`
- popular reads board: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/popular-reads-board.md`
- retention cta board: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/retention-cta-board.md`
- editorial calendar: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/editorial-calendar.md`
- approval evidence sheet: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/approval-evidence-sheet.md`
- approval briefing board: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/approval-briefing-board.html`
- shortlist publish action board: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/shortlist-publish-action-board.md`
- shortlist launchpad: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/shortlist-launchpad.html`
- image upgrade queue: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/image-upgrade-queue.md`
- image leverage board: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/image-leverage-board.md`
- top image action card: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/top-image-action-card.md`
- 원칙: 이 단계에서 글을 읽고 확인한 뒤에만 다음 단계로 넘어갑니다.

## 수동 채널 발행 패턴

- 네이버 블로그 (수동)
  - ready_command: `open https://blog.naver.com and paste html_path content`
  - ready_item_count: `1`
  - one-by-one steps
    - 1) `html_path`에 적힌 파일을 열어 전체 본문을 복사
    - 2) 네이버 블로그 글쓰기 에디터에서 새 글 작성으로 붙여넣기
    - 3) 카테고리/태그: `경제`, `투자`, `주식`, `코인` 중심으로 정리
    - 공개 범위를 확인하고 발행
    - 발행한 뒤 링크에 `출처`를 한 줄 넣고, 수익화 성과 트래킹 시트에 URL 기록
    - 발행 URL을 추후 수동 성과 추적용으로 기록
    - 중복/오타 검수 후 바로 다음 글로 이동

- 티스토리 (수동)
  - ready_command: `open https://www.tistory.com/manage and create a new post with copied html_path content`
  - ready_item_count: `1`
  - one-by-one steps
    - 1) `html_path`에 적힌 파일을 열어 본문을 복사
    - 2) 티스토리 새 글 작성으로 붙여넣기
    - 3) 썸네일/태그/카테고리를 시장 흐름 중심으로 정렬
    - 발행 후 상단 고정 링크와 관련 글 이동 경로를 점검
    - 문단 구분이 깨지면 HTML 보기에서 한 번 더 줄 바꿈 정리
    - 발행 URL과 대표 키워드를 수기 스프레드시트나 텍스트로 저장

- `비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트` / keyword `bitcoin` / verdict `approve` / publish `2026-07-04`
- `AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지` / keyword `ai_semiconductors` / verdict `approve` / publish `2026-07-05`
- `중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유` / keyword `china` / verdict `approve` / publish `2026-07-06`

## 1.5. 하루 200명 목표

- target: `200`
- projected: `190`
- gap: `10`
- status: `needs_more_distribution`
- `fomc` 예상 `95`명: FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지
- `bitcoin` 예상 `95`명: 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트
- actual_verified: `0`
- proof_status: `measurement_missing`
- proof_gap: `200`

## 2. 사용자 확인 명령

- single: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- batch: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- review board: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/review-preview-board.html`
- reply preview: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/run_user_approval_reply_flow.py --reply "bitcoin 글 먼저 진행"`
- reply apply: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/run_user_approval_reply_flow.py --reply "bitcoin 글 먼저 진행" --apply`

## 3. 사용자 확인 후 실행

- `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/run_user_approval_reply_flow.py --reply "bitcoin 글 먼저 진행" --apply`
- `python3 scripts/build_platform_publish_plan.py`
- `python3 scripts/upload_blogger_drafts.py`
- `python3 scripts/prepare_first_cloud_run_verification.py --allow-approved-state`

## 4. 이미지 하나만 보완하면 되는 글

- 현재는 이미지 하나만 보완하면 되는 별도 후보가 없습니다.

## 5. 이미지 작업 레버리지 라인

- 현재는 이미지 레버리지 라인 계산 결과가 없습니다.

## 6. 오늘 수익화 경로

- `main_post` / `비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트` / 페이지뷰와 체류시간 균형 확보
- `seo_followup` / `비트코인 핵심 흐름 초보자 가이드: 지금 꼭 알아야 할 핵심 구조` / 초보 검색 유입과 긴 체류시간 확보
- `next_slot` / `AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지` / 페이지뷰와 체류시간 균형 확보

## 7. 다음 큰 단계

- `phase_1_validate_blogger` / GitHub repo 연결 전후 첫 Blogger draft 검증
- `phase_2_repeatable_content_loop` / 첫 draft 검증 성공 후 3~7일 운영
- `phase_3_measurement_stack` / 반복 발행 루프 확인 후
