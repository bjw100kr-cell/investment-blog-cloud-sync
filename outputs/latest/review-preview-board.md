# Review Preview Board

사용자가 업로드 전에 실제 본문 HTML까지 빠르게 읽어보고 최종 확인할 수 있도록 만든 검토 보드입니다.

- single approval: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`
- batch approval: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords bitcoin`

## 1. 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword: `bitcoin`
- publish_date: `2026-07-08`
- priority_score: `123.0`
- review_verdict: `approve` / score `100`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- CTA focus: ETF·규제·초보 가이드 글로 연결
- final retention CTA: 비트코인은 가격만 보면 놓치는 게 많습니다. 아래 ETF·규제 정리와 초보자 가이드까지 같이 보면 구조가 훨씬 빨리 잡힙니다.
- later revisit CTA: 코인 해설을 짧게 계속 받고 싶다면 텔레그램형 재방문 동선과 연결합니다.
- draft: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/drafts/02-bitcoin.md`
- html: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/publish-ready/02-비트코인-핵심-흐름-해설.html`
- image review required: `True`
- image 대표 이미지: Pexels / `bitcoin blockchain abstract blue finance` / Pexels License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword bitcoin --slot hero --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- image 본문 보조 이미지: Unsplash / `crypto market data abstract` / Unsplash License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword bitcoin --slot inline --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- preview: 한 줄 요약: `현물 ETF 순유입/순유출`, `달러 인덱스와 미국채 금리`, `이더리움과 알트코인 확산 여부` 세 지표를 같이 봐야 이 이슈가 단기 뉴스인지 실제 흐름인지 구분할 수 있습니다.
- preview: - 비트코인 흐름은 가격 캔들만 보면 늦습니다. ETF 자금과 달러 흐름, 규제 뉴스가 먼저 분위기를 바꾸는 경우가 많습니다. - 강한 상승처럼 보여도 실제 자금 유입이 약하거나 달러가 강하면 흐름이 쉽게 끊길 수 있습니다. - 개인 투자자는 비트코인 단독 상승인지, 이더리움·알트코인·나스닥까지 같이 움직이는지를 함께 확인해야 합니다.

## 2. 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword: `china`
- publish_date: `2026-07-10`
- priority_score: `74.0`
- review_verdict: `approve` / score `100`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- CTA focus: 실적·공급망·대표 종목 글로 연결
- draft: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/drafts/04-china.md`
- html: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/publish-ready/04-중국-변수와-시장-영향-해설.html`
- image review required: `True`
- image 대표 이미지: Unsplash / `technology stocks office finance abstract` / Unsplash License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword china --slot hero --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- image 본문 보조 이미지: Pexels / `semiconductor data center abstract` / Pexels License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword china --slot inline --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- preview: 한 줄 요약: `달러/위안 환율`, `중국 부동산·소비 지표`, `구리와 유가` 세 지표를 같이 봐야 이 이슈가 단기 뉴스인지 실제 흐름인지 구분할 수 있습니다.
- preview: - 중국 변수는 중국 증시만의 문제가 아니라 원자재, 환율, 한국 수출주, 글로벌 위험심리로 번질 수 있습니다. - 정책 부양 뉴스가 나와도 실제 소비와 부동산, 위안화 흐름이 따라오는지 확인해야 합니다. - 개인 투자자는 중국 관련 ETF나 소재·산업재만 보지 말고 달러/위안, 구리·유가, 한국 수출주 반응을 같이 보는 편이 좋습니다.

## 3. AI 성장주를 볼 때 놓치기 쉬운 리스크: 매출 성장과 금리 부담

- keyword: `ai_growth_stocks`
- publish_date: `2026-07-09`
- priority_score: `71.0`
- review_verdict: `approve` / score `100`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- CTA focus: 실적·공급망·대표 종목 글로 연결
- draft: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/drafts/03-ai-growth-stocks.md`
- html: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/publish-ready/03-ai-성장주를-볼-때-놓치기-쉬운-리스크-매출-성장과-금리-부담.html`
- image review required: `True`
- image 대표 이미지: Unsplash / `technology stocks office finance abstract` / Unsplash License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword ai_growth_stocks --slot hero --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- image 본문 보조 이미지: Pexels / `semiconductor data center abstract` / Pexels License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword ai_growth_stocks --slot inline --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- preview: 한 줄 요약: `공식 발표 날짜와 핵심 문구`, `달러·금리·주식·코인 중 먼저 반응한 자산`, `거래량과 자금 흐름` 세 지표를 같이 봐야 이 이슈가 단기 뉴스인지 실제 흐름인지 구분할 수 있습니다.
- preview: - AI 성장주를 볼 때 놓치기 쉬운 리스크: 매출 성장과 금리 부담은 제목만 보면 단순 뉴스처럼 보이지만, 실제로는 자금 흐름과 투자심리를 같이 건드릴 수 있는 이슈입니다. - 핵심은 발표 자체보다 시장이 그 발표를 어떤 방향으로 해석했는지입니다. - 개인 투자자는 가격 반응, 관련 자산 확산, 다음 공식 일정을 함께 확인하는 편이 좋습니다.

- board html: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/review-preview-board.html`
