from ..base_types.races.protoss import Protoss
from ..base_types.races.race import Race
from ..base_types.races.terran import Terran
from ..base_types.races.zerg import Zerg


class RaceFactory:
    def get_race(race_str: str) -> Race | None:
        return {
            "protoss" : Protoss(),
            "zerg" : Zerg(),
            "terran" : Terran()
        }[race_str.lower()]
        