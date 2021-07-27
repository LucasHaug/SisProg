from ..events_motor import EventsMotor
from .events import DataReadingEvent, ExpressionEvent

from .conversion_motor import ConversionMotor
from .evaluation_motor import EvaluationMotor

from ..common import BASE_CHOICES


class InterfaceMotor(EventsMotor):
    def __init__(self) -> None:
        super().__init__()

        self.reactions_table["clear"] = self._clear_output
        self.reactions_table["equal"] = self._calculate_result
        self.reactions_table["change_base"] = self._change_base
        self.reactions_table["operation_element"] = self._store_operation_element

        self.output = ""
        self.current_base = BASE_CHOICES[2]

        self.conversion_motor = ConversionMotor()
        self.evaluation_motor = EvaluationMotor()

        self.conversion_motor.set_evaluation_motor(self.evaluation_motor)

    def get_output(self) -> str:
        return self.output

    def categorize_event(self, event: DataReadingEvent) -> str:
        if event.data == "Cl":
            return "clear"
        elif event.data == "=":
            return "equal"
        elif event.data in BASE_CHOICES:
            return "change_base"
        else:
            return "operation_element"

    def _clear_output(self, event: DataReadingEvent) -> None:
        self.output = ""

    def _calculate_result(self, event: DataReadingEvent) -> None:
        self.evaluation_motor.activate()
        self.conversion_motor.activate()

        self.conversion_motor.add_event(ExpressionEvent(self.output, self.current_base))

        all_motors_activeted = True

        while all_motors_activeted:
            self.evaluation_motor.run()
            self.conversion_motor.run()

            all_motors_activeted = (
                self.evaluation_motor.is_active() or self.conversion_motor.is_active()
            )

        self.output = self.conversion_motor.get_converted_output()

    def _change_base(self, event: DataReadingEvent) -> None:
        self.current_base = event.data

    def _store_operation_element(self, event: DataReadingEvent) -> None:
        self.output += event.data
