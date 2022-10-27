import turtle
import random


def random_pattern(outer_line, inner_line, length, angle):
    for i in range(outer_line):
        turtle.right(angle)
        for i in range(inner_line):
            turtle.pencolor(
                random.randrange(1, 100, 4),
                random.randrange(1, 255, 4),
                random.randrange(1, 255, 4),
            )
            turtle.forward(length)
            turtle.right(angle)


scr = turtle.Screen()
scr.colormode(255)
turtle.pensize(2)
random_pattern(
    random.randint(6, 10),
    random.randint(5, 8),
    random.randint(80, 120),
    random.randint(1, 365),
)

turtle.exitonclick()
