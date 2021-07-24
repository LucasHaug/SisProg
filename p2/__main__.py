from .calculator.calculator import Calculator
from .calculator_gui import CalculatorGUI

def main():
    calculator = Calculator()

    gui = CalculatorGUI(calculator.set_input, calculator.get_output)

    # start the GUI
    try:
        gui.start()
    except KeyboardInterrupt:
        gui.stop()

if __name__ == '__main__':
    main()
