# Review Packet

업로드 전에 운영자와 사용자가 함께 확인할 글 검토 패킷입니다.

- 사용자 최종 확인 파일: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/review-approvals.json`
- 사용자 확인 헬퍼: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --keywords fomc bitcoin` 또는 `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_review_approvals.py --all`
- 총 검토 대상: `13`
- 바로 최종 확인 가능: `13`
- 주의 검토: `0`
- 수정 권장: `0`

## FOMC 이후 시장, 주식과 코인이 같이 흔들리는 이유와 확인할 3가지

- keyword: `fomc`
- type: `main_post` / role `lane_focus_macro`
- publish date: `2026-06-30`
- priority: `140.0`
- internal review: `approve` / score `100`
- intent: 당일 이슈를 따라가되 날짜가 지난 뉴스보다 구조를 이해하고 싶은 독자
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

## 비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트

- keyword: `bitcoin`
- type: `main_post` / role `lane_focus_crypto`
- publish date: `2026-07-01`
- priority: `129.0`
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

## 미국 증시 지수 흐름: 나스닥, 금리, 빅테크 실적을 같이 봐야 하는 이유

- keyword: `us_index_flow`
- type: `main_post` / role `lane_focus_us-stocks`
- publish date: `2026-07-02`
- priority: `120.0`
- internal review: `approve` / score `100`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- CTA focus: 실적·공급망·대표 종목 글로 연결
- final retention CTA: 이 글과 함께 아래 읽을거리까지 보면 `실적·공급망·대표 종목 글로 연결` 흐름이 훨씬 더 잘 이어집니다.
- later revisit CTA: 핵심 흐름을 짧게 계속 받고 싶다면 텔레그램형 재방문 동선과 연결합니다.
- draft: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/drafts/03-us-index-flow.md`
- rendered html: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/publish-ready/03-미국-증시-지수-흐름-해설.html`
- image review required: `True`
- image 대표 이미지: Unsplash / query `technology stocks office finance abstract` / license Unsplash License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword us_index_flow --slot hero --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- image 본문 보조 이미지: Pexels / query `semiconductor data center abstract` / license Pexels License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword us_index_flow --slot inline --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- preview:
  한 줄 요약: `나스닥과 S&P500 상대 강도`, `미국채 10년물 금리`, `엔비디아·마이크로소프트 등 빅테크 실적 가이던스` 세 지표를 같이 봐야 이 이슈가 단기 뉴스인지 실제 흐름인지 구분할 수 있습니다.
  - 미국 증시 흐름은 지수 등락률만 보면 부족합니다. 금리와 달러, 빅테크 실적 기대가 같이 움직입니다. - 나스닥이 강해도 시장 폭이 좁으면 일부 대형주 쏠림일 수 있고, 반대로 섹터 확산이 나오면 추세가 더 단단해질 수 있습니다. - 개인 투자자는 지수보다 금리, 반도체·AI 대표주, 실적 가이던스, 거래대금 확산을 함께 보는 편이 좋습니다.

## 중국 변수와 시장 영향: 환율, 경기부양, 원자재를 같이 봐야 하는 이유

- keyword: `china`
- type: `main_post` / role `lane_focus_world-flow`
- publish date: `2026-07-03`
- priority: `103.0`
- internal review: `approve` / score `100`
- intent: 당일 이슈가 내 투자에 어떤 영향을 주는지 빠르게 이해하고 싶은 독자
- CTA focus: 실적·공급망·대표 종목 글로 연결
- final retention CTA: 이 글과 함께 아래 읽을거리까지 보면 `실적·공급망·대표 종목 글로 연결` 흐름이 훨씬 더 잘 이어집니다.
- later revisit CTA: 핵심 흐름을 짧게 계속 받고 싶다면 텔레그램형 재방문 동선과 연결합니다.
- draft: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/drafts/04-china.md`
- rendered html: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/publish-ready/04-중국-변수와-시장-영향-해설.html`
- image review required: `True`
- image 대표 이미지: Unsplash / query `technology stocks office finance abstract` / license Unsplash License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword china --slot hero --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- image 본문 보조 이미지: Pexels / query `semiconductor data center abstract` / license Pexels License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword china --slot inline --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- preview:
  한 줄 요약: `달러/위안 환율`, `중국 부동산·소비 지표`, `구리와 유가` 세 지표를 같이 봐야 이 이슈가 단기 뉴스인지 실제 흐름인지 구분할 수 있습니다.
  - 중국 변수는 중국 증시만의 문제가 아니라 원자재, 환율, 한국 수출주, 글로벌 위험심리로 번질 수 있습니다. - 정책 부양 뉴스가 나와도 실제 소비와 부동산, 위안화 흐름이 따라오는지 확인해야 합니다. - 개인 투자자는 중국 관련 ETF나 소재·산업재만 보지 말고 달러/위안, 구리·유가, 한국 수출주 반응을 같이 보는 편이 좋습니다.

