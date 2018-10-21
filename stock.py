class Stock:
    def __init__(self, quantity: int):
        self._quantity = quantity

    def increment(self):
        self._quantity += 1

    def decrement(self):
        if self._quantity > 1:
            self._quantity -= 1
        else:
            raise RuntimeError('在庫量が足りません')

    def available(self, request_quantity: int=1) -> bool:
        return self._quantity > request_quantity
