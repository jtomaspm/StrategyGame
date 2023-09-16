import time
import unittest

from ..settings import SECRET_KEY

from ..models.payload_data import PayloadData

from ..services.jwt_service import get_jwt_token, get_refresh_token

from ..models.token import Token
from ..services.redis_service import RedisService

class TestRedis(unittest.TestCase):
    redis_service = RedisService()
    token = Token(
        access_token=get_jwt_token(
            payload=PayloadData(
                email="test@test.pt",
                player_id=1,
                name="test",
                roles="test",
                ip_address="1.1.1.1"
                ),
            secret=SECRET_KEY),
        expire_time_ms=time.time() + 3600,
        refresh_token=get_refresh_token()
    )

    def test_get_token(self):
        pass
    
    def test_save_token(self):
        res = self.redis_service.save_token(token=self.token)
        pass

    def test_delete_token(self):
        res = self.redis_service.delete_token(token=self.token)
        pass
