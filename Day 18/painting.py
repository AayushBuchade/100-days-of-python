from random import randint
import colorgram
from turtle import *
turtle_mamu = Turtle()
screen = Screen()
screen.colormode(255)
turtle_mamu.speed("fastest")
# colors = colorgram.extract('painting.jpg', 30)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
#
# print(rgb_colors)

colour_list = [ (208, 160, 82), (54, 89, 131), (146, 91, 40), (140, 26, 48), (222, 206, 108), (132, 177, 203), (158, 45, 83), (47, 55, 103), (167, 160, 38), (128, 189, 143), (84, 20, 44), (36, 42, 70), (187, 93, 105), (187, 139, 170), (84, 123, 181), (59, 39, 31), (78, 153, 165), (88, 157, 91), (195, 79, 72), (45, 74, 78), (161, 202, 220), (80, 73, 44), (57, 131, 121), (218, 176, 188), (220, 183, 166), (166, 207, 165)]

def dotted_line(color_list, number_of_dots, radius, spacing):
    for _ in range(number_of_dots):
        turtle_mamu.color(color_list[randint(0, len(color_list) - 1)])
        turtle_mamu.dot(radius)
        turtle_mamu.up()
        turtle_mamu.forward(spacing + radius)
    turtle_mamu.up()
    turtle_mamu.back((spacing + radius) * number_of_dots)
    turtle_mamu.left(90)
    turtle_mamu.forward(spacing + round(0.5 * radius))
    turtle_mamu.right(90)
    turtle_mamu.down()

def main():
    turtle_mamu.hideturtle()
    turtle_mamu.color("white")
    turtle_mamu.goto(-250, -250)

    for _ in range(15):

        dotted_line(colour_list, 15, 20, 10)
    screen.exitonclick()

if __name__ == '__main__':
    main()






