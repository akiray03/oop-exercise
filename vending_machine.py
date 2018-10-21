from drink import Drink
from drink import Coke
from drink import DietCoke
from drink import Tea
from drink_stock import DrinkStockCollection
from typing import Type


class VendingMachine:

    def __init__(self):
        self._drink_stocks = DrinkStockCollection()
        self._drink_stocks.append(drink_kind=Coke, initial_quantity=5)
        self._drink_stocks.append(drink_kind=DietCoke, initial_quantity=5)
        self._drink_stocks.append(drink_kind=Tea, initial_quantity=5)

        self._number_of_100_yen = 10
        self._change = 0

    # 投入金額. 100円と500円のみ受け付ける.
    # return. ジュース or None
    def buy(self, payment: int, kind_of_drink: Type[Drink]):

        if (payment != 100) and (payment != 500):
            self._change += payment
            return None

        # 対象商品の在庫が切れている場合は、お釣りに入れる
        stock = self._drink_stocks.lookup(drink_kind=kind_of_drink)
        if stock.sold_out():
            self._change += payment
            return None

        if payment == 500 and self._number_of_100_yen < 4:
            self._change += payment
            return None

        if payment == 100:
            self._number_of_100_yen += 1
        elif payment == 500:
            self._change += (payment - 100)
            self._number_of_100_yen -= (payment - 100) / 100

        # 対象商品の在庫を減らす
        stock.decrement()

        return kind_of_drink

    def refund(self):
        result = self._change
        self._change = 0
        return result
