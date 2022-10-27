name = str(input("Enter your name: "))
number = int(input("Enter any number: "))

if number < 10:
    for i in range(number):
        print(name)
else:
    print("Too high\n" * 3)
