from turtle import Turtle, Screen
from random import randint

screen = Screen()


def move_turtle(turtle):
    turtle.forward(randint(1, 20))


def create_turtles(colors):
    turtles = []

    for i, color in enumerate(colors):
        t = Turtle(shape="turtle")
        t.color(color)
        t.speed("slowest")
        t.penup()
        t.goto(-400, -40 * i)
        turtles.append(t)

    return turtles


def draw_finish_line(x_position):
    line = Turtle()
    line.hideturtle()
    line.penup()
    line.goto(x_position, -220)
    line.pendown()
    line.left(90)
    line.forward(300)


def main():
    screen.setup(width=1000, height=500)

    colors = ["red", "blue", "green", "orange", "purple"]
    turtles = create_turtles(colors)

    finish_line_x = 400
    draw_finish_line(finish_line_x)

    bet = screen.textinput("Make your bet","Which color turtle will win the race?")
    race_on = True
    while race_on:
        for turtle in turtles:
            move_turtle(turtle)

            if turtle.xcor() > finish_line_x:
                winner = turtle.color()[0]
                print(f"The winner is {winner}!")

                if bet and bet.lower() == winner:
                    print("You were right!")
                else:
                    print("Your guess was wrong.")

                race_on = False
                break

    screen.exitonclick()


main()