## FOMC 이후 시장이 주식과 코인에 미치는 영향

- keyword: `seo_fomc_1`
- type: `seo_followup` / role `evergreen_seo`
- publish date: `2026-06-30`
- priority: `139.5`
- internal review: `approve` / score `100`
- intent: 뉴스를 봤지만 내 투자에 어떻게 연결되는지 쉽게 이해하고 싶은 독자
- CTA focus: 거시 허브와 당일 해설 글로 연결
- final retention CTA: FOMC 흐름이 여기서 끝이 아닙니다. 아래 체크포인트 글과 초보자 가이드까지 같이 보면 다음 일정에서 뭘 봐야 할지 훨씬 선명해집니다.
- later revisit CTA: 거시 이벤트를 놓치지 않으려면 다음 체크포인트 글까지 같이 보고, 이후에는 텔레그램/구독 채널로 이어 받아보세요.
- draft: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-drafts/01-seo-fomc-1.md`
- rendered html: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-publish-ready/01-fomc-이후-시장이-주식과-코인에-미치는-영향.html`
- image review required: `True`
- image 대표 이미지: Unsplash / query `central bank meeting finance city skyline` / license Unsplash License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword seo_fomc_1 --slot hero --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- image 본문 보조 이미지: Pexels / query `interest rate macro economy abstract` / license Pexels License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword seo_fomc_1 --slot inline --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- preview:
  한 줄 요약: `달러 인덱스`, `미국채 2년물/10년물 금리`, `나스닥과 비트코인 동시 반응` 세 지표를 같이 봐야 이 이슈가 단기 뉴스인지 실제 흐름인지 구분할 수 있습니다.
  - FOMC는 금리 결정 한 줄보다 달러, 미국채 금리, 위험자산 심리를 동시에 바꾸는 이벤트입니다. - 시장은 발표 결과보다 성명서 문구, 점도표, 기자회견 톤이 다음 금리 경로를 어떻게 바꾸는지에 더 민감하게 반응합니다. - 개인 투자자는 발표 직후 방향을 단정하기보다 달러 인덱스, 미국채 2년물/10년물, 나스닥과 비트코인 반응을 같이 확인하는 편이 안전합니다.

## FOMC 이후 시장에서 다음으로 봐야 할 체크포인트 5가지

