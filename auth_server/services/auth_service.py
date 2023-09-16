import time
from ..models.payload_data import PayloadData
from .jwt_service import get_jwt_token, get_refresh_token
from ..settings import SECRET_KEY
from .redis_service import RedisService
from ..models.token import Token


class AuthService:
    redis_service = RedisService()

    def validate_token(token: Token):
        token_data = redis_service.get_token(token.access_token)
        if token_data.refresh_token == token.refresh_token:
            if time.time() < token.expire_time_ms:
                return {"status": "Valid"}
            else:
                return {"status": "Expired"}
        return {"status": "Invalid"}

        
    def generate_token(payload: PayloadData, token_duration_minutes: int) -> Token:
        return Token(
            access_token=get_jwt_token(payload, SECRET_KEY),
            refresh_token=get_refresh_token(),
            expire_time_ms=time.time() + token_duration_minutes * 60 * 1000
        )