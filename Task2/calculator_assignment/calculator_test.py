import pytest
from calculator import Calculator


# setting up calculators with different values
@pytest.fixture
def calculator_positive_starting_value():
    """
    Fixture providing Calculator object with starting value equal to two
    """
    return Calculator(2)


@pytest.fixture
def calculator_negative_starting_value():
    """
    Fixture providing Calculator object with starting value equal to minus two
    """
    return Calculator(-2)


# setting up calculator with value=0
@pytest.fixture
def calculator_0_starting_value():
    """
    Fixture providing Calculator object with starting value equal to zero
    """
    return Calculator()


# Test parameters:
# - input_n: The number used in the operation.
# - expected_a: The expected result of the operation for the Calculator(2)
# - expected_b: The expected result of the operation for the Calculator()
# - expected_c: The expected result of the operation for the Calculator(-2)


# parametrizing to test more data combinations
@pytest.mark.parametrize(
    # 3 expected values for calculators with different starting values
    ('input_n', 'expected_a', 'expected_b', 'expected_c'),
    [
        # testing positive, negative and equal to zero ints
        (5, 7, 5, 3),
        (-5, -3, -5, -7),
        (0, 2, 0, -2),

        # testing positive and negative floats
        (5.1, 7.1, 5.1, 3.1),
        (-5.2, -3.2, -5.2, -7.2),

    ]
)
def test_addition(calculator_positive_starting_value, calculator_0_starting_value, calculator_negative_starting_value,
                  input_n, expected_a, expected_b, expected_c):
    """
    Tests the add method by adding a singular value
    """

    calculator_positive_starting_value.add(input_n)
    calculator_0_starting_value.add(input_n)
    calculator_negative_starting_value.add(input_n)

    assert calculator_positive_starting_value.get_value() == expected_a
    assert calculator_0_starting_value.get_value() == expected_b
    assert calculator_negative_starting_value.get_value() == expected_c


@pytest.mark.parametrize(
    ('input_n', 'expected_a', 'expected_b', 'expected_c'),
    [
        # testing ints
        (10, -8, -10, -12),
        (-5, 7, 5, 3),
        (0, 2, 0, -2),

        # testing floats
        (10.1, -8.1, -10.1, -12.1),
        (-5.2, 7.2, 5.2, 3.2),

    ]
)
def test_subtract(calculator_positive_starting_value, calculator_0_starting_value, calculator_negative_starting_value,
                  input_n, expected_a, expected_b, expected_c):
    """
    Tests the subtract method by subtracting a singular value
    """
    calculator_positive_starting_value.subtract(input_n)
    calculator_0_starting_value.subtract(input_n)
    calculator_negative_starting_value.subtract(input_n)
    assert calculator_positive_starting_value.get_value() == expected_a
    assert calculator_0_starting_value.get_value() == expected_b
    assert calculator_negative_starting_value.get_value() == expected_c


@pytest.mark.parametrize(
    ('input_n', 'expected_a', 'expected_b', 'expected_c'),
    [
        # testing ints
        (4, 8, 0, -8),
        (-2, -4, 0, 4),
        (0, 0, 0, 0),  # 1

        # testing floats
        (4.1, 8.2, 0, -8.2),
        (-2.4, -4.8, 0, 4.8),
    ]
)
def test_multiply(calculator_positive_starting_value, calculator_0_starting_value, calculator_negative_starting_value,
                  input_n, expected_a, expected_b, expected_c):
    """
    Tests the multiply method by multiplying initial value once
    """
    calculator_positive_starting_value.multiply(input_n)
    calculator_0_starting_value.multiply(input_n)
    calculator_negative_starting_value.multiply(input_n)
    # different initial values change the sign of a resultr
    assert calculator_positive_starting_value.get_value() == expected_a
    assert calculator_0_starting_value.get_value() == expected_b
    assert calculator_negative_starting_value.get_value() == expected_c


@pytest.mark.parametrize(
    ('input_n', 'expected_a', 'expected_b', 'expected_c'),
    [
        (2, 1, 0, -1),
        (-2, -1, 0, 1),

        (8, 0.25, 0, -0.25),
        (-10, -0.2, 0, 0.2)
    ]
)
def test_divide(calculator_positive_starting_value, calculator_0_starting_value, calculator_negative_starting_value,
                input_n, expected_a, expected_b, expected_c):
    """
    Tests the divide method by dividing initial value once
    """
    calculator_positive_starting_value.divide(input_n)
    calculator_0_starting_value.divide(input_n)
    calculator_negative_starting_value.divide(input_n)
    assert calculator_positive_starting_value.get_value() == expected_a
    assert calculator_0_starting_value.get_value() == expected_b
    assert calculator_negative_starting_value.get_value() == expected_c

def test_reset(calculator_positive_starting_value):
    """
    Tests the reset method if it zeroes out the value
    """
    calculator_positive_starting_value.reset_calculator()
    assert calculator_positive_starting_value.get_value() == 0


def test_division_by_0(calculator_positive_starting_value, capsys):
    """
    Tests handling attempts to divide by zero. The test verifies both the result of
     the operation and the message displayed in the terminal
    """
    calculator_positive_starting_value.divide(0)
    #capturing output to stdout
    out, err = capsys.readouterr()
    assert out == "You cannot divide by zero. The value has been reset to zero\n"
    assert calculator_positive_starting_value.get_value() == 0


def test_incorrect_types(calculator_positive_starting_value, capsys):
    """
    Tests handling attempts to use incorrect data types in different Calculator methods. The test verifies both the
    result of the operation and the message displayed in the terminal
    """
    incorrect_value = "abc"
    calculator_positive_starting_value.divide(incorrect_value)
    out1, err1 = capsys.readouterr()
    assert out1 == "The value must be a number. The value has been reset to zero\n"
    assert calculator_positive_starting_value.get_value() == 0

    calculator_positive_starting_value.add(incorrect_value)
    out2, err2 = capsys.readouterr()
    assert out2 == "The value must be a number. The value has been reset to zero\n"
    assert calculator_positive_starting_value.get_value() == 0

    calculator_positive_starting_value.subtract(incorrect_value)
    out3, err3 = capsys.readouterr()
    assert out3 == "The value must be a number. The value has been reset to zero\n"
    assert calculator_positive_starting_value.get_value() == 0

    calculator_positive_starting_value.multiply(incorrect_value)
    out4, err4 = capsys.readouterr()
    assert out4 == "The value must be a number. The value has been reset to zero\n"
    assert calculator_positive_starting_value.get_value() == 0

    calculator_incorrect = Calculator(incorrect_value)
    out5, err5 = capsys.readouterr()
    assert out5 == "The value must be a number. The value has been set to zero\n"
    assert calculator_positive_starting_value.get_value() == 0


def test_chaining_multiple_operations(calculator_positive_starting_value):
    """
    Tests the accuracy of chaining multiple arithmetic operations together and
     protection against float representation errors
    """
    calculator_positive_starting_value.add(10)
    calculator_positive_starting_value.subtract(1123)

    calculator_positive_starting_value.multiply(4)
    calculator_positive_starting_value.divide(2)

    calculator_positive_starting_value.add(300.50)
    calculator_positive_starting_value.add(10.25)
    calculator_positive_starting_value.multiply(8)
    calculator_positive_starting_value.divide(16)
    assert calculator_positive_starting_value.get_value() == -955.625
