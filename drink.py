class Drink:
    COKE = 0
    DIET_COKE = 1
    TEA = 2

    def __init__(self, kind: int):
        self._kind = kind

    def get_kind(self) -> int:
        return self._kind
