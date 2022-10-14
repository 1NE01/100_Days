from turtle import *

from random import *

danny = Turtle()

scrn = Screen()
danny.shape('turtle')
scrn.colormode(255)
bgcolor('black')
danny.pensize(2)
a=20

danny.speed("fastest")
while a< 361:

    danny.pencolor(randint(1,255),randint(1,255),randint(1,255))
    danny.circle(50)
    danny.setheading(a)
    a+=20





scrn.exitonclick()