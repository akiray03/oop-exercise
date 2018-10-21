from stock import Stock


class DrinkStock:
    def __init__(self, drink_kind: int, quantity: int):
        self._drink_kind = drink_kind
        self._stock = Stock(quantity=quantity)

    def in_sale(self):
        return self._stock.available()

    def sold_out(self):
        return not self.in_sale()

    def decrement(self):
        self._stock.decrement()
