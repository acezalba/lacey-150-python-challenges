import random

computer_choice = random.randint(1, 10)
user_choice = int(input("Enter a number: "))

while user_choice != computer_choice:
    if user_choice < computer_choice:
        print("Too low.")
    else:
        print("Too high.")
    user_choice = int(input("Enter a number: "))

print("Congrats. You picked the right number. Computer chose number", computer_choice)
