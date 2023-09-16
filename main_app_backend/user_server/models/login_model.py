from dataclasses import dataclass


@dataclass
class LoginModel:
    username: str
    password: str