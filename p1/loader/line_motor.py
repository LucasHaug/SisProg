from ..events_motor import EventsMotor
from .events import DataEvent

class LineMotor(EventsMotor):
    def __init__(self) -> None:
        super().__init__()


    def categorize_event(self, event: DataEvent) -> str:
        pass
