from typing import Optional
from pydantic import BaseModel
from uuid import UUID, uuid4 


class UserSchema(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    email: str
    username: str
    password: str

    class Config:
        orm_mode = True

class UserCredentials(BaseModel):
    username:str
    password:str