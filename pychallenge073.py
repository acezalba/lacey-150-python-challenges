foods = {}
index = 1

while index <= 4:
    entry = input("Enter a food that you like:  ")
    foods.update({index: entry})
    index = index + 1

print(foods)

remove = input("Enter a food to remove: ")

for key, value in foods.items():
    if remove == value:
        foods.pop(key, value)
        break

print(sorted(foods.values()))
