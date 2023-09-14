from dataclasses import dataclass

from core.base_types.troops.troop_attack_type import AttackType


@dataclass
class TroopAttributes:
    attack: int
    attack_type: AttackType
    healt: int
    armor: int
    shield: int
    supply_consumption: int
    speed: float
    ranged: bool
