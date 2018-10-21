from currency import Currency


class PaymentMachine:
    AVAILABLE_COINS = [100, 500]

    def __init__(self, number_of_100_yen: int):
        self._number_of_100_yen = number_of_100_yen
        self._change = 0

    def is_available_coin(self, payment: Currency) -> bool:
        return payment.amount() in self.AVAILABLE_COINS

    def pay_with_refundable(self, payment: Currency) -> bool:
        if payment.amount() == 100:
            return True

        if payment.amount() == 500 and self._number_of_100_yen >= 4:
            return True

        return False

    def pay_without_item(self, payment: Currency):
        self._change += payment.amount()

    def pay_jpy100_item(self, payment: Currency):
        if payment.amount() == 100:
            self._number_of_100_yen += 1

        if payment.amount() == 500:
            self._change += (payment.amount() - 100)
            self._number_of_100_yen -= (payment.amount() - 100) / 100

    def refund(self) -> Currency:
        currency = Currency(self._change)
        self._change = 0
        return currency
