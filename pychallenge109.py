import os

choice = int(
    input(
        """
Choose from the following:
1) Create a new file
2) Display the file
3) Add a new item to the file

Enter the number of your choice:
>>"""
    )
)
print("\n")
if choice not in range(1, 4):
    print("Invalid choice. Exiting.")

if choice == 1:
    new_subject = str(input("Enter your favorite school subject: "))
    file = open("Subject.txt", "w")
    file.write(new_subject + "\n")
    file.close()

if choice == 2:
    file = open("Subject.txt", "r+")
    print(file.read())
    file.close()

if choice == 3:
    file = open("Subject.txt", "a+")
    new_subject = str(input("Enter a new subject: "))
    file.write(new_subject + "\n")
    file.close()
    file = open("Subject.txt", "r+")
    print("Here are your updated subjects: \n")
    print(file.read())
    file.close()
