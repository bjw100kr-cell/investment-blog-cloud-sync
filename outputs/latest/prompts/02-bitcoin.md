# 투자·경제 블로그 초안 생성 프롬프트

아래 패킷을 바탕으로 한국어 블로그 초안을 작성하라.

## 목표

- 투자 권유가 아니라 해설형 글을 만든다.
- 초보 독자도 흐름을 이해할 수 있게 쓴다.
- 검색 유입을 고려해 제목과 소제목을 분명하게 쓴다.
- 사실과 의견을 구분한다.
- 사람이 실제로 쓴 것처럼 친근하고 자연스럽게 쓴다.

## 글의 바이브

- 뉴스앵커처럼 딱딱하게 읽히지 않게 쓴다.
- 너무 완벽하게 매끈한 AI 문체보다, 실제 사람이 시장을 옆에서 설명해 주는 느낌을 만든다.
- 다만 선동적이거나 과장된 카피라이팅 톤은 금지한다.
- 독자가 "그래서 이게 왜 중요한데?"라고 묻기 전에 먼저 풀어준다.
- 한 문단 안에서 숫자만 나열하지 말고 해석을 붙인다.
- 짧은 문장과 중간 길이 문장을 섞어 리듬을 만든다.
- 딱 한두 군데는 대화하듯 연결하되, 지나치게 가벼워 보이지 않게 균형을 잡는다.
- 문장 끝을 전부 같은 어미로만 반복하지 말고 자연스럽게 섞는다.

## 반드시 지킬 것

1. 가격, 금리, 규제, 발표 일정 등은 최신 공식 자료 기준으로 다시 확인이 필요하다는 점을 자연스럽게 반영한다.
2. `무조건 오른다`, `지금 사야 한다` 같은 표현은 금지한다.
3. 시나리오형 표현을 사용한다.
4. 글 마지막에는 제공된 면책문구를 넣는다.
5. 아래 입력 패킷의 `voice_profile`, `human_touch_requirements`, `reader_bridge_phrases`, `direct_address_phrases`, `interpretation_markers`, `avoid_phrases`, `tone_penalties`, `must_include_style_points`, `sentence_rhythm_targets`를 실제 문장에 반영한다.
5-1. 입력 패킷의 `voice_examples`는 좋은 말투 예시다. 문장을 그대로 복사하지 말고, 리듬과 설명 온도만 참고한다.
5-2. 입력 패킷의 `reference_takeaways`는 유튜브/해설 자료에서 뽑은 설명 포인트다. 관점과 흐름은 참고할 수 있지만, 사실 주장으로 쓸 때는 반드시 다른 신뢰 가능한 자료와 함께 검증된 내용만 사용한다.
6. `지금부터 알아보겠습니다`, `살펴보도록 하겠습니다`, `정리해보겠습니다` 같은 AI스러운 문구는 쓰지 않는다.
7. 독자 관점 문장을 적어도 2번은 넣는다.
8. 제목과 소제목은 검색 친화적으로 유지하되, 본문은 키워드 반복보다 자연스러운 설명을 우선한다.
9. 예시 문장을 베끼지 말고, 같은 종류의 친근함과 설명감을 새 문장으로 재구성한다.
10. 도입부 첫 3문장 안에는 독자가 왜 지금 이 글을 읽어야 하는지 직접 말해준다.
11. 숫자나 뉴스 포인트를 언급한 뒤에는 그 의미를 풀어주는 문장을 붙인다.
12. 입력 패킷의 `reference_editorial_pattern`과 `reference_editorial_sources`를 참고해, 현재 잘 나가는 투자/코인 매체의 장점을 구조에만 반영한다.
13. 특히 `search_explainer`, `news_what_it_means`, `followup_checklist` 중 어떤 패턴인지에 맞춰 소제목과 문단 역할을 분명하게 나눈다.
14. 기사 요약에서 끝내지 말고, 글 안에서 반드시 "지금 무슨 일인가 -> 왜 시장이 반응하나 -> 개인 투자자는 다음에 뭘 볼까" 흐름을 완성한다.
15. 독자가 검색해서 들어왔을 때 바로 얻어갈 수 있도록 `오늘 핵심 3줄`, `시장이 반응한 이유`, `내가 확인할 지표`, `상승 시나리오와 리스크`, `자주 하는 오해`를 반드시 포함한다.
16. 추상 표현만 반복하지 않는다. 각 본문 섹션에는 달러, 금리, ETF 자금, 거래량, 규제 일정, 대표 종목, 공식 발표, 다음 경제지표 중 최소 1개 이상의 구체 체크 대상을 넣는다.
17. 문단은 2~4문장 단위로 끊고, 긴 문단 하나로 설명하지 않는다.
18. `핵심 숫자`, `공식 자료`, `다음 이벤트`처럼 확인이 필요한 항목은 뭘 확인해야 하는지 독자가 바로 알 수 있게 쓴다.
19. 제목은 막연한 `흐름 해설`보다 독자가 궁금해할 질문이나 이익을 드러낸다.
20. 글의 목적은 "뉴스를 아는 사람"보다 "뉴스를 봤지만 내 투자와 어떻게 연결되는지 모르는 사람"을 붙잡는 것이다.

