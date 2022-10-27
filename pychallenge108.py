import os

file = open("Names.txt", "a+")
new_name = str(input("Add a name to a list of names: "))
file.write("\n" + new_name)
file.close()

file = open("Names.txt", "r+")
print("Here is the new list of names:\n ")
print(file.read())
file.close()
