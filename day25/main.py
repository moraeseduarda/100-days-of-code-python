# U.S. States Game
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(725, 491)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states = []

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()

while len(guessed_states) < 50:
    answer = turtle.textinput(f"{len(guessed_states)}/50 States Correct",
                              "What's another state name?").title()
    if answer == "Exit":
        missing_states = []
        for state in states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer in states:
        if answer not in guessed_states:
            state_data = data[data.state == answer]
            state_obj = turtle.Turtle()
            state_obj.penup()
            state_obj.hideturtle()
            state_obj.goto(state_data.x.item(), state_data.y.item())
            state_obj.write(answer)
            guessed_states.append(answer)
