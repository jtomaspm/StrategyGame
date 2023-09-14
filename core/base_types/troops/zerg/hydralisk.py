from core.base_types.cost.cost import TimedCost
from core.base_types.races.zerg import Zerg
from core.base_types.troops.base_troop.troop import Troop
from core.base_types.troops.base_troop.troop_attributes import TroopAttributes
from core.base_types.troops.base_troop.troop_rules import TroopRules
from core.base_types.troops.base_troop.troop_upgrade import TroopUpgrade


class Hydralisk(Troop):
    def __init__(self):
        self.name = "Hydralisk"
        self.race = Zerg()

        self.upgrades = TroopUpgrade()
        self.upgrades.attack = 1
        self.upgrades.armor = 1
        
        self.attributes = TroopAttributes()
        self.attributes.attack = 12
        self.attributes.healt = 85
        self.attributes.armor = 0
        self.attributes.shield = 0
        self.attributes.supply_consumption = 2
        self.attributes.speed = 3.15
        self.attributes.iniciative = 11
        self.attributes.attacks_per_turn = 1

        self.cost_research = TimedCost()
        self.cost_research.crystal = 300
        self.cost_research.gas = 150
        self.cost_research.time = 78

        self.cost_training = TimedCost()
        self.cost_training.crystal = 100
        self.cost_training.gas = 50
        self.cost_training.time = 24

        self.rules = TroopRules()
        self.rules.can_attack_air = True
        self.rules.can_attack_ground = True
        self.rules.can_fly = False
        self.rules.attacks_same_unit = False