- keyword: `seo_fomc_2`
- type: `seo_followup` / role `follow_up`
- publish date: `2026-06-30`
- priority: `136.5`
- internal review: `approve` / score `100`
- intent: 발표 이후 다음 일정과 후속 확인 포인트를 빠르게 정리하고 싶은 독자
- CTA focus: 다음 이벤트 캘린더와 관련 거시 글로 연결
- final retention CTA: FOMC 흐름이 여기서 끝이 아닙니다. 아래 체크포인트 글과 초보자 가이드까지 같이 보면 다음 일정에서 뭘 봐야 할지 훨씬 선명해집니다.
- later revisit CTA: 거시 이벤트를 놓치지 않으려면 다음 체크포인트 글까지 같이 보고, 이후에는 텔레그램/구독 채널로 이어 받아보세요.
- draft: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-drafts/02-seo-fomc-2.md`
- rendered html: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-publish-ready/02-fomc-이후-시장에서-다음으로-봐야-할-체크포인트-5가지.html`
- image review required: `True`
- image 대표 이미지: Unsplash / query `central bank meeting finance city skyline` / license Unsplash License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword seo_fomc_2 --slot hero --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- image 본문 보조 이미지: Pexels / query `interest rate macro economy abstract` / license Pexels License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword seo_fomc_2 --slot inline --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- preview:
  한 줄 요약: `달러 인덱스`, `미국채 2년물/10년물 금리`, `나스닥과 비트코인 동시 반응` 세 지표를 같이 봐야 이 이슈가 단기 뉴스인지 실제 흐름인지 구분할 수 있습니다.
  - FOMC는 금리 결정 한 줄보다 달러, 미국채 금리, 위험자산 심리를 동시에 바꾸는 이벤트입니다. - 시장은 발표 결과보다 성명서 문구, 점도표, 기자회견 톤이 다음 금리 경로를 어떻게 바꾸는지에 더 민감하게 반응합니다. - 개인 투자자는 발표 직후 방향을 단정하기보다 달러 인덱스, 미국채 2년물/10년물, 나스닥과 비트코인 반응을 같이 확인하는 편이 안전합니다.

## FOMC 이후 시장 초보자 가이드: 용어부터 시장 반응까지

- keyword: `seo_fomc_3`
- type: `seo_followup` / role `evergreen_seo`
- publish date: `2026-06-30`
- priority: `133.5`
- internal review: `approve` / score `100`
- intent: 기초 개념을 처음부터 이해하고 싶은 초보 독자
- CTA focus: About, 허브 글, 후속 해설 글로 연결
- final retention CTA: FOMC 흐름이 여기서 끝이 아닙니다. 아래 체크포인트 글과 초보자 가이드까지 같이 보면 다음 일정에서 뭘 봐야 할지 훨씬 선명해집니다.
- later revisit CTA: 거시 이벤트를 놓치지 않으려면 다음 체크포인트 글까지 같이 보고, 이후에는 텔레그램/구독 채널로 이어 받아보세요.
- draft: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-drafts/03-seo-fomc-3.md`
- rendered html: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-publish-ready/03-fomc-이후-시장-초보자-가이드-용어부터-시장-반응까지.html`
- image review required: `True`
- image 대표 이미지: Unsplash / query `central bank meeting finance city skyline` / license Unsplash License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword seo_fomc_3 --slot hero --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- image 본문 보조 이미지: Pexels / query `interest rate macro economy abstract` / license Pexels License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword seo_fomc_3 --slot inline --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- preview:
  한 줄 요약: `달러 인덱스`, `미국채 2년물/10년물 금리`, `나스닥과 비트코인 동시 반응` 세 지표를 같이 봐야 이 이슈가 단기 뉴스인지 실제 흐름인지 구분할 수 있습니다.
  - FOMC는 금리 결정 한 줄보다 달러, 미국채 금리, 위험자산 심리를 동시에 바꾸는 이벤트입니다. - 시장은 발표 결과보다 성명서 문구, 점도표, 기자회견 톤이 다음 금리 경로를 어떻게 바꾸는지에 더 민감하게 반응합니다. - 개인 투자자는 발표 직후 방향을 단정하기보다 달러 인덱스, 미국채 2년물/10년물, 나스닥과 비트코인 반응을 같이 확인하는 편이 안전합니다.

## 비트코인 핵심 흐름 초보자 가이드: 지금 꼭 알아야 할 핵심 구조

