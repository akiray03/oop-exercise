from drink import Drink


class VendingMachine:

    def __init__(self):
        self._quantity_of_coke = 5
        self._quantity_of_diet_coke = 5
        self._quantity_of_tea = 5
        self._number_of_100_yen = 10
        self._change = 0

    # 投入金額. 100円と500円のみ受け付ける.
    # return. ジュース or None
    def buy(self, i: int, kind_of_drink: int):

        if (i != 100) and (i != 500):
            self._change += i
            return None

        if (kind_of_drink == Drink.COKE) and (self._quantity_of_coke == 0):
            self._change += i
            return None
        elif (kind_of_drink == Drink.DIET_COKE) and \
                (self._quantity_of_diet_coke == 0):
            self._change += i
            return None
        elif (kind_of_drink == Drink.TEA) and (self._quantity_of_tea == 0):
            self._change += i
            return None

        if i == 500 and self._number_of_100_yen < 4:
            self._change += i
            return None

        if i == 100:
            self._number_of_100_yen += 1
        elif i == 500:
            self._change += (i - 100)
            self._number_of_100_yen -= (i - 100) / 100

        if kind_of_drink == Drink.COKE:
            self._quantity_of_coke -= 1
        elif kind_of_drink == Drink.DIET_COKE:
            self._quantity_of_diet_coke -= 1
        else:
            self._quantity_of_tea -= 1

        return Drink(kind_of_drink)

    def refund(self):
        result = self._change
        self._change = 0
        return result
