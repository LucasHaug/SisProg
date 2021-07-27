import pytest

from p2.calculator.calculator import Calculator

from p2.common import BASE_CHOICES


def test_sum_input():
    calculator = Calculator()

    buttons = ["7", "+", "2", "="]

    for button in buttons:
        calculator.set_input(button)

    assert calculator.get_output() == "9"


def test_subtraction_input():
    calculator = Calculator()

    buttons = ["27", "+", "2", "-", "30", BASE_CHOICES[3], "="]

    for button in buttons:
        calculator.set_input(button)

    assert calculator.get_output() == "-7"


def test_sign_input():
    calculator = Calculator()

    buttons = ["-", "27", "-", "2", "+", "30", BASE_CHOICES[3], "="]

    for button in buttons:
        calculator.set_input(button)

    assert calculator.get_output() == "7"


def test_multi_plus_input():
    calculator = Calculator()

    buttons = ["101", "+", "+", "+", "110", BASE_CHOICES[0], "-", "1", "="]

    for button in buttons:
        calculator.set_input(button)

    assert calculator.get_output() == "1010"


def test_multi_minus_input():
    calculator = Calculator()

    buttons = ["110", "-", "-", "-", "10", BASE_CHOICES[2], "="]

    for button in buttons:
        calculator.set_input(button)

    assert calculator.get_output() == "100"


def test_braces_sign_input():
    calculator = Calculator()

    buttons = ["123", "-", "(", "-", "67", ")", BASE_CHOICES[1], "="]

    for button in buttons:
        calculator.set_input(button)

    assert calculator.get_output() == "212"


def test_multiplication_input():
    calculator = Calculator()

    buttons = ["1111", BASE_CHOICES[0], "*", "10", "-", "111", "="]

    for button in buttons:
        calculator.set_input(button)

    assert calculator.get_output() == "10111"


def test_division_input():
    calculator = Calculator()

    buttons = ["7", "+", "2", "*", "4", "+", "8", "/", "4", "*", "3", "-", "2", "="]

    for button in buttons:
        calculator.set_input(button)

    assert calculator.get_output() == "19"


def test_full_braces():
    calculator = Calculator()

    buttons = ["(", "67", "-", "55", ")", BASE_CHOICES[3], "*", "3", "-", "14", "="]

    for button in buttons:
        calculator.set_input(button)

    assert calculator.get_output() == "22"


def test_clear():
    calculator = Calculator()

    buttons = ["(", "67", "-", "55", ")", BASE_CHOICES[3], "*", "3", "-", "14", "Cl"]

    for button in buttons:
        calculator.set_input(button)

    assert calculator.get_output() == ""


def test_backspace():
    calculator = Calculator()

    buttons = ["(", "67", "-", "55", ")", BASE_CHOICES[3], "*", "3", "3", "⌫", "-", "14", "="]

    for button in buttons:
        calculator.set_input(button)

    assert calculator.get_output() == "22"


def test_invalid_input():
    calculator = Calculator()

    buttons = ["(", "67", "-", "55", ")", BASE_CHOICES[0], "*", "3", "-", "14", "=", "1"]

    with pytest.raises(Exception):
        for button in buttons:
            calculator.set_input(button)
