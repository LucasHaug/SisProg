from ..event import Event


class DataReadingEvent(Event):
    """
    Event type handled by the InterfaceMotor

    Attributes
    ----------
    data : str
        Data read from the interface
    """

    def __init__(self, event_data) -> None:
        super().__init__()

        self.data = event_data


class ExpressionEvent(Event):
    """
    Event type handled by the ConversionMotor

    Attributes
    ----------
    expression : str
        Expression to be converted
    base : str
        Base of the numbers in the expression
    start_type : str
        Type of the start of the expression, may be
        "number", "operator", "empty" or None if not known
    """

    def __init__(self, expression, base, start_type=None) -> None:
        super().__init__()

        self.expression = expression
        self.base = base
        self.start_type = start_type


class OperationElementEvent(Event):
    """
    Event type handled by the EvaluationMotor

    Attributes
    ----------
    element : str or int
        Operation element to be evaluated
    element_type : str
        Type of the operation element, may be
        "number", "operator" or "finish"
    """

    def __init__(self, element, element_type) -> None:
        super().__init__()

        self.element = element
        self.element_type = element_type
