import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(turtle.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    if car_manager.detect_collision(turtle):
        game_is_on = False
        # scoreboard.game_over()

    if turtle.arrived():
        turtle.restart()
        car_manager.level_up()
        # scoreboard.increase_level()

screen.exitonclick()
