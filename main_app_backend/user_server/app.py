from fastapi import FastAPI

from .models.login_model import LoginModel
from .models.register_model import RegisterModel
from .settings import *
from .services.user_service import login, register

app = FastAPI()

@app.post("/login/", response_model=None)
async def login_user(credentials: LoginModel):
    return login(credentials)


@app.post("/register/", response_model=None)
async def register_user(credentials: RegisterModel):
    return register(credentials)
