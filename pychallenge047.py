num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
numtotal = num1 + num2
choice = str(input("Do you want to add another number? y/n ")).lower()
while choice[0] == "y":
    num3 = int(input("Enter another number: "))
    numtotal = numtotal + num3
    choice = str(input("Do you want to add another number? y/n ")).lower()
print("The total is:", numtotal)
