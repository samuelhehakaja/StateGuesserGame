import turtle
import pandas

screen = turtle.Screen()
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
screen.title("US States Game")
image = "blank_states_img.gif"

data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()
answer_list = []

screen.addshape(image)
turtle.shape(image)

score = 0
game_on = True
while game_on:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="Enter a State's Name")
    answer_state = answer_state.title()
    if not answer_state in answer_list:
        for state in states_list:
            if state == answer_state:
                score += 1
                x = int(data[data["state"] == answer_state]["x"])
                y = int(data[data["state"] == answer_state]["y"])
                pen.goto(x, y)
                pen.write(answer_state)
                answer_list.append(answer_state)
    if score == 50:
        game_on = False

screen.exitonclick()
