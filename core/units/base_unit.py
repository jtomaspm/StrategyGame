from dataclasses import dataclass


@dataclass
class BaseUnit:
    unit: str
    race: str
    supply: int
    cost1: int
    cost2: int
    build_time: int
    size: str
    cargo: int
    armor: int
    armor_upgrades: int
    healt: int
    shield: int
    attributes: list[str]
    ground_attack: int
    ground_attack_upgrades: int
    aerial_attack: int
    aerial_attack_upgrades: int
    bonus: list[str]
    ground_dps: float
    ground_dps_upgrade: float
    aerial_dps: float
    aerial_dps_upgrade: float
    bonus_dps: list[str]
    bonus_dps_upgrade: float
    attack_mod: str
    cooldown: float
    speed: float
    speed_upgrade:float
    creepbonus: str
    range: int
    range_upgrade: int
    sight: int