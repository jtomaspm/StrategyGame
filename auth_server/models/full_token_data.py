from dataclasses import dataclass

from ..models.payload_data import PayloadData
from ..models.token import Token


@dataclass
class FullTokenData(PayloadData, Token):
    pass