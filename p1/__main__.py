import numpy as np

from .loader.file_reading_motor import FileReadingMotor
from .loader.line_reading_motor import LineReadingMotor
from .loader.mem_storing_motor import MemStoringMotor
from .loader.events import FileReadingEvent

def main():
    file_reading_motor = FileReadingMotor()
    line_reading_motor = LineReadingMotor()
    mem_storing_motor = MemStoringMotor()

    memory = np.zeros(4096, dtype=np.uint8)

    file_reading_motor.set_file_name("mem.txt")

    file_reading_motor.set_line_reading_motor(line_reading_motor)

    line_reading_motor.set_file_reading_motor(file_reading_motor)
    line_reading_motor.set_mem_storing_motor(mem_storing_motor)

    mem_storing_motor.set_file_reading_motor(file_reading_motor)
    mem_storing_motor.set_memory_pointer(memory)

    file_reading_motor.add_event(FileReadingEvent("open_file"))

    try:
        while file_reading_motor.is_active():
            file_reading_motor.run()
            line_reading_motor.run()
            mem_storing_motor.run()

        np.savetxt("image.txt", memory, fmt='%x')
    except KeyboardInterrupt:
        print("[INFO] Ending Program")


if __name__ == '__main__':
    main()
