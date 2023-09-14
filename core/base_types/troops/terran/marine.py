from core.base_types.cost.cost import TimedCost
from core.base_types.races.terran import Terran
from core.base_types.troops.base_troop.troop import Troop
from core.base_types.troops.base_troop.troop_attributes import TroopAttributes
from core.base_types.troops.base_troop.troop_rules import TroopRules
from core.base_types.troops.base_troop.troop_upgrade import TroopUpgrade


class Marine(Troop):
    def __init__(self):
        self.name = "Marine"
        self.race = Terran()

        self.upgrades = TroopUpgrade()
        self.upgrades.attack = 1
        self.upgrades.armor = 1
        
        self.attributes = TroopAttributes()
        self.attributes.attack = 6
        self.attributes.healt = 45
        self.attributes.armor = 0
        self.attributes.shield = 0
        self.attributes.supply_consumption = 1
        self.attributes.speed = 3.15
        self.attributes.iniciative = 10
        self.attributes.attacks_per_turn = 1

        self.cost_research = None

        self.cost_training = TimedCost()
        self.cost_training.crystal = 50
        self.cost_training.gas = 0
        self.cost_training.time = 25

        self.rules = TroopRules()
        self.rules.can_attack_air = True
        self.rules.can_attack_ground = True
        self.rules.can_fly = False
        self.rules.attacks_same_unit = True