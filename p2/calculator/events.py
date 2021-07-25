from ..event import Event

class DataReadingEvent(Event):
    """
    Event type handled by the InterfaceMotor
    """

    def __init__(self, event_data) -> None:
        super().__init__()

        self.data = event_data
