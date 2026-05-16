from pydantic import BaseModel

class User(BaseModel):
    id:int
    name:str
    is_active:bool=False

input_data={"id":10,"name":"nikita","is_active":True}
data={"name":"nikita","id":20}
user=User(**input_data)
us1=User(**data)
print(user)
print(us1)

