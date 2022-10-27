import array

int_array = array.array("i", [1, 2, 3, 3, 4])

print(int_array)
int_check = int(input("Enter a number found in the array.: "))
int_count = int_array.count(int_check)

print(f"The number you chose appeared {int_count} times")
