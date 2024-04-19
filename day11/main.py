# The Blackjack Capstone Project

import random
import os
from art import logo

start_game = True

def clear():
    """This function cleans the console."""
    os.system('cls')

def deal_card(list_cards):
    """This function deals a card."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    list_cards.append(random_card)

def calculate_score(list_cards):
    """This fuction calculates the total score."""
    score = sum(list_cards)
    if 11 in list_cards and 10 in list_cards and len(list_cards) == 2:
        # Blackjack
        score = 0
        return score
    # Remember that an ace can have two values, 1 if score > 21 and 11 if score < 21
    if 11 in list_cards and score > 21:
        list_cards.remove(11)
        list_cards.append(1)
        return score
    return score
    
def compare(user_score, computer_score):
    """This function compares the user_score and computer_score."""
    if user_score == computer_score:
        return "It's a draw"
    elif user_score == 0:
        return "You win, you have a blackjack :)"
    elif computer_score == 0:
        return "Computer wins, it has a blackjack :("    
    elif user_score > 21 and computer_score < user_score:
        # Bust
        return "Computer wins :("
    elif computer_score > 21 and user_score < computer_score:
        # Bust
        return "You win :)"
    elif computer_score > user_score:
        return "Computer wins :("
    elif user_score > computer_score:
        return "You win :)"

while start_game:
    user_cards = []
    computer_cards = []
    continue_dealing_cards = True

    for card in range(2):
            deal_card(user_cards)
            deal_card(computer_cards)

    should_play = input("Do you want to play a game of Blackjack? Type 'y or 'n': ").lower()
    if should_play == 'y':

        clear()
        print(logo)

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        
        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        while continue_dealing_cards:
            
            if user_score != 0 and user_score < 21:
            
                get_another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                if get_another_card == 'y':

                    deal_card(user_cards)
                    user_score = calculate_score(user_cards)
                    print(f"    Your cards: {user_cards}, current score: {user_score}")
                    print(f"    Computer's first card: {computer_cards[0]}")  

                elif get_another_card == 'n':

                    while calculate_score(computer_cards) < 17 and calculate_score(computer_cards) != 0:
                        deal_card(computer_cards)
                    
                    continue_dealing_cards = False
                    user_score = calculate_score(user_cards)
                    computer_score = calculate_score(computer_cards)

                    print(f"    Your final hand: {user_cards}, final score: {user_score}")
                    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
                    result = compare(user_score, computer_score)
                    print(result)

                else:
                    print("You type an invalid answer.")
            else:
                while calculate_score(computer_cards) < 17 and calculate_score(computer_cards)!= 0:
                    deal_card(computer_cards)

                continue_dealing_cards = False
                user_score = calculate_score(user_cards)
                computer_score = calculate_score(computer_cards)

                print(f"    Your final hand: {user_cards}, final score: {user_score}")
                print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
                result = compare(user_score, computer_score)
                print(result)

    elif should_play == 'n':
        start_game = False
        clear()
        print("Thank you for playing my game :)")

    else:
        print("You typed an invalid answer.")