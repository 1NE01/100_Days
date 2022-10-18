from turtle import *
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.penup()
        self.xmove=10
        self.ymove =10
        self.ball_speed=0.1
    def mov(self):
        newx= self.xcor()+self.xmove
        newy = self.ycor() +self.ymove
        self.goto(newx,newy)
    def bounce_y(self):
        self.ymove *=-1
    def bounce_x(self):
        self.xmove*=-1
        self.ball_speed *=0.9
    def reset_pos(self):
        self.goto(0,0)
        self.ball_speed = 0.1
        self.bounce_x()
