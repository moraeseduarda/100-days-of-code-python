import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
sam_the_triangle = Turtle()

sam_the_triangle.shape("triangle")
sam_the_triangle.color("dark blue")
sam_the_triangle.pencolor("green")


# colours = ["DeepSkyBlue", "MediumSeaGreen", "Gold", "Firebrick", "DeepPink", "MediumOrchid", "BlueViolet",
#            "MidnightBlue"]

# Generating Random RGB Colours
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    final_color = (r, g, b)
    return final_color


# TODO - Challenge 4: Draw a Random Walk

directions = [0, 90, 180, 270]

sam_the_triangle.pensize(10)
sam_the_triangle.speed("fastest")

for _ in range(200):
    sam_the_triangle.color(random_color())
    sam_the_triangle.forward(20)
    sam_the_triangle.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
