import turtle
import random

scr = turtle.Screen()
scr.bgcolor("black")
turtle.pensize(5)
colors = ["#7cff9f", "#dcff7c", "#ff9f7c", "#ff7cdc", "#9f7cff", "#7cdcff"]

for i in range(8):
    turtle.pencolor(colors[random.randint(0, 5)])
    turtle.forward(120)
    turtle.right(45)
turtle.exitonclick()
