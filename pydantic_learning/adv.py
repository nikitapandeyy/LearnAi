from pydantic import BaseModel,field_validator,model_validator
from datetime import datetime

class Person(BaseModel):
    f_name:str
    l_name:str

    @field_validator(f_name,l_name)
    def nums_cap(cls,v):
        if not v.istitle():
            raise ValueError("name must be captilized")
        return v
    
class user(BaseModel):
    email:str
    @field_validator('email')
    def normalize(cls,v):
        return v.lower().strip()
    
class Product(BaseModel):
    price:str
    @field_validator('price')
    def parse(cls,v):
        if isinstance(v,str):
            return float(v.replace('$',"").replace(',',''))
        return v
    
class check_time(BaseModel):
    s_date:datetime
    e_date:datetime
    @model_validator(mode='after')
    def check(cls,v):
        if v.s_date>=v.end_date:
            raise ValueError("sorry cant be right")
        return v