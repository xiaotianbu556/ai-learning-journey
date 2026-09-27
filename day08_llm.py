import requests

with open("api_key.txt", "r", encoding="utf-8") as f:
    API_KEY = f.read().strip()

url = "https://api.deepseek.com/chat/completions"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}
data = {
    "model": "deepseek-chat",
    "messages": [
        {"role": "user", "content": "你好，请用一句话向一个零基础学编程的人介绍你自己"}
    ]
}

resp = requests.post(url, headers=headers, json=data)
result = resp.json()
print(result["choices"][0]["message"]["content"])