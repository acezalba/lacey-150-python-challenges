import csv

file = open("Books.csv", "a")
book = str(input("Enter new book: "))
author = str(input(f"Enter author of {book}: "))
year = str(input(f"Enter year {book} was released: "))
file.write(str(book + "," + author + "," + year + "\n"))
file.close()
file = open("Books.csv", "r")
for line in file:
    print(line)
file.close()
