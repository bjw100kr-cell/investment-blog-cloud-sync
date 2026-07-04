# Review Packet

업로드 전에 운영자와 사용자가 함께 확인할 글 검토 패킷입니다.

- 사용자 최종 확인 파일: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/review-approvals.json`
- 사용자 확인 헬퍼: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords fomc bitcoin` 또는 `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --all`
- 총 검토 대상: `9`
- 바로 최종 확인 가능: `9`
- 주의 검토: `0`
- 수정 권장: `0`

## 유가 상승이 물가와 증시에 번지는 경로: 투자자가 볼 3가지

- keyword: `oil`
- type: `main_post` / role `lane_focus_macro`
- publish date: `2026-07-04`
- priority: `105.0`
- internal review: `approve` / score `100`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- CTA focus: 환율·금리·미국증시 evergreen 글로 연결
- final retention CTA: 이 글과 함께 아래 읽을거리까지 보면 `환율·금리·미국증시 evergreen 글로 연결` 흐름이 훨씬 더 잘 이어집니다.
- later revisit CTA: 핵심 흐름을 짧게 계속 받고 싶다면 텔레그램형 재방문 동선과 연결합니다.
- draft: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/drafts/04-oil.md`
- rendered html: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/publish-ready/04-유가-상승이-물가와-증시에-번지는-경로-투자자가-볼-3가지.html`
- image review required: `True`
- image 대표 이미지: Unsplash / query `central bank finance city skyline market data` / license Unsplash License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword oil --slot hero --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- image 본문 보조 이미지: Pexels / query `interest rate macro economy data screen` / license Pexels License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword oil --slot inline --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- preview:
  한 줄 요약: `공식 발표 날짜와 핵심 문구`, `달러·금리·주식·코인 중 먼저 반응한 자산`, `거래량과 자금 흐름` 세 지표를 같이 봐야 이 이슈가 단기 뉴스인지 실제 흐름인지 구분할 수 있습니다.
  - 유가 상승이 물가와 증시에 번지는 경로: 투자자가 볼 3가지은 제목만 보면 단순 뉴스처럼 보이지만, 실제로는 자금 흐름과 투자심리를 같이 건드릴 수 있는 이슈입니다. - 핵심은 발표 자체보다 시장이 그 발표를 어떤 방향으로 해석했는지입니다. - 개인 투자자는 가격 반응, 관련 자산 확산, 다음 공식 일정을 함께 확인하는 편이 좋습니다.

## 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword: `bitcoin`
- type: `main_post` / role `lane_focus_crypto`
- publish date: `2026-07-05`
- priority: `127.0`
- internal review: `approve` / score `100`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- CTA focus: ETF·규제·초보 가이드 글로 연결
- final retention CTA: 비트코인은 가격만 보면 놓치는 게 많습니다. 아래 ETF·규제 정리와 초보자 가이드까지 같이 보면 구조가 훨씬 빨리 잡힙니다.
- later revisit CTA: 코인 해설을 짧게 계속 받고 싶다면 텔레그램형 재방문 동선과 연결합니다.
- draft: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/drafts/02-bitcoin.md`
- rendered html: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/publish-ready/02-비트코인-핵심-흐름-해설.html`
- image review required: `True`
- image 대표 이미지: Pexels / query `bitcoin blockchain abstract blue finance` / license Pexels License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword bitcoin --slot hero --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- image 본문 보조 이미지: Unsplash / query `crypto market data abstract` / license Unsplash License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword bitcoin --slot inline --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- preview:
  한 줄 요약: `현물 ETF 순유입/순유출`, `달러 인덱스와 미국채 금리`, `이더리움과 알트코인 확산 여부` 세 지표를 같이 봐야 이 이슈가 단기 뉴스인지 실제 흐름인지 구분할 수 있습니다.
  - 비트코인 흐름은 가격 캔들만 보면 늦습니다. ETF 자금과 달러 흐름, 규제 뉴스가 먼저 분위기를 바꾸는 경우가 많습니다. - 강한 상승처럼 보여도 실제 자금 유입이 약하거나 달러가 강하면 흐름이 쉽게 끊길 수 있습니다. - 개인 투자자는 비트코인 단독 상승인지, 이더리움·알트코인·나스닥까지 같이 움직이는지를 함께 확인해야 합니다.

## FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지

