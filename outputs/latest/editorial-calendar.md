# 7일 편집 캘린더

- 생성 시각: `2026-06-30T21:10:07.428280+00:00`
- 목적: stale 뉴스는 직접 발행에서 빼고, 거시경제·코인·미국주식·세계 흐름 레인을 주간 단위로 균형 있게 유지

## 레인 커버리지

- `거시경제` / target `0.3` / scheduled_count `2` / actual_share `0.33` / status `covered`
- `코인` / target `0.3` / scheduled_count `2` / actual_share `0.33` / status `covered`
- `미국주식` / target `0.2` / scheduled_count `1` / actual_share `0.17` / status `covered`
- `세계 흐름` / target `0.2` / scheduled_count `1` / actual_share `0.17` / status `covered`

## 이번 주 배치 메모

- lane `macro` / keyword `fomc` / mode `direct` / freshness `unknown` / target_share `0.3`
- lane `crypto` / keyword `bitcoin` / mode `direct` / freshness `fresh` / target_share `0.3`
- lane `us-stocks` / keyword `us_index_flow` / mode `direct` / freshness `fresh` / target_share `0.2`
- lane `world-flow` / keyword `china` / mode `direct` / freshness `fresh` / target_share `0.2`

## Day 1 · 2026-06-30 · lane_focus_macro

- 브랜드 레인: 거시경제
- planning_mode: direct
- freshness_status: unknown
- 포스트 유형: breaking_explainer
- 타깃 키워드: fomc
- 작업 제목: FOMC 이후 시장 해설
- 글 각도: 공식 소스 기반 확인 가능, 복수 소스 교차 확인 가능 (4개), 거시 해설형 글로 전환 가치 높음
- 검색 의도: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- 수익화 경로: 시의성 유입 확보 후 설명형 글과 내부링크로 체류 확대
- 내부링크 대상: Federal Reserve Monetary Policy Press, Financial Times World, NYT Business, Reuters Markets via Google News RSS
- 근거 소스/연결 키워드: Federal Reserve Monetary Policy Press, Financial Times World, NYT Business, Reuters Markets via Google News RSS
- 발행 메모: 당일 이슈 해설형 글

## Day 2 · 2026-07-01 · lane_focus_crypto

