from ast import List
from dataclasses import dataclass

from pydantic import BaseModel


@dataclass
class PayloadData(BaseModel):
    player_id: int
    name: str
    email: str
    roles: str
    ip_address: str