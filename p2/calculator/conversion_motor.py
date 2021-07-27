from collections import OrderedDict

from ..events_motor import EventsMotor
from .events import ExpressionEvent, OperationElementEvent

from ..common import BASE_CHOICES


class ConversionMotor(EventsMotor):
    def __init__(self) -> None:
        super().__init__()

        self.reactions_table["detect_expression"] = self._detect_expression
        self.reactions_table["read_number"] = self._read_number
        self.reactions_table["read_operator"] = self._read_operator
        self.reactions_table["finish_calculation"] = self._finish_calculation

        self.current_base = BASE_CHOICES[0]

        self.operators = ["+", "-", "*", "/", "(", ")"]

        self.to_base_10 = OrderedDict(
            {
                "0": 0,
                "1": 1,
                "2": 2,
                "3": 3,
                "4": 4,
                "5": 5,
                "6": 6,
                "7": 7,
                "8": 8,
                "9": 9,
                "A": 10,
                "B": 11,
                "C": 12,
                "D": 13,
                "E": 14,
                "F": 15,
            }
        )

        self.from_base_10 = {
            0: "0",
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            10: "A",
            11: "B",
            12: "C",
            13: "D",
            14: "E",
            15: "F",
        }

    def get_converted_output(self) -> str:
        result = self.evaluation_motor.get_result()

        converted_output = self._convert_from_base_10(result, self.current_base)

        return converted_output

    def set_evaluation_motor(self, evaluation_motor) -> None:
        self.evaluation_motor = evaluation_motor

    def activate(self) -> None:
        super().activate()

        self.converted_output = ""

    def categorize_event(self, event: ExpressionEvent) -> str:
        if event.start_type == "number":
            return "read_number"
        elif event.start_type == "operator":
            return "read_operator"
        elif event.start_type == "empty":
            return "finish_calculation"
        else:
            return "detect_expression"

    def _detect_expression(self, event: ExpressionEvent) -> None:
        self.current_base = event.base

        if len(event.expression) == 0:
            next_event = ExpressionEvent("", event.base, "empty")

            self.add_event(next_event)

            return

        base_dict = self._get_base_dict(self.to_base_10, event.base)

        if event.expression[0] in self.operators:
            next_event = ExpressionEvent(event.expression, event.base, "operator")

            self.add_event(next_event)
        elif event.expression[0] in base_dict:
            next_event = ExpressionEvent(event.expression, event.base, "number")

            self.add_event(next_event)
        else:
            raise ValueError("Malformed expression")

    def _read_number(self, event: ExpressionEvent) -> None:
        base_dict = self._get_base_dict(self.to_base_10, event.base)

        number_str = ""

        while len(event.expression) > 0 and event.expression[0] in base_dict:
            number_str += event.expression[0]
            event.expression = event.expression[1:]

        number = self._convert_to_base_10(number_str, event.base)

        eval_next_event = OperationElementEvent(number, "number")

        self.evaluation_motor.add_event(eval_next_event)

        exp_next_event = ExpressionEvent(event.expression, event.base, None)

        self.add_event(exp_next_event)

    def _read_operator(self, event: ExpressionEvent) -> None:
        eval_next_event = OperationElementEvent(event.expression[0], "operator")

        self.evaluation_motor.add_event(eval_next_event)

        exp_next_event = ExpressionEvent(event.expression[1:], event.base, None)

        self.add_event(exp_next_event)

    def _finish_calculation(self, event: ExpressionEvent) -> None:
        next_event = OperationElementEvent("", "empty")

        self.evaluation_motor.add_event(next_event)

        self.deactivate()

    def _convert_to_base_10(self, number: str, base_name: str) -> int:
        """
        Convert a number from a base specified to base 10.

        Uses the self.to_base_10 dictionary to convert each
        digit of the number.

        Arguments
        ---------
        number : str
            Number to convert
        base_name : str
            Name of the base of the number to be converted, the
            options are listed in the BASE_CHOICES constant

        Returns
        -------
        int
            Number converted to base 10
        """

        base = self._get_base_number_in_base_10(base_name)

        base_dict = self._get_base_dict(self.to_base_10, base_name)

        result = 0

        for i in range(len(number)):
            try:
                result += base_dict[number[i]] * (base ** (len(number) - i - 1))
            except KeyError:
                raise ValueError("Malformed expression")

        return result

    def _convert_from_base_10(self, number: int, base_name: str) -> str:
        """
        Convert a number from base 10 to the base specified.

        Uses the self.to_base_10 dictionary to convert each
        digit of the number.

        Arguments
        ---------
        number : int
            Number to convert
        base_name : str
            Name of the base of the number to be converted, the
            options are listed in the BASE_CHOICES constant

        Returns
        -------
        int
            Number converted to the specified base
        """

        base = self._get_base_number_in_base_10(base_name)

        base_dict = self._get_base_dict(self.from_base_10, base_name)

        result = ""

        if number == 0:
            result = "0"
        elif number > 0:
            while number > 0:
                try:
                    result = base_dict[number % base] + result
                except KeyError:
                    raise ValueError("Malformed expression")

                number //= base
        else:
            raise ValueError("Malformed expression")

        return result

    def _slice_odict(self, odict: OrderedDict, start: int, stop: int) -> OrderedDict:
        """
        Slice an OrderedDict.

        Arguments
        ---------
        odict : OrderedDict
            OrderedDict to slice
        start : int
            Start index
        stop : int
            Stop index

        Returns
        -------
        OrderedDict
            Slice of the OrderedDict
        """

        return OrderedDict(list(odict.items())[start:stop])

    def _get_base_number_in_base_10(self, base_name: str) -> int:
        """
        Get the number in base 10.

        Arguments
        ---------
        base_name : str
            Name of the base of the number to be converted, the
            options are listed in the BASE_CHOICES constant

        Returns
        -------
        int
            Number converted to base 10
        """

        if base_name == BASE_CHOICES[0]:
            return 2
        elif base_name == BASE_CHOICES[1]:
            return 8
        elif base_name == BASE_CHOICES[3]:
            return 16
        else:
            return 10

    def _get_base_dict(
        self, conversion_dict: OrderedDict, base_name: str
    ) -> OrderedDict:
        """
        Get the base dictionary.

        Arguments
        ---------
        conversion_dict : OrderedDict
            Base dictionary to get from the base dictionary

        base_name : str
            Name of the base to get

        Returns
        -------
        OrderedDict
            Dictionary of the base
        """

        base = self._get_base_number_in_base_10(base_name)

        base_dict = self._slice_odict(conversion_dict, 0, base)

        return base_dict
