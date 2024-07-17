# The Coffee Machine in OOP

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# object // class
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

should_continue = True

while should_continue:
    # object // class // method
    options = menu.get_items()
    choice = input("What would you like? (espresso/latte/cappuccino/): ").lower()
    if choice == "off":
        should_continue = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        drink = menu.find_drink(choice)
        # class // method // attribute - money_machine.make_payment(drink.cost)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
    else:
        print("Sorry, I didn't understand. Please, try again.")
