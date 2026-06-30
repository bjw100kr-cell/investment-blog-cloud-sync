# Plugin Signal Usage

Updated: 2026-07-01

## Purpose

새로 설치된 플러그인은 블로그 글의 `근거 데이터`와 `운영 공유`를 보강하는 데 사용한다. 플러그인 데이터만으로 투자 판단을 단정하지 않고, 글 발행 전에는 기존 소스 신선도/품질 게이트와 함께 검증한다.

## Confirmed Plugins

### Binance

Use for crypto market signal intake.

- 전체 코인 시장 분위기: market cap, 24h volume, fear/greed index
- 핫토큰 후보: BTC, ETH, SOL, BNB 같은 메이저와 단기 관심 토큰
- 글감 후보: stablecoin, Strategy/MicroStrategy, ETH whale activity, category trend
- 본문 활용 방식: `오늘 핵심 3줄`, `시장이 반응한 이유`, `내가 확인할 지표`에 숫자와 신호를 넣는다.

Latest test snapshot:

- Crypto market cap: `$2.04T`, change `-2.48%`
- 24h volume: `$75.6B`, change `-9.82%`
- Fear/Greed Index: `16`, `Extreme Fear`
- Hot token carousel included: `BNB`, `BTC`, `ETH`, `SOL`, `DOGE`, `SYN`, `XRP`, `XLM`, `RE`, `CELO`
- Community-focus hot coins included: `CATI`, `RSR`, `GLM`, `ESP`, `DYDX`

Editorial rule:

- Binance signal is a first-pass market sensor, not a final source.
- If a post mentions regulation, company actions, ETF flows, macro events, or named institutions, cross-check with official filings, exchange pages, Reuters/CoinDesk/Cointelegraph/The Block, or the existing trusted source flow before publishing.
- Small-cap hot coins should usually be used as `market sentiment examples`, not as standalone recommendation posts.

### Google Drive

Use for user-facing review and operations files when helpful.

- Export daily review packet or operator report to Google Docs/Sheets.
- Keep a simple content calendar or keyword board in Sheets later if the user wants a spreadsheet workflow.
- Do not move secrets or OAuth result files into Drive.

## Next Integration Tasks

- Done: Add a daily `crypto-market-signal` report that records Binance/plugin-compatible market overview plus public crypto market data.
- Done: Feed `fear/greed`, tracked major symbols, and market sentiment into topic scoring.
- Done: Add a quality-gate warning if crypto posts lack at least one concrete market signal.
- Optionally export weekly review summary to Google Drive after GA4/Search Console is connected.
