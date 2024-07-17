# https://docs.python.org/3/library/turtle.html#turtle.forward
# https://cs111.wellesley.edu/reference/colors (turtle colors)
# import turtle
# timmy = turtle.Turtle()
# print(timmy)
import turtle

from turtle import Turtle, Screen
# timmy = object; turtle =  module; Turtle = class
timmy = Turtle()
print(timmy)

# methods
timmy.shape("turtle")
timmy.color("NavajoWhite4", "OliveDrab")
timmy.forward(100)

my_screen = Screen()
# my_screen = object; canvheight = attribute
print(my_screen.canvheight)

# attributes
my_screen.canvheight = 200
my_screen.canvwidth = 300

# my_screen = object; exitonclick() = method
my_screen.exitonclick()
