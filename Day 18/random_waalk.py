from turtle import *
from random import randint
turtle_mamu = Turtle()
screen = Screen()

screen.colormode(255)
turtle_mamu.shape('turtle')
turtle_mamu.pos()


def draw_random_walk(num_of_steps, length_of_step):
    directions = [0, 90, 180, 270]
    turtle_mamu.width(10)
    for _ in range(num_of_steps):
        turtle_mamu.color((randint(0, 255), randint(0, 255), randint(0, 255)))
        turtle_mamu.setheading(directions[randint(0, 3)])
        turtle_mamu.forward(length_of_step)

draw_random_walk(50,20)

screen = Screen()
screen.exitonclick()