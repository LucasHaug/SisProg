import pytest

from p2.calculator.evaluation_motor import EvaluationMotor
from p2.calculator.events import OperationElementEvent


def test_sum_input():
    evaluation_motor = EvaluationMotor()

    evaluation_motor.activate()

    elements = [7, "+", 2]
    elements_types = ["number", "operator", "number"]

    for element, element_type in zip(elements, elements_types):
        evaluation_motor.add_event(OperationElementEvent(element, element_type))

    evaluation_motor.add_event(OperationElementEvent("", "finish"))

    while evaluation_motor.is_active():
        evaluation_motor.run()

    assert evaluation_motor.get_result() == 9


def test_subtraction_input():
    evaluation_motor = EvaluationMotor()

    evaluation_motor.activate()

    elements = [18, "+", 2, "-", 25]
    elements_types = ["number", "operator", "number", "operator", "number"]

    for element, element_type in zip(elements, elements_types):
        evaluation_motor.add_event(OperationElementEvent(element, element_type))

    evaluation_motor.add_event(OperationElementEvent("", "finish"))

    while evaluation_motor.is_active():
        evaluation_motor.run()

    assert evaluation_motor.get_result() == -5


def test_sign_input():
    evaluation_motor = EvaluationMotor()

    evaluation_motor.activate()

    elements = ["-", 18, "-", 2, "+", 25]
    elements_types = ["operator", "number", "operator", "number", "operator", "number"]

    for element, element_type in zip(elements, elements_types):
        evaluation_motor.add_event(OperationElementEvent(element, element_type))

    evaluation_motor.add_event(OperationElementEvent("", "finish"))

    while evaluation_motor.is_active():
        evaluation_motor.run()

    assert evaluation_motor.get_result() == 5


def test_multi_plus_input():
    evaluation_motor = EvaluationMotor()

    evaluation_motor.activate()

    elements = [18, "-", 2, "+", "+", 25]
    elements_types = ["number", "operator", "number", "operator", "operator", "number"]

    for element, element_type in zip(elements, elements_types):
        evaluation_motor.add_event(OperationElementEvent(element, element_type))

    evaluation_motor.add_event(OperationElementEvent("", "finish"))

    while evaluation_motor.is_active():
        evaluation_motor.run()

    assert evaluation_motor.get_result() == 41


def test_multiplication_input():
    evaluation_motor = EvaluationMotor()

    evaluation_motor.activate()

    elements = [18, "+", 2, "*", 25, "-", 8]
    elements_types = [
        "number",
        "operator",
        "number",
        "operator",
        "number",
        "operator",
        "number",
    ]

    for element, element_type in zip(elements, elements_types):
        evaluation_motor.add_event(OperationElementEvent(element, element_type))

    evaluation_motor.add_event(OperationElementEvent("", "finish"))

    while evaluation_motor.is_active():
        evaluation_motor.run()

    assert evaluation_motor.get_result() == 60


def test_division_input():
    evaluation_motor = EvaluationMotor()

    evaluation_motor.activate()

    elements = [18, "+", 24, "/", 2, "-", 8]
    elements_types = [
        "number",
        "operator",
        "number",
        "operator",
        "number",
        "operator",
        "number",
    ]

    for element, element_type in zip(elements, elements_types):
        evaluation_motor.add_event(OperationElementEvent(element, element_type))

    evaluation_motor.add_event(OperationElementEvent("", "finish"))

    while evaluation_motor.is_active():
        evaluation_motor.run()

    assert evaluation_motor.get_result() == 22


def test_invalid_input():
    evaluation_motor = EvaluationMotor()

    evaluation_motor.activate()

    elements = [18, "a", 24, "/", 2, "-", 8]
    elements_types = [
        "number",
        "operator",
        "number",
        "operator",
        "number",
        "operator",
        "number",
    ]

    for element, element_type in zip(elements, elements_types):
        evaluation_motor.add_event(OperationElementEvent(element, element_type))

    evaluation_motor.add_event(OperationElementEvent("", "finish"))

    with pytest.raises(Exception):
        while evaluation_motor.is_active():
            evaluation_motor.run()
