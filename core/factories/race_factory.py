from core.base_types.races.protoss import Protoss
from core.base_types.races.race import Race
from core.base_types.races.terran import Terran
from core.base_types.races.zerg import Zerg


class RaceFactory:
    def get_race(race_str: str) -> Race:
        races = {
            "protoss" : Protoss(),
            "zerg" : Zerg(),
            "terran" : Terran()
        }
        return races[race_str.lower()]
        