- keyword: `fomc`
- type: `main_post` / role `support`
- publish date: `2026-07-07`
- priority: `129.0`
- internal review: `approve` / score `100`
- intent: FOMC가 무엇인지와 금리·주식·코인에 왜 중요한지 알고 싶어 하는 초중급 투자자
- CTA focus: 환율·금리·미국증시 evergreen 글로 연결
- final retention CTA: FOMC 흐름이 여기서 끝이 아닙니다. 아래 체크포인트 글과 초보자 가이드까지 같이 보면 다음 일정에서 뭘 봐야 할지 훨씬 선명해집니다.
- later revisit CTA: 거시 이벤트를 놓치지 않으려면 다음 체크포인트 글까지 같이 보고, 이후에는 텔레그램/구독 채널로 이어 받아보세요.
- draft: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/drafts/01-fomc.md`
- rendered html: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/publish-ready/01-fomc-이후-시장-해설.html`
- image review required: `True`
- image 대표 이미지: Unsplash / query `central bank meeting finance city skyline` / license Unsplash License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword fomc --slot hero --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- image 본문 보조 이미지: Pexels / query `interest rate macro economy abstract` / license Pexels License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword fomc --slot inline --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- preview:
  한 줄 요약: `달러 인덱스`, `미국채 2년물/10년물 금리`, `나스닥과 비트코인 동시 반응` 세 지표를 같이 봐야 이 이슈가 단기 뉴스인지 실제 흐름인지 구분할 수 있습니다.
  - FOMC는 금리 결정 한 줄보다 달러, 미국채 금리, 위험자산 심리를 동시에 바꾸는 이벤트입니다. - 시장은 발표 결과보다 성명서 문구, 점도표, 기자회견 톤이 다음 금리 경로를 어떻게 바꾸는지에 더 민감하게 반응합니다. - 개인 투자자는 발표 직후 방향을 단정하기보다 달러 인덱스, 미국채 2년물/10년물, 나스닥과 비트코인 반응을 같이 확인하는 편이 안전합니다.

## AI 반도체 주가를 볼 때 실적보다 먼저 확인할 3가지

- keyword: `ai_semiconductors`
- type: `main_post` / role `lane_focus_us-stocks`
- publish date: `2026-07-06`
- priority: `111.0`
- internal review: `approve` / score `100`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- CTA focus: 실적·공급망·대표 종목 글로 연결
- final retention CTA: 이 글과 함께 아래 읽을거리까지 보면 `실적·공급망·대표 종목 글로 연결` 흐름이 훨씬 더 잘 이어집니다.
- later revisit CTA: 핵심 흐름을 짧게 계속 받고 싶다면 텔레그램형 재방문 동선과 연결합니다.
- draft: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/drafts/03-ai-semiconductors.md`
- rendered html: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/publish-ready/03-ai-반도체-주가를-볼-때-실적보다-먼저-확인할-3가지.html`
- image review required: `True`
- image 대표 이미지: Unsplash / query `semiconductor chip blue abstract` / license Unsplash License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword ai_semiconductors --slot hero --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- image 본문 보조 이미지: Pexels / query `ai server data center abstract` / license Pexels License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword ai_semiconductors --slot inline --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- preview:
  한 줄 요약: `나스닥과 S&P500 상대 강도`, `미국채 10년물 금리`, `엔비디아·마이크로소프트 등 빅테크 실적 가이던스` 세 지표를 같이 봐야 이 이슈가 단기 뉴스인지 실제 흐름인지 구분할 수 있습니다.
  - 미국 증시 흐름은 지수 등락률만 보면 부족합니다. 금리와 달러, 빅테크 실적 기대가 같이 움직입니다. - 나스닥이 강해도 시장 폭이 좁으면 일부 대형주 쏠림일 수 있고, 반대로 섹터 확산이 나오면 추세가 더 단단해질 수 있습니다. - 개인 투자자는 지수보다 금리, 반도체·AI 대표주, 실적 가이던스, 거래대금 확산을 함께 보는 편이 좋습니다.

## AI 반도체 주식 관련 대표 종목 한눈에 보기

