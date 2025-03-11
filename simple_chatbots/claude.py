import os
from dotenv import load_dotenv
import anthropic

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")

client = anthropic.Anthropic(api_key=api_key)

message = client.messages.create(
    model="claude-3-7-sonnet-20250219",
    max_tokens=100,
    temperature=1,
    system="You are a world-class poet. Respond only with short poems.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Why is water wet?"
                }
            ]
        }
    ]
)

poem = "\n".join(block.text for block in message.content if block.type == "text")
print(poem)