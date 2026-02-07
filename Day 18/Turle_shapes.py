from turtle import *
from random import randint

turtle_mamu = Turtle()
screen = Screen()

screen.colormode(255)
turtle_mamu.shape('turtle')
turtle_mamu.pos()

def make_shapes():
    edges = 3
    for _ in range(8):
        angle = 360 / edges

        red = randint(0, 255)
        green = randint(0, 255)
        blue = randint(0, 255)
        turtle_mamu.color(red, green, blue)

        for _ in range(edges):
            turtle_mamu.forward(60)
            turtle_mamu.right(angle)

        edges += 1

make_shapes()

screen.exitonclick()
