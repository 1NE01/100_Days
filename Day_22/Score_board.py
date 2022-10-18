from  turtle import *
class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score1 = 0
        self.score2 = 0

    def score_update(self):
        self.clear()
        self.goto(-100, 210)
        self.write(self.score1, align="center", font=("SUMMER", 40, "normal"))
        self.goto(100, 210)
        self.write(self.score2, align="center", font=("SUMMER", 40, "normal"))

    def point1(self):
        self.score1+=1
        self.score_update()
    def point2(self):
        self.score2+=1
        self.score_update()

