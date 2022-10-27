def pretty_print(old_list):
    """DEPRECATED: Pretty prints a Python list right away.
    use the following native method: print(*old_list),sep="\n")
    """
    for index, value in enumerate(old_list):
        if index == len(old_list) - 1:
            print(f"{value}.")
        else:
            print(f"{value}, ", end="")


def pretty_list_string(old_list):
    """Returns the pretty string version of a list."""
    new_string = ""
    for index, value in enumerate(old_list):
        if index == len(old_list) - 1:
            new_string = new_string + value + "."
        else:
            new_string = new_string + value + ", "
    return new_string
