# Calculator

import os
from art import logo

# Clear console
def clear():
    os.system('cls')

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)
    initial_number = float(input("What's the first number?: "))
    should_continue = False
    for symbol in operations:
        print(symbol)
    
    while not should_continue:
        operation_symbol = input("Pick a operation: ")
        next_number = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        final_answer = calculation_function(initial_number, next_number)
        
        print(f"{initial_number} {operation_symbol} {next_number} = {final_answer}")

        # The variable should_continue is a flag.
        to_be_continue = input(f"Type 'y' to continue calculating with {final_answer}, type 'n' to start a new calculation: ").lower()
        if to_be_continue == "n":
            should_continue = True
            clear()
            # Recursion concept: a defined function calling itself.
            calculator()
        elif to_be_continue == "y":
            initial_number = final_answer
        else:
            print("You typed an invalid answer.")

calculator()