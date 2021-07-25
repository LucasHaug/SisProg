import pytest

from p2.calculator.converter_motor import ConverterMotor
from p2.common import BASE_CHOICES


def test_valid_convertions_to_base_10():
    converter_motor = ConverterMotor()

    assert converter_motor._convert_to_base_10("0", BASE_CHOICES[0]) == 0
    assert converter_motor._convert_to_base_10("0", BASE_CHOICES[1]) == 0
    assert converter_motor._convert_to_base_10("0", BASE_CHOICES[2]) == 0
    assert converter_motor._convert_to_base_10("0", BASE_CHOICES[3]) == 0

    assert converter_motor._convert_to_base_10("15", BASE_CHOICES[0]) == 15
    assert converter_motor._convert_to_base_10("1111", BASE_CHOICES[1]) == 15
    assert converter_motor._convert_to_base_10("17", BASE_CHOICES[2]) == 15
    assert converter_motor._convert_to_base_10("F", BASE_CHOICES[3]) == 15

    assert converter_motor._convert_to_base_10("152", BASE_CHOICES[0]) == 152
    assert converter_motor._convert_to_base_10("10011000", BASE_CHOICES[1]) == 152
    assert converter_motor._convert_to_base_10("230", BASE_CHOICES[2]) == 152
    assert converter_motor._convert_to_base_10("98", BASE_CHOICES[3]) == 152

    assert converter_motor._convert_to_base_10("1024", BASE_CHOICES[0]) == 1024
    assert converter_motor._convert_to_base_10("10000000000", BASE_CHOICES[1]) == 1024
    assert converter_motor._convert_to_base_10("2000", BASE_CHOICES[2]) == 1024
    assert converter_motor._convert_to_base_10("400", BASE_CHOICES[3]) == 1024


def test_invalid_convertions_to_base_10():
    converter_motor = ConverterMotor()

    with pytest.raises(Exception):
        converter_motor._convert_to_base_10("-1", BASE_CHOICES[0])

    with pytest.raises(Exception):
        converter_motor._convert_to_base_10("-1", BASE_CHOICES[1])

    with pytest.raises(Exception):
        converter_motor._convert_to_base_10("-1", BASE_CHOICES[2])

    with pytest.raises(Exception):
        converter_motor._convert_to_base_10("-1", BASE_CHOICES[3])

    with pytest.raises(Exception):
        converter_motor._convert_to_base_10("1.1", BASE_CHOICES[0])

    with pytest.raises(Exception):
        converter_motor._convert_to_base_10("1.1", BASE_CHOICES[1])

    with pytest.raises(Exception):
        converter_motor._convert_to_base_10("1.1", BASE_CHOICES[2])

    with pytest.raises(Exception):
        converter_motor._convert_to_base_10("1.1", BASE_CHOICES[3])

    with pytest.raises(Exception):
        converter_motor._convert_to_base_10("FF", BASE_CHOICES[0])

    with pytest.raises(Exception):
        converter_motor._convert_to_base_10("33", BASE_CHOICES[1])

    with pytest.raises(Exception):
        converter_motor._convert_to_base_10("91", BASE_CHOICES[2])

    with pytest.raises(Exception):
        converter_motor._convert_to_base_10("G", BASE_CHOICES[3])
