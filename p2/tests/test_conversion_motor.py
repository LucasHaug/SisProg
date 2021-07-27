import pytest

from p2.calculator.conversion_motor import ConversionMotor
from p2.calculator.evaluation_motor import EvaluationMotor
from p2.calculator.events import ExpressionEvent

from p2.common import BASE_CHOICES


def test_sum_expression():
    evaluation_motor = EvaluationMotor()
    conversion_motor = ConversionMotor()

    conversion_motor.set_evaluation_motor(evaluation_motor)

    evaluation_motor.activate()
    conversion_motor.activate()

    conversion_motor.add_event(ExpressionEvent("7+1+2", BASE_CHOICES[2]))

    all_motors_activeted = True

    while all_motors_activeted:
        evaluation_motor.run()
        conversion_motor.run()

        all_motors_activeted = (
            evaluation_motor.is_active() or conversion_motor.is_active()
        )

    assert conversion_motor.get_converted_output() == "10"


def test_subtraction_expression():
    evaluation_motor = EvaluationMotor()
    conversion_motor = ConversionMotor()

    conversion_motor.set_evaluation_motor(evaluation_motor)

    evaluation_motor.activate()
    conversion_motor.activate()

    conversion_motor.add_event(ExpressionEvent("7FF-1-2F", BASE_CHOICES[3]))

    all_motors_activeted = True

    while all_motors_activeted:
        evaluation_motor.run()
        conversion_motor.run()

        all_motors_activeted = (
            evaluation_motor.is_active() or conversion_motor.is_active()
        )

    assert conversion_motor.get_converted_output() == "7CF"


def test_multiplication_expression():
    evaluation_motor = EvaluationMotor()
    conversion_motor = ConversionMotor()

    conversion_motor.set_evaluation_motor(evaluation_motor)

    evaluation_motor.activate()
    conversion_motor.activate()

    conversion_motor.add_event(ExpressionEvent("101*110+10", BASE_CHOICES[0]))

    all_motors_activeted = True

    while all_motors_activeted:
        evaluation_motor.run()
        conversion_motor.run()

        all_motors_activeted = (
            evaluation_motor.is_active() or conversion_motor.is_active()
        )

    assert conversion_motor.get_converted_output() == "100000"


def test_division_expression():
    evaluation_motor = EvaluationMotor()
    conversion_motor = ConversionMotor()

    conversion_motor.set_evaluation_motor(evaluation_motor)

    evaluation_motor.activate()
    conversion_motor.activate()

    conversion_motor.add_event(ExpressionEvent("101*113/31", BASE_CHOICES[1]))

    all_motors_activeted = True

    while all_motors_activeted:
        evaluation_motor.run()
        conversion_motor.run()

        all_motors_activeted = (
            evaluation_motor.is_active() or conversion_motor.is_active()
        )

    assert conversion_motor.get_converted_output() == "303"


def test_braces_expression():
    evaluation_motor = EvaluationMotor()
    conversion_motor = ConversionMotor()

    conversion_motor.set_evaluation_motor(evaluation_motor)

    evaluation_motor.activate()
    conversion_motor.activate()

    conversion_motor.add_event(ExpressionEvent("2*(113+33/11)", BASE_CHOICES[2]))

    all_motors_activeted = True

    while all_motors_activeted:
        evaluation_motor.run()
        conversion_motor.run()

        all_motors_activeted = (
            evaluation_motor.is_active() or conversion_motor.is_active()
        )

    assert conversion_motor.get_converted_output() == "232"
