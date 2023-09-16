from dataclasses import dataclass


@dataclass
class PayloadData:
    sub: int
    name: str
    nickname: str