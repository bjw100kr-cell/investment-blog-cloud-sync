# Model Efficiency Policy

프로젝트의 목표는 최대한 적은 크레딧으로 최대한 많은 작업을 수행하는 것입니다.

이 저장소에서는 모델 역할을 아래처럼 분리합니다.

## High-Performance Models

대상:

- `GPT-5.5`
- `GPT-5.4`
- 그와 동급의 상위 모델 세션

담당:

- 설계
- 아키텍처
- 복잡한 디버깅
- 코드 리뷰
- 중요한 의사결정
- Spark가 실행할 수 있는 `Task Queue` 생성과 우선순위 조정

운영 규칙:

- 상위 모델은 직접 반복 작업을 오래 수행하기보다, Spark가 처리할 일을 최대한 잘게 나눠 `TASK_QUEUE.md`에 저장합니다.
- 중요한 분기점, 외부 의존성, 리스크, 다음 의사결정 포인트는 반드시 `HANDOFF.md`에 정리합니다.
- 설계 변경이 생기면 `TASK_QUEUE.md`와 `HANDOFF.md`를 함께 갱신합니다.

## Spark Models

대상:

- `GPT-5.3 Spark`
- 그와 유사한 경량 실행 모델

예외:

- Spark 크레딧이 없을 때는 `GPT-5.4`가 Spark 역할을 대행합니다.
- 이 경우에도 `GPT-5.4`는 Spark 모드로 동작하며, `TASK_QUEUE.md`에 있는 실행 작업만 처리합니다.
- Spark 대행 중인 `GPT-5.4`는 새로운 아키텍처 제안이나 중요한 우선순위 변경을 하지 않습니다.

담당:

- TODO 수행
- 단순 구현
- 문서 작성
- 테스트
- 리팩토링
- CSS/UI 수정
- 반복 작업

운영 규칙:

- Spark는 `TASK_QUEUE.md`에 이미 정의된 작업만 수행합니다.
- 새로운 아키텍처 제안, 중요한 우선순위 변경, 비용 구조 변경, 외부 연동 전략 변경은 스스로 결정하지 않습니다.
- 작업 완료 후 `TASK_QUEUE.md` 상태를 갱신하고, 다음 상위 모델 세션이 바로 이어받을 수 있게 `HANDOFF.md`에 실행 결과를 남깁니다.

## Canonical Files

- 정책 원문: `MODEL_EFFICIENCY_POLICY.md`
- 실행 큐: `TASK_QUEUE.md`
- 다음 상위 모델 세션용 인계 문서: `HANDOFF.md`

## Session Rule

모든 세션은 종료 전에 아래를 확인합니다.

1. `TASK_QUEUE.md`가 최신 상태인가
2. `HANDOFF.md`가 다음 상위 모델 세션 기준으로 이해 가능하게 정리되어 있는가
3. Spark가 처리할 수 있는 작업을 충분히 큐에 쪼개 넣었는가