- keyword: `seo_bitcoin_4`
- type: `seo_followup` / role `evergreen_seo`
- publish date: `2026-07-01`
- priority: `128.5`
- internal review: `approve` / score `100`
- intent: 가격 기사보다 구조와 기본 개념을 먼저 이해하고 싶은 초보 독자
- CTA focus: 코인 허브와 규제/ETF 글 연결
- final retention CTA: 비트코인은 가격만 보면 놓치는 게 많습니다. 아래 ETF·규제 정리와 초보자 가이드까지 같이 보면 구조가 훨씬 빨리 잡힙니다.
- later revisit CTA: 코인 해설을 짧게 계속 받고 싶다면 텔레그램형 재방문 동선과 연결합니다.
- draft: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-drafts/04-seo-bitcoin-4.md`
- rendered html: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-publish-ready/04-비트코인-핵심-흐름-초보자-가이드-지금-꼭-알아야-할-핵심-구조.html`
- image review required: `True`
- image 대표 이미지: Pexels / query `bitcoin blockchain abstract blue finance` / license Pexels License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword seo_bitcoin_4 --slot hero --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- image 본문 보조 이미지: Unsplash / query `crypto market data abstract` / license Unsplash License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword seo_bitcoin_4 --slot inline --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- preview:
  한 줄 요약: `현물 ETF 순유입/순유출`, `달러 인덱스와 미국채 금리`, `이더리움과 알트코인 확산 여부` 세 지표를 같이 봐야 이 이슈가 단기 뉴스인지 실제 흐름인지 구분할 수 있습니다.
  - 비트코인 흐름은 가격 캔들만 보면 늦습니다. ETF 자금과 달러 흐름, 규제 뉴스가 먼저 분위기를 바꾸는 경우가 많습니다. - 강한 상승처럼 보여도 실제 자금 유입이 약하거나 달러가 강하면 흐름이 쉽게 끊길 수 있습니다. - 개인 투자자는 비트코인 단독 상승인지, 이더리움·알트코인·나스닥까지 같이 움직이는지를 함께 확인해야 합니다.

## 비트코인 핵심 흐름 ETF·규제 이슈 정리

- keyword: `seo_bitcoin_5`
- type: `seo_followup` / role `follow_up`
- publish date: `2026-07-01`
- priority: `125.5`
- internal review: `approve` / score `100`
- intent: 뉴스가 복잡해서 규제와 ETF 이슈만 따로 정리해 보고 싶은 독자
- CTA focus: 당일 코인 해설 글과 초보 가이드 연결
- final retention CTA: 비트코인은 가격만 보면 놓치는 게 많습니다. 아래 ETF·규제 정리와 초보자 가이드까지 같이 보면 구조가 훨씬 빨리 잡힙니다.
- later revisit CTA: 코인 해설을 짧게 계속 받고 싶다면 텔레그램형 재방문 동선과 연결합니다.
- draft: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-drafts/05-seo-bitcoin-5.md`
- rendered html: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-publish-ready/05-비트코인-핵심-흐름-etf-규제-이슈-정리.html`
- image review required: `True`
- image 대표 이미지: Pexels / query `bitcoin blockchain abstract blue finance` / license Pexels License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword seo_bitcoin_5 --slot hero --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- image 본문 보조 이미지: Unsplash / query `crypto market data abstract` / license Unsplash License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword seo_bitcoin_5 --slot inline --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- preview:
  한 줄 요약: `현물 ETF 순유입/순유출`, `달러 인덱스와 미국채 금리`, `이더리움과 알트코인 확산 여부` 세 지표를 같이 봐야 이 이슈가 단기 뉴스인지 실제 흐름인지 구분할 수 있습니다.
  - 비트코인 흐름은 가격 캔들만 보면 늦습니다. ETF 자금과 달러 흐름, 규제 뉴스가 먼저 분위기를 바꾸는 경우가 많습니다. - 강한 상승처럼 보여도 실제 자금 유입이 약하거나 달러가 강하면 흐름이 쉽게 끊길 수 있습니다. - 개인 투자자는 비트코인 단독 상승인지, 이더리움·알트코인·나스닥까지 같이 움직이는지를 함께 확인해야 합니다.

## 비트코인 핵심 흐름 FAQ 10개: 많이 헷갈리는 질문 정리

