from turtle import *
postion = [(0,0),(-20,0),(-40,0)]
travel = 20
up=90
down=270
left=180
right=0
class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]
    def create_snake(self):
        for i in postion:
            tur = Turtle("square")

            tur.penup()
            tur.color("green")
            tur.goto(i)
            self.turtles.append(tur)
    def move(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            x = self.turtles[i - 1].xcor()
            y = self.turtles[i - 1].ycor()
            self.turtles[i].goto(x, y)
        self.head.forward(travel)
    def up(self):
        if self.head.heading() != down:
           self.head.setheading(up)
    def down(self):
        if self.head.heading() != up:
          self.head.setheading(down)
    def left(self):
        if self.head.heading() != right:
          self.head.setheading(left)
    def right(self):
        if self.head.heading() != left:
          self.head.setheading(right)
