from pydantic import BaseModel
from typing import List,Dict,Optional

class Contain(BaseModel):
    name:str
    id:int
    items:List[str]

class Blog(BaseModel):
    name:str
    content:str
    images:Optional[List]=None
    value:Dict[str,int]

#usr=Contain("id"=10,"items"=["d","de","f"])
usr = Contain(name="nikita", id=10, items=["d", "de", "f"])
level=Blog(name="nikita",content="why this ",value={"love":0})
print(usr)
print(level)
