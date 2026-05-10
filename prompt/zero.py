#in this we are doing zero_Shot prmpting whre we directly ask a qution or give task without any prior examples .
from openai import OpenAI
import json
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    api_key="OPENAI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
System="You are model for math only give replies to q like coding or math otherwise say sorry you are restricted"
response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {   "role": "system",
            "content":System
        },
        {
            "role": "user",
            "content": "tell me a joke"
        }
    ]
)

print(response.choices[0].message.content)