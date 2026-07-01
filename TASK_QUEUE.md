# Task Queue

이 문서는 Spark 계열 모델이 우선 수행할 작업 큐입니다.

규칙:

- `Owner`가 `Spark`인 작업은 Spark 세션이 바로 수행합니다.
- Spark 크레딧이 없으면 `GPT-5.4`가 Spark 대행 세션으로 같은 규칙을 적용받습니다.
- `Owner`가 `High`인 작업은 상위 모델만 수행하거나 결정합니다.
- `Blocked`인 작업은 선행 조건이 충족되기 전까지 실행하지 않습니다.
- 완료 후 상태와 메모를 바로 갱신합니다.

## Active Queue

| ID | Owner | Status | Depends On | Task |
| --- | --- | --- | --- | --- |
| SP-001 | Spark | blocked | GitHub repo URL | `bash scripts/bootstrap_github_remote.sh <YOUR_GITHUB_REPO_URL>` 실행 후 원격 연결 검증 |
| SP-002 | Spark | blocked | SP-001 | `outputs/latest/github-actions-sync.sh OWNER/REPO` 또는 GitHub UI로 Secrets/Variables 반영. 현재 `gh` 미설치 상태라 UI 수동 입력으로 대체 필요 |
| SP-003 | Spark | blocked | SP-001, SP-002 | GitHub Actions 첫 수동 실행 후 workflow 로그와 산출물 점검 |
| SP-004 | Spark | completed | none | `python3 scripts/check_setup.py`와 핵심 보고서 재생성으로 현재 준비상태 재검증 |
| SP-005 | Spark | completed | none | `outputs/latest/start-here-runbook.md`, `outputs/latest/go-live-dashboard.md`, `outputs/latest/success-gate.md` 최신성 검토 |
| SP-006 | Spark | blocked | BLOG_BASE_URL 확정 | `SEARCH_CONSOLE_SITE_URL` 입력 후 Search Console 계열 리포트 재생성 |
| SP-007 | Spark | completed | none | `bash scripts/run_pipeline.sh` 재실행 후 OpenAI 초안 품질과 Blogger draft 업로드 결과 검증 (`OPENAI_API_KEY` 없이 fallback 초안으로도 검증 완료) |
| SP-008 | Spark | completed | none | README와 운영 문서에서 실행 순서/무료 운영 모드 설명의 일관성 점검 |
| SP-009 | Spark | pending | SP-003 | 첫 실전 업로드 결과 기준으로 `publish-queue`, `keyword-opportunity-board`, `monetization-readiness-report` 재검토 |
| SP-010 | Spark | completed | none | `outputs/latest/review-packet.md`를 기준으로 사용자에게 검토본을 보여주고 사용자 최종 확인 keyword만 `review-approvals.json`에 반영 |
| SP-011 | Spark | completed | none | `bash scripts/run_pipeline.sh` 재실행 후 `daily-post-brief`, `search-demand-report`, `human-tone-review`, `review-packet`에서 미국 증시 인기 검색어 반영 여부 검증 |
| SP-012 | Spark | completed | SP-011 | 결과물에서 `해설와`, `... 이슈는` 같은 어색한 한국어가 남았는지 전수 확인하고 발견 시 이슈 기록 |
| SP-013 | Spark | pending | user review | `미국 빅테크 흐름 해설` 포함 메인 글 4개 중 사용자 최종 확인된 keyword만 `review-approvals.json`에 반영하고 업로드 재검증 |
| SP-014 | Spark | pending | user review | `미국 빅테크` SEO 후속 글 3종 중 승인된 keyword만 반영해 내부링크형 후속 포스팅 업로드 검증 |
| SP-015 | Spark | blocked | WordPress credentials | `python3 scripts/upload_wordpress_drafts.py` 실업로드 검증 후 `wordpress-upload-report.json` 상태 확인 |
| SP-016 | Spark | completed | user review | 승인 keyword 반영 후 `python3 scripts/build_platform_publish_plan.py`를 재실행해서 채널별 approved upload 후보가 보이는지 확인 |
| SP-017 | Spark | blocked | SP-001, SP-002 | GitHub Actions 첫 실행 후 `review-packet`, `approval-dashboard`, `platform-publish-plan`, `blogger-upload-report`, `wordpress-upload-report`가 클라우드에서 어떻게 생성됐는지 검증 |
| SP-018 | Spark | completed | SP-003 | `python3 scripts/prepare_first_cloud_run_verification.py --allow-approved-state` 포함 승인 후 검증 흐름으로 첫 클라우드 런 결과 모드 전환 정합성을 확인 |
| SP-019 | Spark | completed | none | `automation-scope`, `login-launch-checklist`, `start-here-runbook`, `go-live-dashboard`를 Blogger 우선 최소 자동화 경로 기준으로 정리 |
| SP-020 | Spark | completed | none | `first-approval-path` 산출물을 추가해 오늘 먼저 승인할 글/묶음과 승인 후 실행 명령을 한 장으로 정리 |
| SP-021 | Spark | completed | none | `go-live-readiness`, `monetization-readiness`, `operator-handoff`, `first-live-run-plan` 문구를 Blogger 우선 운영정책 기준으로 일관화 |
| SP-022 | Spark | completed | none | `daily-revenue-focus` 산출물을 추가해 오늘 어떤 글 순서가 수익화에 유리한지와 승인 명령을 한 장으로 정리 |
| SP-023 | Spark | completed | none | `monetization-roadmap` 산출물을 추가해 발행 검증 후 GA4/재방문/AdSense/WordPress 확장 순서를 단계별로 정리 |
| SP-024 | Spark | completed | none | `first-publish-operator-run` 실행 카드를 추가해 첫 승인 이후 실제 실행 명령 흐름을 preview/apply 형태로 정리 |
| SP-025 | Spark | completed | none | `user-review-shortlist` 산출물을 추가해 사용자가 실제로 읽을 글만 짧게 압축해 보여주도록 정리 |
| SP-026 | Spark | completed | none | `today-operator-console` 산출물을 추가해 오늘 운영 핵심을 한 장으로 통합 |
| SP-027 | Spark | completed | none | `prepare_launch_bundle.py`를 자동화 전용 번들 리포트 기준으로 갱신해 최신 운영 카드와 핵심 blocker만 한 장에 정리 |
| SP-028 | Spark | completed | none | `review-preview-board` HTML 검토 보드를 추가해 승인 전 실제 렌더링 글을 한 화면에서 읽고 확인할 수 있게 정리 |
| SP-029 | Spark | completed | none | `operator-home` HTML 운영 홈을 추가해 blocker, 승인 명령, 검토 보드, 다음 실행 명령을 단일 시작 화면으로 통합 |
| SP-030 | Spark | completed | none | 최신 투자/코인 레퍼런스 패턴을 설정과 초안 패킷에 반영해 자동 글 구조가 검색형 설명글과 뉴스 해설형 글을 함께 따르도록 강화 |
| SP-031 | Spark | completed | none | `keyword-capture-strategy` 운영 카드를 추가해 현재 키워드를 어떤 글 패턴과 내부링크 경로로 받아야 하는지 한 장으로 정리 |
| SP-032 | Spark | completed | none | `pre-publish-quality-gate`를 추가해 발행 전 신뢰/내부링크/소스 강도/측정 준비 상태를 자동 점검하도록 강화 |
| SP-033 | Spark | completed | none | 업로드 스크립트가 `pre-publish-quality-gate`를 읽어 `needs_fix`/`review_before_publish` 항목 업로드를 건너뛰게 반영 |
| SP-034 | Spark | completed | none | `platform-publish-plan`에 품질 게이트 정합성을 반영해 `pass` 상태 글만 업로드 후보로 노출 |
| SP-035 | Spark | completed | none | `operator-home`, `login-launch-checklist`를 최소 실행 경로 기준으로 단순화해 `지금 할 일 1개`가 먼저 보이도록 정리 |
| SP-036 | Spark | completed | none | GitHub 연결 명령이 `<OWNER/REPO>` 짧은 입력도 받도록 바꾸고 운영 문서도 같은 표현으로 통일 |
| SP-037 | Spark | completed | none | 저작권 안전 이미지 추천 레이어를 추가해 글별 1~2장 추천, 라이선스 링크, 검토 메모가 자동 생성되도록 정리 |
| SP-038 | Spark | completed | none | `image-selections.json` 승인 파일과 helper를 추가해 선택한 이미지 URL/출처를 렌더링과 발행 draft에 반영할 수 있게 정리 |
| SP-039 | Spark | completed | none | 검토/승인 흐름을 `사용자 최종 확인` 기준으로 재정리하고 `review-packet`, `platform-publish-plan`, `first-cloud-run-verification`, `operator-home` 문구를 일관화 |
| SP-040 | Spark | completed | none | 품질 게이트와 대표 이미지 선택 여부를 반영해 `approval-dashboard`, `first-approval-path`, `user-review-shortlist` 우선순위를 실제 발행 가능성 기준으로 재정렬 |
| SP-041 | Spark | completed | none | `image-upgrade-queue` 산출물을 추가해 이미지 1장만 고르면 ready 후보가 되는 글을 별도 큐로 노출하고 자동 파이프라인에도 연결 |
| SP-042 | Spark | completed | none | `image-leverage-board` 산출물을 추가해 어떤 라인에 이미지를 먼저 보완해야 ready 후보 수가 가장 빨리 늘어나는지 묶음 기준으로 계산하고 운영 화면에 반영 |
| SP-043 | Spark | completed | none | `operator-home`, `user-review-shortlist` 상단에 `초안 먼저 확인 -> 사용자 최종 확인 -> 업로드` 발행 안전 원칙을 더 명확히 노출 |
| SP-044 | Spark | completed | none | `top-image-action-card` 산출물을 추가해 가장 레버리지가 큰 이미지 라인을 검색 링크, 적용 순서, helper 명령까지 한 장으로 실행 가능하게 정리 |
| SP-045 | Spark | completed | none | `full-draft-review-sheet` 산출물을 추가해 shortlist 글 전문을 발행 전 그대로 읽고 확인할 수 있게 콘솔/운영 홈/파이프라인에 연결 |
| SP-046 | Spark | completed | none | `approval-evidence-sheet` 산출물을 추가해 shortlist 글별 소스 이름, headline 예시, 검색 수요 점수를 확인용 시트로 묶고 콘솔/운영 홈/파이프라인에 연결 |
| SP-047 | Spark | completed | none | `approval-briefing-board` HTML/MD 산출물을 추가해 전문, 근거, 이미지 상태, 승인 명령을 한 화면에서 보는 통합 승인 보드를 연결 |
| SP-048 | Spark | completed | none | `shortlist-publish-action-board` 산출물을 추가해 shortlist 글별 남은 blocker와 다음 한 줄 실행 명령을 분리해 콘솔/운영 홈/파이프라인에 연결 |
| SP-049 | Spark | completed | none | `run_shortlist_keyword_flow.py` 헬퍼를 추가해 shortlist 글 1개 기준 실행 체인을 preview/apply하고, action board에 helper 명령을 함께 노출 |
| SP-050 | Spark | completed | none | `shortlist-launchpad` HTML/MD 산출물을 추가해 shortlist 2개 글만 기준으로 검토/근거/실행 명령을 가볍게 보는 시작 화면을 연결 |
| SP-051 | Spark | completed | none | `operator-home`의 `Single Next Action`이 항상 `초안 먼저 확인 -> 사용자 최종 확인 -> 업로드` 흐름을 우선 보여주도록 조정 |
| SP-052 | Spark | completed | none | `current-review-focus` HTML/MD 산출물을 추가해 지금 사용자에게 바로 보여줄 1순위/2순위 초안만 다시 압축하고 운영 홈/콘솔/파이프라인/워크플로우에 연결 |
| SP-053 | Spark | completed | none | `user-approval-inbox` HTML/MD 산출물을 추가해 사용자가 승인 여부만 빠르게 답할 수 있는 확인 전용 화면을 운영 홈/콘솔/파이프라인/워크플로우에 연결 |
| SP-054 | Spark | completed | none | `apply_user_approval_reply.py` 헬퍼를 추가해 `fomc 글 먼저 진행` 같은 사용자 답변을 승인 반영 preview/apply 흐름으로 바꾸고, inbox에 예시 명령을 노출 |
| SP-055 | Spark | completed | none | `run_user_approval_reply_flow.py` 헬퍼를 추가해 짧은 사용자 답변에서 승인 반영 후 게시 후보 재계산까지 preview/apply 흐름으로 이어주고 inbox에 예시 명령을 노출 |
| SP-056 | Spark | completed | none | GitHub Actions `daily-investment-intake` workflow에 로컬 파이프라인과 맞춰 `current-reference-strategy`, `keyword-capture-strategy`, `review-preview-board`, `operator-home`, `first-cloud-run-verification` 생성 단계를 추가 |
| SP-057 | Spark | completed | none | `github-web-launch-checklist`에 최소 Go-Live 경로, Secrets 복붙 목록, WordPress/OpenAI 비필수 여부를 더 압축해 실제 GitHub 웹 연결 체크리스트를 간소화 |
| SP-058 | Spark | completed | none | `github-minimum-launch-card` 산출물을 추가해 `레포 생성 -> 원격 연결 -> Secrets/Variables 입력 -> workflow 실행` 최소 경로를 한 장으로 압축하고 운영 홈/콘솔/파이프라인/워크플로우에 연결 |
| SP-059 | Spark | completed | none | `resume-after-login-report`에도 `github-minimum-launch-card` 링크를 추가해 로그인/재개 직후 GitHub 무료 자동화 진입 카드로 바로 이동 가능하게 정리 |
| SP-060 | Spark | completed | none | `go-live-dashboard`에 `Minimum Cloud Blocker`와 `github-minimum-launch-card` 경로를 추가해 무료 클라우드 자동화 blocker를 한눈에 보게 정리 |
| SP-061 | Spark | completed | none | `pipeline-workflow-parity` 리포트를 추가해 로컬 `run_pipeline.sh`와 GitHub Actions 단계 차이를 자동 점검하고, workflow에도 누락 단계들을 더 맞춰 연결 |
| SP-062 | Spark | completed | none | `pipeline-workflow-parity` 리포트를 `operator-home`, `today-operator-console`, `go-live-dashboard`에 직접 연결해 무료 자동화 상태를 시작 화면에서 바로 점검 가능하게 정리 |
| SP-063 | Spark | completed | none | `user-review-checkpoint` HTML/MD 산출물을 추가해 게시 전에 사용자에게 먼저 보여줄 1순위 초안과 확인 상태를 한 장으로 묶고 운영 홈/콘솔/파이프라인/워크플로우에 연결 |
| SP-064 | Spark | completed | none | `cloud-launch-preflight` 산출물을 추가해 GitHub Actions 실행 직전 repo 연결, Blogger 준비, 승인 안전상태, parity, 클라우드 안전체크를 한 장으로 점검하고 운영 홈/콘솔/런북/워크플로우에 연결 |
| SP-065 | Spark | completed | none | `draft-polish-board` 산출물을 추가해 shortlist 상위 초안의 사람 느낌 보완 문장, 해석 문장, CTA 보정안을 한 장으로 정리하고 운영 홈/콘솔/런북/워크플로우에 연결 |
| SP-066 | Spark | completed | none | `reference-strength-benchmark` 산출물을 추가해 현재 잘 읽히는 투자·경제·코인 레퍼런스의 트래픽 구조와 강점을 우리 운영 액션으로 번역하고 운영 홈/콘솔/런북/워크플로우에 연결 |
| SP-067 | Spark | completed | none | `traffic-cluster-board` 산출물을 추가해 메인 글과 후속 SEO 글 묶음을 트래픽/내부링크/재방문 단위로 우선순위화하고 운영 홈/콘솔/런북/워크플로우에 연결 |
| SP-068 | Spark | completed | none | `popular-reads-board` 산출물을 추가해 메인 글 아래와 허브에 붙일 대표 읽을거리 묶음을 현재 클러스터 기준으로 정리하고 운영 홈/콘솔/런북/워크플로우에 연결 |
| SP-069 | Spark | completed | none | `retention-cta-board` 산출물을 추가해 각 클러스터별 글 하단 CTA, 나중 텔레그램/뉴스레터 전환 CTA 초안을 정리하고 운영 홈/콘솔/런북/워크플로우에 연결 |
| SP-070 | Spark | completed | none | `source-freshness-board` 산출물을 추가해 근거 소스 신선도를 `fresh/aging/stale`로 노출하고, 검토 화면/운영 홈/파이프라인/워크플로우에 연결한 뒤 stale 글은 게시 후보와 Blogger 업로드에서 자동 차단 |
| SP-071 | Spark | completed | none | 유튜브 transcript 기반 `reference_takeaways`를 시장 키워드 중심으로 정제하고, fallback 초안 본문에는 참고 포인트를 1회만 노출하도록 바꿔 비트코인 초안의 반복/잡음 문장을 제거 |
| SP-072 | Spark | completed | none | 주제 선정 로직에 `brand_lane`을 추가해 사용자 노출 기준을 `거시경제 / 코인 / 미국주식 / 세계 흐름` 4개 레인으로 분리하고, `daily-post-brief`, `current-reference-strategy`, `growth-report`에 반영 |
| SP-073 | Spark | completed | none | `user-review-shortlist`, `daily-revenue-focus`, `today-operator-console`, `operator-home`에 브랜드 레인 표시와 레인 중복 최소화 규칙을 반영해 사용자 검토/수익화 화면이 코인 일변도로 보이지 않게 조정 |
| SP-074 | Spark | completed | none | `first-approval-path`를 freshness-aware 승인 경로로 조정해 `stale` 글은 보류 목록으로 분리하고, `shortlist`/`operator console` 승인 명령과 같은 기준으로 통일 |
| SP-075 | Spark | completed | none | `source-freshness-board`와 `shortlist-publish-action-board`에 stale 글의 `evergreen_salvage` 복구 경로를 추가해 `fomc -> seo_fomc_1` 같은 대체 승인/이미지 보완 흐름을 자동 제안 |
| SP-076 | Spark | completed | none | `user-review-checkpoint`와 `user-approval-inbox`에도 stale 글의 `evergreen_salvage` 안내와 답변 예시를 반영해 사용자 확인 화면이 실제 승인 가능 경로와 일치하도록 조정 |
| SP-077 | Spark | completed | none | `apply_user_approval_reply.py`를 보강해 `FOMC 메인 말고 SEO 후속 글로 전환`, `FOMC는 보류하고 bitcoin 먼저 진행` 같은 자연어를 각각 `seo_fomc_1` 승인, `fomc hold + bitcoin approve`로 안전하게 해석 |
| SP-078 | Spark | completed | none | `first-approval-path`에 `selection_summary`와 `why_not_other_topics` 근거를 추가해, 오늘 1순위 주제가 왜 선택됐는지와 더 높은 점수 후보가 왜 보류됐는지를 운영 카드에서 바로 설명 |
| SP-079 | Spark | completed | none | `build_editorial_calendar.py`를 freshness-aware 주간 레인 밸런스 캘린더로 교체해 stale 뉴스 직행 대신 direct/recovery/evergreen 모드를 섞고, `operator-home`과 `today-operator-console`에서 바로 열 수 있게 연결 |
| SP-080 | Spark | completed | none | `daily-revenue-focus`, `user-review-shortlist`, `today-operator-console`를 freshness-aware하게 정리해 stale `fomc`가 상단 검토/next slot 후보처럼 보이지 않게 하고, 대체 레인 후보(`china`)나 fresh 단건만 남도록 조정 |
| SP-081 | Spark | completed | none | `automation-progress-board` 산출물을 추가해 콘텐츠 엔진, Blogger draft loop, 무료 클라우드 자동화, 측정 스택, WordPress 확장 상태를 `complete/in_progress/blocked`로 한 장에 요약하고 `operator-home`/`today-operator-console`에 연결 |
| SP-082 | Spark | completed | none | `automation-unblock-card` 산출물을 추가해 사용자 쪽에서 지금 해야 하는 핵심 2개(`bitcoin 승인`, `GitHub repo 연결`)만 압축해 보여주고 `operator-home`/`today-operator-console`에 연결 |
| SP-083 | Spark | completed | none | `run_minimum_unblock_flow.py` 헬퍼와 `minimum-unblock-flow.md`를 추가해 `bitcoin 승인`과 선택적 `GitHub repo 연결`을 하나의 최소 preview/apply 흐름으로 묶고, `automation-unblock-card`의 shortcut flow로 노출 |
| SP-084 | Spark | completed | none | `first_publish_operator_run.py` 재생성 결과를 현재 `bitcoin` 기준으로 정렬하고, 기존 운영 카드의 수동 예시도 `fomc` 잔재 없이 `bitcoin`/`run_minimum_unblock_flow.py` 기준으로 맞춤 |
| SP-085 | Spark | completed | none | `run_first_blogger_verify_flow.py`와 `first-blogger-verify-card`를 추가해 GitHub 연결 전에도 `bitcoin 승인 -> platform publish plan -> upload_blogger_drafts -> first_cloud_run_verification` 로컬 검증 체인을 preview/apply로 바로 실행할 수 있게 정리 |
| SP-086 | Spark | completed | none | `run_pipeline.sh`와 `prepare_launch_bundle.py`에 새 shortcut/진행 보드 산출물(`automation-progress-board`, `automation-unblock-card`, `minimum-unblock-flow`, `first-blogger-verify-card`, `first-blogger-verify-flow`)을 편입해 전체 재생성 시 누락되지 않게 정리 |
| SP-087 | Spark | completed | none | `.github/workflows/daily-investment-intake.yml`에도 같은 5개 스크립트를 추가해 로컬 파이프라인과 GitHub Actions parity를 `all_core_scripts_present=yes`, `missing_in_workflow=none` 상태로 회복 |
| SP-088 | Spark | completed | none | Binance/공개 API 코인 시장 신호를 `crypto-market-signal` 산출물로 저장하고 topic scoring/품질 게이트에 반영 |
| SP-089 | Spark | pending | none | Google Drive 플러그인으로 주간 검토 리포트 또는 키워드 보드를 내보내는 선택형 export 흐름 설계 |
| SP-090 | Spark | completed | none | 하루 200명 방문 목표 기준 `daily-traffic-goal` 산출물을 만들고 운영 홈/콘솔/워크플로우에 연결 |
| SP-091 | Spark | completed | none | 공개 URL 기반 `traffic-amplification-plan`을 추가해 발행 후 X/Threads, 텔레그램/카카오, 커뮤니티, 후속글 배포 문구와 예상 유입을 자동 생성 |
| SP-092 | Spark | completed | none | `visitor-proof-board`를 추가해 하루 200명 목표의 예상치와 Search Console 실측 증거를 분리하고 운영 홈/콘솔/워크플로우에 연결 |
| SP-093 | Spark | completed | none | Search Console fetch가 로컬 `.env`와 GitHub Actions의 기존 `GOOGLE_*` secrets를 fallback으로 사용하도록 보강하고, 접근 가능한 Search Console 사이트 목록 진단을 추가 |
| SP-094 | Spark | completed | none | `search-console-setup-card`와 `indexing-priority-pack`을 추가해 Search Console 검증 후 제출할 sitemap/URL 검사/내부링크 우선순위를 자동 생성 |
| SP-095 | Spark | pending | Search Console property verified | Search Console 속성 검증 후 `visitor-proof-board`에서 실제 클릭/노출과 200명 목표 달성 여부 재검증 |
| SP-096 | Spark | completed | none | `apply_internal_link_blocks`를 추가해 공개 URL 기반 내부링크 박스를 실제 발행 HTML에 삽입하고, 체류시간/페이지뷰 증가용 연결을 Blogger 업데이트 후보에 반영 |
| SP-097 | Spark | completed | none | `apply_popular_reads_blocks`를 추가해 공개된 후속글 URL을 메인 글 하단 인기글 박스로 삽입하고 검색 유입 후 추가 페이지뷰 동선을 강화 |
| SP-098 | Spark | completed | none | `apply_reader_share_blocks`를 추가해 공개 메인 글에 X/텔레그램/페이스북/원문 공유 버튼을 삽입하고 독자 기반 추가 유입 동선을 강화 |
| SP-099 | High | completed | none | `AGENT_OPERATING_MODEL.md`를 추가해 서브 에이전트 역할, 파일 소유권, 매일 실행 순서, 충돌 방지 규칙을 정의 |
| SP-100 | Spark/5.4 | completed | none | Growth Analyst: `search-console-fetch-report`, `visitor-proof-board`, `setup-check-report`를 읽고 Search Console/GA4 연결을 위해 사용자가 해야 할 최소 액션 1개와 재검증 명령을 정리 |
| SP-101 | Spark/5.4 | pending | SP-100 or fallback data | Growth Analyst: `data/search_console_queries.csv`가 생기면 `search_console_to_feedback.py`, `compile_performance_feedback.py`, `build_visitor_proof_board.py`를 재실행하고 `actual_verified_visitors`, top queries, mapped keywords를 보고 |
| SP-102 | Spark/5.4 | pending | none | Keyword Strategist: Search Console 실측 전에도 쓸 수 있는 제목 A/B 테스트 후보 10개를 `daily-post-brief`, `keyword-opportunity-board`, `crypto-market-signal` 기준으로 생성 |
| SP-103 | Spark/5.4 | pending | none | Draft Producer: 현재 공개 메인 글 4개의 정보량 부족 문단을 점검하고, `draft-polish-board` 또는 관련 생성 스크립트에 보강안 반영 |
| SP-104 | Spark/5.4 | completed | none | Quality Gatekeeper: `build_daily_traffic_goal.py`의 죽은 코드와 운영 리포트의 오래된 승인 문구를 정리하고 품질 게이트 13/13 pass 유지 확인 |
| SP-105 | Spark/5.4 | pending | none | Distribution Planner: 공개 URL별 외부 배포 문구를 플랫폼별 3종씩 만들고, 수동 배포 체크리스트를 `traffic-amplification-plan`에 보강 |
| SP-106 | Spark/5.4 | pending | none | Publish Inventory Agent: `publish-inventory -> manifest selection -> uploader handoff` 계약을 점검해 slug 충돌, orphan manifest, stale ready file이 0인지 자동 리포트로 확인 |
| HQ-001 | High | pending | none | public repo 공개 범위와 비공개 전환 기준 결정 |
| HQ-002 | High | pending | none | OpenAI 유료 초안 생성 활성화 시점과 비용 한도 정책 결정 |
| HQ-003 | High | pending | none | Search Console, GA4, AdSense, 뉴스레터 연결 우선순위 재정렬 |
| HQ-004 | High | pending | none | 레퍼런스 사이트 패턴을 바탕으로 허브/뉴스레터/인기글 구조 우선순위 결정 |
| HQ-005 | High | completed | none | 자동 채널은 Blogger 단일로 먼저 검증하고 WordPress는 이후 확장하는 운영 우선순위 확정 |

