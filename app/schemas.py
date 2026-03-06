from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional
from pydantic import conint


class UserResponse(BaseModel):
    email:EmailStr
    id:int
    created_at:datetime
    class Config:
        from_attributes = True
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
    owner_id:int
    owner:UserResponse
    class Config:
        from_attributes = True

class PostOut(BaseModel):
    Post: PostResponse
    votes: int

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

#---------------vote schema---------------

class Vote(BaseModel):
    post_id:int
    dir:conint(le=1,ge=0)