- keyword: `seo_ai_semiconductors_7`
- type: `seo_followup` / role `evergreen_seo`
- publish date: `2026-07-06`
- priority: `110.5`
- internal review: `approve` / score `100`
- intent: 섹터 뉴스는 봤지만 실제 어떤 기업을 같이 봐야 하는지 알고 싶은 독자
- CTA focus: 대표 종목 글과 허브 글 연결
- final retention CTA: 이 글과 함께 아래 읽을거리까지 보면 `실적·공급망·대표 종목 글로 연결` 흐름이 훨씬 더 잘 이어집니다.
- later revisit CTA: 핵심 흐름을 짧게 계속 받고 싶다면 텔레그램형 재방문 동선과 연결합니다.
- draft: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-drafts/01-seo-ai-semiconductors-7.md`
- rendered html: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-publish-ready/01-ai-반도체-주식-관련-대표-종목-한눈에-보기.html`
- image review required: `True`
- image 대표 이미지: Unsplash / query `semiconductor chip blue abstract` / license Unsplash License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword seo_ai_semiconductors_7 --slot hero --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- image 본문 보조 이미지: Pexels / query `ai server data center abstract` / license Pexels License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword seo_ai_semiconductors_7 --slot inline --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- preview:
  한 줄 요약: `나스닥과 S&P500 상대 강도`, `미국채 10년물 금리`, `엔비디아·마이크로소프트 등 빅테크 실적 가이던스` 세 지표를 같이 봐야 이 이슈가 단기 뉴스인지 실제 흐름인지 구분할 수 있습니다.
  - 미국 증시 흐름은 지수 등락률만 보면 부족합니다. 금리와 달러, 빅테크 실적 기대가 같이 움직입니다. - 나스닥이 강해도 시장 폭이 좁으면 일부 대형주 쏠림일 수 있고, 반대로 섹터 확산이 나오면 추세가 더 단단해질 수 있습니다. - 개인 투자자는 지수보다 금리, 반도체·AI 대표주, 실적 가이던스, 거래대금 확산을 함께 보는 편이 좋습니다.

## AI 반도체 주식 ETF·지수·대표 기업 정리

- keyword: `seo_ai_semiconductors_9`
- type: `seo_followup` / role `evergreen_seo`
- publish date: `2026-07-06`
- priority: `104.5`
- internal review: `approve` / score `100`
- intent: 개별 종목보다 묶음으로 섹터를 이해하고 싶은 독자
- CTA focus: 섹터 허브와 후속 비교 글 연결
- final retention CTA: 이 글과 함께 아래 읽을거리까지 보면 `실적·공급망·대표 종목 글로 연결` 흐름이 훨씬 더 잘 이어집니다.
- later revisit CTA: 핵심 흐름을 짧게 계속 받고 싶다면 텔레그램형 재방문 동선과 연결합니다.
- draft: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-drafts/02-seo-ai-semiconductors-9.md`
- rendered html: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-publish-ready/02-ai-반도체-주식-etf-지수-대표-기업-정리.html`
- image review required: `True`
- image 대표 이미지: Unsplash / query `semiconductor chip blue abstract` / license Unsplash License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword seo_ai_semiconductors_9 --slot hero --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- image 본문 보조 이미지: Pexels / query `ai server data center abstract` / license Pexels License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword seo_ai_semiconductors_9 --slot inline --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- preview:
  한 줄 요약: `나스닥과 S&P500 상대 강도`, `미국채 10년물 금리`, `엔비디아·마이크로소프트 등 빅테크 실적 가이던스` 세 지표를 같이 봐야 이 이슈가 단기 뉴스인지 실제 흐름인지 구분할 수 있습니다.
  - 미국 증시 흐름은 지수 등락률만 보면 부족합니다. 금리와 달러, 빅테크 실적 기대가 같이 움직입니다. - 나스닥이 강해도 시장 폭이 좁으면 일부 대형주 쏠림일 수 있고, 반대로 섹터 확산이 나오면 추세가 더 단단해질 수 있습니다. - 개인 투자자는 지수보다 금리, 반도체·AI 대표주, 실적 가이던스, 거래대금 확산을 함께 보는 편이 좋습니다.

## 국제유가 전망이 주식과 코인에 미치는 영향

- keyword: `seo_oil_10`
- type: `seo_followup` / role `evergreen_seo`
- publish date: `2026-07-04`
- priority: `104.5`
- internal review: `approve` / score `100`
- intent: 뉴스를 봤지만 내 투자에 어떻게 연결되는지 쉽게 이해하고 싶은 독자
- CTA focus: 거시 허브와 당일 해설 글로 연결
- final retention CTA: 이 글과 함께 아래 읽을거리까지 보면 `환율·금리·미국증시 evergreen 글로 연결` 흐름이 훨씬 더 잘 이어집니다.
- later revisit CTA: 핵심 흐름을 짧게 계속 받고 싶다면 텔레그램형 재방문 동선과 연결합니다.
- draft: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-drafts/03-seo-oil-10.md`
- rendered html: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-publish-ready/03-국제유가-전망이-주식과-코인에-미치는-영향.html`
- image review required: `True`
- image 대표 이미지: Unsplash / query `central bank finance city skyline market data` / license Unsplash License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword seo_oil_10 --slot hero --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- image 본문 보조 이미지: Pexels / query `interest rate macro economy data screen` / license Pexels License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword seo_oil_10 --slot inline --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- preview:
  한 줄 요약: `공식 발표 날짜와 핵심 문구`, `달러·금리·주식·코인 중 먼저 반응한 자산`, `거래량과 자금 흐름` 세 지표를 같이 봐야 이 이슈가 단기 뉴스인지 실제 흐름인지 구분할 수 있습니다.
  - 국제유가 전망이 주식과 코인에 미치는 영향은 제목만 보면 단순 뉴스처럼 보이지만, 실제로는 자금 흐름과 투자심리를 같이 건드릴 수 있는 이슈입니다. - 핵심은 발표 자체보다 시장이 그 발표를 어떤 방향으로 해석했는지입니다. - 개인 투자자는 가격 반응, 관련 자산 확산, 다음 공식 일정을 함께 확인하는 편이 좋습니다.

