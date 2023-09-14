from core.base_types.cost.cost import TimedCost
from core.base_types.races.protoss import Protoss
from core.base_types.troops.base_troop.troop import Troop
from core.base_types.troops.base_troop.troop_attributes import TroopAttributes
from core.base_types.troops.base_troop.troop_rules import TroopRules
from core.base_types.troops.base_troop.troop_upgrade import TroopUpgrade


class Zealot(Troop):
    def __init__(self):
        self.name = "Zealot"
        self.race = Protoss()

        self.upgrades = TroopUpgrade()
        self.upgrades.attack = 2
        self.upgrades.armor = 1
        
        self.attributes = TroopAttributes()
        self.attributes.attack = 8
        self.attributes.healt = 100
        self.attributes.armor = 1
        self.attributes.shield = 50
        self.attributes.supply_consumption = 2
        self.attributes.speed = 3.15
        self.attributes.iniciative = 5
        self.attributes.attacks_per_turn = 2

        self.cost_research = None

        self.cost_training = TimedCost()
        self.cost_training.crystal = 100
        self.cost_training.gas = 0
        self.cost_training.time = 30

        self.rules = TroopRules()
        self.rules.can_attack_air = False
        self.rules.can_attack_ground = True
        self.rules.can_fly = False
        self.rules.attacks_same_unit = True