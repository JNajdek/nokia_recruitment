import decimal
from decimal import Decimal as D
from typing import Union, Callable


class Calculator:
    """
    A class for performing basic arithmetic operations
    :param value: Result of calculations
    """

    # changing all float and int arguments to decimal for more accurate representation of the data
    def __init__(self, value: Union[int, float] = D("0")) -> None:
        """
        Initializes the calculator with a starting value
        :param value: The initial value of the calculator, later result of the calculations
        """
        try:
            self.value = D(str(value))
        except decimal.InvalidOperation:
            print("The value must be a number. The value has been set to zero.")
            self.value = D("0")
        except Exception as e:
            print(f"Unexpected error: {e}")
            self.value = D("0")

    @staticmethod
    def arithmetic_operation(func: Callable) -> Callable:
        """
        Decorator responsible for handling exceptions from all functions
        :param func: The decorated function
        :return: The decorated function with exception handling
        """

        def wrapper(self, number: Union[int, float]) -> None:
            try:
                func(self, number)
            except ZeroDivisionError:
                print("You cannot divide by zero. The value has been reset to zero.")
                self.reset_calculator()
            except decimal.InvalidOperation:
                print("The value must be a number. The value has been reset to zero.")
                self.reset_calculator()
            except Exception as e:
                print(f"Unexpected error: {e}")
                self.reset_calculator()

        return wrapper

    @arithmetic_operation
    def add(self, number: Union[int, float]) -> None:
        """
        Adds a number to the current value
        :param number: The added number
        """
        self.value += D(str(number))

    @arithmetic_operation
    def subtract(self, number: Union[int, float]) -> None:
        """
        Subtracts a number from the current value
        :param number: The number to subtract
        """
        self.value -= D(str(number))

    @arithmetic_operation
    def multiply(self, number: Union[int, float]) -> None:
        """
        Multiplies the current value by a number
        :param number: The number to multiply by
        """
        self.value *= D(str(number))

    @arithmetic_operation
    def divide(self, number: Union[int, float]) -> None:
        """
        Divides the current value by a number
        :param number: The number to divide by
        """
        self.value /= D(str(number))

    def get_value(self) -> float:
        """
        Returns the current value of the calculator as a float
        :return:  Float of the current value
        """
        return float(self.value)

    def reset_calculator(self) -> None:
        """
        Resets calculator by changing its value to zero
        """
        self.value = D("0")
