# https://reeborg.ca/reeborg.html (Maze)

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal(): 
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

# I'll come back in day 15 to fix a intermediate level bug the code has.