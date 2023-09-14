from abc import ABC
from dataclasses import dataclass
from core.base_types.cost.cost import TimedCost

from core.base_types.races.race import Race
from core.base_types.troops.base_troop.troop_attributes import TroopAttributes
from core.base_types.troops.base_troop.troop_rules import TroopRules
from core.base_types.troops.base_troop.troop_upgrade import TroopUpgrade


@dataclass
class Troop(ABC):
    name: str
    race: Race
    attributes: TroopAttributes
    cost_research: TimedCost
    cost_training: TimedCost
    upgrades: TroopUpgrade
    rules: TroopRules