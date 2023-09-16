from contextvars import Token
from fastapi import FastAPI

from auth_server.models.payload_data import PayloadData

from .services.auth_service import AuthService
from .services.redis_service import RedisService

app = FastAPI()
auth_service = AuthService()

@app.post("/validate/")
async def validate(token: Token):
    return auth_service.validate_token(token)

@app.post("/login/")
async def generate_token(payload: PayloadData):
    return auth_service.generate_token(payload, 30)
