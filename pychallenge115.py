import csv

file = list(csv.reader(open("Books.csv")))
print("This prints the file along with the row number per line: ")
count = 0

for row in file:
    print(f"{count}: {row}")
    count = count + 1
