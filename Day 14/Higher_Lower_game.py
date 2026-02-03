
#
# person1 = random.choice(game_data.data)
# person2 = random.choice(game_data.)
# while person2 == person1 or per
#
# print(person1)

# random_person1 = random.choice(game_data.data)
# def get_random_person():
#     random_person1 = random.choice(game_data.data)
#     random_person2 = random.choice(game_data.data)
#
#     get_random_person(random_person1, random_person2)
#
#     return [person_1, person_2]
#
# get_random_person()


# person_a = random.choice(game_data.data)
#
# person_b = random.choice(game_data.data)
# while person_b == person_a:
#     person_b = random.choice(game_data.data)
#
# print("A:", person_a["name"]["follower_count"]["description"]["country"])
# print("B:", person_b["name"])
import random
import game_data

score = 0
game_over = False

person_a = random.choice(game_data.data)

while not game_over:

    person_b = random.choice(game_data.data)
    while person_b == person_a:
        person_b = random.choice(game_data.data)

    print(
        f"A: {person_a['name']}, "
        f"{person_a['description']}, "
        f"with followers of: {person_a['follower_count']}, "
        f"from {person_a['country']}"
    )

    print(f"B: {person_b['name']}")

    def actual_answer():
        if person_a['follower_count'] > person_b['follower_count']:
            return "Higher"
        else:
            return "Lower"

    answer = actual_answer()

    player_choice = ""
    while player_choice != "Higher" and player_choice != "Lower":
        player_choice = input("Higher or Lower: ").capitalize()
        if player_choice != "Higher" and player_choice != "Lower":
            print("Invalid input, type only Higher or Lower")

    if player_choice == answer:
        score += 1
        print(f"Correct! Your score is {score}\n")
        person_a = person_b   # carry forward winner
    else:
        print(f"You lose! Final score is {score}")
        game_over = True


