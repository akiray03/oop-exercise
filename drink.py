class Drink:
    def __init__(self, price: int):
        self._price = price

    def price(self):
        return self._price


class Coke(Drink):
    pass


class DietCoke(Drink):
    pass


class Tea(Drink):
    pass
