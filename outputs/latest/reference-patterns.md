# Reference Patterns

조회수와 재방문이 잘 나오는 투자/경제/코인 레퍼런스 사이트를 참고해, 이 프로젝트에 바로 적용할 핵심 패턴을 정리한 문서입니다.

## Reference Set

- CoinDesk
  - https://www.coindesk.com/
  - https://www.similarweb.com/website/coindesk.com/
- A Wealth of Common Sense
  - https://awealthofcommonsense.com/
- Of Dollars and Data
  - https://ofdollarsanddata.com/
  - https://ofdollarsanddata.com/newsletter/
- J.P. Morgan Insights
  - https://www.jpmorgan.com/insights/markets-and-economy

## What These Sites Do Well

### CoinDesk

- 실시간성 높은 키워드와 가격 관심사를 전면에 둡니다.
- 뉴스만이 아니라 `analysis`, `video`, `live price`를 함께 묶어 한 이슈를 여러 포맷으로 소비하게 만듭니다.
- Similarweb 기준 공개 추정치에서 direct traffic 비중이 높고, organic search도 강합니다.
- 시사점:
  - 속보형 주제는 제목부터 검색 의도와 시장 반응을 바로 잡아야 합니다.
  - 메인 글에서 FAQ, 후속 글, 가격/ETF/규제 연결 링크까지 이어지는 구조가 필요합니다.

### A Wealth of Common Sense

- 작성자 신뢰가 매우 선명합니다.
- 카테고리 구조가 잘 보이고, 뉴스레터 구독 CTA가 강합니다.
- 시장 뉴스뿐 아니라 투자 심리, 자산배분, 현재 시장 같은 큰 카테고리로 오래 읽히는 글을 축적합니다.
- 시사점:
  - 블로그는 단발 뉴스보다 카테고리 허브와 뉴스레터형 재방문 장치를 가져가야 합니다.
  - 작성자/운영 주체/면책문구/카테고리 탐색이 항상 보여야 신뢰가 쌓입니다.

### Of Dollars and Data

- 복잡한 내용을 데이터 해석형 설명으로 바꿉니다.
- 검색용 낚시 제목보다 `생각을 정리해 주는 한 문장`이 강합니다.
- 뉴스레터와 인기 글 아카이브가 잘 연결되어 재방문 구조가 만들어져 있습니다.
- 시사점:
  - 우리 글도 단순 뉴스 요약보다 `왜 중요한지`, `내 돈 관점에서 어떻게 봐야 하는지`를 먼저 설명해야 합니다.
  - 인기 FAQ/초보 가이드/핵심 구조 글을 장기 검색 유입용으로 계속 누적해야 합니다.

### J.P. Morgan Insights

- `markets and economy`라는 대분류 아래에서 매크로와 시장을 명확히 묶습니다.
- 경제 지표, 시장 움직임, 투자 영향 해석을 연결해 독자가 다음 행동 포인트를 이해하게 만듭니다.
- 시사점:
  - 우리 블로그도 `거시`, `코인`, `세계 흐름/섹터`라는 정체성을 더 선명하게 유지해야 합니다.
  - 개별 이슈도 반드시 거시/자금흐름/섹터 맥락과 연결해서 풀어야 합니다.

## Applied To This Project

- 검색 수요 우선 정책 강화
  - Google Trends와 검색 수요 점수를 더 강하게 반영하도록 점수화 로직 조정
- 브랜드 정체성 가드레일 추가
  - 경제, 투자, 코인, 거시, 섹터 흐름 범위를 벗어나는 트렌드는 배제
- 설명형 글 강화
  - fallback 초안에서 독자 관점 문장, 해석 문장, 균형 문장 비중 강화
- 업로드 전 리뷰 게이트 추가
  - 리뷰 패킷을 먼저 만들고 승인 전에는 Blogger 업로드 차단

## Next Reference-Driven Improvements

- 메인 페이지와 허브 글에 `popular reads` 또는 `start here` 묶음 추가
- 뉴스레터/구독 CTA를 허브형 CTA로 재설계
- 메인 이슈 글 1개 + 구조 설명 글 1개 + FAQ 글 1개 조합을 일일 운영 기본 단위로 고정
- 검색량이 높은 종목/ETF 키워드를 다룰 때는 반드시 거시/섹터/자금흐름 문장 1개 이상 포함
