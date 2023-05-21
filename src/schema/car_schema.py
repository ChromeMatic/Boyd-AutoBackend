from typing import Optional
from pydantic import BaseModel
from uuid import UUID, uuid4 


class Car(BaseModel):
    id: Optional[UUID] = uuid4()
    make:str
    model:str
    year:str
    mileage:str
    price:str

    class Config:
        orm_mode = True