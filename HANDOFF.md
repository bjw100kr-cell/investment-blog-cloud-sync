# Handoff

## Objective
주식·코인·세계 흐름 중심의 투자/경제 블로그를 사람 같은 톤으로 매일 생성하고, 컴퓨터가 꺼져도 돌아가는 무료 자동화(기본은 Blogger)로 최소 하루 200명 이상 방문하는 블로그로 키우는 것.

## 연속성 규칙 (현재 적용)
- 컨텍스트 오버플로우 방지를 위해 이 문서, `CONVERSATION_SUMMARY.md`, `outputs/latest/context_checkpoint.md`, `outputs/latest/session_memos/session_memories.md`를 `단일 진실원(SSOT)`로만 사용한다.
- 중간중간 세이브 규칙: 큰 단계 전후·정책 변경·원인 변경·지시 변경 시 `bash scripts/refresh_context_window.sh "<note>"`, `python3 scripts/emit_context_checkpoint.py --note "<note>"`, `python3 scripts/persist_session_context.py -n "<note>"`를 차례로 수행한다.
- 추가: 모델 창이 길어질수록 `bash scripts/refresh_context_window.sh`를 매 20~30분 또는 단계 전환 때마다 먼저 실행해 오버플로우 복구 비용을 낮춘다.
- 한 번에 `브라우저 전환 + 명령 실행`이 필요한 구간은 아래 래퍼로 실행해 전/후 체크포인트를 강제하세요.
  - `bash scripts/run_with_context_safety.sh "<short-note>" -- <command>`
- 예시: `bash scripts/run_with_context_safety.sh "github-check" -- bash scripts/open_login_setup_pages.py --print-next`
- 사용자 대화 전환 전에는 `outputs/latest/context_checkpoint.md` 1회 먼저 갱신한 뒤 새 메시지로 진행한다.
- 오버플로우 재발 시 권장 즉시 복귀 순서: `outputs/latest/context_checkpoint.md` → `outputs/latest/session_memos/session_memories.md` → `HANDOFF.md` → `CONVERSATION_SUMMARY.md`.

