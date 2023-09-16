from contextvars import Token
from fastapi import FastAPI

from services.redis_service import RedisService

app = FastAPI()
redis_service = RedisService()

@app.post("/validate/")
async def validate_token(token: Token):

    return {"message": "Hello World"}