from drink import Drink
from drink_stock import DrinkStock


class VendingMachine:

    def __init__(self):
        self._stock_of_coke = DrinkStock(drink_kind=Drink.COKE, quantity=5)
        self._stock_of_diet_coke = DrinkStock(drink_kind=Drink.DIET_COKE, quantity=5)
        self._stock_of_tea = DrinkStock(drink_kind=Drink.TEA, quantity=5)

        self._number_of_100_yen = 10
        self._change = 0

    # 投入金額. 100円と500円のみ受け付ける.
    # return. ジュース or None
    def buy(self, payment: int, kind_of_drink: int):

        if (payment != 100) and (payment != 500):
            self._change += payment
            return None

        if (kind_of_drink == Drink.COKE) and self._stock_of_coke.sold_out():
            self._change += payment
            return None
        elif (kind_of_drink == Drink.DIET_COKE) and self._stock_of_diet_coke.sold_out():
            self._change += payment
            return None
        elif (kind_of_drink == Drink.TEA) and self._stock_of_tea.sold_out():
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

        if kind_of_drink == Drink.COKE:
            self._stock_of_coke.decrement()
        elif kind_of_drink == Drink.DIET_COKE:
            self._stock_of_diet_coke.decrement()
        else:
            self._stock_of_tea.decrement()

        return Drink(kind_of_drink)

    def refund(self):
        result = self._change
        self._change = 0
        return result