- keyword: `seo_bitcoin_6`
- type: `seo_followup` / role `evergreen_seo`
- publish date: `2026-07-01`
- priority: `122.5`
- internal review: `approve` / score `100`
- intent: 짧은 질문 단위로 빠르게 답을 찾고 싶은 독자
- CTA focus: 기초 글과 주간 정리 글 연결
- final retention CTA: 비트코인은 가격만 보면 놓치는 게 많습니다. 아래 ETF·규제 정리와 초보자 가이드까지 같이 보면 구조가 훨씬 빨리 잡힙니다.
- later revisit CTA: 코인 해설을 짧게 계속 받고 싶다면 텔레그램형 재방문 동선과 연결합니다.
- draft: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-drafts/06-seo-bitcoin-6.md`
- rendered html: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-publish-ready/06-비트코인-핵심-흐름-faq-10개-많이-헷갈리는-질문-정리.html`
- image review required: `True`
- image 대표 이미지: Pexels / query `bitcoin blockchain abstract blue finance` / license Pexels License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword seo_bitcoin_6 --slot hero --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- image 본문 보조 이미지: Unsplash / query `crypto market data abstract` / license Unsplash License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword seo_bitcoin_6 --slot inline --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- preview:
  한 줄 요약: `현물 ETF 순유입/순유출`, `달러 인덱스와 미국채 금리`, `이더리움과 알트코인 확산 여부` 세 지표를 같이 봐야 이 이슈가 단기 뉴스인지 실제 흐름인지 구분할 수 있습니다.
  - 비트코인 흐름은 가격 캔들만 보면 늦습니다. ETF 자금과 달러 흐름, 규제 뉴스가 먼저 분위기를 바꾸는 경우가 많습니다. - 강한 상승처럼 보여도 실제 자금 유입이 약하거나 달러가 강하면 흐름이 쉽게 끊길 수 있습니다. - 개인 투자자는 비트코인 단독 상승인지, 이더리움·알트코인·나스닥까지 같이 움직이는지를 함께 확인해야 합니다.

## 미국 증시 지수 흐름 관련 대표 종목 한눈에 보기

- keyword: `seo_us_index_flow_7`
- type: `seo_followup` / role `evergreen_seo`
- publish date: `2026-07-02`
- priority: `119.5`
- internal review: `approve` / score `100`
- intent: 섹터 뉴스는 봤지만 실제 어떤 기업을 같이 봐야 하는지 알고 싶은 독자
- CTA focus: 대표 종목 글과 허브 글 연결
- final retention CTA: 이 글과 함께 아래 읽을거리까지 보면 `실적·공급망·대표 종목 글로 연결` 흐름이 훨씬 더 잘 이어집니다.
- later revisit CTA: 핵심 흐름을 짧게 계속 받고 싶다면 텔레그램형 재방문 동선과 연결합니다.
- draft: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-drafts/07-seo-us-index-flow-7.md`
- rendered html: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-publish-ready/07-미국-증시-지수-흐름-관련-대표-종목-한눈에-보기.html`
- image review required: `True`
- image 대표 이미지: Unsplash / query `technology stocks office finance abstract` / license Unsplash License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword seo_us_index_flow_7 --slot hero --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- image 본문 보조 이미지: Pexels / query `semiconductor data center abstract` / license Pexels License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword seo_us_index_flow_7 --slot inline --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- preview:
  한 줄 요약: `나스닥과 S&P500 상대 강도`, `미국채 10년물 금리`, `엔비디아·마이크로소프트 등 빅테크 실적 가이던스` 세 지표를 같이 봐야 이 이슈가 단기 뉴스인지 실제 흐름인지 구분할 수 있습니다.
  - 미국 증시 흐름은 지수 등락률만 보면 부족합니다. 금리와 달러, 빅테크 실적 기대가 같이 움직입니다. - 나스닥이 강해도 시장 폭이 좁으면 일부 대형주 쏠림일 수 있고, 반대로 섹터 확산이 나오면 추세가 더 단단해질 수 있습니다. - 개인 투자자는 지수보다 금리, 반도체·AI 대표주, 실적 가이던스, 거래대금 확산을 함께 보는 편이 좋습니다.

## 미국 증시 지수 흐름 공급망 정리: 누가 수혜를 보나

