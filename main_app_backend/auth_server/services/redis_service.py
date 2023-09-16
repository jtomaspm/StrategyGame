import redis
import logging

from ..settings import REDIS_HOST, REDIS_PORT, SECRET_KEY

from .jwt_service import decode_jwt_token

from ..models.full_token_data import FullTokenData

from ..models.token import Token, TokenWithExpireTime


class RedisService:
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

    def save_token(self, token: TokenWithExpireTime):
        payload = decode_jwt_token(token.access_token, SECRET_KEY)
        self.r.hset("token:"+str(payload.player_id), mapping=token.__dict__)

    def get_token(self, access_token: str) -> FullTokenData:
        payload = decode_jwt_token(access_token, SECRET_KEY)
        key = "token:"+str(payload.player_id)
        token = self.r.hgetall(key)

        logging.debug(payload)
        logging.debug(key)
        logging.debug(token)

        token["expire_time_ms"] = float(token["expire_time_ms"])

        return FullTokenData(**token, **payload.__dict__)

    def delete_token(self, token: Token):
        payload = decode_jwt_token(token.access_token, SECRET_KEY)
        self.r.delete("token:"+str(payload.player_id))