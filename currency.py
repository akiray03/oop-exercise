class Currency:
    def __init__(self, amount: int):
        self._amount = amount

    def amount(self) -> int:
        return self._amount

    def __repr__(self):
        return '<{cls} amount={amount}>'.format(
            cls=self.__class__.__name__,
            amount=self.amount()
        )