- 브랜드 레인: 코인
- planning_mode: direct
- freshness_status: fresh
- 포스트 유형: breaking_explainer
- 타깃 키워드: bitcoin
- 작업 제목: 비트코인 핵심 흐름 해설
- 글 각도: 복수 소스 교차 확인 가능 (4개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (extreme_fear)
- 검색 의도: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- 수익화 경로: 시의성 유입 확보 후 설명형 글과 내부링크로 체류 확대
- 내부링크 대상: CNBC Top News, CoinDesk RSS, Cointelegraph, Investing.com Crypto News
- 근거 소스/연결 키워드: CNBC Top News, CoinDesk RSS, Cointelegraph, Investing.com Crypto News
- 발행 메모: 사용자 검토만 통과하면 바로 게시 후보로 유지해도 됩니다.

## Day 3 · 2026-07-02 · lane_focus_us-stocks

- 브랜드 레인: 미국주식
- planning_mode: direct
- freshness_status: fresh
- 포스트 유형: breaking_explainer
- 타깃 키워드: us_index_flow
- 작업 제목: 미국 증시 지수 흐름 해설
- 글 각도: 복수 소스 교차 확인 가능 (5개), 검색량 높은 미국 증시 키워드를 시장 맥락으로 해설 가능
- 검색 의도: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- 수익화 경로: 시의성 유입 확보 후 설명형 글과 내부링크로 체류 확대
- 내부링크 대상: Cointelegraph, Financial Times Home, Financial Times World, MarketWatch Breaking News, Reuters Markets via Google News RSS
- 근거 소스/연결 키워드: Cointelegraph, Financial Times Home, Financial Times World, MarketWatch Breaking News, Reuters Markets via Google News RSS
- 발행 메모: 사용자 검토만 통과하면 바로 게시 후보로 유지해도 됩니다.

## Day 4 · 2026-07-03 · lane_focus_world-flow

- 브랜드 레인: 세계 흐름
- planning_mode: direct
- freshness_status: fresh
- 포스트 유형: breaking_explainer
- 타깃 키워드: china
- 작업 제목: 중국 변수와 시장 영향 해설
- 글 각도: 복수 소스 교차 확인 가능 (3개), 섹터/세계 흐름 연결 해설 가능
- 검색 의도: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- 수익화 경로: 시의성 유입 확보 후 설명형 글과 내부링크로 체류 확대
- 내부링크 대상: CNBC Top News, Financial Times Home, 무역킹 Trade King YouTube
- 근거 소스/연결 키워드: CNBC Top News, Financial Times Home, 무역킹 Trade King YouTube
- 발행 메모: 신선도는 괜찮습니다. 이미지나 품질 게이트만 보완하면 됩니다.

## Day 5 · 2026-07-04 · evergreen_support

- 브랜드 레인: 거시경제
- planning_mode: evergreen
- freshness_status: evergreen
- 포스트 유형: evergreen_explainer
- 타깃 키워드: fomc 뜻
- 작업 제목: FOMC 뜻부터 시장 영향까지 한 번에 정리
- 글 각도: 연준 회의가 왜 주식과 코인에 동시에 영향을 주는지 쉽게 설명하는 기본서형 글
- 검색 의도: FOMC가 무엇인지와 금리·주식·코인에 왜 중요한지 알고 싶어 하는 초중급 투자자
- 수익화 경로: 광고 친화적인 초보 투자자 검색 유입, 연관 거시 글 내부링크 강화
- 내부링크 대상: cpi_guide, treasury_guide, dollar_guide
- 근거 소스/연결 키워드: fomc, cpi, pce, jobs, treasury_yields, dollar
- 발행 메모: 검색 저변을 넓히는 설명형 글

## Day 6 · 2026-07-05 · secondary_lane_support

- 브랜드 레인: 코인
- planning_mode: evergreen
- freshness_status: evergreen
- 포스트 유형: evergreen_explainer
- 타깃 키워드: 달러 인덱스 보는법
- 작업 제목: 달러 인덱스 보는 법과 주식·코인 영향 정리
- 글 각도: 달러 강세가 한국 투자자와 미국 주식·코인에 어떤 의미인지 해설
- 검색 의도: 달러 강세와 약세를 어떻게 해석해야 하는지 알고 싶은 독자
- 수익화 경로: 거시 입문 검색 유입, 환율/금리/미국증시 내부링크 허브
- 내부링크 대상: fomc_guide, cpi_guide, treasury_guide
- 근거 소스/연결 키워드: dollar, treasury_yields, fomc, oil, china
- 발행 메모: 검색 저변을 넓히는 설명형 글

## Day 7 · 2026-07-06 · weekly_recap

- 브랜드 레인: 거시경제
- planning_mode: recap
- freshness_status: mixed
- 포스트 유형: weekly_macro_recap
- 타깃 키워드: fomc, bitcoin, us_index_flow
- 작업 제목: 이번 주 주식·코인·거시 흐름 한 번에 정리
- 글 각도: 상위 이슈 3개를 한 글에서 연결해 재방문 독자와 체류 시간을 늘리는 회고형 글
- 검색 의도: 이번 주 시장 흐름을 짧게 복기하고 다음 주 포인트를 잡고 싶은 독자
- 수익화 경로: 주간 회고형 콘텐츠로 페이지뷰 누적과 내부 링크 허브 역할
- 내부링크 대상: fomc, bitcoin, us_index_flow
- 근거 소스/연결 키워드: fomc, bitcoin, us_index_flow
- 발행 메모: 주간 정리형 글로 카테고리 허브 역할 수행
