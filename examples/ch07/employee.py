from examples.ch07.pay import Pay


class Employee:
    def __init__(self, name: str, base_pay: Pay):
        self.name = name
        self.base_pay = base_pay
