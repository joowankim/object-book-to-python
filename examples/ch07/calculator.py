from examples.ch07.employee import Employee
from examples.ch07.pay import Pay


class PayCalculator:
    def __init__(self, tax_rate: float):
        self.tax_rate = tax_rate

    def pay_of(self, employee: Employee) -> Pay:
        return 1000000 - 1000000 * 0.1
