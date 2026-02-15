import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
        self.spawn_counter = 0

    def create_car(self):
        self.spawn_counter += 1

        if self.spawn_counter % 6 == 0:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))

            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)

            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.move_distance)

    def detect_collision(self, player):
        for car in self.all_cars:
            if car.distance(player) < 20:
                return True
        return False

    def level_up(self):
        self.move_distance += MOVE_INCREMENT
