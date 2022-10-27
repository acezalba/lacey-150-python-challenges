num = 10
while num > 0:
    print(
        "There are",
        num,
        "green bottles hanging on the wall,",
        num,
        "green bottles hanging on the wall, and if 1 green bottle should accidentally fall.",
    )
    answer = int(input("How many green bottles will be hanging on the wall?"))
    while answer != num - 1:
        print("No, try again.")
        answer = int(input("How many green bottles will be hanging on the wall?"))
    num = num - 1
print("There are no more green bottles hanging on the wall.")
