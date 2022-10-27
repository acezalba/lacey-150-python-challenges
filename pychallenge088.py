from array import *

nums = array("i", [])
for i in range(5):
    temp = int(input("Enter an integer: "))
    nums.append(temp)

sorted_nums = sorted(nums, reverse=True)
reversed_nums = sorted(nums)

print(f"Here is your array: {nums}")
print(f"Here is your array, sorted: {sorted_nums}")
print(f"Here is your array, reverse-sorted: {reversed_nums}")
