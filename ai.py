# services/ai.py
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
print("Loaded API key:", api_key)

client = OpenAI(api_key=api_key)


def ask_ai(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful real estate assistant.",
                },
                {"role": "user", "content": prompt},
            ],
        )
        return response.choices[0].message["content"]

    except Exception as e:
        return f"Error communicating with AI: {e}"
