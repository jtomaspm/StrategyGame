from ..models.login_model import LoginModel
from ..models.register_model import RegisterModel


def login(credentials: LoginModel):

    return {"status": "Logged in"}

def register(credentials: RegisterModel):
    return {"status": "Registered"}