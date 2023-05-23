from sqlalchemy import  Column, String

from db_config.database_config import  Base

class User(Base):
    __tablename__='user'

    id=Column(String, primary_key=True, index=True)
    first_name=Column(String,nullable=False)
    last_name=Column(String,nullable=False)
    email=Column(String,nullable=False)
    username=Column(String, unique=True, nullable=False)
    password=Column(String, unique=True, nullable=False)
    role=Column(String,nullable=False)