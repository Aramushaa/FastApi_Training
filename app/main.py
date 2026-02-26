from sqlalchemy.util import deprecated
from fastapi import FastAPI,Response,status,HTTPException,Depends
from fastapi.params import Body
from random import randrange
import psycopg
from psycopg.rows import dict_row
import time
from .database import engine,get_db
from . import models,schemas,utils
from sqlalchemy.orm import Session
from typing import List
from .routers import post,user



models.Base.metadata.create_all(bind=engine)




app=FastAPI()



while True:
    try:
        conn = psycopg.connect(host="localhost", dbname="Fastapi", user="postgres", password="ARash1990",row_factory=dict_row)
        cursor = conn.cursor()
        print("Database connection successful")
        break
    except Exception as e:
        print("Database connection failed")
        print("error: ",e)
        time.sleep(2)


my_posts=[{"title":"my first post","content":"today learning 1","published":True,"rating":5,"id":1},{"title":"my second post","content":"today learning 2","published":True,"rating":5,"id":2}]

def find_post(id):
    for post in my_posts:
        if post['id']==id:
            return post

def index_of_post(id):
    for i,p in enumerate(my_posts):
        if p['id']==id:
            return i


app.include_router(post.router)
app.include_router(user.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


