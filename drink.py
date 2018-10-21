class Drink:
    def __init__(self, kind: str, price: int):
        self._kind = kind
        self._price = price

    def kind(self):
        return self._kind

    def price(self):
        return self._price


DRINK_LIST = [
    Drink(kind='Coke', price=100),
    Drink(kind='DietCoke', price=100),
    Drink(kind='Tea', price=100),
]


class DrinkTypes:
    @classmethod
    def lookup(cls, kind: str):
        for drink in DRINK_LIST:
            if drink.kind() == kind:
                return drink
        return None
