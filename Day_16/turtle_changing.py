import turtle

scrn = turtle.Screen()
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
t.shape("turtle")
t.color('green')
t.speed(50)
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%6])
    t.pensize(5)
    t.forward(x+10)
    t.left(90)
    t.forward(x+6)
    t.forward(x+6)

scrn.exitonclick()

