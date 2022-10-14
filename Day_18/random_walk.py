from turtle import *

from random import *

danny = Turtle()

scrn = Screen()
danny.shape('turtle')
scrn.colormode(255)
bgcolor('black')
danny.pensize(10)
degree = [90,180,270,0]
for i in range(50):
    danny.pencolor(randint(1,255),randint(1,255),randint(1,255))
    danny.pendown()
    danny.forward(20)

    danny.left(choice(degree))




scrn.exitonclick()