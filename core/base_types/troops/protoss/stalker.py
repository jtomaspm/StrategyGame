from core.base_types.cost.cost import TimedCost
from core.base_types.races.protoss import Protoss
from core.base_types.troops.base_troop.troop import Troop
from core.base_types.troops.base_troop.troop_attributes import TroopAttributes
from core.base_types.troops.base_troop.troop_rules import TroopRules
from core.base_types.troops.base_troop.troop_upgrade import TroopUpgrade


class Stalker(Troop):
    def __init__(self):
        self.name = "Stalker"
        self.race = Protoss()

        self.upgrades = TroopUpgrade()
        self.upgrades.attack = 1
        self.upgrades.armor = 1
        
        self.attributes = TroopAttributes()
        self.attributes.attack = 18
        self.attributes.healt = 80
        self.attributes.armor = 1
        self.attributes.shield = 80
        self.attributes.supply_consumption = 2
        self.attributes.speed = 4.13
        self.attributes.iniciative = 12
        self.attributes.attacks_per_turn = 1

        self.cost_research = TimedCost()
        self.cost_research.crystal = 375
        self.cost_research.gas = 150
        self.cost_research.time = 135

        self.cost_training = TimedCost()
        self.cost_training.crystal = 125
        self.cost_training.gas = 50
        self.cost_training.time = 45

        self.rules = TroopRules()
        self.rules.can_attack_air = True
        self.rules.can_attack_ground = True
        self.rules.can_fly = False
        self.rules.attacks_same_unit = True
        