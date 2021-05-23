from ..events_motor import EventsMotor
from .events import FileEvent, DataEvent, LineEvent

class LineMotor(EventsMotor):
    def __init__(self) -> None:
        super().__init__()

        self.reactions_table["data"] = self._save_data
        self.reactions_table["line"] = self._read_line

        self.read_data = []

        self.line_count = 0
        self.data_count = 0


    def set_reading_motor(self, reading_motor) -> None:
        self.reading_motor = reading_motor


    def set_storing_motor(self, storing_motor) -> None:
        self.storing_motor = storing_motor


    def activate(self) -> None:
        super().activate()

        self.line_count = 0
        self.data_count = 0


    def categorize_event(self, event: DataEvent) -> str:
        if event.data == "\n":
            return "line"
        else:
            return "data"


    def _save_data(self, event : DataEvent) -> None:
        self.read_data.append(event.data)
        self.data_count += 1

        next_event = FileEvent("read")

        self.reading_motor.add_event(next_event)


    def _read_line(self, event : DataEvent) -> None:
        next_event = LineEvent(self.line_count, self.read_data, self.data_count)

        self.line_count += 1
        self.data_count = 0
        self.read_data = []

        self.storing_motor.add_event(next_event)
