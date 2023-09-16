from fastapi import FastAPI

from .models.token import Token

from .models.payload_data import PayloadData
from .settings import TOKEN_DURATION_MINUTES

from .services.auth_service import AuthService

app = FastAPI()
auth_service = AuthService()

@app.post("/validate/", response_model=None)
async def validate(token: Token, ip_address: str):
    return auth_service.validate_token(token, ip_address)

@app.post("/login/", response_model=None)
async def generate_token(payload: PayloadData):
    return auth_service.generate_token(payload, TOKEN_DURATION_MINUTES)

@app.post("/refresh/", response_model=None)
async def refresh_token(token: Token):
    refreshed_token = auth_service.refresh_token(token, TOKEN_DURATION_MINUTES)
    return refreshed_token if refreshed_token else {"status": "Invalid"}

@app.post("/logout/", response_model=None)
async def logout(token: Token):
    auth_service.logout(token)
    return {"status": "Logged out"}

