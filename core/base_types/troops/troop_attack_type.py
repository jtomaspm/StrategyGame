from abc import ABC


class AttackType(ABC):
    name: str

class Aerial(AttackType):
    name: "Aerial"

class Ground(AttackType):
    name: "Ground"