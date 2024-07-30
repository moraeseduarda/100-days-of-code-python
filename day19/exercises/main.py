# Challenge: Make an Etch-A-Sketch App

import turtle

timmy = turtle.Turtle()
screen = turtle.Screen()


def clear_screen():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


def move_forwards():
    timmy.forward(10)


def move_backwards():
    timmy.backward(10)


def move_right():
    timmy.right(10)


def move_left():
    timmy.left(10)


screen.listen()
screen.onkey(clear_screen, "c")
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkeypress(move_right, "d")
screen.onkeypress(move_left, "a")
screen.exitonclick()
