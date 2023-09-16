from dataclasses import dataclass


@dataclass
class PayloadData:
    player_id: int
    name: str
    email: str
    roles: list(str)
    ip_address: str