## 핵심 상태 (7/1)
- `Blogger` 업로드 자격은 로컬에서 준비됨.
- 서브 에이전트 운영 기준은 `AGENT_OPERATING_MODEL.md`에 저장했습니다. 앞으로는 `Market Scout`, `Keyword Strategist`, `Research Verifier`, `Draft Producer`, `Quality Gatekeeper`, `Publish Inventory Agent`, `Publisher Operator`, `Growth Analyst`, `Distribution & Monetization Planner`로 역할을 나눕니다.
- Spark 크레딧이 없으면 `GPT-5.4`가 Spark 대행으로 `TASK_QUEUE.md`의 `Spark/5.4` 작업을 처리합니다.
- 현재 목표 병목은 `Growth Analyst` 영역입니다. `outputs/latest/visitor-proof-board.json` 기준 `proof_status=measurement_missing`, `actual_verified_visitors=0`이므로 Search Console/GA4 실측 연결 없이는 하루 200명 목표 달성을 증명할 수 없습니다.
- 새로 설치된 플러그인 중 현재 확인된 실사용 후보는 `Binance`와 `Google Drive`입니다.
- `Binance`는 코인 시장 센서로 사용합니다: market cap, volume, fear/greed, hot tokens, whale/player movement를 글감 후보와 본문 근거로 활용하되 단독 출처로 단정하지 않습니다.
- `Google Drive`는 검토본/운영 리포트/키워드 보드 공유에 사용합니다. 비밀키나 OAuth 결과 파일은 Drive로 올리지 않습니다.
- 플러그인 사용 원칙은 `outputs/latest/plugin-signal-usage.md`에 저장했습니다.
- `scripts/build_crypto_market_signal.py`가 `outputs/latest/crypto-market-signal.json/.md`를 만들고, `score_daily_topics.py`와 `build_pre_publish_quality_gate.py`가 이 신호를 반영합니다. GitHub Actions에도 포함되어 컴퓨터가 꺼져도 공개 API 기반 코인 시장 신호가 갱신됩니다.
- 목표가 `하루 최소 200명 방문`으로 구체화되어 `scripts/build_daily_traffic_goal.py`와 `outputs/latest/daily-traffic-goal.md`를 추가했습니다. 이 보드는 상위 글 조합의 예상 방문자, 목표 부족분, GA4/Search Console/재방문 병목을 매일 보여줍니다.
- `scripts/build_traffic_amplification_plan.py`와 `outputs/latest/traffic-amplification-plan.md`를 추가했습니다. 공개 Blogger URL, distribution snippets, traffic cluster, popular reads를 묶어 X/Threads, 텔레그램/카카오, 커뮤니티, 후속글 배포 순서와 예상 유입을 만듭니다.
- `scripts/build_visitor_proof_board.py`와 `outputs/latest/visitor-proof-board.md`를 추가했습니다. `예상 방문자`와 `실측 방문자(Search Console 클릭)`를 분리하며, `proof_status=verified_achieved`가 되기 전까지 하루 200명 목표를 달성으로 처리하지 않습니다.
- `scripts/fetch_search_console_queries.py`는 `SEARCH_CONSOLE_SITE_URL`이 없어도 `BLOG_BASE_URL` 또는 `blogger-upload-state.json`의 공개 Blogger URL에서 사이트 URL을 추론합니다.
- `scripts/fetch_search_console_queries.py`는 로컬 단독 실행 시 `.env`를 읽고, GitHub Actions에서는 Search Console 전용 secrets가 없어도 기존 `GOOGLE_CLIENT_ID/GOOGLE_CLIENT_SECRET/GOOGLE_REFRESH_TOKEN`을 fallback으로 사용합니다.
- `scripts/build_search_console_setup_card.py`와 `outputs/latest/search-console-setup-card.md`를 추가했습니다. Search Console에 등록할 URL-prefix 속성, sitemap URL, 첫 URL 검사 링크를 자동 정리합니다.
- `scripts/build_indexing_priority_pack.py`와 `outputs/latest/indexing-priority-pack.md`를 추가했습니다. 공개 Blogger URL을 예상 유입순으로 정렬하고 URL 검사 링크, site 검색 링크, 내부링크 액션을 자동 생성합니다.
- `scripts/apply_internal_link_blocks.py`와 `outputs/latest/internal-link-application-report.md`를 추가했습니다. `indexing-priority-pack`의 내부링크 액션을 실제 publish-ready HTML에 `함께 읽으면 흐름이 이어지는 글` 박스로 삽입해 체류시간/페이지뷰 상승을 노립니다.
- `scripts/apply_popular_reads_blocks.py`와 `outputs/latest/popular-reads-application-report.md`를 추가했습니다. 이미 공개된 후속글 URL을 메인 글 하단 `지금 같이 많이 볼 만한 글` 박스로 삽입해 검색 유입 후 추가 클릭 동선을 강화합니다.
- `scripts/apply_reader_share_blocks.py`와 `outputs/latest/reader-share-application-report.md`를 추가했습니다. 공개 메인 글 4개에 X/텔레그램/페이스북/원문 공유 버튼을 삽입해 독자 기반 추가 유입을 노립니다.
- `go-live-readiness` 기준 1차 실전(초안 테스트) 준비는 됨.
- `git remote`는 `https://github.com/bjw100kr-cell/investment-blog-cloud-sync`로 연결됐고, `repo_connected=true`, `repo_accessible=true` 상태입니다.
- 자동화 우선 채널은 `blogger`(1순위), `wordpress`(확장)로 고정.
- 컨텍스트 안전: `CONVERSATION_SUMMARY.md`, `outputs/latest/context_checkpoint.md/.json`, `outputs/latest/session_memos/session_memories.md`를 이 세션 기준 진실 소스로 유지.
- 대화/컨텍스트는 매 전환 지점마다 `python3 scripts/persist_session_context.py -n "..."`
  로 `CONVERSATION_SUMMARY.md`와 `outputs/latest/session_memos/`에 압축 저장되며,
  다음 세션은 이 파일부터 읽어 이어갈 수 있도록 설정됨.
