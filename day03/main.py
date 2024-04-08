# Treasure Island
print('''
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa   a
8   8               8               8           8                   8   8
8   8   aaaaaaaaa   8   aaaaa   aaaa8aaaa   aaaa8   aaaaa   aaaaa   8   8
8               8       8   8           8           8   8   8       8   8
8aaaaaaaa   a   8aaaaaaa8   8aaaaaaaa   8aaaa   a   8   8   8aaaaaaa8   8
8       8   8               8           8   8   8   8   8           8   8
8   a   8aaa8aaaaaaaa   a   8   aaaaaaaa8   8aaa8   8   8aaaaaaaa   8   8
8   8               8   8   8       8           8           8       8   8
8   8aaaaaaaaaaaa   8aaa8   8aaaa   8   aaaaa   8aaaaaaaa   8   aaaa8   8
8           8       8   8       8   8       8           8   8           8
8   aaaaa   8aaaa   8   8aaaa   8   8aaaaaaa8   a   a   8   8aaaaaaaaaaa8
8       8       8   8   8       8       8       8   8   8       8       8
8aaaaaaa8aaaa   8   8   8   aaaa8aaaa   8   aaaa8   8   8aaaa   8aaaa   8
8           8   8           8       8   8       8   8       8           8
8   aaaaa   8   8aaaaaaaa   8aaaa   8   8aaaa   8aaa8   aaaa8aaaaaaaa   8
8   8       8           8           8       8   8   8               8   8
8   8   aaaa8aaaa   a   8aaaa   aaaa8aaaa   8   8   8aaaaaaaaaaaa   8   8
8   8           8   8   8   8   8           8               8   8       8
8   8aaaaaaaa   8   8   8   8aaa8   8aaaaaaa8   aaaaaaaaa   8   8aaaaaaa8
8   8       8   8   8           8           8   8       8               8
8   8   aaaa8   8aaa8   aaaaa   8aaaaaaaa   8aaa8   a   8aaaaaaaa   a   8
8   8                   8           8               8               8   8
8   8aaaaaaaaaaaaaaaaaaa8aaaaaaaaaaa8aaaaaaaaaaaaaaa8aaaaaaaaaaaaaaa8aaa8
''')
print("Welcome to The Maze.")
print("Your mission is to find the exit. (You have no weapons, be aware.)") 

direction = input("You're lost. Where do you want to turn?\n Type \"left\" or \"right\"\n").lower()

if direction == "left":
    pirate = input("You've found a pirate.\n Type \"run\" to run from the pirate. Type \"duel\" to duel with the pirate.\n").lower()
  
    if pirate == "run":
        door = input("You found a house with 3 doors.\n One red, one yellow and one blue. Which colour do you choose?\n").lower()
    
        if door == "yellow":
            print("You found the exit. You won!")
        
        elif door == "red":
            print("It's a room full of fire. Game over.")
        
        elif door == "blue":
            print("You enter a room full of beasts. Game over.")
        
        else:
            print("You didn't choose. You're dead.")
    elif pirate == "duel":
        print("You died. Game over.")
    else:
        print("You didn't choose. You're dead.")
elif direction == "right":
    print("You fell into a hole. Game over.")
else:
    print("You didn't choose. You're dead.")
