## Section 2 시작하기

### Token

```
토큰으로 분할되며 토큰은 평균적으로 문자가 네 개지만 다양한 문자 수로 이뤄진다.
그리고 토큰은 가격 책정 면에서 정말 중요하다.
OpenAI에서는 생성되는 입력 토큰과 출력 토큰을 합하여 모델마다 다양한 가격을 청구하기 때문이다. 
```

### API Document
- [document](https://platform.openai.com/docs/api-reference/chat/create)

### Max_Token
- API 에 어떤 값을 지정하지 않으면 16토큰으로 반환
- [document](https://platform.openai.com/docs/api-reference/chat/create#chat/create-max_tokens)

### Stop

### N

### Echo
- 답변에 질문이 포함되게 하느냐 여부
- Echo 를 True 로 설정해 질문을 답변에 같이 받아도 실제 api 토큰 데이터를 가져온뒤 합치기 떄문에 total_tokens 에 포함되지 않아 가격에는 지장이없다.

### GPT - 3.5 & GPT - 4
- GPT 3.5는 새로운 버전의 모델이 아니다.
- GPT-3 에서 수정 및 향상된 버전이다.

### 모델 정보


## Section 3 프롬프트 엔지니어링

### Prompt Design

- 지침을 주는게 매우 중요하다.
  - 모호하거나 불명확한 말을 줄이고 가능한 직접적이고 명확한 지침을 제공하자.

- DB, 개발언어 데이터를 우너하는 형식으로 답변을 얻는것도 가능하다.
  - sql 문으로 하던 CSV 파일에 붙이게 쉽게 하던, JSON 으로 출력 등

### Completion API 모델의 사용 사례
- 요약, 분류
  - 예시) 위키 피디아 요약
- 데이터 추출
  - 예시 ) 구글 지도 리뷰 에서 인기 메뉴 추출
- 감성 분석
  - 예시 ) 구글 지도 리뷰 에서 긍정, 중립, 부정 분석

### Zero-Shot vs Few-Shot 

- 주어진 프롬프트에 제공되는 예시에 개수에 관계가 있다.

- Zero-shot: 예시없이 질문만 할때

- Few-Shot: 몇가지 예시를 제공하면서 학습 및 질문을 하는 방법

### 스텝 바이 스텝으로 사고하기 프롬프팅

- Let's think step by step

- 논리적 추론이 필요한 프롬프트에서 사용하면 정답을 맞출 확률이 올라간다.

### 텍스트 변형 프롬프트

- 특정 단어를 다른 단어로 변형할수있다.
- 예시 ) 번역, 1인칭에서 3인칭으로 변형, 단어에서 이모지로 변경

## Section 4 색 팔레트 생성기 프로젝트

- TODO: 프로젝트 완성 후 링크

## Section 5 주요 API 매개변수

### Temperature

- TODO: Temperature 설정에 대한 이미지 첨부 및 설명

- 같은 질문을 하면서 Temperature 를 조정하면서 창의성 및 다양한 답을 확인할수있다.

- 0 ~ 2 까지 지정가능 하지만 0 ~ 1 만 사용한다.
  - 테스트를 해보면 알수있지만 1 이상으로 올리게 되면 답변이 생각보다 창의적이고 무작위성이 크다.

```
question

nice_print(
    {
        f"Temperature {temperature}": openai.Completion.create(model="text-davinci-003", prompt="""My favorite food is""".strip(), max_tokens=75, echo=True, temperature=temperature)
        .choices[0]["text"]
        .strip()
        for temperature in [0, 0.5, 1, 1.5, 2]
    }
)

answer

Temperature 0:
My favorite food is pizza. I love the combination of the doughy crust, the tangy tomato sauce, and the melty cheese. I
also like to add different toppings like pepperoni, mushrooms, and olives. Pizza is a great meal for any occasion,
whether it's a casual night in or a special celebration.
========================================================================================================================
Temperature 0.5:
My favorite food is pizza. I love the combination of cheese, sauce, and dough that make a delicious pizza. I also love
to add different toppings like pepperoni, sausage, mushrooms, and onions to customize my pizza. I also like to try
different kinds of pizza, like deep dish, thin crust, and stuffed crust. Pizza is a great meal that is easy to make, and
========================================================================================================================
Temperature 1:
My favorite food is pizza. I love the combination of cheese, sauce, and dough. It is something I could eat every day.
There are endless topping combinations to experiment with, making it a versatile dish. It is also very easy to make at
home.
========================================================================================================================
Temperature 1.5:
My favorite food is Burgers. I love making them at home on a homemade bun with some fresh tomatoes, lettuce onions and
pickles and plenty of melted cheddar cheese and creamy avocado. Whenever possible I find myself sneaking in a petite
onion to overpower special aspects that store brought manufacturers ofmass produced burgers cannot show  Apart from
burgers I also love making chowe monds with assorted beans
========================================================================================================================
Temperature 2:
My favorite food is steamed king crab, with partons newbered comrie linenasseter basieu cookies sprinkled over it.
Serveed liddled thybes tourmangan mineader hatuaooterted witster mul of carved derbis lemund butter showerdone catane
helliveo.   The sight and aroma of those flavoursight will make both adults and coastal gourdm
========================================================================================================================

```

### Top P

- TODO: 내용 정리

### Frequency Penalty, Presence Penalty

- TODO: 내용 정리

- 반복적인 결과를 줄이기 위한 매개변수

- -2 ~ 2 까지 설정가능하다.
  - 1보다 큰 값을 사용하기를 권장하지 않는다.
  
- TODO: 2개의 차이 추가

### Stream

- TODO: 내용정리

## Section 6 Chat api 와 GPT-4

- TODO: 전체 강의 정리 필요

## Section 7 GPT-4 챗봇 만들기

- 챗봇 만들기 프로젝트
  - python 으로 질문을 하고 응답을 받는 챗봇을 개발
  - 챗봇에 성격을 부여하고 텍스트에 색상을 스타일링

```python
python chatbot.py
python chatbot.py --personality "silly and goofy"
```

## Section 8 GPT-4로 코드 작업하기

- 코드 설명 요청하기
  - 정상적인 함수를 보내고 파라미터와 함수의 기능의 설명을 확인
- 시간 복잡도 계산하기
  - 버블 정렬, 퀵정렬 함수명을 숨기고 보내서 정확하게 계산하는지 확인
- JS 를 파이썬으로 변환하기
  - 함수명 들을 mystery 및 설정하지 않고 보내서 기능이 정상적으로 돌아가는지 확인
- 코드 버그 수정하기
  - 함수명과 다른 결과같은 내는 함수를 메시지로 보내고 수정요청을 진행하여 확인
  - 구문에러를 발생시키고 수정요청을 진행하여 확인
- 처음부터 코드 작성하기
  - tmi: 모든 코드를 얻으려는 곳으로 생각하지 말고 시작점과 아이디어를 얻을수있는 곳으로 생각하자.
  - 설명만으로 코드를 코딩해주는지 확인

- tmi: Codex 라는 코드 관련 모델이 잇었지만 GPT-3.5 터보와 GPT-4 가 나오면서 사용중지 되었다.