## Spark Execution Notes

### SP-001

- 목적: 컴퓨터가 꺼져 있어도 돌아가는 무료 자동화의 핵심 조건인 GitHub 원격 연결 마무리
- 완료 기준:
  - `git remote -v`에 origin 표시
  - 첫 push 성공
  - `outputs/latest/github-launch-plan.md` 상태 재생성 시 `repo_connected: True`

### SP-002

- 목적: 로컬 `.env`와 클라우드 실행 환경 연결
- 완료 기준:
  - 최소 필수 키 반영
  - `BLOGGER_BLOG_ID`
  - `GOOGLE_CLIENT_ID`
  - `GOOGLE_CLIENT_SECRET`
  - `GOOGLE_REFRESH_TOKEN`

### SP-003

- 목적: 클라우드에서 실제 수집/생성/업로드 흐름이 도는지 검증
- 완료 기준:
  - `Daily Investment Intake` workflow 1회 성공
  - `outputs/latest/` 산출물 갱신 확인
  - 실패 시 에러를 `HANDOFF.md`에 정리

### SP-004

- 목적: 현재 로컬 상태가 launch-ready인지 반복 확인
- 권장 명령:

```bash
python3 scripts/check_setup.py
python3 scripts/build_success_gate.py
python3 scripts/build_go_live_readiness_report.py
```

