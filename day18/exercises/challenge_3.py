from turtle import Turtle, Screen
import random

sam_the_triangle = Turtle()

sam_the_triangle.shape("triangle")
sam_the_triangle.color("dark blue")
sam_the_triangle.pencolor("green")

colours = ["DeepSkyBlue", "MediumSeaGreen", "Gold", "Firebrick", "DeepPink", "MediumOrchid", "BlueViolet",
           "MidnightBlue"]

# TODO - Challenge 3: Drawing Different Shapes
# Triangle, Square, Pentagon, Hexagon, Heptagon, Octagon, Nonagon, Decagon

number_of_sizes = range(3, 10)

for number in number_of_sizes:
    sam_the_triangle.color(random.choice(colours))
    angle = 360 / number
    for i in range(number):
        sam_the_triangle.forward(100)
        sam_the_triangle.right(angle)

screen = Screen()
screen.exitonclick()
