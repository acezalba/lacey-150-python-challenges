def invite(invitations):
    invitations.append(
        str(input("Enter the name of a person you want to invite to the party: "))
    )


people = []

for i in range(3):
    invite(people)

response = str(input("Do you want to invite more people to the party? (Yes/No)"))

while response.lower() != "no":
    invite(people)
    response = str(input("Do you want to invite more people to the party? (Yes/No)"))

print("You have invited", len(people), "people.")