### SP-007

- 목적: 사람 같은 톤의 자동 초안까지 연결
- 완료 기준:
  - `draft-generation-report.json` 갱신
  - `human-tone-review.md` 갱신
  - `blogger-upload-report.json` 또는 관련 업로드 결과 확인
- 참고: `OPENAI_API_KEY`는 아직 없어도 템플릿 기반 초안으로 파이프라인과 업로드 흐름을 검증했습니다.

### SP-015

- 목적: 두 번째 자동 채널인 WordPress 실전 업로드 검증
- 완료 기준:
  - `WORDPRESS_SITE_URL`, `WORDPRESS_USERNAME`, `WORDPRESS_APPLICATION_PASSWORD` 입력 완료
  - `python3 scripts/upload_wordpress_drafts.py` 실행
  - `outputs/latest/wordpress-upload-report.json`에서 `credentials_missing_dry_run`이 아닌 실제 업로드 결과 확인

### SP-019

- 목적: 사용자가 탭 폭탄 없이 Blogger 우선 자동화 경로만 따라갈 수 있게 운영 문서 정리
- 완료 기준:
  - `outputs/latest/automation-scope.md` 생성
  - `outputs/latest/login-launch-checklist.md` 기본 모드에서 WordPress 페이지 제외
  - `outputs/latest/start-here-runbook.md`와 `outputs/latest/go-live-dashboard.md`에 Blogger 우선 정책 반영

