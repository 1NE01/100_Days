from turtle import *


class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.speed1 = 20




        self.shape("square")
        self.shapesize(1,5)
        self.color("white")
        self.penup()
        self.setheading(90)
        self.goto(position)


    def up(self):
        self.forward(self.speed1)

    def down(self):
        self.backward(self.speed1)

