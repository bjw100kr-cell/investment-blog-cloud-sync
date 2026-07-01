# Agent Operating Model

이 문서는 하루 200명 이상이 실제로 들어오는 투자/경제/코인 블로그를 만들기 위한 서브 에이전트 역할 분담표입니다.

## 운영 원칙

- 최종 목표는 `검증된 실제 방문자 200명/일`입니다. 자동 실행, 초안 생성, 예상 방문자는 중간 지표일 뿐입니다.
- Spark 크레딧이 있으면 반복/검증/문서/단순 구현은 Spark가 맡습니다.
- Spark 크레딧이 없으면 `GPT-5.4`가 Spark 대행 역할을 맡습니다.
- 고성능 모델은 설계, 우선순위 결정, 충돌 조정, 위험 판단, 큐 생성만 맡고 반복 작업을 최대한 worker 큐로 넘깁니다.
- 에이전트는 같은 파일을 동시에 수정하지 않습니다. 파일 소유권이 겹치면 main operator가 먼저 조정합니다.
- Blogger 발행 cap은 기본 `1`을 유지합니다. 방문자 목표 때문에 무리하게 중복 발행하지 않습니다.

## 역할 분담

### 1. Market Scout

- 목적: 매일 글감이 되는 시장 변화와 검색 수요 후보를 수집합니다.
- 주 소유 파일:
  - `scripts/collect_investment_sources.py`
  - `scripts/build_search_demand_report.py`
  - `scripts/build_crypto_market_signal.py`
  - `outputs/latest/source-snapshot.*`
  - `outputs/latest/search-demand-report.*`
  - `outputs/latest/crypto-market-signal.*`
- 매일 작업:
  - CoinDesk, CoinNess, Binance market signal, 주요 해외 뉴스의 변화 확인
  - 검색 수요가 있는 키워드만 `fact candidate`, `narrative candidate`, `chart/sentiment sample`, `exclude`로 분류
  - 단순 가격 예측보다 ETF flows, 달러, 금리, 규제, 실적, 섹터 흐름을 우선

### 2. Keyword Strategist

- 목적: 사람들이 검색할 만한 제목과 클러스터를 정합니다.
- 주 소유 파일:
  - `scripts/score_daily_topics.py`
  - `scripts/build_keyword_opportunity_board.py`
  - `scripts/build_keyword_capture_strategy.py`
  - `scripts/build_editorial_calendar.py`
  - `outputs/latest/daily-post-brief.*`
  - `outputs/latest/keyword-opportunity-board.*`
- 매일 작업:
  - 상위 후보를 `거시경제`, `코인`, `미국주식`, `세계 흐름` 레인으로 나눔
  - 같은 레인만 반복되지 않게 주간 편성 조정
  - 제목은 `무슨 일인가`, `왜 흔들리나`, `무엇을 봐야 하나`가 드러나게 작성

### 3. Research Verifier

- 목적: 글에 들어가는 정보가 신뢰 가능한지 검증합니다.
- 주 소유 파일:
  - `scripts/build_current_reference_strategy.py`
  - `scripts/build_reference_strength_benchmark.py`
  - `scripts/build_source_freshness_board.py`
  - `outputs/latest/source-freshness-board.*`
  - `outputs/latest/approval-evidence-sheet.*`
- 매일 작업:
  - stale 뉴스는 메인 발행에서 제외하거나 evergreen 후속 글로 전환
  - 시장 민감 주장에는 1차/공신력 출처 우선 확인
  - 블로그 본문에 과장, 매수 유도, 단정 문장이 없는지 점검

### 4. Draft Producer

- 목적: 사람이 읽기 편한 초안과 발행 가능한 HTML을 만듭니다.
- 주 소유 파일:
  - `templates/investment_blog_draft_prompt.md`
  - `scripts/generate_blog_drafts.py`
  - `scripts/generate_seo_blog_drafts.py`
  - `scripts/render_publish_ready_posts.py`
  - `scripts/render_seo_publish_ready_posts.py`
  - `outputs/latest/drafts/`
  - `outputs/latest/publish-ready/`
  - `outputs/latest/seo-publish-ready/`
- 매일 작업:
  - `오늘 핵심 3줄`, `지금 무슨 일인가`, `개인 투자자가 볼 것`, `오해`, `리스크` 구조 유지
  - 정보량이 부족하거나 읽기 불편한 문단을 짧게 재작성
  - 본문 H1과 발행 title이 검색 클릭형으로 일치하는지 확인

