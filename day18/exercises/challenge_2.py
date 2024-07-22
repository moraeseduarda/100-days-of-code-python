from turtle import Turtle, Screen

sam_the_triangle = Turtle()

sam_the_triangle.shape("triangle")
sam_the_triangle.color("dark blue")
sam_the_triangle.pencolor("green")

# TODO - Challenge 2: Draw a Dashed Line.
for i in range(10):
    sam_the_triangle.forward(10)
    sam_the_triangle.penup()
    sam_the_triangle.forward(10)
    sam_the_triangle.pendown()

screen = Screen()
screen.exitonclick()
