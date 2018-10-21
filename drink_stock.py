from stock import Stock
from drink import Drink
from typing import Type


class DrinkStock:
    def __init__(self, drink_kind: Type[Drink], quantity: int):
        self._drink_kind = drink_kind
        self._stock = Stock(quantity=quantity)

    def in_sale(self):
        return self._stock.available()

    def sold_out(self):
        return not self.in_sale()

    def decrement(self):
        self._stock.decrement()


class DrinkStockCollection:
    def __init__(self):
        self._dict = dict()

    def append(self, drink_kind :Type[Drink], initial_quantity: int):
        self._dict[drink_kind] = DrinkStock(
            drink_kind=drink_kind,
            quantity=initial_quantity,
        )

    def lookup(self, drink_kind: Type[Drink]):
        if drink_kind in self._dict:
            return self._dict[drink_kind]

        raise RuntimeError('未知の飲み物が選択されました')
