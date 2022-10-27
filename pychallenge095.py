from array import array
from random import randint

float_array = array("f", [])
formatted_dividends = []

for i in range(5):
    float_temp = randint(10, 100)
    float_array.append(float_temp)

print("These are the floats to be divided: ")
for i in float_array:
    formatted = "{:.2f}".format(i)
    formatted_dividends.append(formatted)
    print(formatted)

divisor = int(input("Enter a divisor between 2 and 5: "))

while divisor not in range(1, 6):
    print("Divisor out of range.")
    divisor = int(input("Enter a divisor between 2 and 5: "))

for i in range(5):
    print(f"{formatted_dividends[i]}/{divisor} = {round((float_array[i]/divisor),2)}")
