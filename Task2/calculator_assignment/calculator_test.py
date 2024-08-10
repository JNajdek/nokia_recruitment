import pytest
from calculator import Calculator


@pytest.fixture
def calculator_positive_starting_value():
    return Calculator(2)


@pytest.fixture
def calculator_negative_starting_value():
    return Calculator(-2)


@pytest.fixture
def calculator_0_starting_value():
    return Calculator()


@pytest.mark.parametrize(
    ('input_n', 'expected_a', 'expected_b', 'expected_c'),
    [
        (5, 7, 5, 3),
        (-5, -3, -5, -7),
        (0, 2, 0, -2),  # 1

        (5.1, 7.1, 5.1, 3.1),
        (-5.2, -3.2, -5.2, -7.2),

    ]
)
def test_addition(calculator_positive_starting_value, calculator_0_starting_value, calculator_negative_starting_value,
                  input_n, expected_a, expected_b, expected_c):
    # def test_addition(calculator, params1):
    # input_n, expected = params1
    calculator_positive_starting_value.add(input_n)
    calculator_0_starting_value.add(input_n)
    calculator_negative_starting_value.add(input_n)
    assert calculator_positive_starting_value.get_value() == expected_a
    assert calculator_0_starting_value.get_value() == expected_b
    assert calculator_negative_starting_value.get_value() == expected_c


@pytest.mark.parametrize(
    ('input_n', 'expected_a', 'expected_b', 'expected_c'),
    [
        (10, -8, -10, -12),
        (-5, 7, 5, 3),
        (0, 2, 0, -2),  # 1

        (10.1, -8.1, -10.1, -12.1),
        (-5.2, 7.2, 5.2, 3.2),

    ]
)
def test_substract(calculator_positive_starting_value, calculator_0_starting_value, calculator_negative_starting_value,
                   input_n, expected_a, expected_b, expected_c):
    calculator_positive_starting_value.subtract(input_n)
    calculator_0_starting_value.subtract(input_n)
    calculator_negative_starting_value.subtract(input_n)
    assert calculator_positive_starting_value.get_value() == expected_a
    assert calculator_0_starting_value.get_value() == expected_b
    assert calculator_negative_starting_value.get_value() == expected_c


@pytest.mark.parametrize(
    ('input_n', 'expected_a', 'expected_b', 'expected_c'),
    [
        (4, 8, 0, -8),
        (-2, -4, 0, 4),
        (0, 0, 0, 0),  # 1

        (4.1, 8.2, 0, -8.2),
        (-2.4, -4.8, 0, 4.8),
    ]
)
def test_multiply(calculator_positive_starting_value, calculator_0_starting_value, calculator_negative_starting_value,
                  input_n, expected_a, expected_b, expected_c):
    calculator_positive_starting_value.multiply(input_n)
    calculator_0_starting_value.multiply(input_n)
    calculator_negative_starting_value.multiply(input_n)
    assert calculator_positive_starting_value.get_value() == expected_a
    assert calculator_0_starting_value.get_value() == expected_b
    assert calculator_negative_starting_value.get_value() == expected_c


@pytest.mark.parametrize(
    ('input_n', 'expected_a', 'expected_b', 'expected_c'),
    [
        (2, 1, 0, -1),
        (-2, -1, 0, 1),  # 1

        (8, 0.25, 0, -0.25),
        (-10, -0.2, 0, 0.2)
    ]
)
def test_divide(calculator_positive_starting_value, calculator_0_starting_value, calculator_negative_starting_value,
                input_n, expected_a, expected_b, expected_c):
    calculator_positive_starting_value.divide(input_n)
    calculator_0_starting_value.divide(input_n)
    calculator_negative_starting_value.divide(input_n)
    assert calculator_positive_starting_value.get_value() == expected_a
    assert calculator_0_starting_value.get_value() == expected_b
    assert calculator_negative_starting_value.get_value() == expected_c


def test_reset(calculator_positive_starting_value):
    calculator_positive_starting_value.reset_calculator()
    assert calculator_positive_starting_value.get_value() == 0


def test_division_by_0(calculator_positive_starting_value, capsys):
    calculator_positive_starting_value.divide(0)
    out, err = capsys.readouterr()
    assert out == "You cannot divide by zero. The value has been reset to zero\n"
    assert calculator_positive_starting_value.get_value() == 0


def test_incorrect_types(calculator_positive_starting_value, capsys):
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
    calculator_positive_starting_value.add(10)
    calculator_positive_starting_value.subtract(1123)

    calculator_positive_starting_value.multiply(4)
    calculator_positive_starting_value.divide(2)

    calculator_positive_starting_value.add(300.50)
    calculator_positive_starting_value.add(10.25)
    calculator_positive_starting_value.multiply(8)
    calculator_positive_starting_value.divide(16)
    assert calculator_positive_starting_value.get_value() == -955.625
