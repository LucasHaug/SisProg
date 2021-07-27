import tkinter as tk
from tkinter import messagebox

from .common import BASE_CHOICES


NUM_OF_ROWS = 9
NUM_OF_COLUMNS = 4


class CalculatorGUI:
    def __init__(self, set_input, get_output) -> None:
        self.set_input = set_input
        self.get_output = get_output

        # Create the main window
        self.tk_gui = tk.Tk()

        bg_color = "#434344"
        fg_color = "#FFFFFF"

        self.tk_gui.configure(background=bg_color)

        self.tk_gui.title("Calculadora multibase para inteiros")

        self.tk_gui.geometry("540x300")

        for i in range(NUM_OF_ROWS):
            self.tk_gui.rowconfigure(i, weight=1)

        for i in range(NUM_OF_COLUMNS):
            self.tk_gui.columnconfigure(i, weight=1)

        self.tk_gui.bind("<Configure>", self._resize)

        # Create base selector
        self.base_var = tk.StringVar()
        self.base_var.set(BASE_CHOICES[2])

        base_menu = tk.OptionMenu(
            self.tk_gui,
            self.base_var,
            *BASE_CHOICES,
            command=self._base_callback,
        )

        base_menu.grid(row=0, column=0, columnspan=NUM_OF_COLUMNS, sticky="NSEW")

        base_menu.config(
            bg=bg_color,
            fg=fg_color,
            highlightbackground=bg_color,
            highlightcolor=fg_color,
            relief=tk.FLAT,
            direction="below",
            height=1,
            width=7
        )

        # Create expression entry
        self.expression = tk.StringVar()

        expression_field = tk.Entry(
            self.tk_gui,
            textvariable=self.expression,
            fg=fg_color,
            bg=bg_color,
            highlightbackground=bg_color,
            highlightcolor=fg_color,
            relief=tk.FLAT
        )

        expression_field.grid(row=1, column=0, columnspan=NUM_OF_COLUMNS, sticky="NSEW")

        expression_field.columnconfigure(0, weight=1)
        expression_field.rowconfigure(0, weight=1)

        numpad_first_row = 2
        numpad_first_col = 0

        # Create buttons
        calc_buttons_config = {
            "+"  : {"text":  "+", "row": numpad_first_row + 1, "column": numpad_first_col + 3, "fg": fg_color, "bg": "#f1a33c"},
            "-"  : {"text":  "-", "row": numpad_first_row + 2, "column": numpad_first_col + 3, "fg": fg_color, "bg": "#f1a33c"},
            "*"  : {"text":  "*", "row": numpad_first_row + 3, "column": numpad_first_col + 3, "fg": fg_color, "bg": "#f1a33c"},
            "/"  : {"text":  "/", "row": numpad_first_row + 4, "column": numpad_first_col + 3, "fg": fg_color, "bg": "#f1a33c"},
            "="  : {"text":  "=", "row": numpad_first_row + 5, "column": numpad_first_col + 3, "fg": fg_color, "bg": "#f1a33c"},
            "Cl" : {"text": "Cl", "row": numpad_first_row + 0, "column": numpad_first_col + 0, "fg": fg_color, "bg": "#555556"},
            "⌫"  : {"text":  "⌫", "row": numpad_first_row + 0, "column": numpad_first_col + 1, "fg": fg_color, "bg": "#555556"},
            "("  : {"text":  "(", "row": numpad_first_row + 0, "column": numpad_first_col + 2, "fg": fg_color, "bg": "#555556"},
            ")"  : {"text":  ")", "row": numpad_first_row + 0, "column": numpad_first_col + 3, "fg": fg_color, "bg": "#555556"},
            "F"  : {"text":  "F", "row": numpad_first_row + 1, "column": numpad_first_col + 2, "fg": fg_color, "bg": "#717172"},
            "E"  : {"text":  "E", "row": numpad_first_row + 1, "column": numpad_first_col + 1, "fg": fg_color, "bg": "#717172"},
            "D"  : {"text":  "D", "row": numpad_first_row + 1, "column": numpad_first_col + 0, "fg": fg_color, "bg": "#717172"},
            "C"  : {"text":  "C", "row": numpad_first_row + 2, "column": numpad_first_col + 2, "fg": fg_color, "bg": "#717172"},
            "B"  : {"text":  "B", "row": numpad_first_row + 2, "column": numpad_first_col + 1, "fg": fg_color, "bg": "#717172"},
            "A"  : {"text":  "A", "row": numpad_first_row + 2, "column": numpad_first_col + 0, "fg": fg_color, "bg": "#717172"},
            "9"  : {"text":  "9", "row": numpad_first_row + 3, "column": numpad_first_col + 2, "fg": fg_color, "bg": "#717172"},
            "8"  : {"text":  "8", "row": numpad_first_row + 3, "column": numpad_first_col + 1, "fg": fg_color, "bg": "#717172"},
            "7"  : {"text":  "7", "row": numpad_first_row + 3, "column": numpad_first_col + 0, "fg": fg_color, "bg": "#717172"},
            "6"  : {"text":  "6", "row": numpad_first_row + 4, "column": numpad_first_col + 2, "fg": fg_color, "bg": "#717172"},
            "5"  : {"text":  "5", "row": numpad_first_row + 4, "column": numpad_first_col + 1, "fg": fg_color, "bg": "#717172"},
            "4"  : {"text":  "4", "row": numpad_first_row + 4, "column": numpad_first_col + 0, "fg": fg_color, "bg": "#717172"},
            "3"  : {"text":  "3", "row": numpad_first_row + 5, "column": numpad_first_col + 2, "fg": fg_color, "bg": "#717172"},
            "2"  : {"text":  "2", "row": numpad_first_row + 5, "column": numpad_first_col + 1, "fg": fg_color, "bg": "#717172"},
            "1"  : {"text":  "1", "row": numpad_first_row + 5, "column": numpad_first_col + 0, "fg": fg_color, "bg": "#717172"},
            "0"  : {"text":  "0", "row": numpad_first_row + 6, "column": numpad_first_col + 1, "fg": fg_color, "bg": "#717172"},
        }

        button_height = 1
        button_width = 7

        for button_name, button_config in calc_buttons_config.items():
            button = tk.Button(
                self.tk_gui,
                text=button_config["text"],
                fg=button_config["fg"],
                bg=button_config["bg"],
                highlightbackground=bg_color,
                highlightcolor=bg_color,
                height=button_height,
                width=button_width,
                relief=tk.FLAT,
                command=lambda read_char=button_name: self._button_callback(read_char)
            )

            button.grid(row=button_config["row"], column=button_config["column"], sticky="NSEW")

            # Add exception callback
            self.tk_gui.report_callback_exception = self.show_error

    def start(self) -> None:
        self.tk_gui.mainloop()

    def stop(self) -> None:
        self.tk_gui.destroy()

    def _button_callback(self, button: str) -> None:
        self.set_input(button)

        self.expression.set(self.get_output())

    def _base_callback(self, *args) -> None:
        self.set_input(self.base_var.get())

        self.expression.set(self.get_output())

    def _resize(self, event) -> None:
        for widget in self.tk_gui.winfo_children():
            widget.config(font=("TkDefaultFont", event.width // 40, "bold"))

    def show_error(self, exc_type, exc_value, exc_traceback) -> None:
        messagebox.showerror('Error', exc_value)
