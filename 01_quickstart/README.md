# 1. Quickstart

https://platform.openai.com/docs/quickstart


## 1. install
python 라이브러리 설치

가이드는 venv, pip 를 사용했지만 poetry 사용하겠음

```shell
poetry init

poetry add openai
```

## 2. Set Api key
전역 환경 변수로 관리하거나, .env 사용해도 됨
나는 .env 사용하겠음 - pydantic setting install

```shell
poetry add pydantic
poetry add pydantic-settings
```

키 생성은 가이드 따를 것

## 3. Sending Your First API Request

```python
from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)
```
