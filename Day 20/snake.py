from turtle import Turtle

LINK_SIZE = 20
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.num_of_links = 3
        self.body = self.create_body()
        self.head = self.body[0]

    def create_body(self):
        body = []
        for i in range(self.num_of_links):
            segment = Turtle("square")
            segment.penup()
            segment.color("gray")
            segment.goto(-i * LINK_SIZE, 0)
            body.append(segment)
        return body

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            new_x = self.body[i - 1].xcor()
            new_y = self.body[i - 1].ycor()
            self.body[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
