from core.base_types.cost.cost import TimedCost
from core.base_types.races.zerg import Zerg
from core.base_types.troops.base_troop.troop import Troop
from core.base_types.troops.base_troop.troop_attributes import TroopAttributes
from core.base_types.troops.base_troop.troop_rules import TroopRules
from core.base_types.troops.base_troop.troop_upgrade import TroopUpgrade


class Mutalisk(Troop):
    def __init__(self):
        self.name = "Mutalisk"
        self.race = Zerg()

        self.upgrades = TroopUpgrade()
        self.upgrades.attack = 1
        self.upgrades.armor = 1
        
        self.attributes = TroopAttributes()
        self.attributes.attack = 5
        self.attributes.healt = 120
        self.attributes.armor = 0
        self.attributes.shield = 0
        self.attributes.supply_consumption = 2
        self.attributes.speed = 5.6
        self.attributes.iniciative = 20
        self.attributes.attacks_per_turn = 3

        self.cost_research = TimedCost()
        self.cost_research.crystal = 300
        self.cost_research.gas = 300
        self.cost_research.time = 87

        self.cost_training = TimedCost()
        self.cost_training.crystal = 100
        self.cost_training.gas = 100
        self.cost_training.time = 29

        self.rules = TroopRules()
        self.rules.can_attack_air = True
        self.rules.can_attack_ground = True
        self.rules.can_fly = True
        self.rules.attacks_same_unit = False