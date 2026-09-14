import os
import requests

token = os.environ["HF_TOKEN"]

headers = {
    "Authorization": f"Bearer {token}"
}

prompt = """
Create one original YouTube Shorts idea about unusual animals.
Give me:
1. A strong 2-second hook
2. A 30-45 second script
3. A short title

Do not copy an existing video.
"""

response = requests.post(
    "https://router.huggingface.co/v1/chat/completions",
    headers=headers,
    json={
        "model": "Qwen/Qwen2.5-7B-Instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 500
    }
)

response.raise_for_status()

result = response.json()["choices"][0]["message"]["content"]

print(result)
