# The Number Guessing Game

import random
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def random_number():
    """Returns a random number between 1 and 100"""
    # Inclusive endpoint
    # number = random.randint(1, 100)
    # Exclusive endpoint
    number = random.randrange(1, 101)
    return number

def game_mode():
    """Returns the game mode/attempts"""
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        return EASY_LEVEL_TURNS
    elif difficulty == 'hard':
        return HARD_LEVEL_TURNS

def compare(right_answer, guess):
    "Returns if the guess is right"
    if right_answer == guess:
        return True
    else:
        return False
    
def guess_check(right_answer, guess):
    """Returns if the guess was high or low compared to the right answer"""
    if right_answer > guess:
        return "Too low."
    else:
        return "Too high."

def game():
    secret_number = random_number()
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking a number between 1 and 100.")
    # print(f"Pssst, the correct answer is {secret_number}.")

    attempts = game_mode()
    print(f"You have {attempts} attempts remaining to guess the number.")

    while attempts != 0:
        user_guess = int(input("Make a guess: "))
        result = compare(secret_number, user_guess)
        how_far = guess_check(secret_number, user_guess)

        if result == True:
            attempts = 0
            print(f"You win! The answer was {secret_number}.")
        else:
            attempts -= 1 
            if attempts == 0:
                print(f"You've run out of guesses, you lose. The answer was {secret_number}.")
            else:
                print(how_far)
                print(f"Guess again.")
                print(f"You have {attempts} attempts left.")

game()