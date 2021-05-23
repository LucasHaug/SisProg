from ..event import Event

class MemReadingEvent(Event):
    """
    Event type handled by the MemReadingMotor
    """

    def __init__(self, event_type) -> None:
        super().__init__()

        self.type = event_type


class LineWritingEvent(Event):
    """
    Event type handled by the FileWritingMotor
    """

    def __init__(self, event_type, line_data, line_size) -> None:
        super().__init__()

        self.type = event_type
        self.line_data = line_data
        self.line_size = line_size
