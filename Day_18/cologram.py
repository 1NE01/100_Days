import turtle
import random

import colorgram


def paint(cols, rows):

    extracted_colors = colorgram.extract("image.jpg", 30)
    color_list = []
    for col in extracted_colors:
        color_list.append(col.rgb)


    brush = turtle.Turtle()
    brush.shape("circle")

    brush.speed(7)
    brush.penup()
    brush.hideturtle()


    width = screen.window_width()
    height = screen.window_height()

    x_offset = int(width / cols)
    y_offset = int(height / rows)

    x_pos = int(width / -2 + x_offset / 2)
    y_pos = int(height / -2 + y_offset / 2)
    for _ in range(0, rows):
        for __ in range(0, cols):
            brush.setx(x_pos)
            brush.sety(y_pos)
            brush.dot(30, random.choice(color_list))
            x_pos += x_offset

        x_pos = int(width / -2 + x_offset / 2)
        y_pos += y_offset

turtle.colormode(255)
screen = turtle.Screen()
screen.title("Hirst-like art")
screen.setup(width=800, height=600)
paint(cols=6, rows=4)
screen.exitonclick()