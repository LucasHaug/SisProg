from ..events_motor import EventsMotor
from .events import MemReadingEvent, DataWritingEvent, LineWritingEvent

DATA_SIZE = 2

NUM_OF_DATA_PER_LINE = 16
NUM_OF_SPACES_SEPARATORS = 15
MAX_BYTES = NUM_OF_DATA_PER_LINE * DATA_SIZE + NUM_OF_SPACES_SEPARATORS

class LineWritingMotor(EventsMotor):
    def __init__(self) -> None:
        super().__init__()

        self.reactions_table["start"] = self._start
        self.reactions_table["mem_data"] = self._mem_data
        self.reactions_table["line"] = self._line
        self.reactions_table["end"] = self._end

        self.read_data = []

        self.data_count = 0


    def set_file_writing_motor(self, file_writing_motor) -> None:
        self.file_writing_motor = file_writing_motor


    def set_mem_reading_motor(self, mem_reading_motor) -> None:
        self.mem_reading_motor = mem_reading_motor


    def activate(self) -> None:
        super().activate()

        self.read_data = []
        self.data_count = 0


    def categorize_event(self, event: DataWritingEvent) -> str:
        if event.type == "start":
            return "start"
        elif event.type == "mem_data":
            return "mem_data"
        elif event.type == "line":
            return "line"
        else:
            return "end"


    def _start(self, event : DataWritingEvent) -> None:
        data = event.data
        data.append("\n")

        next_event = LineWritingEvent("open_file", data, len(data))

        self.file_writing_motor.add_event(next_event)


    def _mem_data(self, event : DataWritingEvent) -> None:
        for i in range(event.data_size):
            self.read_data.append(event.data[i])

        self.data_count += 1

        if self.data_count < NUM_OF_DATA_PER_LINE:
            self.read_data.append(" ")

            next_event = MemReadingEvent("read")

            self.mem_reading_motor.add_event(next_event)
        else:
            next_event = DataWritingEvent("line", [], 0)

            self.add_event(next_event)


    def _line(self, event : DataWritingEvent) -> None:
        self.read_data.append("\n")

        next_event = LineWritingEvent("write", self.read_data, MAX_BYTES + 1)

        self.file_writing_motor.add_event(next_event)

        self.read_data = []
        self.data_count = 0


    def _end(self, event : DataWritingEvent) -> None:
        if len(self.read_data) != 0:
            self.read_data[-1] = "\n"

        self.read_data.append("")

        next_event = LineWritingEvent("close_file", self.read_data, len(self.read_data))

        self.file_writing_motor.add_event(next_event)
