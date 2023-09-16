from ...cost.cost import TimedCost
from ...races.protoss import Protoss
from ..base_troop.troop import Troop
from ..base_troop.troop_attributes import TroopAttributes
from ..base_troop.troop_rules import TroopRules
from ..base_troop.troop_upgrade import TroopUpgrade


class Immortal(Troop):
    def __init__(self):
        self.name = "Immortal"
        self.race = Protoss()

        self.upgrades = TroopUpgrade()
        self.upgrades.attack = 1
        self.upgrades.armor = 1
        
        self.attributes = TroopAttributes()
        self.attributes.attack = 30
        self.attributes.healt = 200
        self.attributes.armor = 1
        self.attributes.shield = 100
        self.attributes.supply_consumption = 4
        self.attributes.speed = 3.15
        self.attributes.iniciative = 10
        self.attributes.attacks_per_turn = 1

        self.cost_research = TimedCost()
        self.cost_research.crystal = 700
        self.cost_research.gas = 300
        self.cost_research.time = 200

        self.cost_training = TimedCost()
        self.cost_training.crystal = 275
        self.cost_training.gas = 100
        self.cost_training.time = 60

        self.rules = TroopRules()
        self.rules.can_attack_air = False
        self.rules.can_attack_ground = True
        self.rules.can_fly = False
        self.rules.attacks_same_unit = True