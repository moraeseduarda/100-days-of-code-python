# Turtle Racing Game
import random
import turtle
import turtle as t
import random as r

screen = turtle.Screen()
list_of_turtles = []
colors = ["purple", "blue", "green", "yellow", "orange", "red"]

for i in range(0, 6):
    color = colors[i]
    new_turtle = t.Turtle()
    new_turtle.color(color)
    new_turtle.shape("turtle")
    list_of_turtles.append(new_turtle)

x = -300
y = 200

for i in range(0, 6):
    list_of_turtles[i].teleport(x, y)
    y -= 50

user_turtle = t.textinput("Turtle Racing Game", "How will be the winner of the race? Enter a number: ").lower()

pace = 0

while pace < 25:
    for turtle in list_of_turtles:
        for _ in range(1):
            turtle.forward(random.randint(10,20))
            
    pace += 1

screen.exitonclick()
