from .file_reading_motor import FileReadingMotor
from .line_reading_motor import LineReadingMotor
from .mem_storing_motor import MemStoringMotor
from .events import FileReadingEvent

class Loader():
    def __init__(self) -> None:
        self.file_reading_motor = FileReadingMotor()
        self.line_reading_motor = LineReadingMotor()
        self.mem_storing_motor = MemStoringMotor()

        self.file_reading_motor.set_line_reading_motor(self.line_reading_motor)

        self.line_reading_motor.set_file_reading_motor(self.file_reading_motor)
        self.line_reading_motor.set_mem_storing_motor(self.mem_storing_motor)

        self.mem_storing_motor.set_file_reading_motor(self.file_reading_motor)


    def run(self, file_name, memory_pointer):
        self.file_reading_motor.set_file_name(file_name)
        self.mem_storing_motor.set_memory_pointer(memory_pointer)

        self.file_reading_motor.activate()
        self.line_reading_motor.activate()
        self.mem_storing_motor.activate()

        self.file_reading_motor.add_event(FileReadingEvent("open_file"))

        all_motors_activeted = True

        while all_motors_activeted:
            self.file_reading_motor.run()
            self.line_reading_motor.run()
            self.mem_storing_motor.run()

            all_motors_activeted = self.file_reading_motor.is_active() and \
                                   self.line_reading_motor.is_active() and \
                                   self.mem_storing_motor.is_active()

        self.file_reading_motor.deactivate()
        self.line_reading_motor.deactivate()
        self.mem_storing_motor.deactivate()