## 출력 형식

1. 제목
2. 한 줄 요약
3. 오늘 핵심 3줄
4. 도입부
5. 본문
6. 상승 시나리오와 리스크
7. 자주 하는 오해
8. 체크포인트 3개
9. FAQ 2개
10. CTA
11. 면책문구

## 참고 샘플 글

- `templates/sample_post_macro_explainer.md`
- `templates/sample_post_crypto_analysis.md`
- `templates/sample_post_sector_analysis.md`

위 샘플들은 좋은 톤과 문단 리듬의 기준점이다.

- 문장을 그대로 복사하지 않는다.
- 도입부의 온도, 본문 설명 방식, 마무리의 균형감만 참고한다.
- 지나치게 모범답안처럼 딱딱한 보고서체로 쓰지 않는다.

## 현재 잘 나가는 매체에서 가져올 구조적 강점

- `Investopedia`처럼 검색 의도를 바로 만족하는 설명형 구조를 참고한다.
- `CoinDesk`처럼 뉴스와 자금 흐름 해설을 같이 묶는 방식을 참고한다.
- `Cointelegraph`처럼 섹션을 잘게 나눠 체류시간을 늘리는 구성을 참고한다.
- `MarketWatch`처럼 헤드라인 단계에서 왜 중요한지 바로 드러내는 방식을 참고한다.
- `CoinNess`처럼 짧은 핵심 요약과 체크포인트를 먼저 제시하는 흐름을 참고한다.
- 단, 특정 사이트의 문장이나 표현은 복사하지 않는다. 구조와 전달 방식만 참고한다.

## 입력 패킷

