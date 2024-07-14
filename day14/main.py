# Higher Lower Game

import random
import os
from art import logo
from art import vs
from game_data import data

def random_data():
    """This function returns a random data."""
    return random.choice(data)

def compare(user_choice, other_choice):
    """This function compares the user's choice follower count with the other option follower count."""
    if user_choice['follower_count'] > other_choice['follower_count']:
        return True
    else:
        return False
    
def clear():
    """This function cleans the console."""
    os.system('cls')

def game():
    
    score = 0
    continue_game = True
    print(logo)

    choice_a = random_data()
    choice_b = random_data()

    while continue_game:
        choice_a = choice_b
        choice_b = random_data()

        while choice_a == choice_b:
            choice_b = random_data()

        print(f"Compare A: {choice_a['name']}, {choice_a['description']} from {choice_a['country']}.")
        print(vs)
        print(f"Compare B: {choice_b['name']}, {choice_b['description']} from {choice_b['country']}.")
        
        guess = input("Who has more followers? Type 'A' or 'B'? ").lower()

        if guess == 'a':
            user_choice = choice_a
            other_choice = choice_b
        else:
            user_choice = choice_b
            other_choice = choice_a

        comparing = compare(user_choice, other_choice) 
        clear()
        print(logo)

        if comparing == True:
            score += 1
            print(f"You're right! Your current score is: {score}.")
        else:
            continue_game = False
            print(f"Sorry, that's wrong. Final score: {score}.")
game()