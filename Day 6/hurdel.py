def turn_right():
    for i in range(0, 3):
        turn_left()


def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while at_goal() != True:
    while front_is_clear() != True:
        while is_facing_north != True:
            turn_left()
        if wall_on_right():
            move()
        else:
            turn_right()