from examples.ch07.calculator import PayCalculator
from examples.ch07.employee import Employee


# given-when-then pattern
def test_pay_of():
    # given
    # 소득 세율은 10%이다.
    tax_rate = 0.1
    pay_calculator = PayCalculator(tax_rate)
    # 직원 John의 기본급은 1,000,000원이다.
    employee = Employee("John", 1000000)

    # when

    # then
    # 직원 John의 급여는 900,000원이다.
    assert pay_calculator.pay_of(employee) == 900000
