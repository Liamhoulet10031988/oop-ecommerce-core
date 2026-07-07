class PrintMixin:
    """Миксин для печати информации о созданном объекте."""

    def __init__(self) -> None:
        print(repr(self))
