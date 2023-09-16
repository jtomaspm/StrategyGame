from dataclasses import dataclass


@dataclass
class TroopRules:
    can_attack_ground: bool
    can_attack_air: bool
    can_fly: bool
    attacks_same_unit: bool