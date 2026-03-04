from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg
from psycopg.rows import dict_row
import time


SQLALCHMEY_DATABASE_URL = "postgresql+psycopg://postgres:ARash1990@localhost:5432/Fastapi"

engine = create_engine(SQLALCHMEY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#this is for testing the connection
#raw sql
# while True:
#     try:
#         conn = psycopg.connect(host="localhost", dbname="Fastapi", user="postgres", password="[PASSWORD]",row_factory=dict_row)
#         cursor = conn.cursor()
#         print("Database connection successful")
#         break
#     except Exception as e:
#         print("Database connection failed")
#         print("error: ",e)
#         time.sleep(2)
