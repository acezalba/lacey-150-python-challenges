def askNumber():
    return int(input("Give me any number above 1: "))


def countNumber(num):
    for count in range(num):
        print(count + 1)


def main():
    countNumber(askNumber())


main()
