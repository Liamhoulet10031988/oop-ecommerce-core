class PrintMixin:
    """Миксин для печати информации о созданном объекте."""

    def __init__(self) -> None:
        super().__init__()
        print(repr(self))
