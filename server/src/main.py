from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import user
from .database import engine
from . import models

models.base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(user.router)
