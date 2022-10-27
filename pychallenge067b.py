import turtle
import random

scr = turtle.Screen()
scr.colormode(255)
scr.bgcolor("black")

turtle.pensize(2)

for i in range(10):
    turtle.right(36)
    for i in range(8):
        turtle.pencolor(
            random.randrange(1, 100, 4),
            random.randrange(1, 255, 4),
            random.randrange(1, 255, 4),
        )
        turtle.forward(80)
        turtle.right(45)
turtle.exitonclick()
