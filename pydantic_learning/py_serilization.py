from pydantic import BaseModel,ConfigDict
from datetime import datetime

class Adress(BaseModel):
    street:str
    post:str

class User(BaseModel):
    name:str
    email:str
    is_active:bool
    adrs:Adress
    createdAt:datetime

    model_config=ConfigDict(
        json_encoders={ datetime : lambda v:v.strftime('%d-%m-%Y %H:%M:$S' )

        }
    )

user =User(
    name="nikita",
    email="jbhyg",
    is_active=True,
    adrs=Adress(
        street="hg",
        post="jhb"
    ),
    createdAt=datetime(32,4,3,2,13,2)

)
print(user)
print("="*30)
print(user.model_dump())
print("="*30)
print(user.model_dump_json())

