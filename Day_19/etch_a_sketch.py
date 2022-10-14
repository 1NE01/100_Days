from turtle import *
danny = Turtle()
scrn = Screen()

def mov_forward():
    danny.forward(10)
def mov_backward():
    danny.backward(10)
def mov_right():
    danny.right(10)
def mov_left():
    danny.left(10)
def clear():
    
    danny.reset()



scrn.listen()
scrn.onkey(key="w",fun=mov_forward)
scrn.onkey(key="s",fun=mov_backward)
scrn.onkey(key="d",fun=mov_right)
scrn.onkey(key="a",fun=mov_left)
scrn.onkey(key="c",fun=clear)

scrn.exitonclick()