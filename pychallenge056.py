import random

computer_choice = random.randint(1, 10)
user_choice = 0

while user_choice != computer_choice:
    user_choice = int(input("Enter a number: "))

print("Congrats. You picked the right number. Computer chose number", computer_choice)
