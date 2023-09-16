from dataclasses import dataclass

from .payload_data import PayloadData
from .token import TokenWithExpireTime


@dataclass
class FullTokenData(PayloadData, TokenWithExpireTime):
    pass