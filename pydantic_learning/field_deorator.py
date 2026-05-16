from pydantic import BaseModel,Field_validator,model_validator

class username(BaseModel):
    username:str

    @Field_validator('username')
    def username_len(cls,v):
        if len(v)<4:
            raise ValueError("password greter than 4")
        return v
    
class passwd(BaseModel):
    curr_pswd:str
    knw_passwd:str

    @model_validator(mode='after')
    def psswrd_Check(cls,values):
        if values.curr_pswd!=values.knw_passwd:
            raise ValueError("passwrd mismatched")
        return values