### SP-020

- 목적: 사용자가 긴 검토 패킷을 다 읽지 않아도 오늘 승인할 첫 글과 다음 명령을 바로 고를 수 있게 정리
- 완료 기준:
  - `outputs/latest/first-approval-path.md` 생성
  - `fomc` 단건 승인 명령과 `fomc bitcoin` 묶음 승인 명령이 노출됨
  - `go-live-dashboard.md`와 `start-here-runbook.md`에서 해당 산출물로 이동 가능

### SP-021

- 목적: 어떤 운영 문서를 열어도 `Blogger 우선, WordPress는 2차 확장` 정책이 흔들리지 않게 일관화
- 완료 기준:
  - `outputs/latest/go-live-readiness-report.md` 다음 액션이 Blogger 우선 흐름으로 정리
  - `outputs/latest/monetization-readiness-report.md` publishing engine 설명이 Blogger 우선 기준으로 정리
  - `outputs/latest/operator-handoff.md` 필수값/연결순서가 Blogger + GitHub 중심으로 재정리

### SP-022

- 목적: 운영자가 오늘 어떤 글 순서로 올려야 수익화에 유리한지 빠르게 판단할 수 있게 정리
- 완료 기준:
  - `outputs/latest/daily-revenue-focus.md` 생성
  - `main_post -> seo_followup -> next_slot` 형태의 오늘 경로가 표시됨
  - `go-live-dashboard.md`와 `start-here-runbook.md`에서 해당 산출물로 이동 가능

