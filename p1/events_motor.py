from abc import ABC, abstractmethod
from typing import Tuple
from .event import Event

class EventsMotor(ABC):
    def __init__(self) -> None:
        self.events_queue = []

        self.reactions_table = {
            "unknown": None
        }

        self.active = True


    def activate(self):
        self.active = True


    def deactivate(self):
        self.active = False


    def is_active(self):
        return self.active


    def add_event(self, event : Event) -> None:
        self.events_queue.append(event)


    def extract_event(self) -> Tuple[bool, Event]:
        empty_queue = not self.events_queue

        if empty_queue:
            event = None
        else:
            event = self.events_queue.pop(0)

        return (not empty_queue, event)


    @abstractmethod
    def categorize_event(self, event : Event) -> str:
        pass


    def react_to_event(self, event_type : str, event : Event) -> None:
        self.reactions_table[event_type](event)


    def run(self) -> bool:
        has_pending_event, event = self.extract_event()

        if has_pending_event:
            event_type = self.categorize_event(event)

            self.react_to_event(event_type, event)

            return True
        else:
            print("[INFO] No avaible events")

            return False
