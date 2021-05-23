from .loader.reading_motor import ReadingMotor
from .loader.line_motor import LineMotor
from .loader.events import FileEvent

def main():
    reading_motor = ReadingMotor("aaa.txt")
    line_motor = LineMotor()

    reading_motor.set_line_motor(line_motor)

    reading_motor.add_event(FileEvent("open_file"))

    reading_motor.run()

    reading_motor.add_event(FileEvent("read"))
    reading_motor.add_event(FileEvent("read"))
    reading_motor.add_event(FileEvent("close_file"))

    while reading_motor.run():
        print("Running..")


if __name__ == '__main__':
    main()
