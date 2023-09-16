from ...cost.cost import TimedCost
from ...races.zerg import Zerg
from ..base_troop.troop import Troop
from ..base_troop.troop_attributes import TroopAttributes
from ..base_troop.troop_rules import TroopRules
from ..base_troop.troop_upgrade import TroopUpgrade


class Corruptor(Troop):
    def __init__(self):
        self.name = "Corruptor"
        self.race = Zerg()

        self.upgrades = TroopUpgrade()
        self.upgrades.attack = 1
        self.upgrades.armor = 1
        
        self.attributes = TroopAttributes()
        self.attributes.attack = 20
        self.attributes.healt = 200
        self.attributes.armor = 2
        self.attributes.shield = 0
        self.attributes.supply_consumption = 2
        self.attributes.speed = 4.725
        self.attributes.iniciative = 20
        self.attributes.attacks_per_turn = 1

        self.cost_research = TimedCost()
        self.cost_research.crystal = 450
        self.cost_research.gas = 300
        self.cost_research.time = 87

        self.cost_training = TimedCost()
        self.cost_training.crystal = 150
        self.cost_training.gas = 100
        self.cost_training.time = 29

        self.rules = TroopRules()
        self.rules.can_attack_air = True
        self.rules.can_attack_ground = False
        self.rules.can_fly = True
        self.rules.attacks_same_unit = True