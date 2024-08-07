# The Pong Game
from turtle import Screen, Turtle
from scoreboard import Scoreboard
from paddles import Paddle
from ball import Ball
import time

# Screen object and settings
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
# Stop animations
screen.tracer(0)

# Middle dashed lines
y_cor = -405
for i in range(30):
    lines = Turtle(shape="square")
    lines.penup()
    lines.color("white")
    lines.shapesize(stretch_wid=1, stretch_len=0.1)
    y_cor += 40
    lines.goto(lines.xcor(), y_cor)

# Scoreboard and the two paddles objects
scoreboard = Scoreboard()
# Paddle(position=tuple).
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

# Keyboard control settings
screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

# Ball object
ball = Ball()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    # Updates animations
    screen.update()
    ball.move()

    # Detects roof and floor collision and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor()
                                                                    < -320):
        ball.bounce_x()

    # Detect right paddle misses
    if ball.xcor() > 350:
        ball.reset_position()
        scoreboard.left_point()

    # Detect left paddle misses
    if ball.xcor() < -350:
        ball.reset_position()
        scoreboard.right_point()

screen.exitonclick()
