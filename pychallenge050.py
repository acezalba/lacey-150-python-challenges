number = int(input("Enter a number between 10 and 20. >> "))
while number < 10 or number > 20:
    if number < 10:
        print("Too low.")
    else:
        print("Too high.")
    number = int(input("Enter a number between 10 and 20. >> "))
print("Thank you.")
