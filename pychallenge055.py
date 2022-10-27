import random
import sys

computer_choice = random.randint(1, 5)
user_choice = int(input("Choose a number between 1 and 5. >> "))

while user_choice < 1 or user_choice > 5:
    print("Try again.")
    user_choice = int(input("Choose a number between 1 and 5. >> "))

if user_choice == computer_choice:
    print("Correct")
    sys.exit()

if user_choice < computer_choice:
    print("Too low.")

if user_choice > computer_choice:
    print("Too high")

while user_choice < computer_choice or user_choice > computer_choice:
    print("Try again.")
    user_choice = int(input("Choose a second number between 1 and 5. >> "))

if user_choice == computer_choice:
    print("Correct")
else:
    print("You lose")
