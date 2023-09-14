from dataclasses import dataclass
from core.base_types.cost.cost import TimedCost

from core.base_types.races.race import Race
from core.base_types.troops.troop_attributes import TroopAttributes
from core.base_types.troops.troop_upgrade import TroopUpgrade


@dataclass
class Troop:
    name: str
    race: Race
    attributes: TroopAttributes
    cost_research: TimedCost
    cost_training: TimedCost
    uogrades: TroopUpgrade()
    can_attack_ground: bool
    can_attack_air: bool