- `scripts/run_pipeline.sh`는 장기 자동화 시 `run_step` 기준 단계 압축 저장을 자동 호출하도록 갱신됨 (`PIPELINE_CONTEXT_FLUSH_INTERVAL`로 주기 조정 가능).
- `bitcoin` 초안은 현재 승인 후보 1순위입니다: `fresh`, `quality_pass`, `hero_image_selected=True`.
- `review-approvals.json` 기준 승인 상태는 `bitcoin`만 true입니다 (`approved_all=false`, `approved_keywords=["bitcoin"]`).
- `run_shortlist_keyword_flow --keyword bitcoin --apply` 및 `run_first_blogger_verify_flow --apply --run-safety-check` 실행으로 `set_review_approvals -> build_platform_publish_plan -> upload_blogger_drafts -> prepare_first_cloud_run_verification --allow-approved-state` 체인이 정상 동작함.
- `blogger-upload-state.json` 기준 `비트코인 핵심 흐름 해설`은 `post_id=6339528652605057661`, `published=true` 상태입니다. 동일 본문이라 현재는 `already_synced_same_content` 판정만 반복됩니다.
- `2026-07-01`: 자동 발행 모드(`BLOGGER_REQUIRE_REVIEW_APPROVAL=false`)가 `platform-publish-plan`에도 반영되도록 수정했습니다. 이제 `user_final_confirmation_required=false`, `approved_ready_count=12`, Blogger `ready_item_count=12`로 보이며, 실제 업로드는 별도 cap `BLOGGER_MAX_POSTS_PER_RUN=1`로 계속 제한됩니다.
- `2026-07-01`: Growth Analyst `SP-100` 완료. Search Console 병목은 이제 `no_accessible_search_console_sites`로 명확히 표시됩니다. 사용자가 해야 할 최소 액션은 Search Console에서 `https://gimu-economy-insight.blogspot.com/` URL-prefix 속성 추가/검증 1개이며, `python3 scripts/open_login_setup_pages.py --print-next`가 `https://search.google.com/search-console`을 반환합니다.
- `2026-07-01`: Keyword Strategist `SP-102` 완료. `scripts/build_title_experiment_board.py`와 `outputs/latest/title-experiment-board.md/json`을 추가해 Search Console 실측 전에도 제목 A/B 후보를 준비합니다. 로컬 파이프라인과 GitHub Actions 모두 `Sync click titles` 직후 이 보드를 생성합니다.
- 업로드 전 확인용 보드 연결은 계속 유지됨:
  - `outputs/latest/user-review-checkpoint.md`
  - `outputs/latest/user-review-shortlist.md`
  - `outputs/latest/review-preview-board.html`
- `2026-07-01`: `session_memos`에 중복 저장된 동일 노트 1건을 정리하고, `CONVERSATION_SUMMARY.md`/`context_checkpoint`/`session_memos` 압축 저장을 갱신했습니다.
- `2026-07-01`: Search Console 측정 보강 결과, OAuth 자격증명은 `.env`에서 읽히고 사이트 URL도 `https://gimu-economy-insight.blogspot.com/`로 추론됩니다. 현재 실제 병목은 `403 Forbidden`이며 `accessible_sites=[]`라서, 같은 Google 계정의 Search Console에 블로그 속성 등록/검증 또는 권한 연결이 필요합니다.
- `2026-07-01`: Search Console 검증 직후 사용할 `sitemap.xml`, `feeds/posts/default?orderby=UPDATED`, 우선 URL 검사 목록, 내부링크 액션이 자동 생성되도록 연결했습니다.
- `2026-07-01`: 내부링크 적용 검증 결과, 실제 `publish-inventory.json`의 4개 메인 글(`fomc`, `bitcoin`, `us_index_flow`, `china`)에 공개 URL 기반 내부링크 박스가 적용됐고 품질 게이트는 13/13 pass입니다.
- `2026-07-01`: 인기글 라이브 URL 적용 검증 결과, 공개 후속글이 있는 `fomc`, `bitcoin`, `us_index_flow` 3개 메인 글에 인기글 박스가 적용됐습니다. `china`는 아직 공개 후속 URL이 없어 자동 skip입니다.
- `2026-07-01`: 독자 공유 버튼 적용 검증 결과, 공개 메인 글 4개(`fomc`, `bitcoin`, `us_index_flow`, `china`)에 공유 버튼이 적용됐고 품질 게이트는 13/13 pass입니다.

