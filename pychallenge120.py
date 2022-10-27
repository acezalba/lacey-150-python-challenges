from random import randint


def addition():
    values = []
    addFirst = randint(5, 20)
    addSecond = randint(5, 20)
    values.append(addFirst + addSecond)
    user = int(input(f"{addFirst} + {addSecond} = "))
    values.append(user)

    return values


def subtraction():
    values = []
    subtractFirst = randint(25, 50)
    subtractSecond = randint(1, 25)
    values.append(subtractFirst - subtractSecond)
    user = int(input(f"{subtractFirst} - {subtractSecond} = "))
    values.append(user)

    return values


def evaluation(list):
    if list[0] == list[1]:
        print("Correct.")
    else:
        print("Incorrect.")
        print(f"The real answer is {list[0]}")


def main():
    menu = """
    1) Addition
    2) Subtraction
    Enter 1 or 2 >> """

    choice = int(input(menu))
    while choice not in range(3):
        choice = int(
            input(
                "Your choice is not available.\nPick between addition(1) or subtraction(2): "
            )
        )

    if choice == 1:
        evaluation(addition())

    if choice == 2:
        evaluation(subtraction())


main()
