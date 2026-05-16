from pydantic import BaseModel
from typing import List,Optional,Union

class Adress(BaseModel):
    street:str
    pst:str
    state:str

class User(BaseModel):
    name:str
    phone:int
    adr:Adress
adrs=Adress(street="value1",pst="7887",state="up")
user=User(name="nikita",phone=788778,adr=adrs)

user_data={
    'name':'nikita',
    'phone':'45343',
    'adr':{
        'street':'effe',
        'pst':'frwf',
        'state':"hu"
    }

}

print(user)
lan=User(**user_data)
print(lan)

class imagecontent(BaseModel):
    image:str="Image"
class textcontent(BaseModel):
    text:str="text"

class article(BaseModel):
    content:List[Union[imagecontent,textcontent]]
    