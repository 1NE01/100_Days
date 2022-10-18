from turtle import *
import time
from Paddle import *
from Ball import *
from Score_board import *


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
paddle_1 = Paddle((350,0))
paddle_2 =Paddle((-350,0))
ball = Ball()
scoreboard = Score_board()





screen.listen()
screen.onkeypress(key="w", fun=paddle_1.up)
screen.onkeypress(key="s", fun=paddle_1.down)
screen.onkeypress(key="Up", fun=paddle_2.up)
screen.onkeypress(key="Down", fun=paddle_2.down)
game_on = True
while game_on:
    screen.update()
    ball.mov()
    time.sleep(ball.ball_speed)

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    if ball.distance(paddle_1)<50 and ball.xcor()>320 or ball.distance(paddle_2)<50 and ball.ycor()>-320:
        ball.bounce_x()
    if ball.xcor() >380:
        ball.reset_pos()
        scoreboard.point1()
    if ball.xcor() <-380:
        ball.reset_pos()
        scoreboard.point2()


screen.exitonclick()





