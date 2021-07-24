class Calculator:
    def __init__(self) -> None:
        pass


    def set_input(self, input_str: str) -> None:
        self.input_str = input_str


    def get_output(self) -> str:
        self.output_str = self.input_str

        return self.output_str