```json
{
  "keyword": "bitcoin",
  "recommended_title": "비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트",
  "alternate_titles": [
    "비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트: 지금 시장이 반응하는 이유",
    "비트코인 가격보다 먼저 봐야 할 것: ETF 자금, 달러, 규제 체크포인트"
  ],
  "summary_angle": "복수 소스 교차 확인 가능 (3개), 코인 독자 유입과 재방문 가능성, 코인 시장 신호 반영 (extreme_fear)",
  "outline": [
    "오늘 코인 시장 핵심 변화",
    "가격이 아니라 구조상 중요한 포인트",
    "ETF/유동성/규제/온체인과의 연결",
    "강세 시나리오와 리스크",
    "내일 확인할 체크포인트"
  ],
  "reference_takeaways": [],
  "fact_checks": [
    "BTC 가격 기준 시각 재확인",
    "ETF 자금 유입 여부 공식/신뢰 소스 재확인",
    "단정적 가격 전망 문장 제거"
  ],
  "disclaimer": "이 글은 정보 제공 및 학습용 정리이며, 특정 자산에 대한 투자 권유나 자문이 아닙니다. 시장 데이터와 제도는 작성 시점 이후 달라질 수 있으므로 실제 투자 전에는 최신 공식 자료를 다시 확인해야 합니다.",
  "cta": "비트코인과 이더리움 흐름을 계속 추적하고 싶다면 다음 코인 해설 글도 함께 보세요.",
  "source_names": [
    "CoinDesk RSS",
    "Cointelegraph",
    "Investing.com Crypto News"
  ],
  "reference_headlines": [
    "Keyrock acquires BlockFills trading assets to expand institutional crypto business",
    "Crypto for Advisors: Strengthening defenses against AI fraud",
    "Crypto brokerage firm Alpaca raises $135 million for tokenized stock infrastructure",
    "Ledger wants AI agents to manage crypto without holding your keys",
    "Galaxy targets institutional stablecoin yield with new DeFi vaults"
  ],
  "voice_profile": "흥분한 코인방 톤이 아니라 차분한 시장 해설 톤. 가격보다 구조를 설명하는 느낌.",
  "human_touch_requirements": [
    "도입부 첫 3문장 안에 독자 관점 문장 1개를 넣는다.",
    "본문 어딘가에 '왜 이게 중요한지'를 말로 풀어주는 문장을 넣는다.",
    "딱딱한 보고서체 대신 짧은 문장과 중간 길이 문장을 섞는다.",
    "문단마다 숫자만 나열하지 말고 해석 문장을 붙인다.",
    "너무 매끈한 교과서체보다 살짝 대화하듯 풀어쓰되, 과장과 선동은 금지한다.",
    "문장 끝을 같은 어미로만 반복하지 말고 리듬을 만든다."
  ],
  "reader_bridge_phrases": [
    "쉽게 말해",
    "한마디로 보면",
    "이 부분이 중요한 이유는",
    "투자자 입장에서 보면",
    "여기서 진짜 봐야 할 건",
    "생각보다 중요한 포인트는"
  ],
  "direct_address_phrases": [
    "개인 투자자 입장에서는",
    "이걸 내 돈 관점에서 보면",
    "헷갈리기 쉬운 부분인데",
    "여기서 먼저 봐야 할 건",
    "독자 입장에서 중요한 건"
  ],
  "interpretation_markers": [
    "이 숫자의 의미는",
    "시장에서는 이걸 이렇게 해석합니다",
    "결국 핵심은",
    "포인트를 한 줄로 줄이면",
    "다음으로 연결해서 보면"
  ],
  "avoid_phrases": [
    "지금부터 알아보겠습니다",
    "살펴보도록 하겠습니다",
    "정리해보겠습니다",
    "도움이 되셨길 바랍니다",
    "결론적으로 말씀드리면",
    "투자에 참고하시기 바랍니다"
  ],
  "tone_penalties": [
    "문장 대부분이 같은 '~습니다' 어미로만 끝나는 교과서체",
    "숫자만 나열하고 그 의미 설명이 없는 문단",
    "독자 관점이 거의 보이지 않는 해설",
    "검색 키워드를 어색하게 반복하는 문장"
  ],
  "sentence_rhythm_targets": {
    "max_dominant_ending_ratio": 0.72,
    "minimum_direct_address_hits": 2,
    "minimum_interpretation_hits": 2
  },
  "must_include_style_points": [
    "가격 자체보다 수급 또는 규제 구조 설명",
    "강세 시나리오와 리스크를 둘 다 언급",
    "단정적 전망 금지"
  ],
  "voice_examples": {
    "intro_example": "비트코인이 오르거나 내릴 때 가장 먼저 보이는 건 가격입니다. 그런데 투자자 입장에서 더 중요한 건 왜 그런 움직임이 나왔는지, 그 배경이 하루짜리 잡음인지 구조적인 변화인지를 구분하는 일입니다.",
    "analysis_example": "한마디로 보면 코인 시장은 기대감만으로 오래 버티지 못합니다. ETF 자금이 실제로 들어오고 있는지, 달러와 금리가 어떤 환경을 만들고 있는지, 규제 이슈가 심리를 꺾고 있는지까지 같이 봐야 흐름이 보입니다.",
    "closing_example": "다만 코인 시장은 같은 재료라도 해석이 빠르게 뒤집히는 편입니다. 그래서 강세 논리만 보지 말고, 유동성이 약해질 때 어떤 신호가 먼저 나오는지도 함께 체크하는 편이 안전합니다."
  },
  "score_breakdown": {
    "total_score": 85.0,
    "search_score": 29,
    "timeliness_score": 18,
    "explanatory_score": 17,
    "monetization_score": 15,
    "risk_score": 3
  },
  "reference_editorial_pattern_name": "news_what_it_means",
  "reference_editorial_pattern": {
    "when_to_use": [
      "당일 발표 직후",
      "시장 급변",
      "정책 발언",
      "코인 규제 헤드라인"
    ],
    "must_have": [
      "무슨 일이 있었는지 1문단 요약",
      "왜 시장이 반응하는지 해석",
      "주식, 달러, 금리, 코인 중 최소 2개와 연결",
      "지금 단정할 수 없는 변수도 함께 표기"
    ]
  },
  "reference_editorial_sources": [
    {
      "name": "Investopedia",
      "source_type": "official_site_plus_similarweb",
      "focus": "검색 유입형 투자 설명글과 용어 해설",
      "evidence": [
        "Investopedia mission page",
        "Similarweb May 2026: Organic Search 59.88 percent, Investing category rank #23"
      ],
      "transferable_strengths": [
        "검색 의도를 바로 만족하는 제목",
        "용어 정의 후 바로 실전 해석으로 연결",
        "초보 독자도 이해할 수 있는 설명형 문단 구조"
      ]
    },
    {
      "name": "CoinDesk",
      "source_type": "official_site_plus_similarweb",
      "focus": "코인 뉴스와 거시/정책 해설의 결합",
      "evidence": [
        "CoinDesk homepage promise: crypto news, analysis, video and price data",
        "Similarweb May 2026: Direct 54.33 percent, US audience 45.09 percent"
      ],
      "transferable_strengths": [
        "속보를 바로 해설형 글로 연결",
        "가격 자체보다 정책, 자금 흐름, 시장 구조를 같이 설명",
        "브랜드 신뢰를 만드는 차분한 톤"
      ]
    },
    {
      "name": "Cointelegraph",
      "source_type": "similarweb_comparison",
      "focus": "체류시간이 긴 코인 스토리텔링형 기사",
      "evidence": [
        "Similarweb comparison May 2026: Avg Visit Duration 00:03:28, Pages per Visit 2.71"
      ],
      "transferable_strengths": [
        "한 기사 안에서 후속 질문까지 같이 풀어주는 구조",
        "본문 흐름이 길어도 끊기지 않도록 섹션을 촘촘히 나누는 방식",
        "독자가 다음 섹션을 계속 읽게 만드는 서브헤드 구성"
      ]
    },
    {
      "name": "MarketWatch",
      "source_type": "official_site",
      "focus": "시장 속보를 개인 투자자 관점으로 빠르게 번역",
      "evidence": [
        "MarketWatch homepage current market-news framing"
      ],
      "transferable_strengths": [
        "헤드라인에서 바로 왜 중요한지 드러냄",
        "당일 시장 변화와 개인 자산에 미치는 영향을 짧게 연결",
        "숫자보다 의미를 먼저 이해시키는 짧은 문단"
      ]
    },
    {
      "name": "CoinNess",
      "source_type": "official_site",
      "focus": "빠른 속보성과 모바일 친화형 코인 정보 소비",
      "evidence": [
        "CoinNess official site: fast and accurate crypto investment news platform"
      ],
      "transferable_strengths": [
        "짧은 핵심 요약을 먼저 제시",
        "속보형 키워드와 투자자 반응 포인트를 빠르게 연결",
        "반복 방문을 만드는 체크포인트 중심 구성"
      ]
    }
  ],
  "style_translation_rules": [
    "특정 사이트의 표현이나 문장 구조를 복사하지 않는다.",
    "전달력과 구조만 참고하고, 한국어 개인 투자자 독자에게 맞게 다시 쓴다.",
    "검색형 설명글과 재방문형 해설글을 함께 설계한다.",
    "뉴스 요약만 하지 말고 항상 '그래서 내 돈 관점에서 왜 중요한가'를 답한다."
  ]
}
```
