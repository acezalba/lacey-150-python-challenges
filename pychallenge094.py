from array import array
from random import randint

int_array = array("i", [])

for i in range(5):
    temp = randint(0, 100)
    int_array.append(temp)

print(int_array)
int_check = int(input("Enter a number in the array: "))

while int_check not in int_array:
    print("The number cannot be found in the array.")
    print("Try again.")
    int_check = int(input("Enter a number in the array: "))

print(f"The number is in index: {int_array.index(int_check)}")
