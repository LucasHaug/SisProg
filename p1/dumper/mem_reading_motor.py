from ..events_motor import EventsMotor
from .events import MemReadingEvent, DataWritingEvent

ADDRESS_SIZE = 3
DATA_SIZE = 2

class MemReadingMotor(EventsMotor):
    def __init__(self) -> None:
        super().__init__()

        self.reactions_table["start"] = self._start
        self.reactions_table["read"] = self._read
        self.reactions_table["end"] = self._end

        self.memory_pointer = None
        self.memory_position = 0
        self.start_poistion = 0
        self.end_position = 0

        self.encoding_table = {
            0x0 : "0",
            0x1 : "1",
            0x2 : "2",
            0x3 : "3",
            0x4 : "4",
            0x5 : "5",
            0x6 : "6",
            0x7 : "7",
            0x8 : "8",
            0x9 : "9",
            0xA : "A",
            0xB : "B",
            0xC : "C",
            0xD : "D",
            0xE : "E",
            0xF : "F"
        }


    def set_line_writing_motor(self, line_writing_motor) -> None:
        self.line_writing_motor = line_writing_motor


    def set_memory_pointer(self, memory_pointer) -> None:
        self.memory_pointer = memory_pointer


    def set_dumping_area(self, start_poistion, end_position) -> None:
        self.start_poistion = start_poistion
        self.end_position = end_position


    def activate(self):
        super().activate()

        self.memory_position = 0


    def categorize_event(self, event: MemReadingEvent) -> str:
        if event.type == "start":
            return "start"
        elif event.type == "end" or self.memory_position == (self.end_position + 1):
            return "end"
        elif event.type == "read":
            return "read"


    def _start(self, event: MemReadingEvent):
        self.memory_position = self.start_poistion

        encoded_data = self._encode(self.start_poistion, ADDRESS_SIZE)

        next_event = DataWritingEvent("start", encoded_data, ADDRESS_SIZE)

        self.line_writing_motor.add_event(next_event)


    def _read(self, event: MemReadingEvent):
        mem_data = self.memory_pointer[self.memory_position]

        self.memory_position +=1

        encoded_data = self._encode(mem_data, DATA_SIZE)

        next_event = DataWritingEvent("mem_data", encoded_data, DATA_SIZE)

        self.line_writing_motor.add_event(next_event)


    def _end(self, event: MemReadingEvent):
        print("[INFO] Finished dumping")

        next_event = DataWritingEvent("end", [""], 1)

        self.line_writing_motor.add_event(next_event)


    def _encode(self, data, data_size):
        decoded_data = []

        for i in range(data_size):
            partial_data = data >> (4 * i)
            partial_data &= 0xF

            decoded_data.append(self.encoding_table[partial_data])

        return decoded_data
