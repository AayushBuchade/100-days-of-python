from turtle import *
import heroes


turtle_mamu = Turtle()
# turtle_mamu.forward(100)
turtle_mamu.shape("turtle")

def make_square():
    turtle_mamu.forward(100)
    turtle_mamu.right(90)
    turtle_mamu.forward(100)
    turtle_mamu.right(90)
    turtle_mamu.forward(100)
    turtle_mamu.right(90)
    turtle_mamu.forward(100)

def dotted_line():

    for i in range(20):
        turtle_mamu.penup()
        turtle_mamu.forward(5)
        turtle_mamu.pendown()
        turtle_mamu.forward(5)



dotted_line()

screen = Screen()
screen.exitonclick()
