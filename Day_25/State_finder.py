import turtle
import pandas

scrn = turtle.Screen()
scrn.title("State Game")
image = "blank_states_img.gif"
scrn.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
states1 = []

while len(states1) < 50:
    answer = scrn.textinput(title=f"{len(states1)}/50 States Correct",
                            prompt="Nxt State?").title()

    if answer == "Exit":
        missing_states = []
        for state2 in states:
            if state2 not in states1:
                missing_states.append(state2)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer in states:
        states1.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == answer]
        t.goto(int(state_data["x"]), int(state_data["y"]))
        t.write(answer)
turtle.mainloop()
