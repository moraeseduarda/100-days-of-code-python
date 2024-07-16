# The Coffee Machine

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100,
        },
        "cost": 3.0
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

QUARTER = 0.25
DIME = 0.1
NICKEL = 0.05
PENNY = 0.01

profit = 0
should_continue = True


def report(money):
    """This function returns the report."""
    # TODO: 3. Print report.
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]

    return (f"Water: {water}ml \n"
            f"Milk: {milk}ml \n"
            f"Coffee: {coffee}g \n"
            f"Money: ${money}")


def check_resources(drink):
    """This function returns True if there are enough resources and False if there aren't."""
    # TODO: 4. Check resources sufficient?
    for ingredient in drink:
        if drink[ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
        else:
            return True


def process_coins(num_quarters, num_dimes, num_nickels, num_pennies):
    """This function returns the total of the user's payment."""
    # TODO: 5. Process coins.
    total = int(input("How many quarters? ")) * num_quarters
    total += int(input("How many quarters? ")) * num_dimes
    total += int(input("How many quarters? ")) * num_nickels
    total += int(input("How many quarters? ")) * num_pennies
    return total


def check_transaction(payment, drink_price):
    """This function returns True if there's enough payment and False if there isn't."""
    # TODO: 6. Check transaction successful?
    if payment >= drink_price:
        change = round(payment - drink_price, 2)
        print(f"Here is ${change} dollars in change.")
        global profit
        profit += drink_price
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink, ingredients):
    """This function makes coffee and uploads the new available resources."""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink} ☕. Enjoy!")


while should_continue:

    # TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    user_input = input("  What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == "report":
        print(report(profit))

    # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
    elif user_input == "off":
        should_continue = False
    else:
        drink_of_choice = MENU[user_input]
        if check_resources(drink_of_choice["ingredients"]):
            user_payment = process_coins(QUARTER, DIME, NICKEL, PENNY)
            if check_transaction(user_payment, drink_of_choice["cost"]):
                make_coffee(user_input, drink_of_choice["ingredients"])
