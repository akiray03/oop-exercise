from vending_machine import VendingMachine
from drink import DrinkTypes
from currency import Currency


if __name__ == '__main__':
    print('# 200円を入れて 0: COKE を購入')

    money = Currency(amount=200)
    drink_type = DrinkTypes.lookup('Coke')
    vending_machine = VendingMachine()
    my_drink = vending_machine.buy(money, drink_type)
    change = vending_machine.refund()

    print('Drink: {}'.format(my_drink))
    print('Change: {}'.format(change))
    print('->100円か500円しか受け付けないのでそのまま返ってくる')
    print('')

    print('# 500円を入れて 1: DIET_COKE を購入')

    money = Currency(amount=500)
    drink_type = DrinkTypes.lookup('DietCoke')
    vending_machine = VendingMachine()
    my_drink = vending_machine.buy(money, drink_type)
    change = vending_machine.refund()

    print('Drink: {}'.format(my_drink))
    print('Change: {}'.format(change))
    print('->DIET_COKEが出て400円返ってくる')
