from sqlalchemy.util import deprecated
from fastapi import FastAPI,Response,status,HTTPException,Depends
from fastapi.params import Body
from random import randrange
import psycopg
from psycopg.rows import dict_row
import time
from .database import engine,get_db
from . import models,schemas
from sqlalchemy.orm import Session
from typing import List



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

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/posts",response_model=List[schemas.PostResponse])
def get_posts(db:Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts""")
    # posts = cursor.fetchall()
    posts = db.query(models.Post).all()
    return posts

@app.post("/posts",response_model=schemas.PostResponse,status_code=status.HTTP_201_CREATED)
async def create_posts(post:schemas.PostCreate,db:Session = Depends(get_db)):
    # cursor.execute(""" INSERT INTO posts (title,content,published) VALUES (%s,%s,%s) RETURNING *""",
    # (post.title,post.content,post.published))
    # new_post = cursor.fetchone()
    # conn.commit()
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@app.get("/posts/{id}",response_model=schemas.PostResponse)
def get_post(id:int,db:Session = Depends(get_db)):
    # cursor.execute(""" SELECT * FROM posts WHERE id = %s """,(id,))
    # post = cursor.fetchone()
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} not found")
    return post


@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db:Session = Depends(get_db)):
    # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""",(id,))
    # deleted_post = cursor.fetchone()
    # conn.commit()
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} not found")
    db.delete(post)
    db.commit()
    return Response( status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}",response_model=schemas.PostResponse)
def update_post(id:int,updated_post:schemas.PostCreate,db:Session = Depends(get_db)):
    # cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""",
    # (post.title,post.content,post.published,id))
    # updated_post = cursor.fetchone()
    # conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} not found")
        
    post_query.update(updated_post.dict(),synchronize_session=False)
    db.commit()
    return post_query.first()

#------------------------------- user related routes -------------------------------

@app.post("/users",response_model=schemas.UserResponse,status_code=status.HTTP_201_CREATED)
def create_user(user:schemas.UserCreate,db:Session = Depends(get_db)):
    # hash the password - user.password
    hashed_password = pwd_context.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
