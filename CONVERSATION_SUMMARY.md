# 대화 및 작업 요약 (자동 압축)

생성일: 2026-07-01 07:13:25 KST

## 목표
- 주식/코인/세계경제 투자 블로그 자동화 운영 지속 및 수익화

## 현재 상태
- 저장된 published 수: `14`
- 최신 업로드 처리 건수(processed_count): `1`
- 마지막 동기화 시각: `2026-06-30T22:06:20.649965+00:00`
- 최근 소스 후보 수: `13`
- 핵심 체크 통과 여부: `True`
- 승인 상태 안전성: `None`
- 승인 키워드: `bitcoin`

## 다음 우선순위
- 0. 제목 클릭률 개선 반영 사항 확인:
- `scripts/sync_click_titles_from_html.py`가 추가되어 `publish-inventory.json`의 메인 글 manifest만 대상으로 HTML H1을 `title`/`meta_title`에 동기화.
- 로컬/클라우드 파이프라인 모두 `Build publish inventory` 직후 해당 단계를 실행.
- 최신 검증에서 메인 글 4개가 모두 개선됨: `manifest_changed_count=4`, `inventory_changed_count=4`.
- 현재 Blogger 1순위 후보 `bitcoin` 제목은 `비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트`.
- 신규 개선: `score_daily_topics.py` 기본 제목도 클릭형으로 교체했고, `generate_blog_drafts.py`의 미국 증시 제목 부제 중복 버그를 제거.

## 확인용 명령
- `python3 scripts/emit_context_checkpoint.py`
- `python3 scripts/run_pipeline.sh`
- `python3 scripts/prepare_launch_bundle.py`

- 최근 노트: `stable slugs and orphan manifest upload guard added`
