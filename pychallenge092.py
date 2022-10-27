from array import array
from random import randint

rand_array = array("i", [])
user_array = array("i", [])

for i in range(5):
    rand_temp = randint(1, 100)
    rand_array.append(rand_temp)

for i in range(1, 4):
    user_temp = int(input(f"Enter integer {i} of 3: "))
    user_array.append(user_temp)

rand_array.extend(user_array)

sorted_array = sorted(rand_array)

for i in sorted_array:
    print(i)
