from contextvars import Token
from fastapi import FastAPI

from .models.payload_data import PayloadData
from .settings import TOKEN_DURATION_MINUTES

from .services.auth_service import AuthService
from .services.redis_service import RedisService

app = FastAPI()
auth_service = AuthService()

@app.post("/validate/")
async def validate(token: Token):
    status = auth_service.validate_token(token)
    return status if status["status"] == "Valid" else status, 401

@app.post("/login/")
async def generate_token(payload: PayloadData):
    return auth_service.generate_token(payload, TOKEN_DURATION_MINUTES)

@app.post("/refresh/")
async def refresh_token(token: Token):
    refreshed_token = auth_service.refresh_token(token, TOKEN_DURATION_MINUTES)
    return refreshed_token if refreshed_token else {"status": "Invalid"}, 401

@app.post("/logout/")
async def logout(token: Token):
    auth_service.logout(token)
    return {"status": "Logged out"}

