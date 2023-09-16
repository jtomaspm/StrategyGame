from ...cost.cost import TimedCost
from ...races.terran import Terran
from ..base_troop.troop import Troop
from ..base_troop.troop_attributes import TroopAttributes
from ..base_troop.troop_rules import TroopRules
from ..base_troop.troop_upgrade import TroopUpgrade


class Hellion(Troop):
    def __init__(self):
        self.name = "Hellion"
        self.race = Terran()

        self.upgrades = TroopUpgrade()
        self.upgrades.attack = 1
        self.upgrades.armor = 1
        
        self.attributes = TroopAttributes()
        self.attributes.attack = 7
        self.attributes.healt = 90
        self.attributes.armor = 0
        self.attributes.shield = 0
        self.attributes.supply_consumption = 2
        self.attributes.speed = 5.95
        self.attributes.iniciative = 8
        self.attributes.attacks_per_turn = 3

        self.cost_research = TimedCost()
        self.cost_training.crystal = 300
        self.cost_training.gas = 0
        self.cost_training.time = 63

        self.cost_training = TimedCost()
        self.cost_training.crystal = 100
        self.cost_training.gas = 0
        self.cost_training.time = 21

        self.rules = TroopRules()
        self.rules.can_attack_air = False
        self.rules.can_attack_ground = True
        self.rules.can_fly = False
        self.rules.attacks_same_unit = False