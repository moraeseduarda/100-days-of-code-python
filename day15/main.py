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
    # TODO: 3. Print report.
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]

    return (f"Water: {water}ml \n"
            f"Milk: {milk}ml \n"
            f"Coffee: {coffee}g \n"
            f"Money: ${money}")


def check_resources():
    # TODO: 4. Check resources sufficient?
    if user_input == "espresso":
        water = MENU['espresso']['ingredients']['water']
        coffee = MENU['espresso']['ingredients']['coffee']
        milk = MENU['espresso']['ingredients']['milk']
    elif user_input == "latte":
        water = MENU['latte']['ingredients']['water']
        coffee = MENU['latte']['ingredients']['coffee']
        milk = MENU['latte']['ingredients']['milk']
    else:
        water = MENU['cappuccino']['ingredients']['water']
        coffee = MENU['cappuccino']['ingredients']['coffee']
        milk = MENU['cappuccino']['ingredients']['milk']

    if resources['water'] < water:
        print("Sorry there is not enough water.")
        return False
    elif resources['coffee'] < coffee:
        print("Sorry there is not enough coffee.")
        return False
    elif resources['milk'] < milk:
        print("Sorry there is not enough milk.")
        return False
    else:
        return True


def process_coins(num_quarters, num_dimes, num_nickels, num_pennies):
    # TODO: 5. Process coins.
    total_user_money = (num_quarters * QUARTER) + (num_dimes * DIME) + (num_nickels * NICKEL) + (num_pennies * PENNY)
    return total_user_money


def check_transaction(user_total_money):
    # TODO: 6. Check transaction successful?
    espresso_price = MENU["espresso"]["cost"]
    latte_price = MENU["latte"]["cost"]
    cappuccino_price = MENU["cappuccino"]["cost"]

    if user_input == "espresso" and user_total_money > espresso_price:
        change = user_total_money - espresso_price
        print(f"Here is ${change} in change.")
        return espresso_price
    elif user_input == "latte" and user_total_money > latte_price:
        change = user_total_money - latte_price
        print(f"Here is ${change} in change.")
        return latte_price
    elif user_input == "cappuccino" and user_total_money > cappuccino_price:
        change = user_total_money - cappuccino_price
        print(f"Here is ${change} in change.")
        return cappuccino_price
    else:
        print("Sorry that's not enough money. Money refunded.")
        return 0


def make_coffee(user_coffee):
    # TODO: 7. Make coffee.
    # Incomplete.
    print(f"Here is you {user_coffee} ☕. Enjoy!")
    return True


while should_continue:

    # TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    user_input = input("  What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == "report":
        print(report(profit))

    # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
    elif user_input == "off":
        should_continue = False
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        enough_ingredients = check_resources()
        if enough_ingredients:
            quarters = int(input("How many quarters? "))
            dimes = int(input("How many dimes? "))
            nickels = int(input("How many nickels? "))
            pennies = int(input("How many pennies? "))
            user_money = process_coins(quarters, dimes, nickels, pennies)
            profit += check_transaction(user_money)
            make_coffee(user_input)
    else:
        print("Sorry, I didn't understand.")

# TODO: 6. Refactorer code and rename variables
# Incomplete.
