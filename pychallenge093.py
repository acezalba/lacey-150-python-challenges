from array import array
from random import randint
from copy import deepcopy

int_array = array("i", [])

for i in range(1, 6):
    input_temp = int(input(f"Enter a number ({i} of 5): "))
    int_array.append(input_temp)

sorted_array = sorted(int_array)
print("These are your numbers: ", sorted_array)
new_array = deepcopy(sorted_array)

while True:
    try:
        remove_int = int(input("Enter a number to remove from the array: "))
        new_array.remove(remove_int)
        print(new_array)
        break
    except ValueError:
        print("Value not found on the array.")