## 이번 세션에서 완료한 변경
- 모델 효율 규칙 + 작업 큐 문서화(`MODEL_EFFICIENCY_POLICY.md`, `TASK_QUEUE.md`) 유지.
- `HANDOFF.md` 최신화(현재 우선순위/블로커 재정리).
- `run_first_blogger_verify_flow.py` 버그 수정:
  - 승인 전체 확정(`approved_all=true`)일 때 `set_review_approvals` 단일 키워드 강제 실행을 생략.
- 로컬 실행 및 경로 점검:
  - `python3 scripts/check_setup.py`
  - `python3 scripts/sync_blogger_site_pages.py`(BLOGGER_SITE_PAGES 미사용 설정으로 동기화 스킵 처리 확인)
  - `python3 scripts/run_pipeline.sh`는 이전 실행 결과 재검증 완료로 보완됨.
- `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply` 수행으로 승인-업로드 체인 실제 실행 검증.
- `outputs/latest/first-cloud-run-verification.json`에서 승인 반영 후 `all_core_checks_passed` 이슈를 정리했고, 현재 기본 인증/자동모드 기준에서 통과 조건이 안정화됨.
- `python3 scripts/first_publish_operator_run.py` 실행 미리보기를 통해 승인 이후 체인에서 검증 명령이 `prepare_first_cloud_run_verification.py --allow-approved-state`로 표시되는지 확인.
- `python3 scripts/run_first_blogger_verify_flow.py --run-safety-check` 미리보기에서 승인 상태에서 `first-cloud-run-verification`가 `approved_run` 모드로 정상 계산되는지 확인.
- `python3 scripts/run_shortlist_keyword_flow.py --keyword bitcoin --apply` 재실행 시(재생성 기준 확인용) follow-up 체인에서도 승인 모드 플래그를 일관되게 전달하도록 정렬.
- `python3 scripts/check_setup.py`로 현재 로컬 준비 상태 재점검: `BLOGGER` 연동은 준비, GitHub Actions 동기화만 미완료.
- `TASK_QUEUE.md`의 `SP-002/SP-003`를 현재 상태(gh 미설치 + 웹 수동 입력 필요) 기준으로 `blocked`로 반영.
- `scripts/build_first_approval_path.py`의 1순위 추천 정렬 버그를 보정해 due-soon 메인 글이 비트코인 SEO 패키지보다 선행되도록 조정.
  - `due_soon_main` 배치 우선순위와 freshness 미기재 항목에 대한 편향을 낮춤.
  - 결과적으로 1순위 후보가 `bitcoin`으로 정렬되었고, 사용자 확인 안내도 최신 상태로 갱신됨.
- `scripts/upload_blogger_drafts.py` 업로드 엔진을 장애 회복형으로 강화.
  - Google Blogger API 429(Too Many Requests) 및 네트워크 예외 시 재시도(지수 백오프 + Retry-After 우선) 적용.
  - 개별 글 업로드 실패 시에도 전체 배치가 중단되지 않도록 per-item 실패를 저장해 다음 글로 진행.
  - 실패 사유를 `upload_error::<type>: <message>` 형태로 report에 남기도록 고도화.
  - `.env.example`에 API 재시도 튜닝 파라미터 추가: `BLOGGER_API_MAX_ATTEMPTS`, `BLOGGER_API_BACKOFF_BASE_SECONDS`, `BLOGGER_API_BACKOFF_MAX_SECONDS`.
