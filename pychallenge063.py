import turtle


def coloredsquare(new_color):
    turtle.color("black", new_color)
    turtle.begin_fill()
    for i in range(0, 4):
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()
    return


chosen_colors = ["red", "yellow", "green"]

turtle.penup()
turtle.right(180)
turtle.forward(300)
turtle.right(180)
turtle.pendown()

for value in chosen_colors:
    coloredsquare(value)
    turtle.penup()
    turtle.forward(120)
    turtle.pendown()

turtle.exitonclick()
