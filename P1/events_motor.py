from abc import ABC, abstractmethod

class Event():
    def __init__(self) -> None:
        pass


class EventsMotor(ABC):
    def __init__(self) -> None:
        self.events_queue = []

        self.reactions_table = {
            "unknown": None
        }


    def add_event(self, event : Event) -> None:
        self.events_queue.append(event)


    def extract_event(self, event : Event) -> bool:
        if not self.events_queue:
            return False
        else:
            event = self.events_queue.pop(0)

            return True


    @abstractmethod
    def categorize_event(self, event : Event) -> str:
        pass


    def react_to_event(self, event_type : str, event : Event) -> None:
        self.reactions_table[event_type](event)


    def run(self) -> None:
        event = Event()

        if self.extract_event(event):
            event_type = self.categorize_event(event)

            self.react_to_event(event_type, event)
