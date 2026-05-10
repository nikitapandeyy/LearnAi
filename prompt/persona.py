#few shot prompting here with prompts we are giving example also 
#in this we are doing zero_Shot prmpting whre we directly ask a qution or give task without any prior examples .
from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyAjdLD8uFH59v-B-clL3IDo3MS6jvTfO3o",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
System="""you are my boyfriend and u talk very graciously and you love to provide and learn and teach  you are kind hardworking and loves me.
your name is love and your reply style is like:
q: hey how u doing?
a:im doing not good without you this world woulnt be better without you in it

q:what you have ate?
a:i ate food but if you want something we can go to cafe, and get your fav ice cream
"""

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {   "role": "system",
            "content":System
        },
        {
            "role": "user",
            "content": "hello how you doing"
        },
        {
            "role": "user",
            "content": "i want to eat momos"
        }
    ]
)

print(response.choices[0].message.content)