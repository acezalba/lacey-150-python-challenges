# /usr/bin/env python3
"""
Passwords
"""

import csv
import string


def check_user_exists(username):
    # Store all existing users in temporary list
    existing_users = []
    with open("Passwords.csv", "r", newline="") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            existing_users.append(row[0])

    if username in existing_users:
        return True

    return False


def check_pass_length(password):
    if len(password) > 7:
        return 1
    else:
        return 0


def check_upper(password):
    for letter in list(password):
        if letter in string.ascii_uppercase:
            return 1

    return 0


def check_lower(password):
    for letter in list(password):
        if letter in string.ascii_lowercase:
            return 1

    return 0


def check_numbers(password):
    for letter in list(password):
        if letter in string.digits:
            return 1

    return 0


def check_special_char(password):
    special_char_allowed = ["!", "£", "$", "%", "&", "<", "@"]

    for letter in list(password):
        if letter in special_char_allowed:
            return 1

    return 0


def create_password():
    print(
        """Your password must be:
- at least 8 characters
- include uppercase letters
- include lowercase letters
- include numbers; and
- should include at least one of the following characters: !£$%&<@
"""
    )
    new_pass = ""
    valid_pass = False

    while not valid_pass:
        new_pass = str(input("Enter new password: "))

        pass_score = (
            check_pass_length(new_pass)
            + check_upper(new_pass)
            + check_lower(new_pass)
            + check_numbers(new_pass)
            + check_special_char(new_pass)
        )

        if pass_score == 5:
            valid_pass = True
            print("You've entered a strong password.")
            password_reconfirm = input("Enter your password again: ")
            if new_pass != password_reconfirm:
                valid_pass = False
                print("Passwords don't match. Try again.")

        if pass_score in range(3, 5):
            print("This password could be improved.")
            print("Try again.")
            print("Check the criteria; see what you missed.")

        if pass_score < 3:
            print("This is a weak password.")
            print("Try again.")

    return new_pass


def create_user_id():
    with open("Passwords.csv", "a", newline="") as file:
        csv_writer = csv.writer(file)

        print("Creating new user.")
        user_id = ""
        id_passed = False

        # Process new user_id
        while not id_passed:
            user_id = str(input("Enter username: "))

            # Check for whitespaces
            if " " in user_id:
                print("Don't add spaces. Try again.")
                continue

            # Check if ID is in the database
            if check_user_exists(user_id):
                print(f"{user_id} already exists in record. Try again.")
                continue

            id_passed = True

        # Create new password
        password = create_password()

        # Store new user_id and password in file
        id_pass_pair = [user_id, password]
        csv_writer.writerow(id_pass_pair)
        print(f"{user_id} created successfully.")


def change_user_password():
    userid_pass_to_change = input("Enter username: ")

    if not check_user_exists(userid_pass_to_change):
        print(
            f"'{userid_pass_to_change}' does not exists. \n\
Perhaps you meant to create a new user?"
        )
        return

    file_contents = []
    with open("Passwords.csv", "r", newline="") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            file_contents.append(row)

    with open("Passwords.csv", "w", newline="") as file:
        csv_writer = csv.writer(file)
        for row in file_contents:
            if row[0] == userid_pass_to_change:
                row[1] = create_password()
                print(f"{userid_pass_to_change} password changed successfully.")
            csv_writer.writerow(row)


def display_all_users():
    with open("Passwords.csv", "r", newline="") as file:
        csv_reader = csv.reader(file)
        print("These are all users in record: ")
        for row in csv_reader:
            print(row[0])
    print()


def menu():
    menu = "Manage your Passwords File\n \
1) Create a new User ID.\n \
2) Change a password\n \
3) Display all user IDs\n \
4) Quit"
    print(menu)
    choice = input("What do you want to do? ")

    if choice == "1":
        create_user_id()
        return True
    elif choice == "2":
        change_user_password()
        return True
    elif choice == "3":
        display_all_users()
        return True
    elif choice == "4":
        print("Exiting")
        return False
    else:
        print("Choice not recognized.")
        return True


def main():
    open("Passwords.csv", "a+").close()
    while menu():
        continue
    exit()


main()
