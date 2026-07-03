# Keyword Capture Strategy

현재 잡힌 키워드를 어떤 글 타입과 내부링크 경로로 받아먹을지 정리한 운영 카드입니다.

- generated_at: `2026-07-03T17:04:22.861631+00:00`

## 1. fomc

- recommended_title: FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지
- pattern_name: `news_what_it_means`
- capture_route: `breaking_to_evergreen`
- route_description: 당일 해설 글로 유입을 먼저 받고, 바로 evergreen 설명글과 FAQ형 후속 글로 내부링크를 넘깁니다.
- demand_signal_score: `4200`
- search_intent_angle: 공식 소스 기반 확인 가능, 복수 소스 교차 확인 가능 (4개), 거시 해설형 글로 전환 가치 높음
- pattern_must_have:
  - 무슨 일이 있었는지 1문단 요약
  - 왜 시장이 반응하는지 해석
  - 주식, 달러, 금리, 코인 중 최소 2개와 연결
  - 지금 단정할 수 없는 변수도 함께 표기
- recommended_outline:
  - 왜 지금 이 이슈가 중요한가
  - 실제로 발표되거나 벌어진 일
  - 주식·코인·달러·금리에 주는 영향
  - 앞으로 체크할 변수
  - 개인 투자자가 볼 포인트
- sources:
  - CNBC Top News
  - CoinDesk RSS
  - Federal Reserve Monetary Policy Press
  - Financial Times World

## 2. bitcoin

- recommended_title: 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트
- pattern_name: `news_what_it_means`
- capture_route: `breaking_to_evergreen`
- route_description: 당일 해설 글로 유입을 먼저 받고, 바로 evergreen 설명글과 FAQ형 후속 글로 내부링크를 넘깁니다.
- demand_signal_score: `6900`
- search_intent_angle: 복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (extreme_fear)
- pattern_must_have:
  - 무슨 일이 있었는지 1문단 요약
  - 왜 시장이 반응하는지 해석
  - 주식, 달러, 금리, 코인 중 최소 2개와 연결
  - 지금 단정할 수 없는 변수도 함께 표기
- recommended_outline:
  - 오늘 코인 시장 핵심 변화
  - 가격이 아니라 구조상 중요한 포인트
  - ETF/유동성/규제/온체인과의 연결
  - 강세 시나리오와 리스크
  - 내일 확인할 체크포인트
- sources:
  - CoinDesk RSS
  - Cointelegraph
  - Investing.com Crypto News

## 3. ai_semiconductors

- recommended_title: AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지
- pattern_name: `search_explainer`
- capture_route: `sector_hub_to_followups`
- route_description: 섹터 메인 해설 글을 허브로 두고 대표 종목, 공급망, ETF/지수 후속 글로 퍼뜨립니다.
- demand_signal_score: `2000`
- search_intent_angle: 섹터/세계 흐름 연결 해설 가능
- pattern_must_have:
  - 제목에서 핵심 키워드와 독자 질문을 함께 드러낼 것
  - 도입 3문장 안에 왜 지금 읽어야 하는지 답할 것
  - 본문 중간에 초보자용 정의 또는 기준점 1개 포함
  - 끝부분에 다음 체크포인트와 내부링크 연결
- recommended_outline:
  - 지금 이 섹터가 왜 움직이는가
  - 핵심 뉴스와 시장 반응
  - 대표 종목과 자금 흐름
  - 거시 변수와 연결
  - 다음 실적/정책 이벤트
- sources:
  - CoinDesk RSS

## 4. oil

- recommended_title: 유가 상승이 물가와 증시에 번지는 경로: 투자자가 볼 3가지
- pattern_name: `search_explainer`
- capture_route: `search_entry_to_internal_links`
- route_description: 검색형 진입 글에서 정의와 기준점을 설명한 뒤 관련 허브 글로 내부링크를 넘깁니다.
- demand_signal_score: `1200`
- trend_queries: 유조선
- search_intent_angle: 검색 트렌드 반응 존재, 복수 소스 교차 확인 가능 (2개), 거시 해설형 글로 전환 가치 높음, 실제 급상승 검색어 반영 (유조선)
- pattern_must_have:
  - 제목에서 핵심 키워드와 독자 질문을 함께 드러낼 것
  - 도입 3문장 안에 왜 지금 읽어야 하는지 답할 것
  - 본문 중간에 초보자용 정의 또는 기준점 1개 포함
  - 끝부분에 다음 체크포인트와 내부링크 연결
- recommended_outline:
  - 왜 지금 이 이슈가 중요한가
  - 실제로 발표되거나 벌어진 일
  - 주식·코인·달러·금리에 주는 영향
  - 앞으로 체크할 변수
  - 개인 투자자가 볼 포인트
- sources:
  - Financial Times YouTube
  - Google Trends KR

## 5. ai_growth_stocks

- recommended_title: AI 성장주를 볼 때 놓치기 쉬운 리스크: 매출 성장과 금리 부담
- pattern_name: `search_explainer`
- capture_route: `sector_hub_to_followups`
- route_description: 섹터 메인 해설 글을 허브로 두고 대표 종목, 공급망, ETF/지수 후속 글로 퍼뜨립니다.
- demand_signal_score: `0`
- search_intent_angle: 복수 소스 교차 확인 가능 (2개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능
- pattern_must_have:
  - 제목에서 핵심 키워드와 독자 질문을 함께 드러낼 것
  - 도입 3문장 안에 왜 지금 읽어야 하는지 답할 것
  - 본문 중간에 초보자용 정의 또는 기준점 1개 포함
  - 끝부분에 다음 체크포인트와 내부링크 연결
- recommended_outline:
  - 지금 이 섹터가 왜 움직이는가
  - 핵심 뉴스와 시장 반응
  - 대표 종목과 자금 흐름
  - 거시 변수와 연결
  - 다음 실적/정책 이벤트
- sources:
  - Financial Times World
  - 무역킹 Trade King YouTube
