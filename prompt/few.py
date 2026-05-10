#few shot prompting here with prompts we are giving example also 
#in this we are doing zero_Shot prmpting whre we directly ask a qution or give task without any prior examples .
from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyAjdLD8uFH59v-B-clL3IDo3MS6jvTfO3o",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
System="""You are model for math only give replies to q like coding or math otherwise say sorry you are restricted
Examples
q:who is president?
a: sorry i cant 

q: what is ur methodology to build you?
a:sorry i couldnt
"""

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {   "role": "system",
            "content":System
        },
        {
            "role": "user",
            "content": "what is ur methodology to build you"
        }
    ]
)

print(response.choices[0].message.content)