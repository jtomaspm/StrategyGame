from contextvars import Token
from fastapi import FastAPI
from auth_server.models.payload_data import PayloadData
import time
from services.redis_service import RedisService

app = FastAPI()
redis_service = RedisService()

@app.post("/validate/")
async def validate_token(token: Token):
    token_data = redis_service.get_token(token.access_token)
    if token_data.refresh_token == token.refresh_token:
        if time.time() < token.expire_time_ms:
            return {"status": "Valid",
                    "payload": PayloadData(**token_data.__dict__),
                    "token": token}
        else:
            return {"status": "Expired"}
    return {"status": "Invalid"}