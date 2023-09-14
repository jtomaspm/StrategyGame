from dataclasses import dataclass


@dataclass
class Cost:
    crystal: int
    gas: int

@dataclass
class TimedCost(Cost):
    time: int