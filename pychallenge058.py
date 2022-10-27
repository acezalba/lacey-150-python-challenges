import random

points = 0
items = 0

while items < 5:
    items = items + 1
    num1, num2 = random.randint(0, 100), random.randint(0, 100)
    total = num1 + num2
    answer = int(input(f"{items}. {num1} + {num2}: "))
    if answer == total:
        points = points + 1

print("You got", points, "points out of 5.")
