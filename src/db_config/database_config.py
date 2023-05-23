import os
from dotenv import load_dotenv

from sqlalchemy import  create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

SQLALCHEMY_DATABASE_URL = str(os.getenv("DB_URL"))

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={}, future=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)

Base = declarative_base()

# Get DB instance
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()