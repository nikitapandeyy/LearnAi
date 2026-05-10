#chain of thought
#few shot prompting here with prompts we are giving example also 
#in this we are doing zero_Shot prmpting whre we directly ask a qution or give task without any prior examples .
from openai import OpenAI
import json

client = OpenAI(
    api_key="AIzaSyAjdLD8uFH59v-B-clL3IDo3MS6jvTfO3o",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
System="""You are expert in ai and solve use queries based on start(what is input provided by user),plan(what ai plans for them) and output(result) 
rule: you give response in the format of json only 
json output
{"steps":start|plan|output,
"content":"string"}

examples:
start:what is (2+3)/10
plan:{"steps":plan,"content":lets solve this with bodmaas}
plan:{"steps":plan,"content":lets 2+3=5} 
plan:{"steps":plan,"content":then divide 5/10=0.5}
output:{"steps":"output","content":got ur output girl 0.5}"""

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    response_format={"type":"json_object"},#we have added this to justofy what json format we want
    messages=[
        {   "role": "system",
            "content":System
        },
        {
            "role": "user",
            "content": "what is the output of 3+5/12"
        }
    ]
)

print(response.choices[0].message.content)