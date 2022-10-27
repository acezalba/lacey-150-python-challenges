compnum = 50
number = int(input("Guess the number: "))
count = 1
while number != compnum:
    if number < compnum:
        print("Your guess is too low")
    else:
        print("Your guess is too high")
    number = int(input("Have another guess.\nGuess the number: "))
    count = count + 1
print("Well done, you took", count, "attempts")
