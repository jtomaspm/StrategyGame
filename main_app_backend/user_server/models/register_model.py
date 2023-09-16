from dataclasses import dataclass


@dataclass
class RegisterModel:
    username: str
    password: str
    email: str