- `scripts/upload_blogger_drafts.py`에 `BLOGGER_ALLOW_REUPLOAD_SAME_CONTENT`를 추가해 동일 본문 업로드 스킵 정책을 운영자가 제어할 수 있게 보강.
  - 기본값은 `false`로 유지해 중복 업로드를 방지하고, 필요 시 `true`로 동일 본문도 재동기화.
  - 업로드 리포트 요약에 `allow_reupload_same_content`를 남겨 스케줄 실행 이력을 추적.
- `README.md` 및 `.env.example`에 운영 모드 설명에 신규 플래그를 반영.
- 현재 실행 결과 확인: `outputs/latest/blogger-upload-report.json`에서 `processed_count`가 `0`으로 나온 것은 오류가 아니라
  - 모든 manifest가 기존 post와 `already_synced_same_content` 상태이기 때문으로, 네트워크 업로드 대상이 존재하지 않음.
- 동일 본문 재동기화 루프를 방지하기 위해 `state` 기준 상태 비교 로직은 유지하되, 새 본문 생성 시 동일하게 처리되도록 유지.
- 운영 모드 바로 적용 검증:
  - 로컬 `.env`에서 `BLOGGER_REQUIRE_REVIEW_APPROVAL=false`, `BLOGGER_AUTO_PUBLISH_POSTS=true`,
    `BLOGGER_PUBLISH_ONLY_DUE_POSTS=false`, `BLOGGER_MAX_POSTS_PER_RUN=3`로 고정.
  - `scripts/upload_blogger_drafts.py`를 같은 값으로 실행했을 때 `summary`에
    `review_required=False`, `auto_publish=True`, `publish_due_only=False`, `processed_count=0` 확인(동일 본문 재동기화 항목은 업로드 대상에서 제외).
  - `outputs/latest/blogger-upload-state.json`에서 13개 항목 모두 `published=True` 및 실제 Blogger 공개 URL 존재 확인.
  - `.env.example`도 운영값으로 갱신해 다음 세션/새 환경에 재현성 확보.
  - GitHub Actions 업로드 스텝 기본값도 `review=false`, `auto_publish=true`, `publish_only_due=false`,
    `max_posts_per_run=3`으로 변경해 컴퓨터 비가동 시에도 기본 동작이 자동 업로드/공개 되도록 정렬.
- 보조 도구/문서 정비:
  - `scripts/print_github_actions_minimum_inputs.py`에 `BLOGGER_REQUIRE_REVIEW_APPROVAL` 노출 항목 추가.
  - `README.md`에 `5-6. 운영 자동 모드` 섹션 추가(운영 변수 조합과 동작 확인 포인트 정리).
- 파이프라인 재개 안전성 강화:
  - `scripts/run_pipeline.sh`가 각 단계 시작/완료 시 `python3 scripts/emit_context_checkpoint.py`를 호출해 `outputs/latest/context_checkpoint.*`를 실시간 갱신.
  - 단계 실패 시에도 `failed` 노트가 남아 마지막 성공 스텝부터 이어갈 수 있도록 변경.
- 업로드 후보 선택 보강:
  - `scripts/upload_blogger_drafts.py`의 `collect_manifest_files()`가 `publish-inventory.json` 신선도를 판단해 필요 시 `publish-ready`/`seo-publish-ready`에서 보강 후보를 병합.
  - `publish-inventory` 타임스탬프가 최신 산출물보다 오래된 경우에도 새 manifest가 누락되지 않도록 처리.
  - 로컬 검증: `PYTHONPATH=scripts:. python3 - <<'PY'>>` 환경에서 `is_inventory_stale`가 `True`로 판정되고, 후보 집계가 기존 인벤토리 외부 매니페스트까지 반영됨.

