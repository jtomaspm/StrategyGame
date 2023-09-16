from dataclasses import dataclass



@dataclass
class Token:
    access_token: str
    refresh_token: str

@dataclass
class TokenWithExpireTime(Token):
    expire_time_ms: float