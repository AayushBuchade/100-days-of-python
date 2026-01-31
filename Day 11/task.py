import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
shuffled_cards = random.choice(cards)
print("Start Black Jack game :")
My_cards = []
Computers_cards = []
Black_jack = 11 + 10


user_input = str(input("press y to start or n to terminate : "))
if user_input == "y":

    print(f"your cards: [{shuffled_cards}, {shuffled_cards}]")
    print(f"computers cards: [ X , {shuffled_cards}]")
elif user_input == "n":
    print("Black Jack game terminated")
else:
        print("enter valid string !!!!")



def pick_card():
    random.choice(shuffled_cards)

