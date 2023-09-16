from ...cost.cost import TimedCost
from ...races.protoss import Protoss
from ..base_troop.troop import Troop
from ..base_troop.troop_attributes import TroopAttributes
from ..base_troop.troop_rules import TroopRules
from ..base_troop.troop_upgrade import TroopUpgrade



class VoidRay(Troop):
    def __init__(self):
        self.name = "Void Ray"
        self.race = Protoss()

        self.upgrades = TroopUpgrade()
        self.upgrades.attack = 1
        self.upgrades.armor = 1
        
        self.attributes = TroopAttributes()
        self.attributes.attack = 16
        self.attributes.healt = 150
        self.attributes.armor = 0
        self.attributes.shield = 100
        self.attributes.supply_consumption = 2
        self.attributes.speed = 3.85
        self.attributes.iniciative = 20
        self.attributes.attacks_per_turn = 1

        self.cost_research = TimedCost()
        self.cost_research.crystal = 750
        self.cost_research.gas = 450
        self.cost_research.time = 180

        self.cost_training = TimedCost()
        self.cost_training.crystal = 250
        self.cost_training.gas = 150
        self.cost_training.time = 60

        self.rules = TroopRules()
        self.rules.can_attack_air = True
        self.rules.can_attack_ground = True
        self.rules.can_fly = True
        self.rules.attacks_same_unit = True
