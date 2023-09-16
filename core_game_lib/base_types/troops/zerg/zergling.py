from ...cost.cost import TimedCost
from ...races.zerg import Zerg
from ..base_troop.troop import Troop
from ..base_troop.troop_attributes import TroopAttributes
from ..base_troop.troop_rules import TroopRules
from ..base_troop.troop_upgrade import TroopUpgrade


class Zergling(Troop):
    def __init__(self):
        self.name = "Zergling"
        self.race = Zerg()

        self.upgrades = TroopUpgrade()
        self.upgrades.attack = 1
        self.upgrades.armor = 1
        
        self.attributes = TroopAttributes()
        self.attributes.attack = 5
        self.attributes.healt = 70
        self.attributes.armor = 0
        self.attributes.shield = 0
        self.attributes.supply_consumption = 1
        self.attributes.speed = 4.13
        self.attributes.iniciative = 5
        self.attributes.attacks_per_turn = 2

        self.cost_research = None

        self.cost_training = TimedCost()
        self.cost_training.crystal = 50
        self.cost_training.gas = 0
        self.cost_training.time = 17

        self.rules = TroopRules()
        self.rules.can_attack_air = False
        self.rules.can_attack_ground = True
        self.rules.can_fly = False
        self.rules.attacks_same_unit = False