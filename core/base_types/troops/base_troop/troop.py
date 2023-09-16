from abc import ABC
from dataclasses import dataclass
from ...cost.cost import TimedCost

from ...races.race import Race
from base_troop.troop_attributes import TroopAttributes
from base_troop.troop_rules import TroopRules
from base_troop.troop_upgrade import TroopUpgrade


@dataclass
class Troop(ABC):
    name: str
    race: Race
    attributes: TroopAttributes
    cost_research: TimedCost
    cost_training: TimedCost
    upgrades: TroopUpgrade
    rules: TroopRules