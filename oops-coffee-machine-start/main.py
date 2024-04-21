from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeeMaker = CoffeeMaker()
coffeeMenu = Menu()
moneyMachine = MoneyMachine()

is_game=True
while is_game:
    ip = input(f"What would you like? {coffeeMenu.get_items()}")
    if ip == "espresso" or ip == "latte" or ip == "cappuccino":
        if coffeeMaker.is_resource_sufficient(coffeeMenu.find_drink(ip)):
            coffeeCost=coffeeMenu.find_drink(ip).cost
            if moneyMachine.make_payment(coffeeCost) == 1:
                coffeeMaker.make_coffee(coffeeMenu.find_drink(ip))
    elif ip == "report":
        coffeeMaker.report()
    elif ip == 'off':
        is_game = False
    elif ip == "profit":
        moneyMachine.report()
    else: print("invalid input")
