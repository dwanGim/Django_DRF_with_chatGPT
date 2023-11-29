import openai
from django.conf import settings

openai.api_key = settings.APIKEY

def send_code_to_api(code):
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": " You are an dev"},
            {"role": "user", "content": "tell me what language is this code written? {code}"},
            
        ],
    )
    return res["choices"][0]["message"]["content"]