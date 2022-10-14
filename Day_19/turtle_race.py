import random

from turtle import *
scrn = Screen()
scrn.setup(600,600)
bet = scrn.textinput("Make your bet","Which Turtle will win the race? : Choose the colour")
colors = ["red","blue","green","orange","yellow","purple"]
y_postion = [-70,-40,-10,20,50,80]
is_race = False
turtles = []
for i in range(6):
    tur=Turtle("turtle")
    tur.penup()
    tur.color(colors[i])
    tur.goto(-230,y_postion[i])
    turtles.append(tur)
if bet :
    is_race = True
while is_race:
    for turtle in turtles:
        if turtle.xcor()>230:
            is_race = False
            win = turtle.pencolor()
            if win == bet:
                print(f"you won the color of won turtle is {win}")
            else:
                print(f"You lose the color of won turtle is {win}")
        distance = random.randint(0,10)
        turtle.forward(distance)


exitonclick()