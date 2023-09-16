import redis
import logging

from ..settings import SECRET_KEY

from .jwt_service import decode_jwt_token

from ..models.full_token_data import FullTokenData

from ..models.token import Token, TokenWithExpireTime


class RedisService:
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)

    def save_token(self, token: TokenWithExpireTime):
        payload = decode_jwt_token(token.access_token, SECRET_KEY)
        self.r.hset("token:"+str(payload.player_id), mapping=token.__dict__)

    def get_token(self, access_token: str) -> FullTokenData:
        payload = decode_jwt_token(access_token, SECRET_KEY)
        key = "token:"+str(payload.player_id)
        token = self.r.hgetall(key)
        token["expire_time_ms"] = float(token["expire_time_ms"])

        logging.debug(payload)
        logging.debug(key)
        logging.debug(token)

        return FullTokenData(**token, **payload.__dict__)

    def delete_token(self, token: Token):
        payload = decode_jwt_token(token.access_token, SECRET_KEY)
        self.r.delete("token:"+str(payload.player_id))