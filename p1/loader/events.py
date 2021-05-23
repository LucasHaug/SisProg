from ..event import Event

class FileReadingEvent(Event):
    """
    Event type handled by the FileReadingMotor
    """

    def __init__(self, event_type) -> None:
        super().__init__()

        self.type = event_type

class DataReadingEvent(Event):
    """
    Event type handled by the LineReadingMotor
    """

    def __init__(self, event_data) -> None:
        super().__init__()

        self.data = event_data


class LineReadingEvent(Event):
    """
    Event type handled by the MemStoringMotor
    """

    def __init__(self, line_number, line_data, line_size) -> None:
        super().__init__()

        self.line_number = line_number
        self.line_data = line_data
        self.line_size = line_size
