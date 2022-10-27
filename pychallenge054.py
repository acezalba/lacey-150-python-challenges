import random

computer_choice = random.choice(["h", "t"])
user_choice = str(input("Choose heads or tails? h/t >> "))

if user_choice[0].lower() == computer_choice:
    print("You win.")
else:
    print("Bad luck")

print("The computer chose", computer_choice)
