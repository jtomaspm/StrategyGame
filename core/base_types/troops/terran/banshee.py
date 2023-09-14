from core.base_types.cost.cost import TimedCost
from core.base_types.races.terran import Terran
from core.base_types.troops.base_troop.troop import Troop
from core.base_types.troops.base_troop.troop_attributes import TroopAttributes
from core.base_types.troops.base_troop.troop_rules import TroopRules
from core.base_types.troops.base_troop.troop_upgrade import TroopUpgrade


class Banshee(Troop):
    def __init__(self):
        self.name = "Banshee"
        self.race = Terran()

        self.upgrades = TroopUpgrade()
        self.upgrades.attack = 1
        self.upgrades.armor = 1
        
        self.attributes = TroopAttributes()
        self.attributes.attack = 12
        self.attributes.healt = 140
        self.attributes.armor = 0
        self.attributes.shield = 0
        self.attributes.supply_consumption = 3
        self.attributes.speed = 3.85
        self.attributes.iniciative = 20
        self.attributes.attacks_per_turn = 2

        self.cost_research = TimedCost()
        self.cost_training.crystal = 450
        self.cost_training.gas = 300
        self.cost_training.time = 129

        self.cost_training = TimedCost()
        self.cost_training.crystal = 150
        self.cost_training.gas = 100
        self.cost_training.time = 43

        self.rules = TroopRules()
        self.rules.can_attack_air = False
        self.rules.can_attack_ground = True
        self.rules.can_fly = True
        self.rules.attacks_same_unit = True