from .interface_motor import InterfaceMotor

from .events import DataReadingEvent

class Calculator:
    def __init__(self) -> None:
        self.interface_motor = InterfaceMotor()


    def set_input(self, input_str: str) -> None:
        self.interface_motor.add_event(DataReadingEvent(input_str))

        self.interface_motor.run()


    def get_output(self) -> str:
        return self.interface_motor.get_output()
