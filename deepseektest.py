import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.environ.get('OPENROUTER_API_KEY'), base_url="https://openrouter.ai/api/v1")

response = client.chat.completions.create(
    model="tngtech/deepseek-r1t-chimera:free",
    messages=[
        {"role": "system", "content": "Ты - финансовый ассистент Землянского Филиппа Олеговича. Твоя задача - составить новостную сводку по новостям Сбербанка, Магнита и общих тенденций на рынке. Ты не будешь давать финансовые советы."},
        {"role": "user", "content": "Привет, сообщи мне новости за прошедшую неделю ноября."},
    ],
)

print(response.choices[0].message.content)