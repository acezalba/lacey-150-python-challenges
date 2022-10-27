import csv


def add_to_file():
    with open("Salaries.csv", "a", newline="") as file:
        csv_writer = csv.writer(file)
        loop = True
        print(
            "\nAdding entries to Salaries.csv\n \
        Just press enter to return back to the menu."
        )
        while loop:
            entry = []
            name = str(input("Enter name: "))
            if not name:
                print("Returning to menu.")
                break
            salary = float(input("Enter salary: "))
            currency_salary = "${:,.2f}".format(salary)
            entry.append(name)
            entry.append(currency_salary)
            csv_writer.writerow(entry)
            entry.clear()


def show_records():
    with open("Salaries.csv", "r", newline="") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)
    print()


def menu():
    menu = "Manage your Salaries.csv\n \
1) Add to file.\n \
2) View all records\n \
3) Exit the program.\n"
    print(menu)
    choice = int(input("What do you want to do? "))

    if choice == 1:
        add_to_file()
        return True
    elif choice == 2:
        show_records()
        return True
    elif choice == 3:
        print("Exiting")
        return False
    else:
        print("Choice not recognized.")
        return True


def main():
    while menu():
        continue
    exit()


main()
