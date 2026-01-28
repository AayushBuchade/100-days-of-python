import random
import words_list

chosen_word=random.choice(words_list.word_list)
print(chosen_word)

# copy_of_word=[]
# [copy_of_word.append("_") for char in chosen_word]
# print(copy_of_word)

placeholder=""
word_len=len(chosen_word)
for position in range(word_len):
    placeholder+="_"
print(placeholder)


guess = input("Guess a letter: ").lower()
print(guess)

display=""

for letter in chosen_word:
    if letter==guess:
        display += letter
    else:
        display+="_"

print(display)