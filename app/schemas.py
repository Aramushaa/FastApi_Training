from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional

#---------------post schema---------------
class UserResponse(BaseModel):
    email:EmailStr
    id:int
    created_at:datetime
    class Config:
        from_attributes = True

class PostBase(BaseModel):
    title:str
    content:str
    published:bool=True

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id:int
    created_at:datetime
    owner_id:int
    owner:UserResponse
    class Config:
        from_attributes = True

#---------------user schema---------------


class UserCreate(BaseModel):
    email:EmailStr
    password:str



class UserLogin(BaseModel):
    email:EmailStr
    password:str


class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    id:Optional[int] = None
