import turtle
from turtle import Turtle, Screen
import random

sam_the_triangle = Turtle()
turtle.colormode(255)
sam_the_triangle.shape("triangle")
sam_the_triangle.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    new_color = (r, g, b)
    return new_color


# TODO - Challenge 5: Turtle Challenge 5 - Draw a Spirograph

# My solution
for _ in range(80):
    sam_the_triangle.color(random_color())
    sam_the_triangle.circle(100)
    sam_the_triangle.left(5)

# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         sam_the_triangle.color(random_color())
#         sam_the_triangle.circle(100)
#         current_heading = sam_the_triangle.heading()
#         sam_the_triangle.setheading(current_heading + 10)


# draw_spirograph(5)
screen = Screen()
screen.exitonclick()
