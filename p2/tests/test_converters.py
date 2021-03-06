import pytest

from p2.calculator.conversion_motor import ConversionMotor
from p2.common import BASE_CHOICES


def test_valid_convertions_to_base_10():
    conversion_motor = ConversionMotor()

    assert conversion_motor._convert_to_base_10("0", BASE_CHOICES[0]) == 0
    assert conversion_motor._convert_to_base_10("0", BASE_CHOICES[1]) == 0
    assert conversion_motor._convert_to_base_10("0", BASE_CHOICES[2]) == 0
    assert conversion_motor._convert_to_base_10("0", BASE_CHOICES[3]) == 0

    assert conversion_motor._convert_to_base_10("1111", BASE_CHOICES[0]) == 15
    assert conversion_motor._convert_to_base_10("17", BASE_CHOICES[1]) == 15
    assert conversion_motor._convert_to_base_10("15", BASE_CHOICES[2]) == 15
    assert conversion_motor._convert_to_base_10("F", BASE_CHOICES[3]) == 15

    assert conversion_motor._convert_to_base_10("10011000", BASE_CHOICES[0]) == 152
    assert conversion_motor._convert_to_base_10("230", BASE_CHOICES[1]) == 152
    assert conversion_motor._convert_to_base_10("152", BASE_CHOICES[2]) == 152
    assert conversion_motor._convert_to_base_10("98", BASE_CHOICES[3]) == 152

    assert conversion_motor._convert_to_base_10("10000000000", BASE_CHOICES[0]) == 1024
    assert conversion_motor._convert_to_base_10("2000", BASE_CHOICES[1]) == 1024
    assert conversion_motor._convert_to_base_10("1024", BASE_CHOICES[2]) == 1024
    assert conversion_motor._convert_to_base_10("400", BASE_CHOICES[3]) == 1024


def test_invalid_convertions_to_base_10():
    conversion_motor = ConversionMotor()

    with pytest.raises(Exception):
        conversion_motor._convert_to_base_10("-1", BASE_CHOICES[0])

    with pytest.raises(Exception):
        conversion_motor._convert_to_base_10("-1", BASE_CHOICES[1])

    with pytest.raises(Exception):
        conversion_motor._convert_to_base_10("-1", BASE_CHOICES[2])

    with pytest.raises(Exception):
        conversion_motor._convert_to_base_10("-1", BASE_CHOICES[3])

    with pytest.raises(Exception):
        conversion_motor._convert_to_base_10("1.1", BASE_CHOICES[0])

    with pytest.raises(Exception):
        conversion_motor._convert_to_base_10("1.1", BASE_CHOICES[1])

    with pytest.raises(Exception):
        conversion_motor._convert_to_base_10("1.1", BASE_CHOICES[2])

    with pytest.raises(Exception):
        conversion_motor._convert_to_base_10("1.1", BASE_CHOICES[3])

    with pytest.raises(Exception):
        conversion_motor._convert_to_base_10("33", BASE_CHOICES[0])

    with pytest.raises(Exception):
        conversion_motor._convert_to_base_10("91", BASE_CHOICES[1])

    with pytest.raises(Exception):
        conversion_motor._convert_to_base_10("FF", BASE_CHOICES[2])

    with pytest.raises(Exception):
        conversion_motor._convert_to_base_10("G", BASE_CHOICES[3])


def test_valid_convertions_from_base_10():
    conversion_motor = ConversionMotor()

    assert conversion_motor._convert_from_base_10(0, BASE_CHOICES[0]) == "0"
    assert conversion_motor._convert_from_base_10(0, BASE_CHOICES[1]) == "0"
    assert conversion_motor._convert_from_base_10(0, BASE_CHOICES[2]) == "0"
    assert conversion_motor._convert_from_base_10(0, BASE_CHOICES[3]) == "0"

    assert conversion_motor._convert_from_base_10(18, BASE_CHOICES[0]) == "10010"
    assert conversion_motor._convert_from_base_10(18, BASE_CHOICES[1]) == "22"
    assert conversion_motor._convert_from_base_10(18, BASE_CHOICES[2]) == "18"
    assert conversion_motor._convert_from_base_10(18, BASE_CHOICES[3]) == "12"

    assert conversion_motor._convert_from_base_10(152, BASE_CHOICES[0]) == "10011000"
    assert conversion_motor._convert_from_base_10(152, BASE_CHOICES[1]) == "230"
    assert conversion_motor._convert_from_base_10(152, BASE_CHOICES[2]) == "152"
    assert conversion_motor._convert_from_base_10(152, BASE_CHOICES[3]) == "98"

    assert (
        conversion_motor._convert_from_base_10(1024, BASE_CHOICES[0]) == "10000000000"
    )
    assert conversion_motor._convert_from_base_10(1024, BASE_CHOICES[1]) == "2000"
    assert conversion_motor._convert_from_base_10(1024, BASE_CHOICES[2]) == "1024"
    assert conversion_motor._convert_from_base_10(1024, BASE_CHOICES[3]) == "400"

    assert (
        conversion_motor._convert_from_base_10(486485, BASE_CHOICES[0])
        == "1110110110001010101"
    )
    assert conversion_motor._convert_from_base_10(486485, BASE_CHOICES[1]) == "1666125"
    assert conversion_motor._convert_from_base_10(486485, BASE_CHOICES[2]) == "486485"
    assert conversion_motor._convert_from_base_10(486485, BASE_CHOICES[3]) == "76C55"


def test_negative_convertions_from_base_10():
    conversion_motor = ConversionMotor()

    assert conversion_motor._convert_from_base_10(-15, BASE_CHOICES[0]) == "-1111"

    assert conversion_motor._convert_from_base_10(-15, BASE_CHOICES[1]) == "-17"

    assert conversion_motor._convert_from_base_10(-15, BASE_CHOICES[2]) == "-15"

    assert conversion_motor._convert_from_base_10(-15, BASE_CHOICES[3]) == "-F"


def test_invalid_convertions_from_base_10():
    conversion_motor = ConversionMotor()

    with pytest.raises(Exception):
        conversion_motor._convert_from_base_10(1.1, BASE_CHOICES[0])

    with pytest.raises(Exception):
        conversion_motor._convert_from_base_10(1.1, BASE_CHOICES[1])

    with pytest.raises(Exception):
        conversion_motor._convert_from_base_10(1.1, BASE_CHOICES[2])

    with pytest.raises(Exception):
        conversion_motor._convert_from_base_10(1.1, BASE_CHOICES[3])

