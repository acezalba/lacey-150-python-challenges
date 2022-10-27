from random import randint


def compNum():
    number1 = int(input("Pick a low number: "))
    number2 = int(input("Pick a high number: "))

    while number2 < number1:
        print("Number 2 is not higher than number 1.")
        number2 = int(input("Pick a high number: "))

    return randint(number1, number2)


def userNum():
    print("I am thinking of a number.")
    guess = int(input("What number am I thinking of? "))
    return guess


def checkGuess(computerNumber, userNumber):
    if computerNumber == userNumber:
        print("You got it.")
        return True
    elif computerNumber > userNumber:
        print("Too low.")
    elif computerNumber < userNumber:
        print("Too high.")
    else:
        print("I don't understand your guess.")

    return False


def main():
    computer = compNum()
    user = userNum()
    game = checkGuess(computer, user)

    while not game:
        print("Try again.")
        user = userNum()
        game = checkGuess(computer, user)


main()