## 국제유가 전망에서 다음으로 봐야 할 체크포인트 5가지

- keyword: `seo_oil_11`
- type: `seo_followup` / role `follow_up`
- publish date: `2026-07-04`
- priority: `101.5`
- internal review: `approve` / score `100`
- intent: 발표 이후 다음 일정과 후속 확인 포인트를 빠르게 정리하고 싶은 독자
- CTA focus: 다음 이벤트 캘린더와 관련 거시 글로 연결
- final retention CTA: 이 글과 함께 아래 읽을거리까지 보면 `환율·금리·미국증시 evergreen 글로 연결` 흐름이 훨씬 더 잘 이어집니다.
- later revisit CTA: 핵심 흐름을 짧게 계속 받고 싶다면 텔레그램형 재방문 동선과 연결합니다.
- draft: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-drafts/04-seo-oil-11.md`
- rendered html: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-publish-ready/04-국제유가-전망에서-다음으로-봐야-할-체크포인트-5가지.html`
- image review required: `True`
- image 대표 이미지: Unsplash / query `central bank finance city skyline market data` / license Unsplash License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword seo_oil_11 --slot hero --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- image 본문 보조 이미지: Pexels / query `interest rate macro economy data screen` / license Pexels License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword seo_oil_11 --slot inline --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- preview:
  한 줄 요약: `공식 발표 날짜와 핵심 문구`, `달러·금리·주식·코인 중 먼저 반응한 자산`, `거래량과 자금 흐름` 세 지표를 같이 봐야 이 이슈가 단기 뉴스인지 실제 흐름인지 구분할 수 있습니다.
  - 국제유가 전망에서 다음으로 봐야 할 체크포인트 5가지은 제목만 보면 단순 뉴스처럼 보이지만, 실제로는 자금 흐름과 투자심리를 같이 건드릴 수 있는 이슈입니다. - 핵심은 발표 자체보다 시장이 그 발표를 어떤 방향으로 해석했는지입니다. - 개인 투자자는 가격 반응, 관련 자산 확산, 다음 공식 일정을 함께 확인하는 편이 좋습니다.

## 국제유가 전망 초보자 가이드: 용어부터 시장 반응까지

- keyword: `seo_oil_12`
- type: `seo_followup` / role `evergreen_seo`
- publish date: `2026-07-04`
- priority: `98.5`
- internal review: `approve` / score `100`
- intent: 기초 개념을 처음부터 이해하고 싶은 초보 독자
- CTA focus: About, 허브 글, 후속 해설 글로 연결
- final retention CTA: 이 글과 함께 아래 읽을거리까지 보면 `환율·금리·미국증시 evergreen 글로 연결` 흐름이 훨씬 더 잘 이어집니다.
- later revisit CTA: 핵심 흐름을 짧게 계속 받고 싶다면 텔레그램형 재방문 동선과 연결합니다.
- draft: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-drafts/05-seo-oil-12.md`
- rendered html: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-publish-ready/05-국제유가-전망-초보자-가이드-용어부터-시장-반응까지.html`
- image review required: `True`
- image 대표 이미지: Unsplash / query `central bank finance city skyline market data` / license Unsplash License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword seo_oil_12 --slot hero --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- image 본문 보조 이미지: Pexels / query `interest rate macro economy data screen` / license Pexels License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword seo_oil_12 --slot inline --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- preview:
  한 줄 요약: `공식 발표 날짜와 핵심 문구`, `달러·금리·주식·코인 중 먼저 반응한 자산`, `거래량과 자금 흐름` 세 지표를 같이 봐야 이 이슈가 단기 뉴스인지 실제 흐름인지 구분할 수 있습니다.
  - 국제유가 전망 초보자 가이드: 용어부터 시장 반응까지은 제목만 보면 단순 뉴스처럼 보이지만, 실제로는 자금 흐름과 투자심리를 같이 건드릴 수 있는 이슈입니다. - 핵심은 발표 자체보다 시장이 그 발표를 어떤 방향으로 해석했는지입니다. - 개인 투자자는 가격 반응, 관련 자산 확산, 다음 공식 일정을 함께 확인하는 편이 좋습니다.
