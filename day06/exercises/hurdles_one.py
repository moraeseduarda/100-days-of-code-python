# https://reeborg.ca/reeborg.html (Hurdle 1)

# Creating functions
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
    
# Using for loop
for step in range(6):
    jump()

num_of_hurdles = 6

# Using while loop
while num_of_hurdles > 0:
    jump()
    num_of_hurdles -= 1
    print(num_of_hurdles)