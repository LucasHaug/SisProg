import logging
import argparse

from .calculator.calculator import Calculator
from .calculator_gui import CalculatorGUI

def main():
    parser = argparse.ArgumentParser(description='Calculadora Multibase Para Inteiros')

    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose (opcional)')

    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(filename='logfile.log',
                            level=logging.DEBUG)
    else:
        logging.basicConfig(filename='logfile.log',
                            level=logging.INFO)

    calculator = Calculator()

    gui = CalculatorGUI(calculator.set_input, calculator.get_output)

    # start the GUI
    try:
        gui.start()
    except KeyboardInterrupt:
        gui.stop()

if __name__ == '__main__':
    main()