### SP-023

- 목적: 발행 자동화가 붙은 뒤 수익화 확장 순서를 운영 단계로 명확히 정리
- 완료 기준:
  - `outputs/latest/monetization-roadmap.md` 생성
  - `Blogger 검증 -> 반복 발행 루프 -> GA4 -> 재방문 -> AdSense -> WordPress 확장` 단계가 드러남
  - `go-live-dashboard.md`와 `start-here-runbook.md`에서 해당 산출물로 이동 가능

### SP-024

- 목적: 첫 승인 이후 운영자가 실제 어떤 명령을 순서대로 실행해야 하는지 한 장으로 정리
- 완료 기준:
  - `outputs/latest/first-publish-operator-run.md` 생성
  - 기본 preview 모드에서 추천 승인 keyword 와 실행 명령 4개가 노출됨
  - `go-live-dashboard.md`에서 해당 실행 카드가 바로 보임

### SP-025

- 목적: 사용자가 긴 리뷰 패킷 대신 실제로 확인할 글 2~3개만 빠르게 읽을 수 있게 정리
- 완료 기준:
  - `outputs/latest/user-review-shortlist.md` 생성
  - 현재 우선 검토 글의 제목, 요약, 승인 명령이 압축 표시됨
  - `go-live-dashboard.md`에서 해당 축약본 존재를 확인 가능

