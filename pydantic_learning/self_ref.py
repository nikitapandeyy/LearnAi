from pydantic import BaseModel
from typing import List,Optional

class Comment(BaseModel):
    id:int
    content:str
    reply:Optional[List["Comment"]]=None

Comment.model_rebuild()

comment=Comment(
    id=1,
    content="this is hillarious",
    reply=[
        Comment(id=2,content="wow u must be amazing "),
        Comment(id=2,content="no u are "),
        Comment(id=2,content="bye",reply=[])
    ]


)
print(comment)


