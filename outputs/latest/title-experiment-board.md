# Title Experiment Board

검색 클릭률을 높이기 위한 제목 A/B 후보 보드입니다.

- status: `ready_for_manual_title_ab_testing`
- measurement_note: Search Console 연결 전에는 실제 CTR 검증이 불가하므로, 검색 의도 기반 후보를 준비합니다.
- crypto_market_sentiment: `extreme_fear`

## Next Actions

- Search Console 연결 전에는 추천 제목을 배포 문구와 내부링크 앵커에 우선 사용합니다.
- Search Console 연결 후 노출은 높고 CTR이 낮은 글부터 recommended_title로 교체 테스트합니다.
- 급등/매수 유도형 제목은 제외하고 체크포인트/이유/자금 흐름 중심으로 테스트합니다.

## 1. fomc

- lane: `macro`
- current_title: FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지
- recommended_title: FOMC 이후 시장 체크포인트 3가지: 금리, 달러, 위험자산
- recommended_angle: `macro-link`
- demand_signal_score: `3200`
- public_url: https://gimu-economy-insight.blogspot.com/2026/06/fomc.html

### Variants

- `fomc-v4` score `90` angle `macro-link`: FOMC 이후 시장 체크포인트 3가지: 금리, 달러, 위험자산
  - why: 독자가 글에서 얻을 정보를 제목에서 바로 알 수 있습니다.
- `fomc-v1` score `78` angle `checklist`: FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지
  - why: 독자가 글에서 얻을 정보를 제목에서 바로 알 수 있습니다.
- `fomc-v3` score `78` angle `checklist`: FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지: 주식·코인 흐름 함께 보기
  - why: 독자가 글에서 얻을 정보를 제목에서 바로 알 수 있습니다.
- `fomc-v2` score `78` angle `checklist`: FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지: 지금 시장이 반응하는 이유
  - why: 독자가 글에서 얻을 정보를 제목에서 바로 알 수 있습니다.
- `fomc-v6` score `70` angle `explainer`: FOMC 이후 투자자가 오늘 확인할 숫자들
  - why: 현재 주제를 설명형 검색어로 받아내기 위한 후보입니다.

## 2. bitcoin

- lane: `crypto`
- current_title: 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트
- recommended_title: 비트코인 가격보다 먼저 볼 것: ETF 자금과 달러 흐름
- recommended_angle: `fund-flow`
- demand_signal_score: `6800`
- public_url: https://gimu-economy-insight.blogspot.com/2026/06/blog-post.html

### Variants

- `bitcoin-v3` score `97` angle `fund-flow`: 비트코인 가격보다 먼저 볼 것: ETF 자금과 달러 흐름
  - why: 공포 구간에서는 가격 예측보다 자금 흐름과 리스크 확인형 제목이 클릭 의도에 더 맞습니다.
- `bitcoin-v1` score `97` angle `fund-flow`: 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트
  - why: 공포 구간에서는 가격 예측보다 자금 흐름과 리스크 확인형 제목이 클릭 의도에 더 맞습니다.
- `bitcoin-v2` score `97` angle `fund-flow`: 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트: 지금 시장이 반응하는 이유
  - why: 공포 구간에서는 가격 예측보다 자금 흐름과 리스크 확인형 제목이 클릭 의도에 더 맞습니다.
- `bitcoin-v4` score `93` angle `risk-check`: 비트코인, 공포 구간에서 확인할 리스크 체크포인트 5가지
  - why: 공포 구간에서는 가격 예측보다 자금 흐름과 리스크 확인형 제목이 클릭 의도에 더 맞습니다.
- `bitcoin-v5` score `70` angle `fund-flow`: 비트코인 투자자가 오늘 놓치면 안 되는 규제와 자금 흐름
  - why: 공포 구간에서는 가격 예측보다 자금 흐름과 리스크 확인형 제목이 클릭 의도에 더 맞습니다.

## 3. ai_semiconductors

- lane: `us-stocks`
- current_title: AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지
- recommended_title: AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지
- recommended_angle: `stock-market`
- demand_signal_score: `2300`
- public_url: `missing`

### Variants

- `ai_semiconductors-v1` score `85` angle `stock-market`: AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지
  - why: 독자가 글에서 얻을 정보를 제목에서 바로 알 수 있습니다.
- `ai_semiconductors-v3` score `85` angle `stock-market`: AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지: 주식·코인 흐름 함께 보기
  - why: 독자가 글에서 얻을 정보를 제목에서 바로 알 수 있습니다.
