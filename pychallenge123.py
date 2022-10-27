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
    with open("Salaries.csv", "r", encoding="utf-8-sig", newline="") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)
    print()


def delete_a_record():
    old_record = []
    names_in_old_record = []

    with open("Salaries.csv", "r", encoding="utf-8-sig", newline="") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            old_record.append(row)
        print(old_record)

    names_in_old_record = [i[0] for i in old_record]
    print(names_in_old_record)

    with open("Salaries.csv", "w", encoding="utf-8-sig", newline="") as file:
        record_to_delete = str(input("Whose record do you want to delete? "))
        if record_to_delete in names_in_old_record:
            del old_record[names_in_old_record.index(record_to_delete)]
            print(f"{record_to_delete} deleted.")
            csv_writer = csv.writer(file)
            for row in old_record:
                csv_writer.writerow(row)
        else:
            print(f"{record_to_delete} not found.")


def menu():
    menu = "Manage your Salaries.csv\n \
1) Add to file.\n \
2) View all records\n \
3) Delete a record\n \
4) Exit the program.\n"
    print(menu)
    choice = int(input("What do you want to do? "))

    if choice == 1:
        add_to_file()
        return True
    elif choice == 2:
        show_records()
        return True
    elif choice == 3:
        delete_a_record()
        return True
    elif choice == 4:
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
