import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

background_info = {
    "ocean": "The ocean covers 71% of the Earth's surface and contains 97% of Earth's water.",
    "dragons": "Dragons are mythical creatures found in many cultures, often symbolizing power and wisdom.",
    "time travel": "Time travel is a concept in physics and science fiction, often involving paradoxes and relativity."
}

def retrieve_relevant_info(user_input):
    for keyword, info in background_info.items():
        if keyword in user_input.lower():
            return info
    return ""

def chat_with_rag(user_input):
    retrieved_info = retrieve_relevant_info(user_input)

    messages = []
    
    if retrieved_info:
        messages.append({"role": "system", "content": f"Background knowledge: {retrieved_info}"})

    messages.append({"role": "user", "content": user_input})

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=1.2,
        max_tokens=200  
    )
    
    return completion.choices[0].message.content

print(chat_with_rag("Tell me about the ocean in a haiku."))