- `ai_semiconductors-v2` score `85` angle `stock-market`: AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지: 지금 시장이 반응하는 이유
  - why: 독자가 글에서 얻을 정보를 제목에서 바로 알 수 있습니다.
- `ai_semiconductors-v4` score `77` angle `stock-market`: AI 반도체 주가를 볼 때 실적보다 먼저 확, 나스닥과 빅테크가 같이 움직이는 이유
  - why: 뉴스를 이미 본 독자가 시장 반응의 이유를 확인하려는 검색 의도에 맞습니다.
- `ai_semiconductors-v5` score `77` angle `macro-link`: AI 반도체 주가를 볼 때 실적보다 먼저 확 체크포인트: 금리, 실적, 섹터 폭을 같이 봐야 하는 이유
  - why: 독자가 글에서 얻을 정보를 제목에서 바로 알 수 있습니다.

## 4. tariffs_trade

- lane: `world-flow`
- current_title: 관세와 무역 갈등이 증시에 미치는 영향: 환율과 공급망까지 보기
- recommended_title: 관세와 무역 갈등이 증시에 미치는 영향, 환율과 원자재까지 같이 봐야 하는 이유
- recommended_angle: `macro-link`
- demand_signal_score: `0`
- public_url: `missing`

### Variants

- `tariffs_trade-v3` score `77` angle `macro-link`: 관세와 무역 갈등이 증시에 미치는 영향, 환율과 원자재까지 같이 봐야 하는 이유
  - why: 뉴스를 이미 본 독자가 시장 반응의 이유를 확인하려는 검색 의도에 맞습니다.
- `tariffs_trade-v2` score `77` angle `macro-link`: 관세와 무역 갈등이 증시에 미치는 영향: 환율과 공급망까지 보기: 지금 시장이 반응하는 이유
  - why: 뉴스를 이미 본 독자가 시장 반응의 이유를 확인하려는 검색 의도에 맞습니다.
- `tariffs_trade-v5` score `70` angle `macro-link`: 관세와 무역 갈등이 증시에 미치는 영향 핵심 변수 3가지: 경기부양, 환율, 수요
  - why: 독자가 글에서 얻을 정보를 제목에서 바로 알 수 있습니다.
- `tariffs_trade-v1` score `62` angle `macro-link`: 관세와 무역 갈등이 증시에 미치는 영향: 환율과 공급망까지 보기
  - why: 현재 주제를 설명형 검색어로 받아내기 위한 후보입니다.
- `tariffs_trade-v4` score `50` angle `explainer`: 관세와 무역 갈등이 증시에 미치는 영향이 시장에 번지는 경로: 주식, 코인, 원자재 체크
  - why: 현재 주제를 설명형 검색어로 받아내기 위한 후보입니다.

## 5. oil

- lane: `macro`
- current_title: 유가 상승이 물가와 증시에 번지는 경로: 투자자가 볼 3가지
- recommended_title: 유가 상승이 물가와 증시에 번지는 경로 체크포인트 3가지: 금리, 달러, 위험자산
- recommended_angle: `macro-link`
- demand_signal_score: `2600`
- public_url: `missing`

### Variants

- `oil-v4` score `85` angle `macro-link`: 유가 상승이 물가와 증시에 번지는 경로 체크포인트 3가지: 금리, 달러, 위험자산
  - why: 독자가 글에서 얻을 정보를 제목에서 바로 알 수 있습니다.
- `oil-v2` score `73` angle `checklist`: 유가 상승이 물가와 증시에 번지는 경로: 투자자가 볼 3가지: 지금 시장이 반응하는 이유
  - why: 독자가 글에서 얻을 정보를 제목에서 바로 알 수 있습니다.
- `oil-v3` score `65` angle `explainer`: 유가 상승이 물가와 증시에 번지는 경로, 지금 주식과 코인이 같이 흔들리는 이유
  - why: 뉴스를 이미 본 독자가 시장 반응의 이유를 확인하려는 검색 의도에 맞습니다.
- `oil-v5` score `65` angle `explainer`: 유가 상승이 물가와 증시에 번지는 경로을 투자자가 봐야 하는 이유: 오늘 확인할 숫자들
  - why: 뉴스를 이미 본 독자가 시장 반응의 이유를 확인하려는 검색 의도에 맞습니다.
- `oil-v1` score `58` angle `checklist`: 유가 상승이 물가와 증시에 번지는 경로: 투자자가 볼 3가지
  - why: 독자가 글에서 얻을 정보를 제목에서 바로 알 수 있습니다.