## 다음 하이프리오리티 액션
0. 제목 클릭률 개선 반영 사항 확인:
   - `scripts/sync_click_titles_from_html.py`가 추가되어 `publish-inventory.json`의 메인 글 manifest만 대상으로 HTML H1을 `title`/`meta_title`에 동기화.
   - 로컬/클라우드 파이프라인 모두 `Build publish inventory` 직후 해당 단계를 실행.
   - 최신 검증에서 메인 글 4개가 모두 개선됨: `manifest_changed_count=4`, `inventory_changed_count=4`.
   - 현재 Blogger 1순위 후보 `bitcoin` 제목은 `비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트`.
   - 신규 개선: `score_daily_topics.py` 기본 제목도 클릭형으로 교체했고, `generate_blog_drafts.py`의 미국 증시 제목 부제 중복 버그를 제거.
   - `daily-traffic-goal.json`은 이제 실제 발행 인벤토리 제목과 코인 시장 신호(`extreme_fear`, BTC 변동, Fear/Greed)를 같이 보여줌.
   - 중복 발행 방지: 메인 글은 keyword별 안정 slug를 사용하고, 업로더는 기본적으로 `publish-inventory.json` 후보만 사용.
   - 최신 클라우드 검증: GitHub Actions run `28479394787`이 commit `a19b01c`에서 `success`로 완료됨. 새 중복은 만들지 않았고 비트코인 글은 기존 URL `https://gimu-economy-insight.blogspot.com/2026/06/blog-post.html`에 반영됨.
   - 주의: `2026-06-30T22:06Z` 클라우드 실행에서 FOMC 중복 글 `https://gimu-economy-insight.blogspot.com/2026/06/fomc-3.html`이 생성됨. 기존 원본 `https://gimu-economy-insight.blogspot.com/2026/06/fomc.html`은 유지됨.
   - 중복 정리 도구: `scripts/cleanup_blogger_posts.py`와 workflow input `cleanup_duplicate_post_ids` 추가. 수동 실행 때 post_id `1530213910086239357`만 입력하면 GitHub Actions의 Blogger secret으로 중복 글을 삭제하고 state에서도 제거할 수 있음. 공개 URL은 이미 404로 확인됐으므로 API 404도 삭제 완료로 처리해야 함.
1. 서브 에이전트 운영 모델이 추가됨:
   - `AGENT_OPERATING_MODEL.md`
   - `TASK_QUEUE.md`의 `SP-100`~`SP-106`
2. FOMC 중복 정리는 완료됨:
   - `outputs/latest/blogger-cleanup-report.json`의 `deleted_count=1`
   - `outputs/latest/blogger-cleanup-report.json`의 `removed_from_state_count=1`
   - `https://gimu-economy-insight.blogspot.com/2026/06/fomc-3.html`은 404
   - 원본 `https://gimu-economy-insight.blogspot.com/2026/06/fomc.html`은 200
3. 다음 병목은 방문자 측정 연결:
   - `outputs/latest/visitor-proof-board.json`는 아직 `measurement_missing`, `actual_verified_visitors=0`
   - Search Console/GA4 연결 전까지 200명 목표 달성은 증명 불가

## 지금 당장 필요한 사용자 입력 (한 곳만 처리하면 됨)
- 먼저 GitHub Actions Secrets/Variables 입력이 선행입니다. 현재 리포지토리 주소는 `bjw100kr-cell/investment-blog-cloud-sync`입니다.
- 아래로 다음 URL만 확인하면 1단계 작업이 끝납니다.
  - `python3 scripts/open_login_setup_pages.py --print-next` 출력의 `next_url`
