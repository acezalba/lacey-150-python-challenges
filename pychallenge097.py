new_2d = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [2, 4, 0]]

for i in new_2d:
    print(i)

x = int(input("Enter a row (0-3): "))
y = int(input("Enter a column (0-2): "))

print(f"{x},{y} contains value { new_2d[x][y] } ")
