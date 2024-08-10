import decimal
from decimal import Decimal as D
from typing import Union

class Calculator:
    def __init__(self, value: Union[int, float] = D("0")) -> None:
        try:
            self.value = D(str(value))
        except decimal.InvalidOperation:
            print("The value must be a number. The value has been set to zero")
            self.value = D("0")
        except Exception as e:
            print(f"Unexpected error: {e}")
            self.value = D("0")

    def add(self, number: Union[int, float]) -> None:
        try:
            self.value += D(str(number))
        except decimal.InvalidOperation:
            print("The value must be a number. The value has been reset to zero")
            self.reset_calculator()
        except Exception as e:
            print(f"Unexpected error: {e}")
            self.reset_calculator()

    def subtract(self, number: Union[int, float]) -> None:
        try:
            self.value -= D(str(number))
        except decimal.InvalidOperation:
            print("The value must be a number. The value has been reset to zero")
            self.reset_calculator()
        except Exception as e:
            print(f"Unexpected error: {e}")
            self.reset_calculator()

    def multiply(self, number: Union[int, float]) -> None:
        try:
            self.value *= D(str(number))
        except decimal.InvalidOperation:
            print("The value must be a number. The value has been reset to zero")
            self.reset_calculator()
        except Exception as e:
            print(f"Unexpected error: {e}")
            self.reset_calculator()

    def divide(self, number: Union[int, float]) -> None:
        try:
            self.value /= D(str(number))
        except ZeroDivisionError:
            print("You cannot divide by zero. The value has been reset to zero")
            self.reset_calculator()
        except decimal.InvalidOperation:
            print("The value must be a number. The value has been reset to zero")
            self.reset_calculator()
        except Exception as e:
            print(f"Unexpected error: {e}")
            self.reset_calculator()

    def get_value(self) -> float:
        return float(self.value)

    def reset_calculator(self) -> None:
        self.value = D("0")
