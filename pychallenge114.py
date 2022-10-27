import csv

file = list(csv.reader(open("Books.csv")))
print("Display books published in a range of years:")
startingYear = int(input("Enter year to start: "))
endingYear = int(input("Enter year to end: "))

for row in file:
    if int(row[2]) in range(startingYear - 1, endingYear + 1):
        print(row)
