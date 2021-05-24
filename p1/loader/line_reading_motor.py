from ..events_motor import EventsMotor
from .events import FileReadingEvent, DataReadingEvent, LineReadingEvent

class LineReadingMotor(EventsMotor):
    def __init__(self) -> None:
        super().__init__()

        self.reactions_table["data"] = self._save_data
        self.reactions_table["line"] = self._read_line
        self.reactions_table["file_end"] = self._file_end

        self.read_data = []

        self.line_count = 0
        self.data_count = 0


    def set_file_reading_motor(self, file_reading_motor) -> None:
        self.file_reading_motor = file_reading_motor


    def set_mem_storing_motor(self, mem_storing_motor) -> None:
        self.mem_storing_motor = mem_storing_motor


    def activate(self) -> None:
        super().activate()

        self.read_data = []
        self.line_count = 0
        self.data_count = 0


    def categorize_event(self, event: DataReadingEvent) -> str:
        if event.data == "\n":
            return "line"
        elif event.data == "":
            return "file_end"
        else:
            return "data"


    def _save_data(self, event : DataReadingEvent) -> None:
        self.read_data.append(event.data)
        self.data_count += 1

        next_event = FileReadingEvent("read")

        self.file_reading_motor.add_event(next_event)


    def _read_line(self, event : DataReadingEvent) -> None:
        first_line = True if self.line_count == 0 else False

        next_event = LineReadingEvent(first_line, self.read_data, self.data_count)

        self.line_count += 1
        self.data_count = 0
        self.read_data = []

        self.mem_storing_motor.add_event(next_event)

    def _file_end(self, event : DataReadingEvent) -> None:
        # Add end line event
        next_event = LineReadingEvent(False, [], 0)

        self.mem_storing_motor.add_event(next_event)

        self.deactivate()
