import csv
import copy


def filePrint(newfile):
    count = 0
    for row in file:
        print(f"{count}: {row}")
        count = count + 1


file = list(csv.reader(open("Books.csv")))
filePrint(file)

removeRow = int(input("Which row do you want removed? "))
del file[removeRow]
filePrint(file)

changeRow = int(input("Which row do you want changed? "))
if changeRow:
    book = str(input("Enter new book: "))
    author = str(input(f"Enter author of {book}: "))
    year = int(input(f"Enter year {book} was published: "))
    temp = []
    temp.append(book)
    temp.append(author)
    temp.append(year)
    file[changeRow] = temp

filePrint(file)

with open("Books.csv", "w", newline="") as newCsv:
    csvWriter = csv.writer(newCsv)
    for row in file:
        csvWriter.writerow(row)
