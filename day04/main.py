# Rock Paper Scissor 

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]

computer_number = random.randint(0,2)

computer_option = options[computer_number]

user_number = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))

if (user_number >= 3) or (user_number < 0):
    print("You typed an invalid number, you lose!")
else:
    user_option = options[user_number]
    print(user_option)
    print(f"Computer chose:\n {computer_option}")
    if computer_number == user_number:
        print("It's a draw")
    elif computer_number == 0 and user_number == 2:
        print("You lose")
    elif computer_number == 2 and user_number == 0:
        print("You win")
    elif user_number > computer_number:
        print("You Win.")
    elif user_number < computer_number:
        print("You Lose.")