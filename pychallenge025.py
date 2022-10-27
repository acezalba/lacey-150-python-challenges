first_name = str(input("Enter your first name: "))

if len(first_name) < 5:
    print((first_name + str(input("Enter your last name: "))).upper())
else:
    print(first_name.lower())
