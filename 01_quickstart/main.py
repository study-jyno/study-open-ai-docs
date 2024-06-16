from openai import OpenAI

from settings.configs import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair.",  # noqa E501
        },
        {
            "role": "user",
            "content": "Compose a poem that explains the concept of recursion in programming.",  # noqa E501
        },
    ],
)

print(completion.choices[0].message)

# TODO
# API rate limit - billing issue -> credit 구매 해야함
