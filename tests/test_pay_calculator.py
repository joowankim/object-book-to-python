from examples.ch07.calculator import PayCalculator
from examples.ch07.employee import Employee


# given-when-then pattern
from examples.ch07.pay import Pay


def test_pay_of():
    # given
    # 소득세율은 10%이다.
    tax_rate = 0.1
    pay_calculator = PayCalculator(tax_rate)
    # 직원 John의 기본급은 1,000,000원이다.
    employee = Employee("John", 1000000)

    # when

    # then
    # 직원 John의 급여는 900,000원이다.
    assert pay_calculator.pay_of(employee) == Pay(900000)


# Rspec
def test_pay_of_with_rspec():
    # Describe
    # PayCalculator의 pay_of 메소드는
    pay_calculator = PayCalculator(0)

    # Context
    # 소득세율이 10%일 때
    pay_calculator.tax_rate = 0.1
    # 직원의 기본급이 1,000,000원일 때
    employee = Employee("John", 1000000)

    # It
    # 900,000원의 급여를 반환한다.
    assert pay_calculator.pay_of(employee) == Pay(900000)
