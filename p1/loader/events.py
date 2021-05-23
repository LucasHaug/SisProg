from ..event import Event

class FileEvent(Event):
    """
    Event type handled by the ReadingMotor
    """

    def __init__(self, event_type) -> None:
        super().__init__()

        self.type = event_type