- Secrets/Variables는 한 번에 값 입력: https://github.com/bjw100kr-cell/investment-blog-cloud-sync/settings/secrets/actions
- 넣을 항목 (현재 최우선 필수):
  - Secrets: `BLOGGER_BLOG_ID`, `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`, `GOOGLE_REFRESH_TOKEN`
  - Variables: `OPENAI_MODEL`, `BLOGGER_SYNC_SITE_PAGES`, `BLOGGER_SITE_PAGES_PUBLISH`, `BLOGGER_INCLUDE_OPTIONAL_SITE_PAGES`, `BLOGGER_REQUIRE_REVIEW_APPROVAL`, `BLOGGER_AUTO_PUBLISH_POSTS`, `BLOGGER_PUBLISH_ONLY_DUE_POSTS`, `BLOGGER_MAX_POSTS_PER_RUN`
- 모든 입력 후 Actions에서 `Daily Investment Intake`를 `Run workflow`로 1회 실행하면 첫 자동 업로드 블로킹이 해제됩니다.

## 다음 세션 주의점
- 긴 작업 중에는 `CONTEXT_PROTOCOL.md`를 먼저 확인하고, 대화가 길어지기 전에 `CONVERSATION_SUMMARY.md`와 이 파일을 갱신한다.
- 오버플로우 예방이 필요할 때는 아래 3단계를 먼저 실행하세요.
  - `bash scripts/refresh_context_window.sh "handoff"`
  - `python3 scripts/emit_context_checkpoint.py --note "handoff"`
  - `python3 scripts/persist_session_context.py -n "handoff"`
- 대화 이어붙임이 길어질 땐 `bash scripts/refresh_context_window.sh "handoff"`로 압축 저장 후
  아래 4개만 읽고 진행하세요: `outputs/latest/context_checkpoint.md`, `outputs/latest/session_memos/session_memories.md`, `CONVERSATION_SUMMARY.md`, `HANDOFF.md`.
- 다음 세션은 전체 채팅 로그보다 `CONVERSATION_SUMMARY.md`, `HANDOFF.md`, `TASK_QUEUE.md`, `outputs/latest/blogger-upload-state.json`, `outputs/latest/blogger-upload-report.json`를 우선 신뢰한다.
- 컨텍스트 오버플로우 대비: 작업 방향이 바뀌거나 업로드 정책이 바뀌면, 새 작업 시작 전 `python3 scripts/emit_context_checkpoint.py --note "handoff"`를 먼저 실행해 현재 상태를 압축 저장한 뒤 진행한다.
- `run_pipeline.sh`는 단계별 시작/완료마다 checkpoint를 남기고, 기본 5단계마다 `persist_session_context.py`로 추가 요약 저장(`pipeline-run-step-*`)도 함께 남겨 놓는다.
- 중간 점검이 필요하면 `run_pipeline.sh`가 마지막에 남긴 `outputs/latest/context_checkpoint.*`와 최근 `outputs/latest/session_memos/session_memories.md`를 같이 읽고 다음 단계부터 이어갈 수 있다.
- `first-cloud-run-verification`의 `review_approval_state_is_safe`는 승인 반영 전/안전 상태에서 통과 조건이고,
- 운영 승인 상태(`user_confirmed_keywords` 반영)에서는 `--allow-approved-state`로 `approved_run` 모드를 명시해 검증해야 한다.
- 승인 적용 직후 검증 미리보기는 `python3 scripts/prepare_first_cloud_run_verification.py --allow-approved-state`로 확인.
- 운영자가 승인 후보를 바꾸려면 `python3 scripts/set_review_approvals.py --clear` 후 다시 반영할 키워드로 재적용하면 된다.

## 탭 최소화 체크

- 1개 탭만 열어야 할 때: `python3 scripts/open_login_setup_pages.py --open-next`
- 실행하면 `next_url=...` 형태로 실제 열어야 할 URL을 한 줄로 출력합니다.
- 현재 권장 URL: `https://github.com/bjw100kr-cell/investment-blog-cloud-sync/settings/secrets/actions`
- 값 복사용 즉시 출력: `python3 scripts/print_github_actions_minimum_inputs.py`
