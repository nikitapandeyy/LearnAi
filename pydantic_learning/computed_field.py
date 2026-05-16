from pydantic import BaseModel,computed_field

class Hotel_mng(BaseModel):
    name:str
    night:int
    price:int
    room_id:int
    user_id:int
    @computed_field
    @property
    def calculateprice(self) ->float:
        return self.night*self.price
    
    

user=Hotel_mng(
    name="nikita",
    night=3,
    price=10000,
    room_id=567,
    user_id=7887
)

print(user.calculateprice)
print(user.model_dump())


