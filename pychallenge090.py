from array import array

int_list = array("i", [])
count = 0

while count < 5:
    temp = int(input("Enter a number: "))
    if temp > 10 and temp < 20:
        int_list.append(temp)
        count = count + 1
    else:
        print("Outside range.")

print("Thank you.")

for i in int_list:
    print(i)
