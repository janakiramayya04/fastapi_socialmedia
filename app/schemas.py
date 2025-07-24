from pydantic import BaseModel
from typing import Optional

class PostBase(BaseModel):
    title: str
    content: str
    published: Optional[bool] = True # Default for the incoming request body

class PostCreate(PostBase):
    pass # If you need additional fields for creation only

class Post(PostBase): 
    id: int
    class config:
        orm_mode=True