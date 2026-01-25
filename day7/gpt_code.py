import random
import word_list

chosen_word=random.choice(word_list.word_list)
print(chosen_word)

# copy_of_word=[]
# [copy_of_word.append("_") for char in chosen_word]
# print(copy_of_word)

placeholder=""
word_len=len(chosen_word)
for position in range(word_len):
    placeholder+="_"
print(placeholder)

game_is_over=False
correct_letters =[]

while not game_is_over:
    guess = input("Guess a letter: ").lower()
    print(guess)
    display=""

for letter in chosen_word:
    # if letter==guess:
    #     display += letter
    # else:
    #     display+="_"
            if letter in correct_letters:
                display += letter
            else:
                display += "_"
print(display)

if "_" not in display:
    game_is_over = True
    print("Win!!")