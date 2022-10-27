name = str(input("Who do you want to invite to the party?"))
count = 1
print(name, "has now been invited")

choice = str(input("Do you want to invite somebody else? y/n ")).lower()

while choice[0] == "y":
    name = str(input("Who do you want to invite to the party?"))
    count = count + 1
    print(name, "has now been invited")
    choice = str(input("Do you want to add another person? y/n ")).lower()

print("You have invited", count, "people.")
