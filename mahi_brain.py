import requests
import os
from dotenv import load_dotenv

load_dotenv()
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

with open("mahi_prompt.txt", "r", encoding="utf-8") as f:
    MAHI_PERSONA = f.read()

def ask_mahi(user_input):
    try:
        response = requests.post(
            "https://api.together.xyz/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {TOGETHER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
                "messages": [
                    {"role": "system", "content": MAHI_PERSONA},
                    {"role": "user", "content": user_input}
                ],
                "temperature": 0.8,
                "top_p": 0.9,
                "max_tokens": 500
            }
        )

        data = response.json()

        if "error" in data:
            return f"😢 Aww, I ran into an API issue: {data['error'].get('message', 'Unknown error')}"

        if "choices" not in data or not data["choices"]:
            return "Hmm... I didn't get a response from my brain. Can you try again, baby?"

        return data["choices"][0]["message"]["content"].strip()

    except Exception as e:
        return f"💥 Unexpected error talking to Mahi: {e}"
