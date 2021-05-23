from .loader.reading_motor import ReadingMotor
from .loader.line_motor import LineMotor
from .loader.events import FileEvent

def main():
    reading_motor = ReadingMotor()
    line_motor = LineMotor()

    reading_motor.set_file_name("aaa.txt")

    reading_motor.set_line_motor(line_motor)
    line_motor.set_reading_motor(reading_motor)

    reading_motor.add_event(FileEvent("open_file"))

    while reading_motor.is_active():
        reading_motor.run()
        line_motor.run()


if __name__ == '__main__':
    main()
