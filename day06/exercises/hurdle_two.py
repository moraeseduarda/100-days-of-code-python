# https://reeborg.ca/reeborg.html (Hurdle 2)

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while at_goal() == False:
    jump()

# while not at_goal():
#     jump()

# while at_goal != True:
#     jump()