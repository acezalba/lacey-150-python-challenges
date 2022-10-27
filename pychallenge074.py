list = [
    "red",
    "yellow",
    "green",
    "purple",
    "black",
    "magenta" "pink",
    "teal",
    "fuchsia",
    "cobalt" "grey",
]

print(list)

while True:
    try:
        init_index = int(input("Enter a number between 1 and 4: "))

        while init_index not in range(0, 5):
            print("Try again.")
            init_index = int(input("Enter a number between 1 and 4: "))

        end_index = int(input("Enter a number between 5 and 9: "))

        while end_index not in range(4, 10):
            print("Try again.")
            end_index = int(input("Enter a number between 5 and 9: "))

        break

    except ValueError:
        print("Error: not a valid number")

print(list[init_index:end_index])
