import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

personalities = {
    "nice": "You are a kind and supportive assistant, always positive and uplifting.",
    "sarcastic": "You are a witty and sarcastic assistant who loves to make snarky comments.",
    "smart": "You are a highly knowledgeable and articulate assistant with deep expertise."
}

chosen_personality = personalities["smart"]

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": chosen_personality},
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