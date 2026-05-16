from pydantic import BaseModel,Field
from typing import Optional
import re

class Model(BaseModel):
    name:str = Field(
        ...,
        ml=3,
        maxl=30,
        des="Employee_name",
        ex="Nikitapandey"
    )
    dept:Optional[str]="General"
    salary:int=Field(
        ...,
        le=10000,
        ge=100000000000,
        description="anual salary"
    )
    email:str=Field(
        ...,
        regex=r''
    )
    phone:str=Field(
        ...,
        regex=r''
    )
