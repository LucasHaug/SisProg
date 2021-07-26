from collections import OrderedDict

from ..events_motor import EventsMotor
from .events import ExpressionEvent

from ..common import BASE_CHOICES


class ConverterMotor(EventsMotor):
    def __init__(self) -> None:
        super().__init__()

        self.reactions_table["detect_expression"] = self._detect_expression
        self.reactions_table["read_number"] = self._read_number
        self.reactions_table["read_operator"] = self._read_operator
        self.reactions_table["get_result"] = self._get_result

        self.converted_output = ""

        self.to_base_10 = OrderedDict({
            "0" : 0,
            "1" : 1,
            "2" : 2,
            "3" : 3,
            "4" : 4,
            "5" : 5,
            "6" : 6,
            "7" : 7,
            "8" : 8,
            "9" : 9,
            "A" : 10,
            "B" : 11,
            "C" : 12,
            "D" : 13,
            "E" : 14,
            "F" : 15,
        })

        self.from_base_10 = {
            0  : "0",
            1  : "1",
            2  : "2",
            3  : "3",
            4  : "4",
            5  : "5",
            6  : "6",
            7  : "7",
            8  : "8",
            9  : "9",
            10 : "A",
            11 : "B",
            12 : "C",
            13 : "D",
            14 : "E",
            15 : "F"
        }


    def get_converted_output(self) -> str:
        return self.converted_output


    def set_evaluator_motor(self, evaluator_motor) -> None:
        self.evaluator_motor = evaluator_motor


    def activate(self) -> None:
        super().activate()

        self.converted_output = ""


    def deactivate(self) -> None:
        super().deactivate()

        self.converted_output = ""


    def categorize_event(self, event: ExpressionEvent) -> str:
        if event.start_type == "number":
            return "read_number"
        elif event.start_type == "operator":
            return "read_operator"
        elif event.start_type == "empty":
            return "get_result"
        else:
            return "detect_expression"


    def _detect_expression(self, event: ExpressionEvent) -> None:
        pass


    def _read_number(self, event: ExpressionEvent) -> None:
        pass


    def _read_operator(self, event: ExpressionEvent) -> None:
        pass


    def _get_result(self, event: ExpressionEvent) -> None:
        pass


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

        base = 0

        if base_name == "Binário":
            base = 2
        elif base_name == "Octal":
            base = 8
        elif base_name == "Hexadecimal":
            base = 16
        else:
            base = 10

        base_dict = self._slice_odict(self.to_base_10, 0, base)

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

        base = 0

        if base_name == "Binário":
            base = 2
        elif base_name == "Octal":
            base = 8
        elif base_name == "Hexadecimal":
            base = 16
        else:
            base = 10

        base_dict = self._slice_odict(self.from_base_10, 0, base)

        result = ""

        if number == 0:
            result = "0"
        else:
            while number > 0:
                try:
                    result = base_dict[number % base] + result
                except KeyError:
                    raise ValueError("Malformed expression")

                number //= base

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