### 5. Quality Gatekeeper

- 목적: 발행 전 품질, 내부링크, 이미지, 공유 버튼, 중복 위험을 차단합니다.
- 주 소유 파일:
  - `scripts/build_pre_publish_quality_gate.py`
  - `scripts/build_review_packet.py`
  - `scripts/build_full_draft_review_sheet.py`
  - `scripts/build_platform_publish_plan.py`
  - `scripts/build_publish_inventory.py`
  - `scripts/sync_click_titles_from_html.py`
  - `outputs/latest/pre-publish-quality-gate.*`
  - `outputs/latest/platform-publish-plan.*`
- 매일 작업:
  - `needs_fix_count=0` 확인
  - stale/orphan manifest, slug 충돌, 중복 발행 위험 확인
  - 발행 후보가 Blogger cap `1` 안에서 안전하게 잡혔는지 확인

### 6. Publish Inventory Agent

- 목적: `publish-inventory -> manifest selection -> uploader handoff` 계약을 지킵니다.
- 주 소유 파일:
  - `scripts/build_publish_queue.py`
  - `scripts/build_publish_inventory.py`
  - `scripts/render_publish_ready_posts.py`
  - `scripts/render_seo_publish_ready_posts.py`
  - `outputs/latest/publish-queue.*`
  - `outputs/latest/publish-inventory.*`
  - `outputs/latest/publish-ready-report.*`
  - `outputs/latest/seo-publish-ready-report.*`
- 매일 작업:
  - inventory 후보 수와 slug 충돌 여부 확인
  - orphan manifest가 uploader로 들어가지 않는지 확인
  - 제목 변경으로 slug가 바뀌어 기존 글 대신 새 글이 생기지 않도록 안정 slug 계약 유지

### 7. Publisher Operator

- 목적: GitHub Actions와 Blogger 업로드를 안전하게 운영합니다.
- 주 소유 파일:
  - `.github/workflows/daily-investment-intake.yml`
  - `scripts/upload_blogger_drafts.py`
  - `scripts/cleanup_blogger_posts.py`
  - `outputs/latest/blogger-upload-report.*`
  - `outputs/latest/blogger-upload-state.json`
  - `outputs/latest/blogger-cleanup-report.json`
- 매일 작업:
  - Actions 성공 여부 확인
  - `processed_count`, `already_synced_same_content`, `published URL` 확인
  - 중복 글은 지정 post_id cleanup으로만 정리

### 8. Growth Analyst

- 목적: 실제 200명/일 달성 여부를 증명하고 부족분을 계산합니다.
- 주 소유 파일:
  - `scripts/fetch_search_console_queries.py`
  - `scripts/search_console_to_feedback.py`
  - `scripts/compile_performance_feedback.py`
  - `scripts/build_daily_traffic_goal.py`
  - `scripts/build_visitor_proof_board.py`
  - `outputs/latest/visitor-proof-board.*`
  - `outputs/latest/daily-traffic-goal.*`
  - `outputs/latest/performance-feedback.*`
- 매일 작업:
  - Search Console/GA4 연결 상태 확인
  - `actual_verified_visitors`와 목표 차이 계산
  - 노출은 있는데 클릭률이 낮은 쿼리를 제목 테스트 큐로 넘김

### 9. Distribution & Monetization Planner

- 목적: 발행 후 유입과 수익화 동선을 설계합니다.
- 주 소유 파일:
  - `scripts/build_traffic_amplification_plan.py`
  - `scripts/build_traffic_cluster_board.py`
  - `scripts/build_popular_reads_board.py`
  - `scripts/apply_internal_link_blocks.py`
  - `scripts/apply_popular_reads_blocks.py`
  - `scripts/apply_reader_share_blocks.py`
  - `scripts/build_monetization_readiness_report.py`
  - `scripts/build_monetization_roadmap.py`
- 매일 작업:
  - 공개 URL 기준 배포 문구 생성
  - 내부링크/인기글/공유 버튼 적용 확인
  - AdSense, 뉴스레터, WordPress 확장 순서를 방문자 증거 기반으로 조정

## 충돌 방지 규칙

