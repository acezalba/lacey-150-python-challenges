nums = []

for i in range(3):
    user_input = int(input("Enter a number: "))
    nums.append(user_input)
    print(nums)

response = str(input("Do you still want the number you last entered saved: yes/no "))

if response.lower() == "no":
    nums.pop()

print(nums)
