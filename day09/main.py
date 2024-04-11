# Secret Auction

import os
from art import logo
print(logo)

end_auction = False
auction_dict = {}

def secret_auction():
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    auction_dict[name] = bid

def highest_bid(auction_dict):
    highest_value = 0
    for name in auction_dict:
        bid_amount = auction_dict[name]
        if bid_amount > highest_value:
            highest_value = bid_amount
            winner = name
    print(f"The winner is {winner}, with a bid of ${highest_value}")

def clear():
    os.system('cls')

while end_auction == False:
    secret_auction()
    repeat = input("Are these any other bidders? Type 'yes' or 'no'. \n ").lower().strip()
    if repeat == "no":
        end_auction = True
        highest_bid(auction_dict)
    else:
        clear()

    