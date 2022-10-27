import random

digits = []

for i in range(4):
    digits.append(random.randint(100, 999))

print(*digits, sep="\n")

while True:
    try:
        user_choice = int(input("Enter a number from the list. >> "))
        print("It is located in index", digits.index(user_choice))
        break
    except ValueError:
        print("That is not on the list.")
