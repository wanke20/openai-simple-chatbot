import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Who was Alan Turing?"
        }
    ],
    temperature=1.5,
    # top_p=0.9,
    max_tokens=50  
)

print(completion.choices[0].message.content)