import random
import Art

print(Art.logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

your_cards = [random.choice(cards), random.choice(cards)]
computer_cards = [random.choice(cards), random.choice(cards)]

def calculate_score(hand):
    score = sum(hand)
    if 11 in hand and score > 21:
        score -= 10
    return score

your_score = calculate_score(your_cards)
computer_score = calculate_score(computer_cards)

print(f"Your cards: {your_cards}, score: {your_score}")
print(f"Computer's first card: {computer_cards[0]}")

#IF BLACKjACK winner or looser

if your_score == 21:
    print("You have blackjack => WIN")
elif computer_score == 21:
    print("Computer has blackjack => LOSE")
else:
    # +1 card sathii
    game_over = False
    while not game_over:
        choice = input("Do you want another card? (y/n): ").lower()
        if choice == "y":
            your_cards.append(random.choice(cards))
            your_score = calculate_score(your_cards)
            print(f"Your cards: {your_cards}, score: {your_score}")

            if your_score > 21:
                print("You went over 21 => LOSE")
                game_over = True
        else:
            game_over = True
            print(" Stand.")
            while computer_score < 17 :
                computer_cards.append(random.choice(cards))
                computer_score = calculate_score(computer_cards)

    print(f"Computer Cards : {computer_cards}, Computer Score : {computer_score}")

    if computer_score > 21:
        print("You win, Computer Bust")
    elif your_score > 21:
        print("Computer wins , You Bust")
    elif computer_score > your_score:
        print("Computer wins")
    elif your_score > computer_score:
        print("You win")
    else:
        print("DRAW")


