number = int(input("Enter a number between 1 and 12: "))

if number < 1 or number > 12:
    print("Number out of range")
    exit()

for i in range(1, 13):
    print(number, "*", i, "=", number * i)
