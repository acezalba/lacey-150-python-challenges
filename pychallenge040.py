number = int(input("Enter a number below 50: "))

if number > 50:
    print("Too large.")
    exit()

for i in range(50, number - 1, -1):
    print(i)
