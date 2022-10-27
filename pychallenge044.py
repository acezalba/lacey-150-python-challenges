people = int(input("How many people do you want invited to a party? "))
if people > 9:
    print("Too many people.")
else:
    for i in range(people):
        invited = str(input("Enter a name: "))
        print(invited, "has been invited.")
