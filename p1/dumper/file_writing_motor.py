from ..events_motor import EventsMotor
from .events import LineWritingEvent, MemReadingEvent

class FileWritingMotor(EventsMotor):
    def __init__(self) -> None:
        super().__init__()

        self.reactions_table["open_file"] = self._open_file
        self.reactions_table["write"] = self._write
        self.reactions_table["close_file"] = self._close_file
        self.reactions_table["error"] = self._error

        self.encoding_table = {
            ""   : b'',
            "\n" : b'\x0A',
            " "  : b'\x20',
            "0"  : b'\x30',
            "1"  : b'\x31',
            "2"  : b'\x32',
            "3"  : b'\x33',
            "4"  : b'\x34',
            "5"  : b'\x35',
            "6"  : b'\x36',
            "7"  : b'\x37',
            "8"  : b'\x38',
            "9"  : b'\x39',
            "A"  : b'\x41',
            "B"  : b'\x42',
            "C"  : b'\x43',
            "D"  : b'\x44',
            "E"  : b'\x45',
            "F"  : b'\x46'
        }


    def set_file_name(self, file_name):
        self.file_name = file_name


    def set_mem_reading_motor(self, mem_reading_motor) -> None:
        self.mem_reading_motor = mem_reading_motor


    def categorize_event(self, event: LineWritingEvent) -> str:
        if event.type == "open_file":
            return "open_file"
        elif event.type == "write":
            return "write"
        elif event.type == "close_file":
            return "close_file"
        else:
            return "error"


    def _open_file(self, event: LineWritingEvent) -> None:
        self.file = open(self.file_name, 'wb')

        next_event = LineWritingEvent("write", event.line_data, event.line_size)

        self.add_event(next_event)


    def _write(self, event: LineWritingEvent) -> None:
        for i in range(event.line_size):
            encoded_data = self._encode(event.line_data[i])

            if encoded_data is not None:
                self.file.write(encoded_data)
            else:
                next_event = LineWritingEvent("error", [], 0)

                self.add_event(next_event)

        next_event = MemReadingEvent("read")

        self.mem_reading_motor.add_event(next_event)


    def _close_file(self, event: LineWritingEvent) -> None:
        # Write pending data
        for i in range(event.line_size):
            encoded_data = self._encode(event.line_data[i])

            if encoded_data is not None:
                self.file.write(encoded_data)

        self.file.close()

        self.deactivate()


    def _error(self, event: LineWritingEvent) -> None:
        print("[ERROR] Incorrect data type")

        next_event = LineWritingEvent("close_file", [], 0)

        self.add_event(next_event)


    def _encode(self, read_char):
        if read_char in self.encoding_table:
            return self.encoding_table[read_char]
        else:
            return None
