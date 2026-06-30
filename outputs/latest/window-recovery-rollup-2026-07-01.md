# 창 복구 롤업 (2026-07-01)

## 핵심 목표
- 주식/코인/세계경제 투자 블로그를 사람 같은 톤으로 매일 운영 가능한 자동화 시스템으로 구축하고
  수익화(1차는 Blogger, 2차는 WordPress 확장) 체계로 전개한다.

## 지금까지 진행 요약
- 사용자 요청대로 YouTube/해외뉴스/코인데스크/무역킹 등의 자료 수집, 키워드 우선화, 인간적인 톤, 다중 플랫폼 전략, 무료 자동화, 일일 포스팅을 반복적으로 정렬.
- 오버플로우 우려로 `CONTEXT_PROTOCOL.md`, `HANDOFF.md`, `CONVERSATION_SUMMARY.md`, `TASK_QUEUE.md`,
  `outputs/latest/context_checkpoint.*`, `outputs/latest/session_memos/*`를 SSOT(단일 진실원)로 고정.
- GitHub 액션 연동은 여전히 `repo_connected=false`로 확인되어 `https://github.com/new`에서 저장소 생성 후
  시크릿/변수 등록이 남아 있음.
- 로컬 파이프라인은 Blogger 업로드/검증 경로 기준으로 실행되며, 최근 `pipeline-finished` 상태와 함께
  업로드된 총본 수(`published_count`)를 기준으로 동작함.
- 컨텍스트 복구용 체크포인트를 여러 차례 강제 실행했으며, 최근 상태는
  `bash scripts/refresh_context_window.sh "post-summary-guard"`로 갱신 완료.
- 최근 상태에서 `next actions`는 GitHub 저장소 생성/연결 후 `Daily Investment Intake` 수동 1회 실행, 
  그 후 `blogger-upload-report`, `first-cloud-run-verification` 재확인이다.

## 저장 위치(이번 세션 이후 바로 이어가기용)
- `/work/investment-blog-cloud-sync/CONVERSATION_SUMMARY.md`
- `/work/investment-blog-cloud-sync/HANDOFF.md`
- `/work/investment-blog-cloud-sync/TASK_QUEUE.md`
- `/work/investment-blog-cloud-sync/outputs/latest/context_checkpoint.md`
- `/work/investment-blog-cloud-sync/outputs/latest/session_memos/session_memories.md`

## 불필요 항목 처리 원칙
- 대화 원문 전체 삭제는 불가(플랫폼 히스토리는 영속).
- 대신 다음 4개만 읽고 재개하고, 매 큰 단계 전후에 체크포인트 저장으로 오버플로우를 방지.
- `outputs/latest/session_memos/session_memories.md|jsonl`는 요약만 유지되도록 계속 압축/정리.

## 다음 재개용 즉시 명령
- `cd /Users/bjw100kr/Documents/Codex/2026-06-25/https-youtu-be-bec7hkseki-si-ehsln/work/investment-blog-cloud-sync`
- `bash scripts/refresh_context_window.sh "handoff"`
- `python3 scripts/open_login_setup_pages.py --print-next`
- `bash scripts/prepare_github_web_launch_checklist.py`
