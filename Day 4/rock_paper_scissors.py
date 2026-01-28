import random

print("Welcome to the game of Rock Paper Scissors!")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]

user_input = int(input("Choose 1 for Rock, 2 for Paper, and 3 for Scissors: "))

user_choice = user_input - 1

computer_choice = random.randint(0, 2)

print("\nYou chose:")
print(options[user_choice])

print("Computer chose:")
print(options[computer_choice])

if user_choice == computer_choice:
    print("It's a draw!")
elif (user_choice == 0 and computer_choice == 2) or \
     (user_choice == 1 and computer_choice == 0) or \
     (user_choice == 2 and computer_choice == 1):
    print("You win!")
else:
    print("You lose!")
