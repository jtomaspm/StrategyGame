from core.base_types.races.protoss import Protoss
from core.base_types.troops.troop import Troop
from core.base_types.troops.troop_attack_type import Ground
from core.base_types.troops.troop_attributes import TroopAttributes


class ProtossTroopFactory:

    def zealot() -> Troop:
        attributes = TroopAttributes()
        attributes.attack = 8
        attributes.attack_type = Ground()
        attributes.food_consumption = 1
        
        
        troop = Troop()
        troop.name = "Zealot"
        troop.race = Protoss()
        troop.attributes = attributes
        return troop
