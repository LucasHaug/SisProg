from ..events_motor import EventsMotor
from .events import FileReadingEvent, LineReadingEvent

ADDRESS_SIZE = 3
DATA_SIZE = 2

NUM_OF_DATA_PER_LINE = 16
NUM_OF_SPACES_SEPARATORS = 15
MAX_BYTES = NUM_OF_DATA_PER_LINE * DATA_SIZE + NUM_OF_SPACES_SEPARATORS

class MemStoringMotor(EventsMotor):
    def __init__(self) -> None:
        super().__init__()

        self.reactions_table["initial_line"] = self._initial_line
        self.reactions_table["middle_line"] = self._middle_line
        self.reactions_table["last_line"] = self._last_line
        self.reactions_table["invalid_line"] = self._invalid_line

        self.memory_pointer = None
        self.memory_position = 0

        self.decoding_table = {
            "0" : 0x0,
            "1" : 0x1,
            "2" : 0x2,
            "3" : 0x3,
            "4" : 0x4,
            "5" : 0x5,
            "6" : 0x6,
            "7" : 0x7,
            "8" : 0x8,
            "9" : 0x9,
            "A" : 0xA,
            "B" : 0xB,
            "C" : 0xC,
            "D" : 0xD,
            "E" : 0xE,
            "F" : 0xF
        }


    def set_file_reading_motor(self, file_reading_motor) -> None:
        self.file_reading_motor = file_reading_motor


    def set_memory_pointer(self, memory_pointer) -> None:
        self.memory_pointer = memory_pointer


    def activate(self):
        super().activate()

        self.memory_position = 0


    def categorize_event(self, event: LineReadingEvent) -> str:
        if event.first_line:
            if event.line_size != ADDRESS_SIZE:
                return "invalid_line"

            return "initial_line"
        elif event.line_size > MAX_BYTES:
            return "invalid_line"
        elif event.line_size == 0:
            return "last_line"
        else:
            return "middle_line"



    def _initial_line(self, event: LineReadingEvent):
        data = event.line_data
        decoded_data = self._decode(data, ADDRESS_SIZE)

        self.memory_position = decoded_data

        next_event = FileReadingEvent("read")

        self.file_reading_motor.add_event(next_event)


    def _middle_line(self, event: LineReadingEvent):
        line_data = event.line_data

        data = []

        for i in range(event.line_size):
            if line_data[i] == " ":
                if len(data) == DATA_SIZE:
                    decoded_data = self._decode(data, DATA_SIZE)

                    self.memory_pointer[self.memory_position] = decoded_data

                    data = []

                    self.memory_position += 1
                else:
                    # Send ivalid line event
                    next_event = LineReadingEvent(False, [], MAX_BYTES + 1)

                    self.add_event(next_event)
            else:
                data.append(line_data[i])

        next_event = FileReadingEvent("read")

        self.file_reading_motor.add_event(next_event)


    def _last_line(self, event: LineReadingEvent):
        print("[INFO] Finished loading")

        next_event = FileReadingEvent("close_file")

        self.file_reading_motor.add_event(next_event)


    def _invalid_line(self, event: LineReadingEvent):
        print("[ERROR] Make sure to follow the input file specification")

        next_event = FileReadingEvent("close_file")

        self.file_reading_motor.add_event(next_event)


    def _decode(self, data, data_size):
        decoded_data = 0

        for i in range(data_size):
            decoded_data = decoded_data << 4
            decoded_data += self.decoding_table[data[i]]

        return decoded_data
