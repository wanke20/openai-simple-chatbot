import os, json
from dotenv import load_dotenv
from openai import OpenAI
import anthropic

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

openai_client = OpenAI(api_key=openai_api_key)
anthropic_client = anthropic.Anthropic(api_key=anthropic_api_key)

with open("prompts.json", "r") as file:
    roles = json.load(file)

print("System: Hello!")
while True:
    print("Please choose your role: student, tutor, or administrator.")
    user_role = input("You: ").strip().lower()

    if user_role not in roles:
        print("System: I didn't recognize that.")
    else:
        break

print("System: Got it! I'll tailor my responses accordingly and provide links when relevant. Type 'quit' to exit.")

chat_log = [
    {"role": "system", "content": roles[user_role]}
]

while True:
    user_message = input("You: ").strip()
    
    if user_message.lower() == "quit":
        print("System: Goodbye! Have a great day!")
        break

    chat_log.append({"role": "user", "content": user_message})

    # OpenAI API Response
    openai_response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=chat_log
    )
    openai_reply = openai_response.choices[0].message.content.strip()
    print("ChatGPT: ", openai_reply, end="\n\n")

    # Anthropic API Response
    anthropic_response = anthropic_client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=300,
        messages=[{"role": "user", "content": [{"type": "text", "text": user_message}]}]
    )

    claude_reply = "\n".join(block.text for block in anthropic_response.content if block.type == "text")
    print("Claude: ", claude_reply)

    chat_log.append({"role": "assistant", "content": openai_reply})
    chat_log.append({"role": "assistant", "content": claude_reply})
