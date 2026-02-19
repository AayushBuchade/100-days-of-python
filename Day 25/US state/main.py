import os
import turtle
import pandas as pd

TOTAL_STATES = 50

def main():
    path = os.path.dirname(os.path.realpath(__file__))

    screen = turtle.Screen()
    screen.title("U.S. States Game")
    screen.addshape(f"{path}/blank_states_img.gif")
    turtle.shape(f"{path}/blank_states_img.gif")

    data = pd.read_csv(f"{path}/50_states.csv")
    states = data.state.tolist()
    guessed = []

    while len(guessed) < TOTAL_STATES:
        answer = screen.textinput(
            title=f"{len(guessed)}/{TOTAL_STATES} Correct",
            prompt="State name (or 'exit'):"
        )

        if not answer or answer.lower() == "exit":
            break

        answer = answer.title()

        if answer in states and answer not in guessed:
            guessed.append(answer)
            row = data[data.state == answer]

            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(int(row.x), int(row.y))
            t.write(answer)

    if len(guessed) < TOTAL_STATES:
        missing = [s for s in states if s not in guessed]
        pd.DataFrame(missing).to_csv(f"{path}/states_to_learn.csv", index=False, header=False)
    else:
        t = turtle.Turtle()
        t.hideturtle()
        t.write("WELL DONE", align="center", font=("Courier", 24, "normal"))

if __name__ == "__main__":
    main()
