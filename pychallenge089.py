import array, random

nums = array.array("i", [])
for i in range(5):
    temp = random.randint(0, 100)
    nums.append(temp)

print(nums)

for i in nums:
    print(i)
