from turtle import Turtle
ALIGNMENT = "center"
FONT = ("SUMMER", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self,screen):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore=int(data.read())


        self.color("white")
        self.penup()
        self.goto(0, (self.screen.window_height() / 2) - (self.screen.window_height() * 0.1))
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score:{self.highscore}", align=ALIGNMENT, font=FONT)
    def update_set_highscore(self):
        with open("data.txt",mode="w") as data:
            data.write(f"{self.highscore}")

    def reset(self):


        self.score=0
        self.update_scoreboard()


    def increase_score(self):
        self.score += 1
        if self.score > self.highscore:
            self.highscore=self.score
            self.update_set_highscore()

        self.update_scoreboard()
