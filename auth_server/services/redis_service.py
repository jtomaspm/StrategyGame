import redis

from ..settings import SECRET_KEY

from .jwt_service import decode_jwt_token

from ..models.full_token_data import FullTokenData

from ..models.payload_data import PayloadData
from ..models.token import Token


class RedisService:
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)

    def save_token(self, token: Token):
        payload = decode_jwt_token(token.access_token, SECRET_KEY)
        self.r.hset("token:"+payload.player_id, mapping=token)

    def get_token(self, access_token: str) -> FullTokenData:
        payload = decode_jwt_token(access_token, SECRET_KEY)
        return FullTokenData(**self.r.hgetall("token:"+payload.player_id), **payload.__dict__)