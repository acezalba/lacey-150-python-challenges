old_password = str(input("Enter your password: "))
new_password = str(input("Enter your password again: "))

while old_password != new_password:
    if old_password.lower() == new_password.lower():
        print("They must be in the same case.")
    else:
        print("Incorrect.")

    old_password = str(input("Enter your password: "))
    new_password = str(input("Enter your password again: "))

print("Thank you.")
