import redis

from ..models.full_token_data import FullTokenData

from ..models.payload_data import PayloadData
from ..models.token import Token


class RedisService:
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)

    def save_token(self, token: Token, payload: PayloadData):
        payload_dict = payload.__dict__.copy()
        payload_dict["expire_time_ms"] = token.expire_time_ms
        payload_dict["refresh_token"] = token.refresh_token
        self.r.hset(token.access_token, mapping=payload_dict)

    def get_token(self, access_token: str) -> FullTokenData:
        return FullTokenData(access_token=access_token,**self.r.hgetall(access_token))