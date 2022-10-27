def add_name(list):
    new_name = str(input("Add a name to the list: "))
    list.append(new_name)
    print(f"{new_name} is added to the list.")


def change_name(list):
    name_to_be_changed = str(input("What name do you want to change? "))
    if name_to_be_changed in list:
        name_to_replace = str(input(f"Replace {name_to_be_changed} with what name? "))
        list[list.index(name_to_be_changed)] = name_to_replace
    else:
        print(f"{name_to_be_changed} not found.")


def remove_name(list):
    name_to_be_removed = str(input("What name do you want removed? "))
    if name_to_be_removed in list:
        del list[list.index(name_to_be_removed)]
    else:
        print(f"{name_to_be_removed} not found.")


def show_list(list):
    print(list)


def menu(list):
    print(
        "\nManage a list of names:\n \
    1) Add name to the list\n \
    2) Change a name on the list\n \
    3) Remove a name from the list\n \
    4) Show the list of names\n \
    0) Exit\n"
    )
    choice = int(input("What do you want to do? "))

    if choice == 1:
        add_name(list)
        return True
    elif choice == 2:
        change_name(list)
        return True
    elif choice == 3:
        remove_name(list)
        return True
    elif choice == 4:
        show_list(list)
        return True
    else:
        return False


def main():
    name_list = []
    while menu(name_list):
        continue
    print("Exiting")
    exit()


main()
