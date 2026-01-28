import random
import words_list
import ascii_art

choosen_word = random.choice(words_list.word_list)
print(choosen_word)
lives = 6
copy_of_word = []
[copy_of_word.append("_") for character in choosen_word]

print(copy_of_word)
guess = input("Guess the letter : ").lower()
#print(guess)

while "_" in copy_of_word and lives > 0:
    guess = input("guess a letter: ").lower()
    print(guess)
display = ""
for letters in choosen_word:
    if letters == guess:
        display += letters

    else:
        display += "_"

print(display)