- keyword: `seo_us_index_flow_8`
- type: `seo_followup` / role `follow_up`
- publish date: `2026-07-02`
- priority: `116.5`
- internal review: `approve` / score `100`
- intent: 테마가 실제 공급망과 실적에 어떻게 연결되는지 알고 싶은 독자
- CTA focus: 실적 해설과 글로벌 섹터 허브 연결
- final retention CTA: 이 글과 함께 아래 읽을거리까지 보면 `실적·공급망·대표 종목 글로 연결` 흐름이 훨씬 더 잘 이어집니다.
- later revisit CTA: 핵심 흐름을 짧게 계속 받고 싶다면 텔레그램형 재방문 동선과 연결합니다.
- draft: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-drafts/08-seo-us-index-flow-8.md`
- rendered html: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-publish-ready/08-미국-증시-지수-흐름-공급망-정리-누가-수혜를-보나.html`
- image review required: `True`
- image 대표 이미지: Unsplash / query `technology stocks office finance abstract` / license Unsplash License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword seo_us_index_flow_8 --slot hero --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- image 본문 보조 이미지: Pexels / query `semiconductor data center abstract` / license Pexels License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword seo_us_index_flow_8 --slot inline --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- preview:
  한 줄 요약: `나스닥과 S&P500 상대 강도`, `미국채 10년물 금리`, `엔비디아·마이크로소프트 등 빅테크 실적 가이던스` 세 지표를 같이 봐야 이 이슈가 단기 뉴스인지 실제 흐름인지 구분할 수 있습니다.
  - 미국 증시 흐름은 지수 등락률만 보면 부족합니다. 금리와 달러, 빅테크 실적 기대가 같이 움직입니다. - 나스닥이 강해도 시장 폭이 좁으면 일부 대형주 쏠림일 수 있고, 반대로 섹터 확산이 나오면 추세가 더 단단해질 수 있습니다. - 개인 투자자는 지수보다 금리, 반도체·AI 대표주, 실적 가이던스, 거래대금 확산을 함께 보는 편이 좋습니다.

## 미국 증시 지수 흐름 ETF·지수·대표 기업 정리

- keyword: `seo_us_index_flow_9`
- type: `seo_followup` / role `evergreen_seo`
- publish date: `2026-07-02`
- priority: `113.5`
- internal review: `approve` / score `100`
- intent: 개별 종목보다 묶음으로 섹터를 이해하고 싶은 독자
- CTA focus: 섹터 허브와 후속 비교 글 연결
- final retention CTA: 이 글과 함께 아래 읽을거리까지 보면 `실적·공급망·대표 종목 글로 연결` 흐름이 훨씬 더 잘 이어집니다.
- later revisit CTA: 핵심 흐름을 짧게 계속 받고 싶다면 텔레그램형 재방문 동선과 연결합니다.
- draft: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-drafts/09-seo-us-index-flow-9.md`
- rendered html: `/home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/outputs/latest/seo-publish-ready/09-미국-증시-지수-흐름-etf-지수-대표-기업-정리.html`
- image review required: `True`
- image 대표 이미지: Unsplash / query `technology stocks office finance abstract` / license Unsplash License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword seo_us_index_flow_9 --slot hero --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- image 본문 보조 이미지: Pexels / query `semiconductor data center abstract` / license Pexels License
- image apply helper: `python3 /home/runner/work/investment-blog-cloud-sync/investment-blog-cloud-sync/scripts/set_image_selection.py --keyword seo_us_index_flow_9 --slot inline --selected-url <IMAGE_URL> --selected-credit "Photo by ..." --approve`
- preview:
  한 줄 요약: `나스닥과 S&P500 상대 강도`, `미국채 10년물 금리`, `엔비디아·마이크로소프트 등 빅테크 실적 가이던스` 세 지표를 같이 봐야 이 이슈가 단기 뉴스인지 실제 흐름인지 구분할 수 있습니다.
  - 미국 증시 흐름은 지수 등락률만 보면 부족합니다. 금리와 달러, 빅테크 실적 기대가 같이 움직입니다. - 나스닥이 강해도 시장 폭이 좁으면 일부 대형주 쏠림일 수 있고, 반대로 섹터 확산이 나오면 추세가 더 단단해질 수 있습니다. - 개인 투자자는 지수보다 금리, 반도체·AI 대표주, 실적 가이던스, 거래대금 확산을 함께 보는 편이 좋습니다.
