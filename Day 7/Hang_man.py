import random
import words_list

chosen_word = random.choice(words_list.word_list)
print(chosen_word)

placeholder = ""
word_len = len(chosen_word)
for _ in range(word_len):
    placeholder += "_"
print(placeholder)

game_is_over = False
correct_letters = []

while not game_is_over:
    guess = input("Guess a letter: ").lower()

    if guess not in correct_letters:
        correct_letters.append(guess)

    display = ""

    for letter in chosen_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_is_over = True
        print("Win!!")
