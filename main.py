from fastapi import FastAPI
from models.users import users_model
from routes.users import users_router
from routes.login import login_router
from models.database import engine

from fastapi.middleware.cors import CORSMiddleware
from decouple import config

app = FastAPI(
    title="OneUser",
    description="The Single Sign-on API",
    version="1.0",
)
origins = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    config('VIEWER_URL')
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(login_router.router)
# app.include_router(users_router.router)


@app.get("/")
async def root():
    return {"message": "What's up?"}


