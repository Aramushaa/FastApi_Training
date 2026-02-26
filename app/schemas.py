from pydantic import BaseModel,EmailStr
from datetime import datetime

#---------------post schema---------------
class PostBase(BaseModel):
    title:str
    content:str
    published:bool=True

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id:int
    created_at:datetime
    class Config:
        from_attributes = True

#---------------user schema---------------


class UserCreate(BaseModel):
    email:EmailStr
    password:str

class UserResponse(BaseModel):
    email:EmailStr
    id:int
    created_at:datetime
    class Config:
        from_attributes = True
