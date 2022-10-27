import os

file = open("Names.txt", "r+")
print(file.read())
file.seek(0, 0)
del_person = str(input("\nEnter the name you want deleted: ")) + "\n"
new_names = []

for line in file:
    if del_person != line:
        new_names.append(line)

new_file = open("Names2.txt", "w+")
new_file.writelines(new_names)
file.close()
new_file.close()
