from turtle import *
from random import *


scrn= Screen()
t= Pen()
t.shape("turtle")
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
bgcolor('black')
t.color("green")
i=3


for _ in range(11):
    count = 0
    while(count<i):
        t.pencolor(colors[i % 6])
        t.forward(50)
        t.left(360/i)
        count+=1
    i+=1


scrn.exitonclick()