from fastapi import APIRouter

user_router = APIRouter()

@user_router.get("/api/v1/user")
async def get_users():
    return "users"

@user_router.get("/api/v1/user/{id}")
async def get_users_by_id(id:str):
    return {id}