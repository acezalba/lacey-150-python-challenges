nursery_input = str(input("Type the line of a nursery rhyme: "))
print(len(nursery_input))
first_number = int(input("Type the initial number to cut the rhyme: "))
last_number = int(input("Type the last number to cut the rhyme: "))

if first_number > -1 and last_number < len(nursery_input):
    print(nursery_input[first_number:last_number])
else:
    print("Out of range")
