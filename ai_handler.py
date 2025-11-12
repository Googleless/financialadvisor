import os
import json
from openai import OpenAI
from dotenv import load_dotenv
from flask import session

#loads ai api keys
load_dotenv()

with open("tools.json", "r", encoding="utf-8") as f:
    tools = json.load(f)

api_keys = {
    'deepseek': os.environ.get('OPENAI_API_KEY'),
    'openrouter': os.environ.get('OPENROUTER_API_KEY')
}

def run_openrouter(user_input, api_key):
    client = OpenAI(api_key=api_key, base_url="https://openrouter.ai/api/v1")
    response = client.chat.completions.create(
        model="tngtech/deepseek-r1t-chimera:free",
        messages=[
            {"role": "system", "content": "Ты — финансовый ассистент Землянского Филиппа Олеговича. Твоя задача — составить новостную сводку по новостям Сбербанка, Магнита и общих тенденций на рынке. Не давай финансовых советов."},
            {"role": "user", "content": user_input},
        ],
    )
    return response.choices[0].message.content


def run_deepseek(user_input, api_key):
    client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "Ты — финансовый ассистент Землянского Филиппа Олеговича. Твоя задача — составить подробный, но не длинный и затянутый, отчет о запрошенной теме с ссылками на источники. Ты будешь показывать только самую достоверную и актуальную информацию к запросу."},
            {"role": "user", "content": user_input},
        ],
        temperature=1,
        tools=tools
    )
    return response.choices[0].message.content

def run_model():
    current_agent = session.get('ai_agent', 'deepseek')
    user_input = session.get('user_input', 'Привет, сообщи мне новости за прошедшую неделю.')
    api_key = api_keys.get(current_agent)

    if current_agent == 'openrouter':
        return run_openrouter(user_input, api_key)
    else:
        return run_deepseek(user_input, api_key)
