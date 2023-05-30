import pytest

from calculator import Calculator

class TestCalc:
    def setup_method(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert  self.calc.adding(self, 1, 1) == 2

    def test_adding_unsuccess(self):
        assert self.calc.adding(self, 1, 2) == 2

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def test_multiply_success(self):
        assert  self.calc.multiply(self, 2, 3) == 6

    def test_division_success(self):
        assert  self.calc.division(self, 6, 2) == 3

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 7, 3) == 4

    def tesrdown_method(self):
        print("teardown-------")