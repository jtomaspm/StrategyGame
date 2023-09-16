import time
from ..models.payload_data import PayloadData
from .jwt_service import get_jwt_token, get_refresh_token
from ..settings import SECRET_KEY
from .redis_service import RedisService
from ..models.token import Token, TokenWithExpireTime


class AuthService:
    redis_service = RedisService()

    def validate_token(self, token: Token):
        token_data = self.redis_service.get_token(token.access_token)
        if token_data.refresh_token == token.refresh_token:
            if time.time() < token_data.expire_time_ms:
                return {"status": "Valid"}
            else:
                return {"status": "Expired"}
        return {"status": "Invalid"}

        
    def generate_token(self, payload: PayloadData, token_duration_minutes: int) -> Token:
        token = TokenWithExpireTime(
            access_token=get_jwt_token(payload, SECRET_KEY),
            refresh_token=get_refresh_token(),
            expire_time_ms=time.time() + token_duration_minutes * 60 * 1000
        )
        self.redis_service.save_token(token)
        return token

    def logout(self, token: Token):
        self.redis_service.delete_token(token)

    def refresh_token(self, token: Token, token_duration_minutes: int) -> Token | None:
        token_data = self.redis_service.get_token(token.access_token)
        if token_data.refresh_token == token.refresh_token:
            self.redis_service.delete_token(token)
            return self.generate_token(PayloadData(player_id=token_data.player_id), token_duration_minutes)