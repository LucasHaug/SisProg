from .file_writing_motor import FileWritingMotor
from .line_writing_motor import LineWritingMotor
from .mem_reading_motor import MemReadingMotor
from .events import MemReadingEvent

class Dumper():
    def __init__(self) -> None:
        self.file_writing_motor = FileWritingMotor()
        self.line_writing_motor = LineWritingMotor()
        self.mem_reading_motor = MemReadingMotor()

        self.file_writing_motor.set_mem_reading_motor(self.mem_reading_motor)

        self.line_writing_motor.set_file_writing_motor(self.file_writing_motor)
        self.line_writing_motor.set_mem_reading_motor(self.mem_reading_motor)

        self.mem_reading_motor.set_line_writing_motor(self.line_writing_motor)


    def run(self, file_name, memory_pointer, start_poistion, end_position):
        self.file_writing_motor.set_file_name(file_name)
        self.mem_reading_motor.set_memory_pointer(memory_pointer)
        self.mem_reading_motor.set_dumping_area(start_poistion, end_position)

        self.file_writing_motor.activate()
        self.line_writing_motor.activate()
        self.mem_reading_motor.activate()

        self.mem_reading_motor.add_event(MemReadingEvent("start"))

        all_motors_activeted = True

        while all_motors_activeted:
            self.file_writing_motor.run()
            self.line_writing_motor.run()
            self.mem_reading_motor.run()

            all_motors_activeted = self.file_writing_motor.is_active() and \
                                   self.line_writing_motor.is_active() and \
                                   self.mem_reading_motor.is_active()

        self.file_writing_motor.deactivate()
        self.line_writing_motor.deactivate()
        self.mem_reading_motor.deactivate()
