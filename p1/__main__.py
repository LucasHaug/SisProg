import numpy as np

from .loader.reading_motor import ReadingMotor
from .loader.line_motor import LineMotor
from .loader.storing_motor import StoringMotor
from .loader.events import FileEvent

def main():
    reading_motor = ReadingMotor()
    line_motor = LineMotor()
    storing_motor = StoringMotor()

    memory = np.zeros(4096, dtype=np.uint8)

    reading_motor.set_file_name("mem.txt")

    reading_motor.set_line_motor(line_motor)

    line_motor.set_reading_motor(reading_motor)
    line_motor.set_storing_motor(storing_motor)

    storing_motor.set_reading_motor(reading_motor)
    storing_motor.set_memory_pointer(memory)

    reading_motor.add_event(FileEvent("open_file"))

    try:
        while reading_motor.is_active():
            reading_motor.run()
            line_motor.run()
            storing_motor.run()

        np.savetxt("image.txt", memory, fmt='%x')
    except KeyboardInterrupt:
        print("[INFO] Ending Program")


if __name__ == '__main__':
    main()
