# U.S. States Game
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(725, 491)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_correct = 0
data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
x_list = data["x"].to_list()
y_list = data["y"].to_list()

while states_correct < 50:
    answer = turtle.textinput(f"{states_correct}/50 States Correct", "What's another state name?")
    for state in states:
        if answer == state:
            state_index = states.index(state)
            new_x = x_list[state_index]
            new_y = y_list[state_index]
            state_obj = turtle.Turtle()
            state_obj.penup()
            state_obj.hideturtle()
            state_obj.teleport(new_x, new_y)
            state_obj.write(state)
            states_correct += 1

screen.exitonclick()
