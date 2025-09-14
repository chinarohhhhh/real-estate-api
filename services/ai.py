import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Get API key securely from .env
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Simple test
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful AI assistant for real estate.",
        },
        {
            "role": "user",
            "content": "Hello! Can you help me find a 2-bedroom apartment in Nairobi?",
        },
    ],
)

print(response.choices[0].message.content)
