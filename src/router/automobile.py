from fastapi import APIRouter

automobile_router = APIRouter()

@automobile_router.get("/api/v1/cars")
async def get_cars():
    return []

@automobile_router.get("/api/v1/cars/{Id}")
async def get_cars_by_id(Id:str):
    return {}
