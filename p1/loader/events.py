from ..event import Event

class FileEvent(Event):
    """
    Event type handled by the ReadingMotor
    """

    def __init__(self, event_type) -> None:
        super().__init__()

        self.type = event_type

class DataEvent(Event):
    """
    Event type handled by the LineMotor
    """

    def __init__(self, event_data) -> None:
        super().__init__()

        self.data = event_data


class LineEvent(Event):
    """
    Event type handled by the StoringMotor
    """

    def __init__(self, line_number, line_data, line_size) -> None:
        super().__init__()

        self.line_number = line_number
        self.line_data = line_data
        self.line_size = line_size
