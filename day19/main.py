# Turtle Racing Game
import turtle as t
import random as r

screen = t.Screen()
screen.setup(width=500, height=400)
list_of_turtles = []
colors = ["purple", "blue", "green", "yellow", "orange", "red"]
is_race_on = False

for i in range(0, 6):
    color = colors[i]
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    list_of_turtles.append(new_turtle)

x = -200
y = 130

for i in range(0, 6):
    list_of_turtles[i].teleport(x, y)
    y -= 50

user_bet = t.textinput("Turtle Racing Game", "How will be the winner of the race? Enter a color: ").lower()

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in list_of_turtles:
        if turtle.xcor() > 200:
            is_race_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"You win! The {winner_color} turtle is the winner.")
            else:
                print(f"You lose. The {winner_color} turtle is the winner.")
        turtle.forward(r.randint(0, 10))

screen.exitonclick()
