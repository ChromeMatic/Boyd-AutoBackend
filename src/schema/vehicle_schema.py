from typing import Optional
from pydantic import BaseModel
from uuid import UUID, uuid4 


class VehicleImageSchema(BaseModel):
    id: Optional[UUID]
    name: str

    class Config:
        orm = True

class VehicleScheme(BaseModel):
    id: Optional[UUID]
    make:str
    model:str
    year: int
    mileage: float
    price:float

    class Config:
        orm_mode = True