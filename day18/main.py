# The Hirst Painting Project7
# https://trinket.io/docs/colors

# from turtle import *
# import turtle as t
from turtle import Turtle, Screen

sam_the_triangle = Turtle()
# sam_the_triangle = turtle.Turtle()
sam_the_triangle.shape("triangle")
sam_the_triangle.color("dark blue")

# TODO - Challenge 1: Draw a Square.
for i in range(4):
    sam_the_triangle.forward(100)
    sam_the_triangle.right(90)

screen = Screen()
# screen = turtle.Screen()
screen.exitonclick()