### SP-026

- 목적: 오늘 운영에 필요한 핵심 상태와 실행 흐름을 한 장으로 통합
- 완료 기준:
  - `outputs/latest/today-operator-console.md` 생성
  - 읽을 글, 승인 명령, 승인 후 실행 명령, 수익화 경로, 다음 단계가 함께 표시됨
  - 사실상 운영자가 오늘 가장 먼저 열 문서 역할을 할 수 있어야 함

### SP-027

- 목적: 오래된 셋업 로그 묶음 대신 자동화 적합 상태만 빠르게 확인하는 런치 번들 리포트로 교체
- 완료 기준:
  - `python3 scripts/prepare_launch_bundle.py` 실행 시 최신 자동화 카드들이 재생성됨
  - `outputs/latest/launch-bundle-report.md`에 자동 채널, blocker, 승인 후보, 승인 후 명령이 요약됨
  - 로그인/OAuth 탭 열기 같은 수동 셋업 단계가 기본 번들 흐름에서 제거됨

### SP-028

- 목적: 사용자가 실제 업로드 전 글의 렌더링 결과를 빠르게 읽고 승인할 수 있는 검토 보드 추가
- 완료 기준:
  - `python3 scripts/build_review_preview_board.py` 실행 시 HTML 검토 보드가 생성됨
  - `outputs/latest/review-preview-board.html`에서 shortlist 글의 실제 렌더링과 요약을 함께 볼 수 있음
  - `run_pipeline.sh`, `start-here-runbook.md`, `today-operator-console.md`, `launch-bundle-report.md`에서 해당 보드 접근 경로가 드러남

### SP-029

