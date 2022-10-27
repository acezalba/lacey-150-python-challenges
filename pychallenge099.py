new_2d = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [2, 4, 0]]

for i in new_2d:
    print(i)

x = int(input("Enter a row you would like displayed (0-3): "))

print(f"Row {x} contains value { new_2d[x] } ")

y = int(input("Enter a column from the row (0-2): "))

print(f"{x},{y} contains value { new_2d[x][y] } ")
change = str(input("Do you want to change the value (yes or now) :"))

if change.lower() == "yes":
    new_2d[x][y] = int(input("Enter new value: "))
    print(f"{x},{y} contains new value {new_2d[x][y]}")
    print(f"Row {x} contains {new_2d[x]}")

if change.lower() == "no":
    print("Thank you.")
