from ..events_motor import EventsMotor
from .events import DataEvent, FileEvent

class LineMotor(EventsMotor):
    def __init__(self) -> None:
        super().__init__()

        self.reactions_table["data"] = self._save_data
        self.reactions_table["line"] = self._read_line

        self.read_data = []


    def set_reading_motor(self, reading_motor) -> None:
        self.reading_motor = reading_motor


    def set_storing_motor(self, storing_motor) -> None:
        self.storing_motor = storing_motor


    def categorize_event(self, event: DataEvent) -> str:
        if event.data == "\n":
            return "line"
        else:
            return "data"


    def _save_data(self, event) -> None:
        self.read_data.append(event.data)

        next_event = FileEvent("read")

        self.reading_motor.add_event(next_event)


    def _read_line(self, event) -> None:
        print(self.read_data)

        next_event = FileEvent("close_file")

        self.reading_motor.add_event(next_event)
