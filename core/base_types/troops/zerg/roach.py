from core.base_types.cost.cost import TimedCost
from core.base_types.races.zerg import Zerg
from core.base_types.troops.base_troop.troop import Troop
from core.base_types.troops.base_troop.troop_attributes import TroopAttributes
from core.base_types.troops.base_troop.troop_rules import TroopRules
from core.base_types.troops.base_troop.troop_upgrade import TroopUpgrade


class Roach(Troop):
    def __init__(self):
        self.name = "Roach"
        self.race = Zerg()

        self.upgrades = TroopUpgrade()
        self.upgrades.attack = 1
        self.upgrades.armor = 1
        
        self.attributes = TroopAttributes()
        self.attributes.attack = 16
        self.attributes.healt = 120
        self.attributes.armor = 1
        self.attributes.shield = 0
        self.attributes.supply_consumption = 2
        self.attributes.speed = 3.15
        self.attributes.iniciative = 10
        self.attributes.attacks_per_turn = 1

        self.cost_research = TimedCost()
        self.cost_research.crystal = 225
        self.cost_research.gas = 75
        self.cost_research.time = 57

        self.cost_training = TimedCost()
        self.cost_training.crystal = 75
        self.cost_training.gas = 25
        self.cost_training.time = 19

        self.rules = TroopRules()
        self.rules.can_attack_air = False
        self.rules.can_attack_ground = True
        self.rules.can_fly = False
        self.rules.attacks_same_unit = True