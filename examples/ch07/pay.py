from dataclasses import dataclass


@dataclass
class Pay:
    def __init__(self, amount: int):
        self.amount = amount
        self.unit = "KRW"

    def __rmul__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return Pay(int(other * self.amount))
        return Pay(other.amount * self.amount)
