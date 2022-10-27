import random

colors = ["red", "green", "yellow", "white", "grey"]
computer_guess = random.choice(colors)

print("Choose from the following: ", end="")
for index, value in enumerate(colors):
    if index == len(colors) - 1:
        print(f"{value}.")
    else:
        print(f"{value}, ", end="")

user_guess = str(input("What is your guess? >> ")).lower()

while user_guess != computer_guess:
    print("You must be feeling", computer_guess.upper(), "right now.")
    user_guess = str(input("What is your new guess? >> ")).lower()

print("You are correct. The correct color is", computer_guess)
