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

## 출력 형식

1. 제목
2. 한 줄 요약
3. 도입부
4. 본문
5. 체크포인트 3개
6. FAQ 2개
7. CTA
8. 면책문구

## 참고 샘플 글

- `templates/sample_post_macro_explainer.md`
- `templates/sample_post_crypto_analysis.md`
- `templates/sample_post_sector_analysis.md`

위 샘플들은 좋은 톤과 문단 리듬의 기준점이다.

- 문장을 그대로 복사하지 않는다.
- 도입부의 온도, 본문 설명 방식, 마무리의 균형감만 참고한다.
- 지나치게 모범답안처럼 딱딱한 보고서체로 쓰지 않는다.

## 입력 패킷

```json
{
  "keyword": "oil",
  "recommended_title": "유가 흐름 해설",
  "alternate_titles": [
    "유가 흐름 해설: 지금 시장이 반응하는 이유",
    "유가 흐름 해설와 주식·코인 흐름 함께 보기"
  ],
  "summary_angle": "검색 트렌드 반응 존재, 복수 소스 교차 확인 가능 (5개), 거시 해설형 글로 전환 가치 높음, 실제 급상승 검색어 반영 (유조선)",
  "outline": [
    "왜 지금 이 이슈가 중요한가",
    "실제로 발표되거나 벌어진 일",
    "주식·코인·달러·금리에 주는 영향",
    "앞으로 체크할 변수",
    "개인 투자자가 볼 포인트"
  ],
  "reference_takeaways": [],
  "fact_checks": [
    "WTI/Brent 수치 재확인",
    "공급 뉴스 원문 출처 확인",
    "인플레이션/금리 연결 문장 점검"
  ],
  "disclaimer": "이 글은 정보 제공 및 학습용 정리이며, 특정 자산에 대한 투자 권유나 자문이 아닙니다. 시장 데이터와 제도는 작성 시점 이후 달라질 수 있으므로 실제 투자 전에는 최신 공식 자료를 다시 확인해야 합니다.",
  "cta": "이런 거시 이벤트 해설을 꾸준히 받고 싶다면 다음 글도 이어서 확인해 보세요.",
  "source_names": [
    "CNBC Top News",
    "CoinDesk RSS",
    "Financial Times Home",
    "Google Trends KR",
    "Reuters Markets via Google News RSS"
  ],
  "reference_headlines": [
    "유조선",
    "Bitcoin back above $60,000, ETH, SOL recoup losses as AI stocks stage rebound",
    "Oil prices erase wartime gains as supply concerns ease with Hormuz tanker traffic resuming",
    "Oil price back at prewar levels as Gulf flows pick up",
    "They think it’s oil over"
  ],
  "voice_profile": "뉴스 브리핑보다 가까운 설명형 톤. 거시 이슈를 친구에게 풀어주듯 쓰되 숫자와 출처는 정확하게.",
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
    "왜 지금 이 이슈가 개인 투자자에게 중요한지 한 문장 설명",
    "달러, 금리, 주식, 코인 중 최소 2개와 연결한 해석",
    "다만/반면 같은 균형 문장"
  ],
  "voice_examples": {
    "intro_example": "미국 기준금리 이야기는 멀게 느껴질 수 있습니다. 그런데 막상 시장이 흔들릴 때는 이 이슈가 달러, 나스닥, 비트코인까지 한 번에 건드리는 경우가 많습니다. 투자자 입장에서 보면 결국 중요한 건 발표 그 자체보다, 그 발표가 자금 흐름을 어떻게 바꾸느냐입니다.",
    "analysis_example": "쉽게 말해 시장은 숫자 하나만 보는 게 아닙니다. 같은 금리 동결이어도 연준이 앞으로 어떤 표정을 짓는지에 따라 달러가 움직이고, 그다음에 성장주와 코인이 반응할 수 있습니다. 그래서 headline만 보고 끝내면 흐름을 놓치기 쉽습니다.",
    "closing_example": "여기서 진짜 봐야 할 건 다음 이벤트입니다. 이번 발표가 끝이 아니라, 다음 CPI나 고용지표에서 같은 방향이 확인되는지가 더 중요할 수 있습니다."
  },
  "score_breakdown": {
    "total_score": 89.0,
    "search_score": 30,
    "timeliness_score": 21,
    "explanatory_score": 18,
    "monetization_score": 15,
    "risk_score": 5
  }
}
```