- 목적: 여러 운영 문서를 넘나들지 않고도 오늘 필요한 상태와 액션을 단일 첫 화면에서 볼 수 있게 정리
- 완료 기준:
  - `python3 scripts/build_operator_home.py` 실행 시 HTML 운영 홈이 생성됨
  - `outputs/latest/operator-home.html`에서 blocker, 승인 명령, shortlist, 채널 상태, review board 가 한 장에 표시됨
  - `run_pipeline.sh`, `start-here-runbook.md`, `launch-bundle-report.md`에서 해당 홈 접근 경로가 드러남

### SP-030

- 목적: 조회수 잘 나오는 투자/코인 매체의 구조적 강점을 자동 글 생성 규칙에 직접 반영
- 완료 기준:
  - `config/current_editorial_reference_patterns.json` 추가
  - `scripts/build_current_reference_strategy.py`로 운영 문서 생성
  - `build_draft_packets.py`와 `templates/investment_blog_draft_prompt.md`가 해당 패턴을 입력 패킷과 프롬프트에 반영
  - `run_pipeline.sh`, `start-here-runbook.md`, `launch-bundle-report.md`에서 새 전략 문서 접근 경로가 드러남

### SP-031

- 목적: 검색 수요를 실제 글 타입 결정까지 연결해 운영자가 키워드-패턴 매핑을 바로 볼 수 있게 정리
- 완료 기준:
  - `python3 scripts/build_keyword_capture_strategy.py` 실행 시 전략 카드가 생성됨
  - `outputs/latest/keyword-capture-strategy.md`에 키워드별 `pattern_name`, `capture_route`, `route_description`이 표시됨
  - `run_pipeline.sh`, `start-here-runbook.md`, `launch-bundle-report.md`에서 해당 문서 접근 경로가 드러남

### SP-032

- 목적: 발행 직전 글 품질을 자동으로 걸러내어 검색/신뢰/수익화에 불리한 누락을 빨리 잡기
- 완료 기준:
  - `python3 scripts/build_pre_publish_quality_gate.py` 실행 시 품질 게이트 리포트가 생성됨
  - `outputs/latest/pre-publish-quality-gate.md`에 글별 status 와 세부 체크 결과가 표시됨
  - `run_pipeline.sh`, `start-here-runbook.md`, `launch-bundle-report.md`, `operator-home`에서 해당 게이트가 드러남

### SP-033

- 목적: 업로드 실행 단계에서 `pre-publish-quality-gate`를 추가로 준수해 `needs_fix`/`review_before_publish` 글은 실전 업로드 후보에서 제외
- 완료 기준:
  - `python3 scripts/upload_blogger_drafts.py` 실행 시 품질 게이트 미달 글이 `pre_publish_quality_gate_review` 또는 `pre_publish_quality_gate_needs_fix` 사유로 차단됨
  - `python3 scripts/upload_wordpress_drafts.py`도 동일 사유로 차단되며, 준비된 채널에서 동일한 기준으로 일관 적용됨

### SP-034

- 목적: 플랫폼 게시 플랜에서 `platform-publish-plan`도 품질 게이트 `pass`와 완전히 정합되도록 정리
- 완료 기준:
  - `python3 scripts/build_platform_publish_plan.py` 실행 시 `quality_ready_count`가 생성되고 `ready_item_count`와 1차 후보 리스트가 품질 패스 항목만 반영됨
  - 업로드 후보 노출 시 `quality= True`인 항목만 `ready_item_count` 집계에 반영됨

### SP-035

- 목적: 현재 단계에서 중요하지 않은 옵션을 뒤로 보내고 운영자가 `다음 한 단계`만 보도록 운영 홈과 로그인 흐름 단순화
- 완료 기준:
  - `outputs/latest/login-launch-checklist.md`에 `Minimum Go-Live Path`가 별도로 표시됨
  - repo 미연결 상태에서는 `GitHub repository or new repo`만 최소 페이지로 먼저 보임
  - `outputs/latest/operator-home.md`에 `Single Next Action`과 `Later Improvements`가 분리 표시됨

### SP-036

- 목적: GitHub 연결 단계에서 긴 remote URL 복붙 대신 `OWNER/REPO`만 넣어도 되도록 마찰 최소화
- 완료 기준:
  - `scripts/bootstrap_github_remote.sh`가 `OWNER/REPO`, `https`, `git@` 입력을 모두 허용
  - 운영 문서와 생성 리포트의 추천 명령이 `<OWNER/REPO>` 기준으로 통일됨

### SP-037

- 목적: 블로그 글마다 사용 가능한 안전 이미지 1~2장을 추천하고 라이선스/검색 링크를 함께 남겨 이미지 운영을 자동화 친화적으로 정리
- 완료 기준:
  - `publishing-assets`와 `seo-publishing-assets`에 `image_plan`이 생성됨
  - `review-packet`과 `review-preview-board`에서 이미지 추천과 라이선스 링크를 함께 확인 가능
  - `safe-image-suggestions.md`가 생성되어 운영자가 한 장으로 이미지 후보를 검토할 수 있음

### SP-038

- 목적: 운영자가 고른 이미지 URL/출처를 별도 승인 파일에 기록하면 최종 HTML과 발행 draft에 자동 반영되도록 연결
- 완료 기준:
  - `scripts/set_image_selection.py`로 keyword/slot별 선택값을 저장할 수 있음
  - `render_publish_ready_posts.py`가 `image-selections.json`을 읽어 manifest와 HTML에 반영함
  - 검토 문서에 이미지 적용 helper 명령이 함께 표시됨

### SP-039

- 목적: 재방문과 나중 구독 전환을 위한 CTA 운영 카드를 실제 산출물로 생성하고 운영 홈/콘솔/런북/워크플로우에서 바로 열 수 있게 연결
- 완료 기준:
  - `outputs/latest/retention-cta-board.md`와 `.json`이 생성됨
  - `today-operator-console`, `operator-home`, `start-here-runbook`, `launch-bundle-report`에 링크가 노출됨
  - `pipeline-workflow-parity.md` 기준 로컬/워크플로우 단계 수와 순서가 그대로 정합함

