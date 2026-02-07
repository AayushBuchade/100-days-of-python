from turtle import Turtle, Screen
from random import randint

screen = Screen()
turtle_mamu = Turtle()

screen.colormode(255)
turtle_mamu.shape('arrow')
turtle_mamu.speed('fastest')

def draw_spirograph(num_of_circles, radius):
    for _ in range(num_of_circles):
        turtle_mamu.color((randint(0, 255), randint(0, 255), randint(0, 255)))
        turtle_mamu.circle(radius)
        turtle_mamu.right(round(360 / num_of_circles))
        turtle_mamu.width()


draw_spirograph(50,100)



screen.exitonclick()