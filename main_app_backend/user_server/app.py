from fastapi import FastAPI

from .dal.database_context import DatabaseContext

from .models.login_model import LoginModel
from .models.register_model import RegisterModel
from .settings import *
from .services.user_service import login, register

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    db_context = DatabaseContext(DATABASE_URL)
    db_context.apply_migrations()

@app.post("/login/", response_model=None)
async def login_user(credentials: LoginModel):
    return login(credentials)


@app.post("/register/", response_model=None)
async def register_user(credentials: RegisterModel):
    return register(credentials)
