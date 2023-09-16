from ast import List
from dataclasses import dataclass



@dataclass
class PayloadData:
    player_id: int
    name: str
    email: str
    roles: str
    ip_address: str