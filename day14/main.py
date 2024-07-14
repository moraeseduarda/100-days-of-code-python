# Higher Lower Game

import random
import os
from art import logo
from art import vs
from game_data import data

def random_data(data):
    data_item = random.randint(0, 49)
    item = data[data_item]
    return item

def compare(user_choice, other_choice):
    if user_choice['follower_count'] > other_choice['follower_count']:
        return True
    else:
        return False
    
def clear():
    """This function cleans the console."""
    os.system('cls')

score = 0
print(logo)

a = random_data(data)
b = random_data(data)

print(f"Compare A: {a['name']}, {a['description']} from {a['country']}.")

print(vs)

print(f"Compare B: {b['name']}, {b['description']} from {b['country']}.")

guess = input("Who has more followers? Type 'A' or 'B'? ").lower()

if guess == 'a':
    user_choice = a
    other_choice = b
else:
    user_choice = b
    other_choice = a

comparing = compare(user_choice, other_choice)  
clear()

if comparing == True:
    score += 1
    print(f"Score: {score}")
else:
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")