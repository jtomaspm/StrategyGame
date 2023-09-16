from dataclasses import dataclass

from .payload_data import PayloadData
from .token import Token


@dataclass
class FullTokenData(PayloadData, Token):
    pass