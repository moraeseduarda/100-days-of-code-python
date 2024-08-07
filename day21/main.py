# Snake Game Part 2 and Final
import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.tracer(0)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect Collisions with Food
    # object.distance(another_object) - measures the distance between the centers of two distinct objects.
    if snake.snake_head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.record()

    # Detect Collisions with Wall
    if (snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280
            or snake.snake_head.ycor() < -280):
        game_is_on = False
        scoreboard.game_over()

    # Detect Collisions with Tail
    for segment in snake.snake_body[1:]:
        if snake.snake_head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
