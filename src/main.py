from fastapi import FastAPI
from router import user, automobile

app = FastAPI(
    title="Boyd-Auto Rest-API Backend",
    description="This application provides restful api endpoints for the frontend application.",
    version="0.0.1"
)

@app.get("/")
def server():
    return "server up & running."

app.include_router(user.user_router)
app.include_router(automobile.automobile_router)