from core.base_types.cost.cost import TimedCost
from core.base_types.races.terran import Terran
from core.base_types.troops.base_troop.troop import Troop
from core.base_types.troops.base_troop.troop_attributes import TroopAttributes
from core.base_types.troops.base_troop.troop_rules import TroopRules
from core.base_types.troops.base_troop.troop_upgrade import TroopUpgrade


class Battlecruiser(Troop):
    def __init__(self):
        self.name = "Battlecruiser"
        self.race = Terran()

        self.upgrades = TroopUpgrade()
        self.upgrades.attack = 1
        self.upgrades.armor = 1
        
        self.attributes = TroopAttributes()
        self.attributes.attack = 8
        self.attributes.healt = 550
        self.attributes.armor = 3
        self.attributes.shield = 0
        self.attributes.supply_consumption = 6
        self.attributes.speed = 2.62
        self.attributes.iniciative = 19
        self.attributes.attacks_per_turn = 3

        self.cost_research = TimedCost()
        self.cost_training.crystal = 1200
        self.cost_training.gas = 900
        self.cost_training.time = 190

        self.cost_training = TimedCost()
        self.cost_training.crystal = 400
        self.cost_training.gas = 300
        self.cost_training.time = 64

        self.rules = TroopRules()
        self.rules.can_attack_air = True
        self.rules.can_attack_ground = True
        self.rules.can_fly = True
        self.rules.attacks_same_unit = True