### SP-040

- 목적: `retention-cta-board` 내용을 실제 publish-ready HTML에 반영해 글 하단 CTA가 generic 문구가 아니라 사람다운 재방문 유도 문구로 렌더되게 만들기
- 완료 기준:
  - `render_publish_ready_posts.py`가 `retention-cta-board.json`을 읽음
  - 메인 글과 SEO 후속 글 HTML에 `post-retention-cta` 섹션이 생성됨
  - 기존 사용자 승인/업로드 차단 상태는 그대로 유지되고 `cloud-launch-preflight.md`의 승인 안전 상태가 변하지 않음

### SP-041

- 목적: 사용자 검토 화면에서도 최종 발행본에 들어갈 retention CTA를 함께 보여줘서 승인 전에 실제 발행 톤을 더 정확히 확인하게 만들기
- 완료 기준:
  - `review-packet.md`, `review-preview-board.md/html`, `full-draft-review-sheet.md`에 `final retention CTA`와 `later revisit CTA`가 노출됨
  - `review-preview-board.json` 카드에 `retention_cta_enabled`, `retention_cta`가 포함됨
  - 사용자 승인 안전 가드(`review-approvals.json` empty state)는 바뀌지 않음

### SP-042

- 목적: 사용자가 실제로 가장 먼저 보게 되는 `current-review-focus`, `user-approval-inbox`, `user-review-checkpoint`에도 최종 retention CTA를 노출해 승인 직전 검토 흐름 전체를 일관화
- 완료 기준:
  - 세 산출물의 md/html/json에 `retention_cta_enabled`, `retention_cta` 또는 `final retention CTA` 문구가 반영됨
  - `user-review-checkpoint`에서 최우선 글의 최종 CTA를 승인 전에 바로 읽을 수 있음
  - 업로드 차단 상태와 승인 파일 빈 기본값은 그대로 유지됨

### SP-043

- 상태: 완료
- 목적: Blogger에 표시되는 글 제목과 메타 제목이 본문 H1보다 약한 `~해설` 제목으로 남는 문제를 제거해 검색 클릭률 기반을 개선
- 완료 기준:
  - `scripts/sync_click_titles_from_html.py`가 `publish-inventory.json`의 메인 글 manifest만 대상으로 HTML H1을 `title`/`meta_title`에 동기화함
  - `run_pipeline.sh`와 `.github/workflows/daily-investment-intake.yml`에서 `Build publish inventory` 직후 자동 실행됨
  - `outputs/latest/click-title-sync-report.md/json`이 생성되고 `operator-home`, `today-operator-console`에서 바로 확인 가능
  - 검증 결과 메인 글 4개 제목이 클릭형 H1로 동기화됨

### SP-044

- 상태: 완료
- 목적: 신규 초안 후보 자체가 처음부터 검색 클릭형 제목과 현재 코인 시장 신호를 반영하도록 개선
- 완료 기준:
  - `scripts/score_daily_topics.py`의 기본 제목이 `~해설`이 아니라 질문/체크포인트형 제목으로 생성됨
  - `scripts/generate_blog_drafts.py`에서 미국 증시 계열 제목 부제가 중복으로 붙지 않음
  - `scripts/build_daily_traffic_goal.py`가 `publish-inventory.json`의 실제 발행 제목과 `crypto-market-signal.json`의 시장 신호를 함께 표시함
  - 검증 결과 `daily-post-brief`, `publish-inventory`, `daily-traffic-goal`의 대표 4개 제목이 클릭형으로 정렬되고 품질 게이트 `needs_fix_count=0`

### SP-045

- 상태: 완료
- 목적: 제목 개선으로 slug가 바뀌어 기존 글 대신 새 중복 글이 발행되는 문제를 방지
- 완료 기준:
  - 메인 글 4개는 `generate_publishing_assets.py`에서 keyword별 안정 slug를 사용함
  - SEO 후속 글은 메인 글 slug와 충돌하지 않는 안정 토픽 기반 slug를 사용함
  - `upload_blogger_drafts.py`는 기본적으로 `publish-inventory.json` 후보만 업로드하고, orphan manifest는 `BLOGGER_INCLUDE_ORPHAN_MANIFESTS=true`일 때만 포함함
  - 업로드 후보 13개의 slug 충돌이 0개이고, publish-ready/seo-publish-ready의 stale 파일이 0개로 정리됨

### SP-046

- 상태: 완료
- 목적: 실수로 생성된 Blogger 중복 글을 로컬 자격증명 없이도 GitHub Actions에서 안전하게 정리할 수 있게 만들기
- 완료 기준:
  - `scripts/cleanup_blogger_posts.py`가 `BLOGGER_CLEANUP_POST_IDS`에 지정된 post_id만 삭제함
  - `.github/workflows/daily-investment-intake.yml`의 수동 실행 입력 `cleanup_duplicate_post_ids`가 비어 있으면 평소 자동 실행에는 아무 삭제도 하지 않음
  - 빈 입력 로컬 검증에서 `deleted_count=0`으로 종료됨
  - 다음 수동 실행에서 FOMC 중복 post_id `1530213910086239357`만 지정해 정리 가능

## Backlog For Later

- Spark가 로컬 실행 결과를 모아 간단한 `verification summary`만 갱신하는 자동 보고 루틴 추가
- GitHub Actions 실패 케이스를 재실행하기 위한 troubleshooting 문서 초안화
- OpenAI 비활성 상태에서도 fallback 원고 품질을 비교하는 샘플 세트 정리
- Search Console 연결 전후로 `weak-trend fallback`이 어떤 키워드를 얼마나 보정하는지 비교 리포트 추가
