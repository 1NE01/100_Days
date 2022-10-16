from turtle import Turtle
ALIGNMENT = "center"
FONT = ("SUMMER", 24, "normal")


class Scoreboard(Turtle,):

    def __init__(self,screen):
        super().__init__()
        self.screen = screen
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, (self.screen.window_height() / 2) - (self.screen.window_height() * 0.1))
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
