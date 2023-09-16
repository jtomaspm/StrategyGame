from dataclasses import dataclass


@dataclass
class Cost:
    crystal: int
    gas: int

class TimedCost(Cost):
    time: int