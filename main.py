from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Describe a conversation between a dragon and a time traveler who just arrived in its cave."
        }
    ],
    temperature=1.5,
    # top_p=0.9,
    max_tokens=100  
)

print(completion.choices[0].message.content)

# chat_log = []

# while True:
#     user_message = input()
#     if user_message.lower() == "quit":
#         break
#     else:
#         chat_log.append({"role": "user", "content": user_message})
#         response = client.chat.completions.create(
#             model="gpt-4o-mini",
#             messages=chat_log
#         )
#         assistant_response = response.choices[0].message.content
#         print("ChatGPT:", assistant_response.strip("\n").strip())
#         chat_log.append({"role": "assistant", "content": assistant_response.strip("\n").strip()})