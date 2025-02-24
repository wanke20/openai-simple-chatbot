import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

with open("prompts.json", "r") as file:
    roles = json.load(file)

print("ChatGPT: Hello!")
while True:
    print("Please choose your role: student, tutor, or administrator.")
    user_role = input("You: ").strip().lower()

    if user_role not in roles:
        print("ChatGPT: I didn't recognize that.")
    else:
        break

print("ChatGPT: Got it! I'll tailor my responses accordingly and provide links when relevant. Type 'quit' to exit.")

chat_log = [
    {"role": "system", "content": roles[user_role]}
]

while True:
    user_message = input("You: ")
    if user_message.lower() == "quit":
        print("ChatGPT: Goodbye! Have a great day!")
        break
    else:
        chat_log.append({"role": "user", "content": user_message})
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=chat_log
        )
        assistant_response = response.choices[0].message.content
        print("ChatGPT:", assistant_response.strip("\n").strip())
        chat_log.append({"role": "assistant", "content": assistant_response.strip("\n").strip()})
