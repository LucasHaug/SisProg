from ..events_motor import EventsMotor
from .events import FileEvent, DataEvent

class ReadingMotor(EventsMotor):
    def __init__(self, file_name) -> None:
        super().__init__()

        self.reactions_table["open_file"] = self._open_file
        self.reactions_table["read"] = self._read
        self.reactions_table["close_file"] = self._close_file
        self.reactions_table["error"] = self._error

        self.file_name = file_name

        self.decoding_table = {
            b'\x0A': "\n",
            b'\x20': " ",
            b'\x30': "0",
            b'\x31': "1",
            b'\x32': "2",
            b'\x33': "3",
            b'\x34': "4",
            b'\x35': "5",
            b'\x36': "6",
            b'\x37': "7",
            b'\x38': "8",
            b'\x39': "9",
            b'\x41': "A",
            b'\x42': "B",
            b'\x43': "C",
            b'\x44': "D",
            b'\x45': "E",
            b'\x46': "F"
        }


    def set_line_motor(self, line_motor) -> None:
        self.line_motor = line_motor


    def categorize_event(self, event: FileEvent) -> str:
        if event.type == "open_file":
            return "open_file"
        elif event.type == "read":
            return "read"
        elif event.type == "close_file":
            return "close_file"
        else:
            return "error"


    def _open_file(self, event) -> None:
        self.file = open(self.file_name, 'rb')

        next_event = FileEvent("read")

        self.add_event(next_event)


    def _read(self, event) -> None:
        data = self.file.read(1)

        decoded_data = self._decode(data)

        if decoded_data is not None:
            next_event = DataEvent(decoded_data)

            self.line_motor.add_event(next_event)


    def _close_file(self, event) -> None:
        self.file.close()


    def _error(self, event) -> None:
        print("[ERROR] Incorrect file content")


    def _decode(self, read_byte):
        if read_byte in self.decoding_table:
            return self.decoding_table[read_byte]
        else:
            next_event = FileEvent("error")

            self.add_event(next_event)

            return None
