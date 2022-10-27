invitations = []
attendee = ""

for i in range(3):
    invitations.append(
        str(input("Enter the name of a person you want to invite to the party: "))
    )

response = str(input("Do you want to invite more people to the party? (Yes/No)"))

while response.lower() != "no" and response:
    response = attendee = str(
        input("Enter the name of a person you want to invite to the party: ")
    )
    if attendee.lower() != "no" and attendee:
        invitations.append(attendee)

print("You have invited", len(invitations), "people.")
print("Here are the attendees: ")
print(*invitations, sep="\n")

attendee = str(input("Enter the name of someone in the list: "))

if invitations.index(attendee):
    print("Person is in the list")
else:
    print("Person is not on the list.")

response = str(input("Do you want the person to attend the party? Yes or no? "))

if response.lower() == "no":
    invitations.remove(attendee)

print("Here are your new attendees: ")
print(*invitations, sep="\n")
