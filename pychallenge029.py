import math

number = int(input("Enter an integer over 500: "))
if number > 500:
    print(round(math.sqrt(number), 2))
else:
    print("This is less than 500. Run the program again.")
