from vending_machine import VendingMachine


if __name__ == '__main__':
    print('# 200円を入れて 0: COKE を購入')

    money = 200
    drink_type = 0
    vending_machine = VendingMachine()
    my_drink = vending_machine.buy(money, drink_type)
    change = vending_machine.refund()

    print('Drink: {}'.format(my_drink))
    print('Change: {}'.format(change))
    print('->100円か500円しか受け付けないのでそのまま返ってくる')

    print('# 500円を入れて 1: DIET_COKE を購入')

    money = 500
    drink_type = 1
    vending_machine = VendingMachine()
    my_drink = vending_machine.buy(money, drink_type)
    change = vending_machine.refund()

    print('Drink: {}'.format(my_drink.get_kind()))
    print('Change: {}'.format(change))
    print('->DIET_COKEが出て400円返ってくる')
