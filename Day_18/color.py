from turtle import *
import turtle
from random import randint

tur = turtle.Turtle()

tur.shape('turtle')
for i in range(50):
    tur.pendown()
    tur.goto(randint(-150,0),randint(0,150))

turtle.done()