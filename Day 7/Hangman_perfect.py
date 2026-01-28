import random
import words_list
import ascii_art

chosen_word = random.choice(words_list.word_list)
word_length = len(chosen_word)

print(chosen_word)
lives = 6
display = ["_"] * word_length
end_of_game = False

print(ascii_art.stages[lives])
print(display)

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You already guessed '{guess}'")

    for i in range(word_length):
        if chosen_word[i] == guess:
            display[i] = guess

    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong guess! Lives left: {lives}")
        print(ascii_art.stages[lives])

        if lives == 0:
            end_of_game = True
            print("You lose ")
            print(f"The word was: {chosen_word}")

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win ")