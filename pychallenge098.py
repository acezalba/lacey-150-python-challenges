new_2d = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [2, 4, 0]]

for i in new_2d:
    print(i)

x = int(input("Enter a row you would like displayed (0-3): "))

print(f"Row {x} contains value { new_2d[x] } ")

new_num = int(input("Enter a number to append to the chosen row: "))

new_2d[x].append(new_num)

print(f"Row {x} contains new value { new_2d[x] } ")
