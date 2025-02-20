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

print("ChatGPT: Hello!")
while True:
    print("Please choose a personality: nice, sarcastic, or smart.")
    chosen_personality = input("You: ").strip().lower()

    if chosen_personality not in personalities:
        print("ChatGPT: I didn't recognize that.")
    else:
        break

print("ChatGPT: Great choice! Let's start chatting. Type 'quit' to exit.")

chat_log = [
    {"role": "system", "content": personalities[chosen_personality]}
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