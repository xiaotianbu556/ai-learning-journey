import json
import requests

API_URL = "https://api.deepseek.com/chat/completions"


def read_api_key():
    with open("api_key.txt", "r", encoding="utf-8") as f:
        return f.read().strip()


def extract_info(text, api_key):
    """调用 DeepSeek，从简历文字中提取 姓名/城市/技能，返回 JSON 字符串"""
    messages = [
        # 咒语一：system 设定角色
        {"role": "system", "content": (
            "你是简历信息提取助手。从用户提供的自我介绍中提取：姓名、城市、技能。"
            "技能可能有多项，用列表存放。"
            "只输出 JSON，不要输出任何多余文字。"
            "格式：{\"姓名\": \"...\", \"城市\": \"...\", \"技能\": [\"...\"]}"
        )},
        # 咒语二：few-shot 给格式示例
        {"role": "user", "content": "我叫李雷，来自上海，熟练使用 Python 和 Excel，还会一点 SQL。"},
        {"role": "assistant", "content": "{\"姓名\": \"李雷\", \"城市\": \"上海\", \"技能\": [\"Python\", \"Excel\", \"SQL\"]}"},
        {"role": "user", "content": "王芳，北京人，做财务的，擅长 Excel、PPT 和用友软件。"},
        {"role": "assistant", "content": "{\"姓名\": \"王芳\", \"城市\": \"北京\", \"技能\": [\"Excel\", \"PPT\", \"用友软件\"]}"},
        # 用户输入放最后
        {"role": "user", "content": text},
    ]
    resp = requests.post(
        API_URL,
        headers={"Authorization": f"Bearer {api_key}"},
        json={"model": "deepseek-chat", "messages": messages},
        timeout=60,
    )
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]


def main():
    api_key = read_api_key()
    print("请逐行粘贴一段自我介绍/简历文字（输入 q 退出）：")
    while True:
        text = input().strip()
        if text == "q":
            break
        reply = extract_info(text, api_key)
        # 防御：AI 可能输出多余文字导致解析失败
        try:
            info = json.loads(reply)
        except json.JSONDecodeError:
            print("解析失败，AI 的原始回复如下，方便排查：")
            print(reply)
            continue
        print("姓名：" + info["姓名"])
        print("城市：" + info["城市"])
        print("技能：" + " / ".join(info["技能"]))


main()