- `Publisher Operator`만 `.github/workflows/*`, Blogger state, cleanup script를 수정합니다.
- `Publish Inventory Agent`만 publish queue, publish inventory, manifest handoff 계약을 수정합니다.
- `Quality Gatekeeper`는 품질 게이트 판정을 담당하지만 publish inventory 계약을 직접 바꾸지 않습니다.
- `Draft Producer`는 원고/HTML 생성까지 담당하고 업로드 state를 직접 건드리지 않습니다.
- `Growth Analyst`는 측정/성과 산출물을 담당하고 제목 생성 규칙을 직접 바꾸지 않습니다. 제목 변경은 `Keyword Strategist`에게 큐로 넘깁니다.
- `Market Scout`는 자료 수집만 담당하고 발행 여부를 결정하지 않습니다.
- `Pipeline Orchestrator`만 `scripts/run_pipeline.sh`와 `.github/workflows/daily-investment-intake.yml`의 단계 순서를 바꿉니다.
- `main operator`는 여러 역할이 같은 파일을 수정해야 할 때 순서를 정하고 커밋 범위를 나눕니다.

## 매일 실행 체크

1. Market Scout: 새 시장/뉴스/검색 수요 수집
2. Keyword Strategist: 오늘 1순위 주제와 후속 클러스터 선정
3. Research Verifier: stale/근거 부족 후보 제거
4. Draft Producer: 초안과 HTML 생성
5. Quality Gatekeeper: 품질/slug/중복/내부링크 점검
6. Publish Inventory Agent: inventory와 uploader handoff 계약 확인
7. Publisher Operator: Blogger 1건 발행 또는 업데이트 검증
8. Growth Analyst: 실제 방문자 증거 확인
9. Distribution Planner: 공개 URL 배포/내부링크/수익화 동선 보강

## 현재 가장 중요한 병목

- `outputs/latest/visitor-proof-board.json` 기준 `proof_status=measurement_missing`, `actual_verified_visitors=0`입니다.
- 따라서 지금 1순위는 Search Console/GA4 연결을 끝내고, 실제 클릭/방문자 데이터를 매일 가져오는 것입니다.
- 측정 연결 전까지 `daily-traffic-goal`의 projected 값은 운영 참고값일 뿐 목표 달성 증거가 아닙니다.

## 현재 확인된 목표 병목

1. Search Console 측정이 끊겨 있습니다.
   - 증거: `outputs/latest/visitor-proof-board.json`의 `proof_status=measurement_missing`, `actual_verified_visitors=0`
   - 증거: `outputs/latest/search-console-fetch-report.json`의 `403 Forbidden`, `accessible_sites=[]`
   - 담당: `Growth Analyst`
2. 검색 쿼리 피드백 루프가 비어 있습니다.
   - 증거: `outputs/latest/search-console-conversion-report.md` 상태가 `없음`
   - 증거: `data/search_console_queries.csv`가 없거나 비어 있으면 `performance-feedback`가 비어 있음
   - 담당: `Growth Analyst`가 수집하고, `Keyword Strategist`가 제목 테스트로 반영
3. 200명 예상치는 증거가 아닙니다.
   - 증거: `outputs/latest/daily-traffic-goal.json`의 projected 값은 참고값이고, `visitor-proof-board`의 `projection_is_proof=false`
   - 담당: `Growth Analyst`
4. 실행 가능한 발행 후보가 좁습니다.
   - 증거: `outputs/latest/platform-publish-plan.json`의 approved ready 후보 수
   - 담당: `Quality Gatekeeper`, `Publish Inventory Agent`, `Publisher Operator`
5. 재방문/외부 배포 동선이 아직 약합니다.
   - 증거: `outputs/latest/traffic-amplification-plan.json`의 `manual_execution_required`
   - 증거: `outputs/latest/monetization-readiness-report.json`의 `retention_stack` 미완료
   - 담당: `Distribution & Monetization Planner`

## 서브 에이전트 실행 방식

- 기본은 한 번에 2~3명만 병렬로 둡니다. 너무 많이 띄우면 같은 파일을 건드릴 위험과 검토 비용이 커집니다.
- 먼저 `explorer`가 증거를 찾고, 그 다음 `worker`가 파일 소유권이 분리된 작은 패치를 맡습니다.
- Spark 사용량 제한이 나오면 같은 작업을 `GPT-5.4`가 Spark 대행으로 처리합니다.
- 고성능 모델은 매 세션 끝에 다음 worker가 바로 집을 수 있는 작은 작업을 `TASK_QUEUE.md`에 남깁니다.
- worker가 파일을 수정했다면 final에서 수정 파일 목록과 검증 명령을 반드시 보고합니다.
