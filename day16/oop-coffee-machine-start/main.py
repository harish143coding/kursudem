from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
cmaker = CoffeeMaker()
money_machine = MoneyMachine()


user_ip = True
while user_ip:
    selection = input("What would you like? (espresso/latte/cappuccino/):")
    if selection == "off":
        user_ip = False
    elif selection == "report":
        print(cmaker.report())
        print(money_machine.report())
    else:
        drink = coffee_menu.find_drink(selection)
        if cmaker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            cmaker.make_coffee(drink)

