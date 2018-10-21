from currency import Currency
from drink import Drink
from drink import DrinkTypes
from drink_stock import DrinkStockCollection
from payment_machine import PaymentMachine


class VendingMachine:

    def __init__(self):
        self._drink_stocks = self._init_drink_stocks()
        self._payment_machine = PaymentMachine(number_of_100_yen=10)

    @staticmethod
    def _init_drink_stocks() -> DrinkStockCollection:
        stocks = DrinkStockCollection()
        stocks.append(drink_kind=DrinkTypes.lookup('Coke'), initial_quantity=5)
        stocks.append(drink_kind=DrinkTypes.lookup('DietCoke'), initial_quantity=5)
        stocks.append(drink_kind=DrinkTypes.lookup('Tea'), initial_quantity=5)

        return stocks

    # 投入金額. 100円と500円のみ受け付ける.
    # return. ジュース or None
    def buy(self, payment: Currency, kind_of_drink: Drink) -> (Drink or None):
        if not self._payment_machine.is_available_coin(payment=payment):
            return None

        # 対象商品の在庫が切れている場合は、お釣りに入れる
        stock = self._drink_stocks.lookup(drink_kind=kind_of_drink)

        if stock.sold_out():
            self._payment_machine.pay_without_item(payment=payment)
            return None

        if not self._payment_machine.pay_with_refundable(payment=payment):
            self._payment_machine.pay_without_item(payment=payment)
            return None

        self._payment_machine.pay_jpy100_item(payment=payment)

        # 対象商品の在庫を減らす
        stock.decrement()

        return kind_of_drink

    def refund(self) -> Currency:
        return self._payment_machine.refund()
