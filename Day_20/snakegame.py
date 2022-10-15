import time
from turtle import *
from snake1 import *
scrn = Screen()
scrn.tracer(0)
snake = Snake()
scrn.setup(600,600)
scrn.bgcolor("black")
scrn.listen()
scrn.onkeypress(snake.up,"w")
scrn.onkeypress(snake.down,"s")
scrn.onkeypress(snake.left,"a")
scrn.onkeypress(snake.right,"d")

gameis = True
while gameis:
    scrn.update()
    time.sleep(0.1)
    snake.move()










scrn.exitonclick()