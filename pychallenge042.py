total = int(0)
print("Enter five numbers in the following sequence.")
for i in range(5):
    number = int(input("Enter a number: "))
    choice = str(input("Do you want to add that to the total? y or n? "))[0]
    if choice.lower() == "y":
        total = total + number

print(total)
