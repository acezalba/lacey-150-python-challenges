direction = str(input("What direction do you want to count to? up or down? "))
if direction.lower() == "up":
    number = int(input("What number would you want to count to? "))
    for i in range(1, number + 1):
        print(i)
elif direction.lower() == "down":
    number = int(input("Enter a number below 20: "))
    if number < 20:
        for i in range(number, 0, -1):
            print(i)
else:
    print("I don't understand.")
