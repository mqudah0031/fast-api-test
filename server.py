from fastapi import FastAPI
from auth import auth
import db

app = FastAPI()

app.include_router(auth.router, prefix="/auth")
