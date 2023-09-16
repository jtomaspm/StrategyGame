from dataclasses import dataclass


@dataclass
class TroopAttributes:
    attack: int
    healt: int
    armor: int
    shield: int
    supply_consumption: int
    speed: float
    iniciative: int
    attacks_per_turn: int
