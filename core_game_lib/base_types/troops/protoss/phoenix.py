from ...cost.cost import TimedCost
from ...races.protoss import Protoss
from ..base_troop.troop import Troop
from ..base_troop.troop_attributes import TroopAttributes
from ..base_troop.troop_rules import TroopRules
from ..base_troop.troop_upgrade import TroopUpgrade


class Phoenix(Troop):
    def __init__(self):
        self.name = "Phoenix"
        self.race = Protoss()

        self.upgrades = TroopUpgrade()
        self.upgrades.attack = 1
        self.upgrades.armor = 1
        
        self.attributes = TroopAttributes()
        self.attributes.attack = 8
        self.attributes.healt = 120
        self.attributes.armor = 0
        self.attributes.shield = 60
        self.attributes.supply_consumption = 2
        self.attributes.speed = 5.95
        self.attributes.iniciative = 20
        self.attributes.attacks_per_turn = 2

        self.cost_research = TimedCost()
        self.cost_research.crystal = 450
        self.cost_research.gas = 300
        self.cost_research.time = 135

        self.cost_training = TimedCost()
        self.cost_training.crystal = 150
        self.cost_training.gas = 100
        self.cost_training.time = 45

        self.rules = TroopRules()
        self.rules.can_attack_air = True
        self.rules.can_attack_ground = False
        self.rules.can_fly = True
        self.rules.attacks_same_unit = True
