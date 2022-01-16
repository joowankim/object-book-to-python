from dataclasses import dataclass


@dataclass
class Pay:
    def __init__(self, amount: int):
        self.amount = amount
        self.unit = "KRW"
