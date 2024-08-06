from turtle import Turtle
import random

colors = ["blue", "green", "red", "yellow", "purple"]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.refresh()

    def random_color(self):
        random_number = random.randint(0, len(colors) - 1)
        new_color = colors[random_number]
        self.color(new_color)

    def refresh(self):
        self.random_color()
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)
