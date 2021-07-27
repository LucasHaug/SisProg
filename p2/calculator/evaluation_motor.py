# Logic based on https://www.geeksforgeeks.org/expression-evaluation/

import logging

from ..events_motor import EventsMotor
from .events import OperationElementEvent


class EvaluationMotor(EventsMotor):
    def __init__(self):
        super().__init__()

        self.reactions_table["opening_brace"] = self._opening_brace
        self.reactions_table["number"] = self._number
        self.reactions_table["closing_brace"] = self._closing_brace
        self.reactions_table["basic_operator"] = self._basic_operator
        self.reactions_table["sign"] = self._sign
        self.reactions_table["finish"] = self._finish

        self.values_stack = []
        self.operations_stack = []

        self.last_event = OperationElementEvent("", None)

        self.change_sign = False

        self.result = 0

    def get_result(self):
        if len(self.values_stack) != 0 or len(self.operations_stack) != 0:
            raise Exception("Calculation not finished")

        return self.result

    def activate(self) -> None:
        super().activate()

        self.values_stack = []
        self.operations_stack = []

        self.last_event = OperationElementEvent("", None)

        self.change_sign = False

        self.result = 0

    def deactivate(self) -> None:
        super().deactivate()

        self.values_stack = []
        self.operations_stack = []

        self.change_sign = False

        self.last_event = OperationElementEvent("", None)

    def categorize_event(self, event: OperationElementEvent) -> str:
        if event.element == "(" and event.element_type == "operator":
            return "opening_brace"
        elif event.element_type == "number":
            return "number"
        elif event.element == ")" and event.element_type == "operator":
            return "closing_brace"
        elif event.element_type == "empty":
            return "finish"
        elif event.element == "-" and self.last_event.element_type in [
            "operator",
            None,
        ]:
            return "sign"
        else:
            return "basic_operator"

    def _opening_brace(self, event: OperationElementEvent) -> None:
        self.operations_stack.append(event.element)

        self.last_event = event

    def _number(self, event: OperationElementEvent) -> None:
        number = event.element

        if self.change_sign:
            self.change_sign = False
            number *= -1

        self.values_stack.append(number)

        self.last_event = event

    def _closing_brace(self, event: OperationElementEvent) -> None:
        while len(self.operations_stack) != 0 and self.operations_stack[-1] != "(":
            self._calc_from_stack()

        # Pop opening brace.
        self.operations_stack.pop()

        self.last_event = event

    def _basic_operator(self, event: OperationElementEvent) -> None:
        while len(self.operations_stack) != 0 and self._precedence(
            self.operations_stack[-1]
        ) >= self._precedence(event.element):

            self._calc_from_stack()

        # Push current token to 'self.operations_stack'
        self.operations_stack.append(event.element)

        self.last_event = event

    def _sign(self, event: OperationElementEvent) -> None:
        if self.last_event.element_type is None:
            self.values_stack.append(0)
            self.operations_stack.append(event.element)
        elif self.last_event.element == "-":
            self.operations_stack.pop()
            self.operations_stack.append("+")
            event.element = "+"
        else:
            self.change_sign = True

        self.last_event = event

    def _finish(self, event: OperationElementEvent) -> None:
        while len(self.operations_stack) != 0:
            self._calc_from_stack()

        self.result = self.values_stack.pop()

        self.deactivate()

    def _precedence(self, operator):
        if operator == "*" or operator == "/":
            return 2
        elif operator == "+" or operator == "-":
            return 1
        else:
            return 0

    def _apply_operation(self, first_value, second_value, operator):
        if operator == "*":
            return first_value * second_value
        elif operator == "/":
            return first_value // second_value
        elif operator == "+":
            return first_value + second_value
        elif operator == "-":
            return first_value - second_value
        else:
            raise Exception("Invalid operator")

    def _calc_from_stack(self):
        logging.debug(f"Operation stack: {self.operations_stack}")
        logging.debug(f"Values stack: {self.values_stack}")

        try:
            second_value = self.values_stack.pop()

            operation = self.operations_stack.pop()

            if len(self.values_stack) == 0 and operation in ["+", "-"]:
                first_value = 0
            else:
                first_value = self.values_stack.pop()

            self.values_stack.append(
                self._apply_operation(first_value, second_value, operation)
            )

            logging.debug(f"{first_value} {operation} {second_value} = {self.values_stack[-1]}")

        except IndexError:
            raise Exception("Invalid expression")
