# Using the phonebook data from program 139, write a program that will
# display the following menu:
#
# Main Menu:
# 1) View Phone book
# 2) Add to Phone book
# 3) Search for surname
# 4) Delete person from phone book
# 5) Quit
#
# Enter your selection:
#
# If the user selects 1, they should be able to view the entire notebook.
# If they select 2, it should allow them to add a new person to the phonebook.
# If they select 3, it should ask them for a surname and then display
# only the records of people with the same surname.
# If they select 4, it should ask for an ID and then delete that record
# from the table.
# If they select 5, it should end the program
# Finally, it should display a suitable message if they enter an incorrect selection
# from the menu.
#
# They should return to the menu after each action, until they select 5.

import sqlite3


def view_phonebook(cursor):
    cursor.execute("SELECT * FROM Names")
    for x in cursor.fetchall():
        print(x)


def add_to_phonebook(cursor):
    first_name = str(input("Enter first name: "))
    surname = str(input("Enter surname: "))
    phone_number = int(input("Enter 11-digit phone number: "))
    cursor.execute("SELECT * FROM Names ORDER BY id DESC LIMIT 1")
    last_row = cursor.fetchone()
    id = int(last_row[0]) + 1

    query = """
        INSERT INTO names(id,first_name,surname,phone_number)
        VALUES
            (?,?,?,?)
    """
    data = [id, first_name, surname, phone_number]
    print(data)

    cursor.execute(query, data)


def search_phonebook(cursor):
    surname_search = str(input("Enter a surname: "))
    cursor.execute("SELECT * FROM names WHERE surname=?", [surname_search])
    check_surname_search = cursor.fetchone()

    if check_surname_search is None:
        print("No results exists for this query.")
    else:
        for x in cursor.fetchall():
            print(x)


def delete_in_phonebook(cursor):
    id_to_delete = int(input("Enter id of entry to delete: "))
    cursor.execute("SELECT * FROM names WHERE id=?", [id_to_delete])
    row_to_delete = cursor.fetchone()

    if row_to_delete is None:
        print(f"There is no record with the ID of {id_to_delete}.")
    else:
        name_to_delete = row_to_delete[1]
        cursor.execute("DELETE FROM names WHERE id=?", [id_to_delete])
        print(f"Record for user {name_to_delete} was deleted.")


def menu(db, cursor):

    while True:
        print(
            "\nManage Phone Book: \n \
            1) View Phone book\n \
            2) Add to Phone book\n \
            3) Search for surname\n \
            4) Delete person from phone book\n \
            5) Quit\n"
        )

        choice = int(input("What do you want to do? "))

        if choice == 1:
            view_phonebook(cursor)
        elif choice == 2:
            add_to_phonebook(cursor)
            db.commit()
        elif choice == 3:
            search_phonebook(cursor)
        elif choice == 4:
            delete_in_phonebook(cursor)
            db.commit()
        elif choice == 5:
            return False
        else:
            print("\nYou picked an invalid choice.")
            return True

    menu(db, cursor)


def main():
    with sqlite3.connect("PhoneBook.db") as db:
        cursor = db.cursor()
    while menu(db, cursor):
        continue
    db.close()
    print("Exiting")
    exit()


####################################################

main()
